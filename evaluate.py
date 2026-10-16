"""
Comprehensive Model Evaluation & Out-of-Distribution Rejection Audit
====================================================================
Evaluates genuine trained PyTorch MobileNetV3-Large checkpoint on the held-out
test dataset (207 images across 30 classes) and measures unknown species rejection.

Outputs:
1. Top-1 and Top-3 accuracy
2. Macro Precision, Recall, and F1-Score
3. Per-Class classification metrics & support
4. Formatted classification report text file (classification_report.txt)
5. Confusion matrix heatmap (confusion_matrix.png)
6. Out-of-Distribution / Unknown-Species rejection analysis (ood_rejection_report.json)
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from PIL import Image

import database
from model import PlantLeafClassifier, PlantInferenceEngine, INFERENCE_TRANSFORMS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
CHECKPOINT_PATH = os.path.join(MODELS_DIR, "plant_classifier.pth")
TEST_DATA_DIR = os.path.join(BASE_DIR, "dataset", "test")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")
os.makedirs(EVAL_DIR, exist_ok=True)


def evaluate_checkpoint(
    checkpoint_path: str = CHECKPOINT_PATH,
    test_dir: str = TEST_DATA_DIR,
    batch_size: int = 16
):
    print("=" * 70)
    print("[+] PhytoMed AI: Rigorous Model Evaluation on Held-Out Test Data")
    print("=" * 70)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Compute Device: {device}")

    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(f"Checkpoint not found at: {checkpoint_path}")

    # Load checkpoint
    ckpt = torch.load(checkpoint_path, map_location=device, weights_only=False)
    classes = ckpt.get("classes", [])
    num_classes = len(classes)
    class_to_idx = ckpt.get("class_to_idx", {c: i for i, c in enumerate(classes)})
    idx_to_class = {int(k): v for k, v in ckpt.get("idx_to_class", {}).items()} if ckpt.get("idx_to_class") else {i: c for i, c in enumerate(classes)}

    print(f"[INFO] Loaded Checkpoint Architecture: {ckpt.get('architecture', 'MobileNetV3-Large')}")
    print(f"[INFO] Number of Classes: {num_classes}")

    # Instantiate model
    model = PlantLeafClassifier(num_classes=num_classes).to(device)
    model.load_state_dict(ckpt["state_dict"])
    model.eval()

    # Load test dataset
    test_dataset = datasets.ImageFolder(test_dir, transform=INFERENCE_TRANSFORMS)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=0)
    print(f"[INFO] Evaluating on {len(test_dataset)} untouched held-out test images across {len(test_dataset.classes)} directories...")

    all_preds = []
    all_targets = []
    all_probs = []

    start_time = time.time()
    with torch.no_grad():
        for imgs, lbls in test_loader:
            imgs = imgs.to(device)
            outputs = model(imgs)
            probs = F.softmax(outputs, dim=1).cpu().numpy()
            preds = np.argmax(probs, axis=1)

            all_preds.extend(preds)
            all_targets.extend(lbls.numpy())
            all_probs.extend(probs)

    eval_duration = time.time() - start_time
    num_samples = len(all_targets)
    all_targets = np.array(all_targets)
    all_preds = np.array(all_preds)
    all_probs = np.array(all_probs)

    # 1. Top-1 and Top-3 Accuracy
    top1_correct = np.sum(all_preds == all_targets)
    top1_acc = (top1_correct / num_samples) * 100.0

    top3_correct = 0
    for i in range(num_samples):
        top3_indices = np.argsort(all_probs[i])[::-1][:3]
        if all_targets[i] in top3_indices:
            top3_correct += 1
    top3_acc = (top3_correct / num_samples) * 100.0

    # 2. Per-class metrics
    per_class = {}
    precisions, recalls, f1s = [], [], []

    for c_idx in range(num_classes):
        c_name = idx_to_class.get(c_idx, f"Class_{c_idx}")
        tp = int(np.sum((all_preds == c_idx) & (all_targets == c_idx)))
        fp = int(np.sum((all_preds == c_idx) & (all_targets != c_idx)))
        fn = int(np.sum((all_preds != c_idx) & (all_targets == c_idx)))
        support = int(np.sum(all_targets == c_idx))

        prec = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
        rec = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        f1 = float(2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

        precisions.append(prec)
        recalls.append(rec)
        f1s.append(f1)

        per_class[c_name] = {
            "precision": round(prec * 100.0, 2),
            "recall": round(rec * 100.0, 2),
            "f1_score": round(f1 * 100.0, 2),
            "support": support
        }

    macro_precision = float(np.mean(precisions)) * 100.0
    macro_recall = float(np.mean(recalls)) * 100.0
    macro_f1 = float(np.mean(f1s)) * 100.0

    # 3. Confusion Matrix
    cm = np.zeros((num_classes, num_classes), dtype=int)
    for t, p in zip(all_targets, all_preds):
        cm[t, p] += 1

    metrics_payload = {
        "evaluation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "checkpoint_evaluated": os.path.basename(checkpoint_path),
        "test_dataset_size": num_samples,
        "evaluation_time_seconds": round(eval_duration, 2),
        "top1_accuracy": round(top1_acc, 2),
        "top3_accuracy": round(top3_acc, 2),
        "macro_precision": round(macro_precision, 2),
        "macro_recall": round(macro_recall, 2),
        "macro_f1": round(macro_f1, 2),
        "per_class": per_class,
        "confusion_matrix": cm.tolist()
    }

    # Save metrics JSON
    metrics_path = os.path.join(EVAL_DIR, "evaluation_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics_payload, f, indent=2)
    print(f"\n[INFO] Saved verified evaluation metrics to: {metrics_path}")

    # 4. Generate Classification Report Text File
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("PHYTOMED AI: HELD-OUT TEST CLASSIFICATION REPORT")
    report_lines.append(f"Evaluated on: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    report_lines.append(f"Model Backbone: MobileNetV3-Large | Test Samples: {num_samples} | Classes: {num_classes}")
    report_lines.append("=" * 80)
    report_lines.append(f"{'Class / Botanical Species':<45} | {'Precision':<9} | {'Recall':<9} | {'F1-Score':<9} | {'Support':<7}")
    report_lines.append("-" * 88)

    for c_idx in range(num_classes):
        c_name = idx_to_class.get(c_idx, f"Class_{c_idx}")
        stats = per_class[c_name]
        report_lines.append(
            f"{c_name:<45} | {stats['precision']:>8.2f}% | {stats['recall']:>8.2f}% | {stats['f1_score']:>8.2f}% | {stats['support']:>7d}"
        )

    report_lines.append("-" * 88)
    report_lines.append(f"{'MACRO AVERAGE':<45} | {macro_precision:>8.2f}% | {macro_recall:>8.2f}% | {macro_f1:>8.2f}% | {num_samples:>7d}")
    report_lines.append(f"{'TOP-1 ACCURACY':<45} | {top1_acc:>8.2f}%")
    report_lines.append(f"{'TOP-3 ACCURACY':<45} | {top3_acc:>8.2f}%")
    report_lines.append("=" * 80)

    report_text = "\n".join(report_lines)
    report_path = os.path.join(EVAL_DIR, "classification_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"[INFO] Saved classification report text to: {report_path}")

    # 5. Plot Confusion Matrix
    plt.figure(figsize=(15, 13))
    short_names = [idx_to_class[i].split(" (")[0] for i in range(num_classes)]
    sns.heatmap(cm, annot=False, cmap="Blues", fmt="d",
                xticklabels=short_names, yticklabels=short_names)
    plt.title(f"Confusion Matrix on Held-Out Test Set (Top-1 Accuracy: {top1_acc:.2f}%)", fontsize=14, pad=15)
    plt.xlabel("Predicted Botanical Species", fontsize=12)
    plt.ylabel("True Botanical Species", fontsize=12)
    plt.xticks(rotation=90, fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.tight_layout()
    cm_path = os.path.join(EVAL_DIR, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=200)
    plt.close()
    print(f"[INFO] Saved confusion matrix heatmap to: {cm_path}")

    # 6. Out-of-Distribution (OOD) / Unknown Species Rejection Test
    print("\n" + "-" * 70)
    print("[+] Evaluating Unknown-Species / Out-of-Distribution Rejection Performance...")
    print("-" * 70)

    ood_trials = []
    # Test 1: Pure Gaussian noise images (non-leaf background)
    np.random.seed(101)
    for trial_idx in range(15):
        noise = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        pil_noise = Image.fromarray(noise)
        t_noise = INFERENCE_TRANSFORMS(pil_noise).unsqueeze(0).to(device)
        with torch.no_grad():
            out = model(t_noise)
            probs = F.softmax(out, dim=1).cpu().numpy()[0]
        max_p = float(np.max(probs)) * 100.0
        ood_trials.append({
            "type": "gaussian_noise",
            "max_confidence": round(max_p, 2),
            "rejected_at_40pct": max_p < 40.0,
            "rejected_at_50pct": max_p < 50.0
        })

    # Test 2: Uniform blank canvases (white, gray, black, green)
    for color, name in [((255, 255, 255), "blank_white"), ((128, 128, 128), "blank_gray"), ((0, 0, 0), "blank_black"), ((34, 139, 34), "solid_green")]:
        canvas = np.full((224, 224, 3), color, dtype=np.uint8)
        pil_canvas = Image.fromarray(canvas)
        t_canvas = INFERENCE_TRANSFORMS(pil_canvas).unsqueeze(0).to(device)
        with torch.no_grad():
            out = model(t_canvas)
            probs = F.softmax(out, dim=1).cpu().numpy()[0]
        max_p = float(np.max(probs)) * 100.0
        ood_trials.append({
            "type": name,
            "max_confidence": round(max_p, 2),
            "rejected_at_40pct": max_p < 40.0,
            "rejected_at_50pct": max_p < 50.0
        })

    rejected_40 = sum(1 for t in ood_trials if t["rejected_at_40pct"])
    total_ood = len(ood_trials)
    rejection_rate_40 = (rejected_40 / total_ood) * 100.0

    ood_report = {
        "total_ood_samples": total_ood,
        "uncertainty_threshold": 40.0,
        "rejection_rate_pct": round(rejection_rate_40, 2),
        "mean_ood_confidence": round(float(np.mean([t["max_confidence"] for t in ood_trials])), 2),
        "trials": ood_trials
    }

    ood_path = os.path.join(EVAL_DIR, "ood_rejection_report.json")
    with open(ood_path, "w") as f:
        json.dump(ood_report, f, indent=2)
    print(f"[INFO] Saved OOD rejection report to: {ood_path}")
    print(f"[INFO] OOD / Unknown Species Rejection Rate at 40% threshold: {rejection_rate_40:.1f}%")

    print("\n" + "=" * 70)
    print("VERIFIED TEST SET EVALUATION SUMMARY:")
    print(f"  Top-1 Test Accuracy:  {top1_acc:.2f}%")
    print(f"  Top-3 Test Accuracy:  {top3_acc:.2f}%")
    print(f"  Macro Precision:      {macro_precision:.2f}%")
    print(f"  Macro Recall:         {macro_recall:.2f}%")
    print(f"  Macro F1-Score:       {macro_f1:.2f}%")
    print(f"  Target >= 90% Met:    {'YES' if top1_acc >= 90.0 else 'NO'}")
    print("=" * 70 + "\n")

    return metrics_payload


if __name__ == "__main__":
    evaluate_checkpoint()
