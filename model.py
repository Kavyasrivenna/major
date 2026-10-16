"""
Deep Learning Model Architecture & Grad-CAM Explainability Engine
================================================================
Implements PyTorch MobileNetV3-Large classifier for plant species identification,
with full checkpoint metadata restoration, top-K probability scoring,
uncertainty handling / out-of-distribution rejection, and Gradient-weighted
Class Activation Mapping (Grad-CAM) visual explainability for leaf images.
"""

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image
import numpy as np
import cv2
from typing import List, Dict, Tuple, Any, Optional

import database

# Standard ImageNet normalization parameters
IMAGE_SIZE = 224
NORM_MEAN = [0.485, 0.456, 0.406]
NORM_STD = [0.229, 0.224, 0.225]

# Preprocessing transform
INFERENCE_TRANSFORMS = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=NORM_MEAN, std=NORM_STD)
])

class PlantLeafClassifier(nn.Module):
    """
    Medicinal plant leaf classifier using MobileNetV3-Large backbone
    with customized dense classification head.
    """
    def __init__(self, num_classes: int = len(database.PLANT_DATABASE)):
        super(PlantLeafClassifier, self).__init__()
        try:
            backbone = models.mobilenet_v3_large(weights=None)
        except Exception:
            backbone = models.mobilenet_v3_large(pretrained=False)
            
        self.features = backbone.features
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))

        # MobileNetV3-Large feature output channels = 960
        in_features = 960
        self.classifier = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.LayerNorm(512),
            nn.Hardswish(inplace=True),
            nn.Dropout(p=0.3),
            nn.Linear(512, 256),
            nn.LayerNorm(256),
            nn.Hardswish(inplace=True),
            nn.Dropout(p=0.2),
            nn.Linear(256, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


class GradCAM:
    """
    Gradient-weighted Class Activation Mapping (Grad-CAM)
    for visual model explainability on leaf imagery.
    """
    def __init__(self, model: nn.Module, target_layer: nn.Module):
        self.model = model
        self.target_layer = target_layer
        self.gradients: Optional[torch.Tensor] = None
        self.activations: Optional[torch.Tensor] = None
        self.hook_handles: List[Any] = []
        self._register_hooks()

    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output.detach()

        def backward_hook(module, grad_in, grad_out):
            self.gradients = grad_out[0].detach()

        h1 = self.target_layer.register_forward_hook(forward_hook)
        h2 = self.target_layer.register_full_backward_hook(backward_hook)
        self.hook_handles = [h1, h2]

    def remove_hooks(self):
        for h in self.hook_handles:
            h.remove()

    def generate_heatmap(self, input_tensor: torch.Tensor, class_idx: int) -> np.ndarray:
        """Compute normalized Grad-CAM activation heatmap for a specified class index."""
        self.model.eval()
        self.model.zero_grad()

        output = self.model(input_tensor)
        score = output[0, class_idx]
        score.backward()

        if self.gradients is None or self.activations is None:
            return np.ones((IMAGE_SIZE, IMAGE_SIZE), dtype=np.float32)

        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        cam = torch.sum(weights * self.activations, dim=1, keepdim=True)
        cam = F.relu(cam)

        cam_np = cam.squeeze().cpu().numpy()
        cam_min, cam_max = np.min(cam_np), np.max(cam_np)
        if cam_max - cam_min > 1e-8:
            cam_np = (cam_np - cam_min) / (cam_max - cam_min)
        else:
            cam_np = np.zeros_like(cam_np)

        return cam_np


class PlantInferenceEngine:
    """
    High-level engine that manages model loading, leaf inference,
    uncertainty rejection, Grad-CAM heatmap overlay, and pharmacological lookup.
    """
    def __init__(self, weights_path: Optional[str] = None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.weights_path = weights_path or os.path.join(
            os.path.dirname(__file__), "models", "plant_classifier.pth"
        )
        self.checkpoint_metadata = {}
        self.checkpoint_loaded = False
        self.classes: List[str] = []
        self.class_to_idx: Dict[str, int] = {}
        self.idx_to_class: Dict[int, str] = {}
        self.num_classes: int = 0

        self._load_weights()
        self.grad_cam = GradCAM(self.model, self.model.features[-1])

    def _load_weights(self):
        if os.path.exists(self.weights_path):
            try:
                ckpt = torch.load(self.weights_path, map_location=self.device, weights_only=False)
                if isinstance(ckpt, dict) and "state_dict" in ckpt:
                    self.checkpoint_metadata = ckpt
                    self.classes = ckpt.get("classes", [])
                    self.num_classes = len(self.classes)
                    self.class_to_idx = ckpt.get("class_to_idx", {c: i for i, c in enumerate(self.classes)})
                    self.idx_to_class = {int(k): v for k, v in ckpt.get("idx_to_class", {}).items()} if ckpt.get("idx_to_class") else {i: c for i, c in enumerate(self.classes)}
                    
                    self.model = PlantLeafClassifier(num_classes=self.num_classes).to(self.device)
                    self.model.load_state_dict(ckpt["state_dict"])
                    self.checkpoint_loaded = True
                    print(f"[INFO] Loaded trained model with {self.num_classes} classes from: {self.weights_path}")
                else:
                    self.classes = database.get_species_classes()
                    self.num_classes = len(self.classes)
                    self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
                    self.idx_to_class = {i: c for i, c in enumerate(self.classes)}
                    self.model = PlantLeafClassifier(num_classes=self.num_classes).to(self.device)
                    self.model.load_state_dict(ckpt)
                    self.checkpoint_loaded = True
                    print(f"[INFO] Loaded raw state_dict from: {self.weights_path}")
            except Exception as e:
                print(f"[WARNING] Could not load weights: {e}. Model initialized with default state.")
                self._fallback_init()
        else:
            print(f"[INFO] No pre-saved weights found at {self.weights_path}. Initializing default model.")
            self._fallback_init()

    def _fallback_init(self):
        self.checkpoint_loaded = False
        self.classes = database.get_species_classes()
        self.num_classes = len(self.classes)
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
        self.idx_to_class = {i: c for i, c in enumerate(self.classes)}
        self.model = PlantLeafClassifier(num_classes=self.num_classes).to(self.device)

    def predict(
        self,
        pil_image: Image.Image,
        top_k: int = 3,
        generate_explainability: bool = True,
        uncertainty_threshold: float = 40.0
    ) -> Dict[str, Any]:
        """
        Run inference on a single PIL leaf image.
        Returns top-k predicted classes, confidence scores, uncertainty flag,
        Grad-CAM heatmap, and authoritative pharmacological monograph for the top prediction.
        """
        # Ensure RGB mode
        if pil_image.mode != "RGB":
            pil_image = pil_image.convert("RGB")

        orig_w, orig_h = pil_image.size
        input_tensor = INFERENCE_TRANSFORMS(pil_image).unsqueeze(0).to(self.device)
        input_tensor.requires_grad = True

        # Forward pass
        output = self.model(input_tensor)
        probabilities = F.softmax(output, dim=1).squeeze(0).detach().cpu().numpy()

        # Top-K predictions
        top_k_count = min(top_k, self.num_classes)
        top_indices = np.argsort(probabilities)[::-1][:top_k_count]
        predictions = []

        for idx in top_indices:
            idx = int(idx)
            cls_name = self.idx_to_class.get(idx, f"Class_{idx}")
            plant_data = database.get_plant_by_id(cls_name)

            predictions.append({
                "species_id": plant_data["id"] if plant_data else cls_name,
                "dataset_class": cls_name,
                "scientific_name": plant_data["scientific_name"] if plant_data else cls_name,
                "common_names": plant_data["common_names"] if plant_data else [cls_name],
                "is_medicinal": plant_data["is_medicinal"] if plant_data else False,
                "medicinal_status": plant_data["medicinal_status"] if plant_data else "Unclassified",
                "confidence": round(float(probabilities[idx]) * 100, 2)
            })

        top_pred = predictions[0]
        top_class_idx = int(top_indices[0])
        top_species_name = self.idx_to_class.get(top_class_idx, "")
        top_monograph = database.get_plant_by_id(top_species_name)

        # Fallback if no matching monograph in database
        if top_monograph is None:
            top_monograph = {
                "id": top_species_name,
                "dataset_class": top_species_name,
                "scientific_name": f"Botanical Specimen ({top_species_name})",
                "botanical_family": "Unspecified Family",
                "common_names": [top_species_name],
                "is_medicinal": False,
                "medicinal_status": "Unverified / Non-Pharmacopoeial Plant",
                "status_badge_color": "slate",
                "evidence_category": "No Pharmacopoeial Monograph Available",
                "authoritative_sources": ["System Safety Fallback Standard"],
                "documented_medicinal_uses": ["No validated therapeutic indications found in authoritative pharmacopoeias."],
                "traditionally_used_parts": [],
                "preparation_information": [],
                "dosage_information": [{"source": "Safety Warning", "preparation": "All forms", "dose": "UNVERIFIED: Do not consume without professional botanical verification."}],
                "precautions_warnings": ["Unknown species risk: Wild leaves may contain uncharacterized phytotoxins."],
                "contraindications_interactions": ["Strictly contraindicated for internal therapeutic consumption without botanical confirmation."],
                "active_phytochemicals": []
            }

        # Uncertainty handling & out-of-distribution rejection
        is_uncertain = top_pred["confidence"] < uncertainty_threshold
        uncertainty_message = None
        if is_uncertain:
            uncertainty_message = (
                f"Confidence is {top_pred['confidence']}% (< {uncertainty_threshold}% threshold). "
                "The leaf image does not strongly match any supported botanical species. "
                "Always verify with an expert botanist before medicinal consumption."
            )

        # Grad-CAM Explainability
        gradcam_overlay_bgr = None
        if generate_explainability:
            try:
                heatmap = self.grad_cam.generate_heatmap(input_tensor, top_class_idx)
                heatmap_resized = cv2.resize(heatmap, (orig_w, orig_h))
                heatmap_uint8 = np.uint8(255 * heatmap_resized)
                heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)

                orig_bgr = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                gradcam_overlay_bgr = cv2.addWeighted(orig_bgr, 0.6, heatmap_color, 0.4, 0)
            except Exception as e:
                print(f"[WARNING] Grad-CAM generation error: {e}")

        return {
            "top_prediction": top_pred,
            "top_k": predictions,
            "is_uncertain": is_uncertain,
            "uncertainty_message": uncertainty_message,
            "monograph": top_monograph,
            "gradcam_overlay_bgr": gradcam_overlay_bgr,
            "checkpoint_status": {
                "loaded": self.checkpoint_loaded,
                "path": self.weights_path,
                "classes_count": self.num_classes
            }
        }
