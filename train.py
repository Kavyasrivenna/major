"""
Reproducible Training & Evaluation Pipeline for Medicinal Plant Leaf Classification
===================================================================================
Fine-tunes MobileNetV3-Large on the Indian Medicinal Leaves Dataset (30 classes),
saves the best validation checkpoint with complete metadata, and performs comprehensive
evaluation on the held-out test partition.
"""

import os
import sys
import time
import json
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for headless execution
import matplotlib.pyplot as plt
import seaborn as sns

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

# Global configuration constants
IMAGE_SIZE = 224
NORM_MEAN = [0.485, 0.456, 0.406]
NORM_STD = [0.229, 0.224, 0.225]

def get_transforms():
    """Build train and validation/test transforms."""
    train_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomResizedCrop(IMAGE_SIZE, scale=(0.8, 1.0)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.2),
        transforms.RandomRotation(degrees=20),
        transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.15),
        transforms.ToTensor(),
        transforms.Normalize(mean=NORM_MEAN, std=NORM_STD)
    ])

    eval_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(IMAGE_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(mean=NORM_MEAN, std=NORM_STD)
    ])
    return train_tf, eval_tf

class ManifestDataset(torch.utils.data.Dataset):
    """Dataset loaded deterministically from a leakage-safe split manifest."""
    def __init__(self, manifest_path: str, partition: str, data_root: str, transform=None):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        self.samples = []
        all_classes = sorted(list({entry["class_name"] for entry in manifest["assignments"].values()}))
        self.classes = all_classes
        self.class_to_idx = {c: i for i, c in enumerate(all_classes)}
        for rel_path, entry in manifest["assignments"].items():
            if entry["partition"] == partition:
                full_path = os.path.join(data_root, rel_path)
                if os.path.exists(full_path):
                    self.samples.append((full_path, self.class_to_idx[entry["class_name"]]))
        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, target = self.samples[idx]
        with Image.open(path) as img:
            img = img.convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, target

