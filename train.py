"""
Deep Learning Training and Fine-Tuning Pipeline
=============================================
Provides a PyTorch training pipeline for retraining or fine-tuning
the medicinal plant classifier on custom leaf image datasets
(e.g., PlantVillage, Kaggle Indian Medicinal Leaves Dataset).

Usage:
    python train.py --data_dir ./dataset --epochs 25 --batch_size 16 --lr 0.0005
"""

import os
import argparse
import time
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

import database
from model import PlantLeafClassifier, IMAGE_SIZE, NORM_MEAN, NORM_STD

def get_data_transforms():
    """Data augmentation for training and standard normalization for validation."""
    train_transform = transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.2),
        transforms.RandomRotation(degrees=25),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=NORM_MEAN, std=NORM_STD)
    ])

    val_transform = transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=NORM_MEAN, std=NORM_STD)
    ])

    return train_transform, val_transform


def train_model(data_dir: str, epochs: int = 20, batch_size: int = 16, lr: float = 1e-4, save_path: str = "models/plant_classifier.pth"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Using device: {device}")

    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")

    if not os.path.exists(train_dir):
        print(f"[ERROR] Training directory '{train_dir}' not found.")
        print("Please structure your dataset as:")
        print("  dataset/")
        print("    ├── train/")
        print("    │   ├── ocimum_sanctum/")
        print("    │   └── azadirachta_indica/")
        print("    └── val/")
        return

    train_tf, val_tf = get_data_transforms()
    train_dataset = datasets.ImageFolder(train_dir, transform=train_tf)
    val_dataset = datasets.ImageFolder(val_dir, transform=val_tf) if os.path.exists(val_dir) else None

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2) if val_dataset else None

    num_classes = len(train_dataset.classes)
    print(f"[INFO] Detected {num_classes} plant classes: {train_dataset.classes}")

    model = PlantLeafClassifier(num_classes=num_classes).to(device)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-3)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    history = {"train_loss": [], "train_acc": [], "val_loss": [], "val_acc": []}
    best_acc = 0.0

    print(f"\n{'='*50}\nStarting Training Pipeline ({epochs} epochs)\n{'='*50}")
    start_time = time.time()

    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs, 1)
            correct += torch.sum(preds == labels.data).item()
            total += labels.size(0)

        epoch_train_loss = running_loss / total
        epoch_train_acc = (correct / total) * 100.0
        history["train_loss"].append(epoch_train_loss)
        history["train_acc"].append(epoch_train_acc)

        val_info = ""
        if val_loader:
            model.eval()
            val_loss = 0.0
            val_correct = 0
            val_total = 0
            with torch.no_grad():
                for images, labels in val_loader:
                    images, labels = images.to(device), labels.to(device)
                    outputs = model(images)
                    loss = criterion(outputs, labels)
                    val_loss += loss.item() * images.size(0)
                    _, preds = torch.max(outputs, 1)
                    val_correct += torch.sum(preds == labels.data).item()
                    val_total += labels.size(0)

            epoch_val_loss = val_loss / val_total
            epoch_val_acc = (val_correct / val_total) * 100.0
            history["val_loss"].append(epoch_val_loss)
            history["val_acc"].append(epoch_val_acc)
            val_info = f" | Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc:.2f}%"

            if epoch_val_acc > best_acc:
                best_acc = epoch_val_acc
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                torch.save(model.state_dict(), save_path)
        else:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            torch.save(model.state_dict(), save_path)

        scheduler.step()
        print(f"Epoch [{epoch:02d}/{epochs:02d}] - Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc:.2f}%{val_info}")

    total_time = time.time() - start_time
    print(f"\n[SUCCESS] Training completed in {total_time/60:.2f} minutes.")
    print(f"[INFO] Best model weights saved to: {save_path}")

    # Plot metrics curve
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history["train_loss"], label="Train Loss")
    if history["val_loss"]:
        plt.plot(history["val_loss"], label="Val Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss Trajectory")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history["train_acc"], label="Train Accuracy")
    if history["val_acc"]:
        plt.plot(history["val_acc"], label="Val Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy (%)")
    plt.title("Accuracy Trajectory")
    plt.legend()

    plot_path = os.path.join(os.path.dirname(save_path), "training_curves.png")
    plt.tight_layout()
    plt.savefig(plot_path)
    print(f"[INFO] Training plots saved to: {plot_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Medicinal Plant Classifier")
    parser.add_argument("--data_dir", type=str, default="./dataset", help="Path to dataset directory")
    parser.add_argument("--epochs", type=int, default=15, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=16, help="Batch size")
    parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--save_path", type=str, default="models/plant_classifier.pth", help="Path to save weights")
    args = parser.parse_args()

    train_model(args.data_dir, args.epochs, args.batch_size, args.lr, args.save_path)
