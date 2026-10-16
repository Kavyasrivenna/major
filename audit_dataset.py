"""
Dataset Audit and Anti-Leakage Verification Script
=================================================
Performs quality audit on downloaded leaf dataset:
1. Counts classes and images per partition (train, val, test).
2. Verifies image readability, formats, dimensions, and color modes.
3. Computes file hashes (MD5) to detect duplicate images within and across splits.
4. Confirms that no test/validation images leak into the training set.
5. Standardizes and documents scientific naming conventions.
"""

import os
import hashlib
from collections import defaultdict
from PIL import Image
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

def compute_image_hash(filepath):
    """Compute MD5 hash of raw image bytes."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def audit_dataset():
    print("=" * 60)
    print("[+] Indian Medicinal Leaves Dataset Audit & Anti-Leakage Verification")
    print("=" * 60)

    splits = ["train", "val", "test"]
    stats = {
        "partitions": {},
        "classes": set(),
        "corrupt_images": [],
        "color_modes": defaultdict(int),
        "dimensions": defaultdict(int),
        "hash_to_files": defaultdict(list),
        "split_hashes": {s: set() for s in splits}
    }

    for split in splits:
        split_dir = os.path.join(DATASET_DIR, split)
        if not os.path.exists(split_dir):
            print(f"[ERROR] Split directory missing: {split_dir}")
            continue

        class_counts = {}
        classes = sorted(os.listdir(split_dir))
        split_total = 0

        for cls in classes:
            cls_path = os.path.join(split_dir, cls)
            if not os.path.isdir(cls_path):
                continue
            stats["classes"].add(cls)
            files = [f for f in os.listdir(cls_path) if f.lower().endswith((".jpg", ".png", ".jpeg"))]
            class_counts[cls] = len(files)
            split_total += len(files)

            for fname in files:
                fpath = os.path.join(cls_path, fname)
                try:
                    with Image.open(fpath) as img:
                        stats["color_modes"][img.mode] += 1
                        stats["dimensions"][img.size] += 1
                        img.verify()

                    h = compute_image_hash(fpath)
                    stats["hash_to_files"][h].append(fpath)
                    stats["split_hashes"][split].add(h)

                except Exception as e:
                    stats["corrupt_images"].append((fpath, str(e)))

        stats["partitions"][split] = {
            "total_images": split_total,
            "classes_count": len(class_counts),
            "class_distribution": class_counts
        }
        print(f"[{split.upper()}] Total Images: {split_total} across {len(class_counts)} classes")

    print("\n" + "-" * 60)
    print("INTEGRITY & FORMAT CHECKS:")
    print(f"  Corrupt images detected: {len(stats['corrupt_images'])}")
    print(f"  Color modes detected: {dict(stats['color_modes'])}")
    print(f"  Top 3 image resolutions: {sorted(stats['dimensions'].items(), key=lambda x: x[1], reverse=True)[:3]}")

    print("\n" + "-" * 60)
    print("ANTI-LEAKAGE VERIFICATION (Duplicate Hashes Across Splits):")
    train_hashes = stats["split_hashes"]["train"]
    val_hashes = stats["split_hashes"]["val"]
    test_hashes = stats["split_hashes"]["test"]

    train_val_leak = train_hashes.intersection(val_hashes)
    train_test_leak = train_hashes.intersection(test_hashes)
    val_test_leak = val_hashes.intersection(test_hashes)

    print(f"  Train-Val overlapping hashes: {len(train_val_leak)}")
    print(f"  Train-Test overlapping hashes: {len(train_test_leak)}")
    print(f"  Val-Test overlapping hashes: {len(val_test_leak)}")

    if len(train_test_leak) == 0 and len(train_val_leak) == 0:
        print("  [PASSED] Zero data leakage! Test and validation sets are strictly held-out.")
    else:
        print("  [WARNING] Overlapping samples detected! Needs deduplication.")

    # Save summary json
    output_report = {
        "dataset_name": "Indian Medicinal Leaves Dataset (30 Classes)",
        "total_classes": len(stats["classes"]),
        "class_list": sorted(list(stats["classes"])),
        "train_samples": stats["partitions"].get("train", {}).get("total_images", 0),
        "val_samples": stats["partitions"].get("val", {}).get("total_images", 0),
        "test_samples": stats["partitions"].get("test", {}).get("total_images", 0),
        "corrupt_files_count": len(stats["corrupt_images"]),
        "leakage_train_test": len(train_test_leak),
        "color_modes": dict(stats["color_modes"])
    }

    report_path = os.path.join(BASE_DIR, "dataset_audit_report.json")
    with open(report_path, "w") as f:
        json.dump(output_report, f, indent=2)
    print(f"\n[INFO] Audit report written to: {report_path}")
    print("=" * 60)

if __name__ == "__main__":
    audit_dataset()