def build_model(num_classes, pretrained=True):
    """Construct MobileNetV3-Large with customized dense classification head."""
    if pretrained:
        weights = models.MobileNet_V3_Large_Weights.DEFAULT
        model = models.mobilenet_v3_large(weights=weights)
    else:
        model = models.mobilenet_v3_large(weights=None)

    in_features = 960
    model.classifier = nn.Sequential(
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
    return model

def compute_metrics(y_true, y_pred, y_probs, class_names):
    """Compute top-1, top-3 accuracy, macro precision/recall/F1, and per-class stats."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_probs = np.array(y_probs)
    num_samples = len(y_true)
    num_classes = len(class_names)

    # Top-1 Accuracy
    top1_acc = np.mean(y_true == y_pred) * 100.0

    # Top-3 Accuracy
    top3_correct = 0
    for i in range(num_samples):
        top3_indices = np.argsort(y_probs[i])[::-1][:3]
        if y_true[i] in top3_indices:
            top3_correct += 1
    top3_acc = (top3_correct / num_samples) * 100.0

    # Per-class metrics
    per_class = {}
    precisions, recalls, f1s = [], [], []

    for c_idx, c_name in enumerate(class_names):
        tp = np.sum((y_pred == c_idx) & (y_true == c_idx))
        fp = np.sum((y_pred == c_idx) & (y_true != c_idx))
        fn = np.sum((y_pred != c_idx) & (y_true == c_idx))
        support = np.sum(y_true == c_idx)

        prec = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
        rec = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        f1 = float(2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

        precisions.append(prec)
        recalls.append(rec)
        f1s.append(f1)

        per_class[c_name] = {
            "precision": round(prec * 100, 2),
            "recall": round(rec * 100, 2),
            "f1_score": round(f1 * 100, 2),
            "support": int(support)
        }

    macro_precision = float(np.mean(precisions)) * 100.0
    macro_recall = float(np.mean(recalls)) * 100.0
    macro_f1 = float(np.mean(f1s)) * 100.0

    # Confusion matrix
    cm = np.zeros((num_classes, num_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1

    return {
        "top1_accuracy": round(top1_acc, 2),
        "top3_accuracy": round(top3_acc, 2),
        "macro_precision": round(macro_precision, 2),
        "macro_recall": round(macro_recall, 2),
        "macro_f1": round(macro_f1, 2),
        "per_class": per_class,
        "confusion_matrix": cm.tolist()
    }

def train_and_evaluate(
    data_dir="./dataset",
    manifest_path=None,
    epochs_head=6,
    epochs_fine=10,
    batch_size=32,
    save_path="models/plant_classifier.pth",
    resume_path=None,
    evaluate_only=False
):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Using device: {device}")

    eval_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evaluation")
    os.makedirs(eval_dir, exist_ok=True)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    if evaluate_only:
        from evaluate import evaluate_checkpoint
        target_ckpt = resume_path or save_path
        test_dir = os.path.join(data_dir, "test")
        print(f"[INFO] Running in evaluate-only mode using checkpoint: {target_ckpt}")
        return evaluate_checkpoint(checkpoint_path=target_ckpt, test_dir=test_dir, batch_size=batch_size)

    train_tf, eval_tf = get_transforms()

    if manifest_path and os.path.exists(manifest_path):
        print(f"[INFO] Loading datasets from reproducible manifest: {manifest_path}")
        train_ds = ManifestDataset(manifest_path, "train", data_dir, transform=train_tf)
        val_ds = ManifestDataset(manifest_path, "val", data_dir, transform=eval_tf)
        test_ds = ManifestDataset(manifest_path, "test", data_dir, transform=eval_tf)
        class_names = train_ds.classes
        num_classes = len(class_names)
        class_to_idx = train_ds.class_to_idx
        idx_to_class = {v: k for k, v in class_to_idx.items()}
    else:
        train_dir = os.path.join(data_dir, "train")
        val_dir = os.path.join(data_dir, "val")
        test_dir = os.path.join(data_dir, "test")

        train_ds = datasets.ImageFolder(train_dir, transform=train_tf)
        val_ds = datasets.ImageFolder(val_dir, transform=eval_tf)
        test_ds = datasets.ImageFolder(test_dir, transform=eval_tf)

        class_names = train_ds.classes
        num_classes = len(class_names)
        class_to_idx = train_ds.class_to_idx
        idx_to_class = {v: k for k, v in class_to_idx.items()}

    print(f"[INFO] Loaded dataset with {num_classes} classes.")
    print(f"  Train samples: {len(train_ds)} | Val samples: {len(val_ds)} | Test samples: {len(test_ds)}")

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, num_workers=0)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=0)

    model = build_model(num_classes, pretrained=(resume_path is None)).to(device)

    start_epoch = 1
    best_val_acc = 0.0
    history = {
        "train_loss": [], "train_acc": [],
        "val_loss": [], "val_acc": []
    }

    if resume_path and os.path.exists(resume_path):
        print(f"[INFO] Resuming training from checkpoint: {resume_path}")
        ckpt = torch.load(resume_path, map_location=device, weights_only=False)
        if isinstance(ckpt, dict) and "state_dict" in ckpt:
            model.load_state_dict(ckpt["state_dict"])
            best_val_acc = float(ckpt.get("best_val_accuracy", 0.0))
            if "training_metadata" in ckpt and "history" in ckpt["training_metadata"]:
                history = ckpt["training_metadata"]["history"]
            print(f"[INFO] Restored weights. Previous best validation accuracy: {best_val_acc:.2f}%")
        else:
            model.load_state_dict(ckpt)
            print(f"[INFO] Restored raw state_dict.")

    criterion = nn.CrossEntropyLoss(label_smoothing=0.08)
    best_weights = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    # =========================================================================
    # STAGE 1: Classifier Head Warmup (features frozen)
    # =========================================================================
    print("\n" + "=" * 65)
    print(f"STAGE 1: Classifier Head Training ({epochs_head} epochs, backbone frozen)")
    print("=" * 65)

    for param in model.features.parameters():
        param.requires_grad = False

    optimizer_head = torch.optim.AdamW(model.classifier.parameters(), lr=1.5e-3, weight_decay=1e-4)
    scheduler_head = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer_head, T_max=epochs_head)

    total_epochs = epochs_head + epochs_fine
    current_epoch = 1

    for epoch in range(1, epochs_head + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for imgs, lbls in train_loader:
            imgs, lbls = imgs.to(device), lbls.to(device)
            optimizer_head.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, lbls)
            loss.backward()
            optimizer_head.step()

            running_loss += loss.item() * imgs.size(0)
            preds = outputs.argmax(dim=1)
            correct += (preds == lbls).sum().item()
            total += lbls.size(0)

        tr_loss = running_loss / total
        tr_acc = (correct / total) * 100.0

        # Validation
        model.eval()
        v_loss = 0.0
        v_correct = 0
        v_total = 0
        with torch.no_grad():
            for imgs, lbls in val_loader:
                imgs, lbls = imgs.to(device), lbls.to(device)
                outputs = model(imgs)
                loss = criterion(outputs, lbls)
                v_loss += loss.item() * imgs.size(0)
                preds = outputs.argmax(dim=1)
                v_correct += (preds == lbls).sum().item()
                v_total += lbls.size(0)

        val_loss = v_loss / v_total
        val_acc = (v_correct / v_total) * 100.0

        history["train_loss"].append(tr_loss)
        history["train_acc"].append(tr_acc)
        history["val_loss"].append(val_loss)
        history["val_acc"].append(val_acc)

        scheduler_head.step()

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_weights = {k: v.cpu().clone() for k, v in model.state_dict().items()}

        print(f"Epoch [{current_epoch:02d}/{total_epochs:02d}] (Head) - Loss: {tr_loss:.4f} | Acc: {tr_acc:.2f}% | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.2f}% (Best: {best_val_acc:.2f}%)")
        current_epoch += 1

    # =========================================================================
    # STAGE 2: End-to-End Fine-Tuning (unfreeze top backbone layers)
    # =========================================================================
    print("\n" + "=" * 65)
    print(f"STAGE 2: End-to-End Fine-Tuning ({epochs_fine} epochs)")
    print("=" * 65)

    # Unfreeze high-level feature layers
    for param in model.features[-6:].parameters():
        param.requires_grad = True

    optimizer_fine = torch.optim.AdamW([
        {"params": model.features[-6:].parameters(), "lr": 1e-4},
        {"params": model.classifier.parameters(), "lr": 5e-4}
    ], weight_decay=1e-4)
    scheduler_fine = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer_fine, T_max=epochs_fine)

    for epoch in range(1, epochs_fine + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for imgs, lbls in train_loader:
            imgs, lbls = imgs.to(device), lbls.to(device)
            optimizer_fine.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, lbls)
            loss.backward()
            optimizer_fine.step()

            running_loss += loss.item() * imgs.size(0)
            preds = outputs.argmax(dim=1)
            correct += (preds == lbls).sum().item()
            total += lbls.size(0)

        tr_loss = running_loss / total
        tr_acc = (correct / total) * 100.0

        # Validation
        model.eval()
        v_loss = 0.0
        v_correct = 0
        v_total = 0
        with torch.no_grad():
            for imgs, lbls in val_loader:
                imgs, lbls = imgs.to(device), lbls.to(device)
                outputs = model(imgs)
                loss = criterion(outputs, lbls)
                v_loss += loss.item() * imgs.size(0)
                preds = outputs.argmax(dim=1)
                v_correct += (preds == lbls).sum().item()
                v_total += lbls.size(0)

        val_loss = v_loss / v_total
        val_acc = (v_correct / v_total) * 100.0

        history["train_loss"].append(tr_loss)
        history["train_acc"].append(tr_acc)
        history["val_loss"].append(val_loss)
        history["val_acc"].append(val_acc)

        scheduler_fine.step()

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_weights = {k: v.cpu().clone() for k, v in model.state_dict().items()}

        print(f"Epoch [{current_epoch:02d}/{total_epochs:02d}] (Fine) - Loss: {tr_loss:.4f} | Acc: {tr_acc:.2f}% | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.2f}% (Best: {best_val_acc:.2f}%)")
        current_epoch += 1

    # =========================================================================
    # HELD-OUT TEST EVALUATION
    # =========================================================================
    print("\n" + "=" * 65)
    print("EVALUATING ON UNTOUCHED HELD-OUT TEST SET (207 images)")
    print("=" * 65)

    # Load best weights
    model.load_state_dict(best_weights)
    model.eval()

    all_preds = []
    all_targets = []
    all_probs = []

    with torch.no_grad():
        for imgs, lbls in test_loader:
            imgs = imgs.to(device)
            outputs = model(imgs)
            probs = torch.softmax(outputs, dim=1).cpu().numpy()
            preds = np.argmax(probs, axis=1)

            all_preds.extend(preds)
            all_targets.extend(lbls.numpy())
            all_probs.extend(probs)

    test_metrics = compute_metrics(all_targets, all_preds, all_probs, class_names)

    print(f"\n[FINAL TEST RESULTS]")
    print(f"  Top-1 Accuracy:   {test_metrics['top1_accuracy']}%")
    print(f"  Top-3 Accuracy:   {test_metrics['top3_accuracy']}%")
    print(f"  Macro Precision:  {test_metrics['macro_precision']}%")
    print(f"  Macro Recall:     {test_metrics['macro_recall']}%")
    print(f"  Macro F1-Score:   {test_metrics['macro_f1']}%")

    if test_metrics['top1_accuracy'] >= 90.0:
        print(f"  >>> TARGET MET: Top-1 Test Accuracy ({test_metrics['top1_accuracy']}%) >= 90.0% <<<")
    else:
        print(f"  >>> NOTE: Top-1 Test Accuracy is {test_metrics['top1_accuracy']}% <<<")

    # Save Checkpoint with Complete Metadata
    checkpoint_payload = {
        "architecture": "MobileNetV3-Large",
        "state_dict": best_weights,
        "num_classes": num_classes,
        "classes": class_names,
        "class_to_idx": class_to_idx,
        "idx_to_class": idx_to_class,
        "input_size": (IMAGE_SIZE, IMAGE_SIZE),
        "norm_mean": NORM_MEAN,
        "norm_std": NORM_STD,
        "best_val_accuracy": round(best_val_acc, 2),
        "test_metrics": {
            "top1_accuracy": test_metrics["top1_accuracy"],
            "top3_accuracy": test_metrics["top3_accuracy"],
            "macro_precision": test_metrics["macro_precision"],
            "macro_recall": test_metrics["macro_recall"],
            "macro_f1": test_metrics["macro_f1"]
        },
        "training_metadata": {
            "dataset": "Indian Medicinal Leaves Dataset (30 classes)",
            "train_samples": len(train_ds),
            "val_samples": len(val_ds),
            "test_samples": len(test_ds),
            "epochs_head": epochs_head,
            "epochs_fine": epochs_fine,
            "optimizer": "AdamW",
            "scheduler": "CosineAnnealingLR"
        }
    }

    torch.save(checkpoint_payload, save_path)
    print(f"\n[INFO] Saved compatible model checkpoint with metadata to: {save_path}")

    # Save metrics JSON
    metrics_path = os.path.join(eval_dir, "evaluation_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(test_metrics, f, indent=2)
    print(f"[INFO] Saved evaluation metrics to: {metrics_path}")

    # Plot Confusion Matrix
    cm = np.array(test_metrics["confusion_matrix"])
    plt.figure(figsize=(14, 12))
    sns.heatmap(cm, annot=False, cmap="Blues", fmt="d",
                xticklabels=[c.split(" (")[0] for c in class_names],
                yticklabels=[c.split(" (")[0] for c in class_names])
    plt.title(f"Confusion Matrix on Held-Out Test Set (Top-1 Acc: {test_metrics['top1_accuracy']}%)", fontsize=13, pad=15)
    plt.xlabel("Predicted Species", fontsize=11)
    plt.ylabel("True Species", fontsize=11)
    plt.xticks(rotation=90, fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.tight_layout()
    cm_path = os.path.join(eval_dir, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=200)
    plt.close()
    print(f"[INFO] Saved confusion matrix to: {cm_path}")

    # Plot Learning Curves
    plt.figure(figsize=(10, 4.5))
    plt.subplot(1, 2, 1)
    plt.plot(history["train_loss"], label="Train Loss", color="#059669", linewidth=2)
    plt.plot(history["val_loss"], label="Val Loss", color="#dc2626", linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Cross-Entropy Loss Trajectory")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.subplot(1, 2, 2)
    plt.plot(history["train_acc"], label="Train Acc", color="#059669", linewidth=2)
    plt.plot(history["val_acc"], label="Val Acc", color="#2563eb", linewidth=2)
    plt.axhline(y=90.0, color="#d97706", linestyle=":", label="90% Target")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy (%)")
    plt.title("Accuracy Trajectory")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    curves_path = os.path.join(eval_dir, "training_curves.png")
    plt.savefig(curves_path, dpi=200)
    plt.close()
    print(f"[INFO] Saved training curves to: {curves_path}")

    return test_metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train & Evaluate Medicinal Plant Classifier")
    parser.add_argument("--data_dir", type=str, default="./dataset", help="Path to dataset directory")
    parser.add_argument("--manifest", type=str, default=None, help="Path to reproducible dataset split manifest")
    parser.add_argument("--epochs_head", type=int, default=6, help="Warmup epochs for classifier head")
    parser.add_argument("--epochs_fine", type=int, default=10, help="Fine-tuning epochs for backbone")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--save_path", type=str, default="models/plant_classifier.pth", help="Checkpoint save path")
    parser.add_argument("--resume", type=str, default=None, help="Resume training from existing checkpoint")
    parser.add_argument("--evaluate_only", action="store_true", help="Evaluate checkpoint on held-out test set without training")
    args = parser.parse_args()

    train_and_evaluate(
        data_dir=args.data_dir,
        manifest_path=args.manifest,
        epochs_head=args.epochs_head,
        epochs_fine=args.epochs_fine,
        batch_size=args.batch_size,
        save_path=args.save_path,
        resume_path=args.resume,
        evaluate_only=args.evaluate_only
    )
