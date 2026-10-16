"""
Automated Test Suite for PhytoMed AI System
===========================================
Validates knowledge base integrity, computer vision segmentation,
PyTorch deep learning inference, Grad-CAM explainability,
and Flask REST API endpoints.
"""

import os
import io
import json
import unittest
import numpy as np
from PIL import Image
import torch

import database
import cv_utils
from model import PlantInferenceEngine
from app import app

class TestPhytoMedAI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.samples_dir = os.path.join(os.path.dirname(__file__), "static", "samples")

    def test_database_integrity(self):
        """Verify all registered plant monographs have required pharmacological fields."""
        species = database.get_all_species()
        self.assertGreaterEqual(len(species), 10, "Database should contain at least 10 species")

        required_fields = [
            "id", "scientific_name", "common_names", "botanical_family",
            "is_medicinal", "medicinal_status", "authoritative_sources",
            "documented_medicinal_uses", "traditionally_used_parts",
            "preparation_information", "dosage_information",
            "precautions_warnings", "contraindications_interactions",
            "active_phytochemicals"
        ]

        for plant in species:
            for field in required_fields:
                self.assertIn(field, plant, f"Plant '{plant.get('id')}' missing required field '{field}'")
            self.assertIsInstance(plant["is_medicinal"], bool)
            self.assertGreater(len(plant["documented_medicinal_uses"]), 0)
            self.assertGreater(len(plant["dosage_information"]), 0)

        # Test search
        search_results = database.search_plants("cough")
        self.assertGreater(len(search_results), 0, "Search for 'cough' should return matching plants")

    def test_cv_utils(self):
        """Verify leaf segmentation and morphological metrics calculation."""
        # Create dummy green leaf synthetic image
        img = np.full((300, 300, 3), 240, dtype=np.uint8)
        # Draw green circle
        import cv2
        cv2.circle(img, (150, 150), 70, (40, 120, 50), -1)

        segmented, mask, contour = cv_utils.segment_leaf(img)
        self.assertEqual(segmented.shape, (300, 300, 3))
        self.assertEqual(mask.shape, (300, 300))
        self.assertIsNotNone(contour)

        features = cv_utils.extract_leaf_features(img, contour)
        self.assertIn("circularity", features)
        self.assertIn("aspect_ratio", features)
        self.assertIn("vein_texture_density", features)
        self.assertGreater(features["circularity"], 0.5)

    def test_model_inference_and_gradcam(self):
        """Verify deep learning inference and Grad-CAM heatmap generation."""
        engine = PlantInferenceEngine()
        sample_path = os.path.join(self.samples_dir, "ocimum_sanctum.jpg")
        if not os.path.exists(sample_path):
            pil_img = Image.new("RGB", (224, 224), color=(34, 139, 34))
        else:
            pil_img = Image.open(sample_path).convert("RGB")

        result = engine.predict(pil_img, top_k=3, generate_explainability=True)
        self.assertIn("top_prediction", result)
        self.assertIn("confidence", result["top_prediction"])
        self.assertIn("top_k", result)
        self.assertEqual(len(result["top_k"]), 3)
        self.assertIn("monograph", result)
        self.assertIsNotNone(result.get("gradcam_overlay_bgr"))

    def test_uncertainty_handling(self):
        """Verify uncertainty flag and safety message logic on low confidence."""
        engine = PlantInferenceEngine()
        noise_img = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))
        # With high threshold (e.g. 99.0%), noise input is uncertain
        result = engine.predict(noise_img, uncertainty_threshold=99.0)
        self.assertIn("is_uncertain", result)
        self.assertTrue(result["is_uncertain"])
        self.assertIsNotNone(result.get("uncertainty_message"))

    def test_all_dataset_classes_have_monographs(self):
        """Verify all 30 classes from the Indian Medicinal Leaves dataset map to valid monographs."""
        engine = PlantInferenceEngine()
        self.assertEqual(engine.num_classes, 30, "Engine should load exactly 30 classes from checkpoint")
        for cls_name in engine.classes:
            mono = database.get_plant_by_id(cls_name)
            self.assertIsNotNone(mono, f"Dataset class '{cls_name}' must resolve to a valid monograph")
            self.assertTrue(len(mono["documented_medicinal_uses"]) > 0)
            self.assertTrue(len(mono["dosage_information"]) > 0)

    def test_flask_routes(self):
        """Verify web routes render properly."""
        r_index = self.app.get("/")
        self.assertEqual(r_index.status_code, 200)

        r_encyclopedia = self.app.get("/encyclopedia")
        self.assertEqual(r_encyclopedia.status_code, 200)

        r_about = self.app.get("/about")
        self.assertEqual(r_about.status_code, 200)

        r_details = self.app.get("/species/ocimum_sanctum")
        self.assertEqual(r_details.status_code, 200)

        r_details_tulsi = self.app.get("/species/ocimum_tenuiflorum")
        self.assertEqual(r_details_tulsi.status_code, 200)

    def test_api_endpoints(self):
        """Verify REST API identification endpoint and JSON queries."""
        # Test /api/classes
        r_classes = self.app.get("/api/classes")
        self.assertEqual(r_classes.status_code, 200)
        data = r_classes.get_json()
        self.assertIn("total", data)
        self.assertGreaterEqual(data["total"], 30)

        # Test /api/search
        r_search = self.app.get("/api/search?q=diabetes")
        self.assertEqual(r_search.status_code, 200)
        s_data = r_search.get_json()
        self.assertGreater(s_data["count"], 0)

        # Test /api/identify with an image file
        sample_path = os.path.join(self.samples_dir, "ocimum_sanctum.jpg")
        with open(sample_path, "rb") as f:
            img_bytes = f.read()

        data = {
            "leaf_image": (io.BytesIO(img_bytes), "tulsi_test.jpg")
        }
        r_identify = self.app.post("/api/identify", data=data, content_type="multipart/form-data")
        self.assertEqual(r_identify.status_code, 200)
        res = r_identify.get_json()
        self.assertIn("prediction", res)
        self.assertIn("monograph", res)
        self.assertIn("morphology", res)
        self.assertIn("is_uncertain", res)
        self.assertTrue(res["prediction"]["confidence"] > 0)
        self.assertIn("checkpoint_status", res)
        self.assertTrue(res["checkpoint_status"]["loaded"])

    def test_invalid_and_corrupt_image_upload(self):
        """Verify API safely rejects corrupt, non-image, and unsupported uploads with 400."""
        # 1. Corrupt random bytes pretending to be JPEG
        corrupt_data = {"leaf_image": (io.BytesIO(b"MALFORMED_CORRUPT_BYTES_XYZ123"), "corrupt.jpg")}
        r1 = self.app.post("/api/identify", data=corrupt_data, content_type="multipart/form-data")
        self.assertEqual(r1.status_code, 400)
        self.assertIn("error", r1.get_json())

        # 2. Plain text file upload
        txt_data = {"leaf_image": (io.BytesIO(b"Hello this is a plain text file"), "notes.txt")}
        r2 = self.app.post("/api/identify", data=txt_data, content_type="multipart/form-data")
        self.assertEqual(r2.status_code, 400)
        self.assertIn("error", r2.get_json())

        # 3. Tiny 2x2 image
        tiny_img = Image.new("RGB", (4, 4), color=(0, 255, 0))
        tiny_bytes = io.BytesIO()
        tiny_img.save(tiny_bytes, format="JPEG")
        tiny_bytes.seek(0)
        tiny_data = {"leaf_image": (tiny_bytes, "tiny.jpg")}
        r3 = self.app.post("/api/identify", data=tiny_data, content_type="multipart/form-data")
        self.assertEqual(r3.status_code, 400)
        self.assertIn("error", r3.get_json())

    def test_dihedral_perceptual_hash_invariance(self):
        """Verify D4 dihedral perceptual hash is strictly invariant across rotations and flips."""
        from dataset_pipeline import compute_dihedral_dhash
        # Create asymmetric test image with distinct features
        img = Image.new("RGB", (64, 64), color=(255, 255, 255))
        # Draw asymmetric black triangle on left
        for y in range(10, 40):
            for x in range(10, y):
                img.putpixel((x, y), (0, 0, 0))

        canonical_hash, _ = compute_dihedral_dhash(img, hash_size=16)

        # Test all 4 rotations and horizontal flip
        for rot in [Image.Transpose.ROTATE_90, Image.Transpose.ROTATE_180, Image.Transpose.ROTATE_270]:
            rot_img = img.transpose(rot)
            rot_hash, _ = compute_dihedral_dhash(rot_img, hash_size=16)
            self.assertEqual(canonical_hash, rot_hash, f"Dihedral dHash failed rotation invariance: {rot}")

        flip_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        flip_hash, _ = compute_dihedral_dhash(flip_img, hash_size=16)
        self.assertEqual(canonical_hash, flip_hash, "Dihedral dHash failed horizontal flip invariance")

    def test_split_manifest_integrity(self):
        """Verify reproducible dataset split manifest exists and has zero cross-partition leakage."""
        manifest_path = os.path.join(os.path.dirname(__file__), "dataset_split_manifest.json")
        self.assertTrue(os.path.exists(manifest_path), "dataset_split_manifest.json must exist")

        with open(manifest_path, "r") as f:
            manifest = json.load(f)

        self.assertIn("assignments", manifest)
        self.assertIn("metadata", manifest)
        self.assertGreaterEqual(manifest["metadata"]["total_images"], 1800)

        # Cluster integrity check: verify no cluster is split across multiple partitions
        cluster_to_partitions = {}
        for path, entry in manifest["assignments"].items():
            cid = entry["cluster_id"]
            part = entry["partition"]
            if cid not in cluster_to_partitions:
                cluster_to_partitions[cid] = set()
            cluster_to_partitions[cid].add(part)

        leakage_clusters = {cid: parts for cid, parts in cluster_to_partitions.items() if len(parts) > 1}
        self.assertEqual(len(leakage_clusters), 0, f"Found {len(leakage_clusters)} clusters leaking across partitions!")

    def test_toxic_plant_safety_handling(self):
        """Verify toxic and non-medicinal plants are explicitly flagged with warnings and contraindications."""
        nerium = database.get_plant_by_id("Nerium Oleander (Oleander)")
        self.assertIsNotNone(nerium)
        self.assertFalse(nerium["is_medicinal"], "Nerium Oleander must NOT be marked medicinal")
        self.assertIn("toxic", nerium["medicinal_status"].lower())
        self.assertGreater(len(nerium["precautions_warnings"]), 0)
        self.assertGreater(len(nerium["contraindications_interactions"]), 0)

    def test_unverified_species_fallback_monograph(self):
        """Verify unverified/unclassified species return safe fallback monograph with contraindications."""
        engine = PlantInferenceEngine()
        # Set all class mappings to unverified synthetic species
        engine.idx_to_class = {i: f"Unverified_Wild_Species_{i}" for i in range(engine.num_classes)}
        # Create green test image
        img = Image.new("RGB", (224, 224), color=(50, 150, 50))
        res = engine.predict(img)
        self.assertIn("monograph", res)
        mono = res["monograph"]
        self.assertFalse(mono["is_medicinal"])
        self.assertIn("precautions_warnings", mono)
        self.assertIn("contraindications_interactions", mono)

    def test_zip_download_route(self):
        """Verify /download-zip endpoint serves the project zip."""
        with self.app.get("/download-zip") as r_zip:
            self.assertEqual(r_zip.status_code, 200)
            self.assertEqual(r_zip.headers["Content-Type"], "application/zip")


if __name__ == "__main__":
    unittest.main()

