"""
Dataset Pipeline, Duplicate & Near-Duplicate Auditing, and Leakage-Safe Splitting
================================================================================
Comprehensive pipeline for medicinal plant leaf datasets:
1. Local Dataset Scanning & Validation: format, corrupt images, dimensions, color modes.
2. Exact Duplicate Detection: SHA-256 byte-level collision analysis.
3. Dihedral Perceptual Hashing (D4-invariant dHash): detects flipped, rotated, resized,
   and visually augmented near-duplicate leaf images.
4. Specimen / Cluster Grouping: Disjoint Set Union (DSU) groups exact and near-duplicates.
5. Leakage-Safe Stratified Splitting: splits whole clusters atomically to guarantee zero leakage.
6. Dataset Provenance & Split Manifest Generation: exports reproducible manifests and provenance records.
7. Scientific Name & Class Mapping Validation: verifies all classes against the botanical knowledge base.
"""

import os
import sys
import json
import time
import hashlib
from collections import defaultdict
from typing import Dict, List, Tuple, Set, Any, Optional

import numpy as np
from PIL import Image

# Import local database for botanical monograph validation
try:
    import database
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import database

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA_DIR = os.path.join(BASE_DIR, "dataset")


# -----------------------------------------------------------------------------
# 1. Image Hashing (Exact & D4-Dihedral Invariant Perceptual Hash)
# -----------------------------------------------------------------------------

def compute_sha256(filepath: str) -> str:
    """Compute exact SHA-256 hash of file content."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        buf = f.read(65536)
        while buf:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()


def compute_dihedral_dhash(img: Image.Image, hash_size: int = 16) -> Tuple[int, int]:
    """
    Compute dihedral D4-invariant difference hash (dHash).
    Invariant under all 8 2D plane symmetries:
      - 0, 90, 180, 270 degree rotations
      - Horizontal / vertical flips

    Returns:
        (canonical_hash_int, canonical_hash_bits)
    """
    # Resize to square (hash_size, hash_size)
    gray = img.convert("L").resize((hash_size, hash_size), Image.Resampling.BILINEAR)
    pixels = np.array(gray, dtype=np.int32)

    # 8 dihedral transformations of the pixel grid
    transforms = [
        pixels,                                   # 0 deg
        np.rot90(pixels, 1),                      # 90 deg
        np.rot90(pixels, 2),                      # 180 deg
        np.rot90(pixels, 3),                      # 270 deg
        np.fliplr(pixels),                        # flip horizontal
        np.rot90(np.fliplr(pixels), 1),           # flip + rot90
        np.rot90(np.fliplr(pixels), 2),           # flip + rot180
        np.rot90(np.fliplr(pixels), 3),           # flip + rot270
    ]

    min_hash_int = None

    for grid in transforms:
        diff = grid[:, 1:] > grid[:, :-1]
        hash_val = 0
        for bit in diff.flatten():
            hash_val = (hash_val << 1) | int(bit)

        if min_hash_int is None or hash_val < min_hash_int:
            min_hash_int = hash_val

    return min_hash_int, hash_size * (hash_size - 1)


def hamming_distance(hash1: int, hash2: int) -> int:
    """Compute Hamming distance between two integer bitstrings."""
    x = hash1 ^ hash2
    return bin(x).count("1")


# -----------------------------------------------------------------------------
# 2. Disjoint Set Union (Union-Find) for Specimen Clustering
# -----------------------------------------------------------------------------

class UnionFind:
    """Disjoint Set Union with path compression and rank optimization."""
    def __init__(self, elements: List[str]):
        self.parent = {elem: elem for elem in elements}
        self.rank = {elem: 0 for elem in elements}

    def find(self, item: str) -> str:
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1: str, item2: str):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 == root2:
            return
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    def get_clusters(self) -> Dict[str, List[str]]:
        clusters = defaultdict(list)
        for item in self.parent:
            root = self.find(item)
            clusters[root].append(item)
        return dict(clusters)


# -----------------------------------------------------------------------------
# 3. Main Dataset Pipeline Class
# -----------------------------------------------------------------------------

class DatasetPipeline:
    """
    End-to-end dataset validation, deduplication, and leakage-safe splitting engine.
    """

    def __init__(self, dataset_dir: str = DEFAULT_DATA_DIR):
        self.dataset_dir = os.path.abspath(dataset_dir)
        self.images_metadata: Dict[str, Dict[str, Any]] = {}
        self.corrupt_files: List[Dict[str, str]] = []
        self.classes: List[str] = []
        self.class_validation: Dict[str, Dict[str, Any]] = {}
        self.exact_duplicates: Dict[str, List[str]] = defaultdict(list)
        self.near_duplicates: List[Dict[str, Any]] = []
        self.clusters: Dict[str, List[str]] = {}
        self.split_manifest: Dict[str, Any] = {}

    def scan_and_audit(self) -> Dict[str, Any]:
        """
        Inspect all images across partitions or raw folders.
        Verifies readability, dimensions, color modes, and SHA-256 hashes.
        """
        print(f"[+] Scanning dataset directory: {self.dataset_dir}")
        self.images_metadata.clear()
        self.corrupt_files.clear()

        # Check whether partitioned (train/val/test) or unpartitioned
        partitions = [p for p in ["train", "val", "test"] if os.path.isdir(os.path.join(self.dataset_dir, p))]
        scan_roots = [os.path.join(self.dataset_dir, p) for p in partitions] if partitions else [self.dataset_dir]

        found_classes = set()
        color_modes = defaultdict(int)
        dim_samples = defaultdict(int)

        for s_root in scan_roots:
            partition_name = os.path.basename(s_root) if partitions else "unassigned"
            for cls_name in sorted(os.listdir(s_root)):
                cls_dir = os.path.join(s_root, cls_name)
                if not os.path.isdir(cls_dir):
                    continue

                found_classes.add(cls_name)
                for fname in os.listdir(cls_dir):
                    if not fname.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                        continue

                    fpath = os.path.join(cls_dir, fname)
                    rel_path = os.path.relpath(fpath, self.dataset_dir).replace("\\", "/")

                    # Integrity verification
                    try:
                        with Image.open(fpath) as img:
                            mode = img.mode
                            width, height = img.size
                            img.verify()

                        # Re-open after verify() to test actual pixel decoding
                        with Image.open(fpath) as img:
                            img.convert("RGB")
                            dhash_val, total_bits = compute_dihedral_dhash(img, hash_size=16)

                        sha256_hash = compute_sha256(fpath)
                        color_modes[mode] += 1
                        dim_samples[f"{width}x{height}"] += 1

                        self.images_metadata[rel_path] = {
                            "relative_path": rel_path,
                            "absolute_path": fpath,
                            "filename": fname,
                            "class_name": cls_name,
                            "partition": partition_name,
                            "size_bytes": os.path.getsize(fpath),
                            "dimensions": [width, height],
                            "color_mode": mode,
                            "sha256": sha256_hash,
                            "dhash": dhash_val
                        }

                    except Exception as err:
                        self.corrupt_files.append({
                            "relative_path": rel_path,
                            "class_name": cls_name,
                            "error": str(err)
                        })

        self.classes = sorted(list(found_classes))
        self._validate_botanical_classes()

        print(f"[INFO] Scanned {len(self.images_metadata)} valid images across {len(self.classes)} classes.")
        print(f"[INFO] Corrupt / unreadable images detected: {len(self.corrupt_files)}")

        return {
            "total_valid_images": len(self.images_metadata),
            "total_classes": len(self.classes),
            "corrupt_count": len(self.corrupt_files),
            "color_modes": dict(color_modes),
            "top_dimensions": dict(sorted(dim_samples.items(), key=lambda x: x[1], reverse=True)[:5])
        }

    def _validate_botanical_classes(self):
        """Cross-reference detected dataset classes against the authoritative botanical knowledge base."""
        self.class_validation.clear()
        for c in self.classes:
            monograph = database.get_plant_by_id(c)
            if monograph:
                self.class_validation[c] = {
                    "matched": True,
                    "monograph_id": monograph["id"],
                    "scientific_name": monograph["scientific_name"],
                    "common_names": monograph["common_names"],
                    "botanical_family": monograph["botanical_family"],
                    "is_medicinal": monograph["is_medicinal"],
                    "medicinal_status": monograph["medicinal_status"]
                }
            else:
                self.class_validation[c] = {
                    "matched": False,
                    "monograph_id": None,
                    "scientific_name": c,
                    "common_names": [c],
                    "botanical_family": "Unknown",
                    "is_medicinal": False,
                    "medicinal_status": "Unverified Database Record"
                }

    def detect_duplicates_and_clusters(self, hamming_distance_threshold: int = 4) -> Dict[str, Any]:
        """
        Identifies:
        1. Exact byte-level duplicates (SHA-256 collision).
        2. Dihedral perceptual near-duplicates (rotation/flip/resize invariant within Hamming threshold).
        3. Groups images into Specimen Clusters to prevent cross-split leakage.
        """
        print(f"[+] Detecting exact duplicates and dihedral near-duplicates (Hamming dist <= {hamming_distance_threshold})...")
        
        # 1. Exact duplicates by SHA-256
        sha_map = defaultdict(list)
        for rel_path, meta in self.images_metadata.items():
            sha_map[meta["sha256"]].append(rel_path)

        self.exact_duplicates = {h: paths for h, paths in sha_map.items() if len(paths) > 1}

        # 2. Near-duplicates via dihedral dHash within the same class
        # Comparing pairs intra-class is botanically sound and prevents unrelated species clustering
        dsu = UnionFind(list(self.images_metadata.keys()))
        self.near_duplicates.clear()

        # Connect exact duplicates in DSU
        for paths in self.exact_duplicates.values():
            for p_other in paths[1:]:
                dsu.union(paths[0], p_other)

        # Group by class for intra-class pairwise perceptual comparison
        class_images = defaultdict(list)
        for rel_path, meta in self.images_metadata.items():
            class_images[meta["class_name"]].append(rel_path)

        for cls_name, paths in class_images.items():
            n = len(paths)
            for i in range(n):
                p1 = paths[i]
                h1 = self.images_metadata[p1]["dhash"]
                for j in range(i + 1, n):
                    p2 = paths[j]
                    h2 = self.images_metadata[p2]["dhash"]
                    dist = hamming_distance(h1, h2)

                    if dist <= hamming_distance_threshold:
                        dsu.union(p1, p2)
                        self.near_duplicates.append({
                            "class_name": cls_name,
                            "image1": p1,
                            "image2": p2,
                            "hamming_distance": dist,
                            "type": "exact_dihedral" if dist == 0 else "near_dihedral"
                        })

        self.clusters = dsu.get_clusters()
        multi_image_clusters = {k: v for k, v in self.clusters.items() if len(v) > 1}

        print(f"[INFO] Found {len(self.exact_duplicates)} exact duplicate sets.")
        print(f"[INFO] Found {len(self.near_duplicates)} near-duplicate pairs.")
        print(f"[INFO] Total grouped specimen clusters: {len(self.clusters)} ({len(multi_image_clusters)} multi-image clusters).")

        return {
            "exact_duplicate_sets": len(self.exact_duplicates),
            "near_duplicate_pairs": len(self.near_duplicates),
            "total_clusters": len(self.clusters),
            "multi_image_clusters": len(multi_image_clusters)
        }

    def verify_existing_split_leakage(self) -> Dict[str, Any]:
        """
        Audits existing train/val/test folders for cross-partition data leakage
        (both exact and near-duplicate leakage).
        """
        exact_cross_leakage = []
        near_cross_leakage = []

        # Check exact duplicates across partitions
        for h, paths in self.exact_duplicates.items():
            partitions = {self.images_metadata[p]["partition"] for p in paths}
            if len(partitions) > 1:
                exact_cross_leakage.append({"sha256": h, "partitions": list(partitions), "files": paths})

        # Check near duplicates across partitions
        for pair in self.near_duplicates:
            p1 = pair["image1"]
            p2 = pair["image2"]
            part1 = self.images_metadata[p1]["partition"]
            part2 = self.images_metadata[p2]["partition"]
            if part1 != part2 and part1 != "unassigned" and part2 != "unassigned":
                near_cross_leakage.append({
                    "image1": p1,
                    "partition1": part1,
                    "image2": p2,
                    "partition2": part2,
                    "distance": pair["hamming_distance"]
                })

        return {
            "exact_cross_leakage_count": len(exact_cross_leakage),
            "exact_cross_leakage_samples": exact_cross_leakage[:5],
            "near_cross_leakage_count": len(near_cross_leakage),
            "near_cross_leakage_samples": near_cross_leakage[:5]
        }

    def generate_reproducible_split(
        self,
        train_ratio: float = 0.70,
        val_ratio: float = 0.15,
        test_ratio: float = 0.15,
        random_seed: int = 42
    ) -> Dict[str, Any]:
        """
        Generates a leakage-safe split manifest.
        Atomic Unit: Specimen Clusters. Every cluster of related/duplicate images
        is assigned entirely to one split (Train, Val, or Test).
        """
        np.random.seed(random_seed)
        assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-4

        # Group clusters by botanical class
        clusters_by_class = defaultdict(list)
        for cluster_id, members in self.clusters.items():
            cls = self.images_metadata[members[0]]["class_name"]
            clusters_by_class[cls].append((cluster_id, members))

        split_assignments = {}
        partition_counts = {"train": 0, "val": 0, "test": 0}
        class_partition_distribution = defaultdict(lambda: {"train": 0, "val": 0, "test": 0})

        for cls, cls_clusters in sorted(clusters_by_class.items()):
            # Sort for deterministic shuffling
            cls_clusters = sorted(cls_clusters, key=lambda x: x[0])
            indices = np.random.permutation(len(cls_clusters))

            n = len(cls_clusters)
            n_train = max(1, int(round(n * train_ratio)))
            n_val = max(1, int(round(n * val_ratio)))
            # Remainder to test
            if n_train + n_val >= n:
                if n_val > 1:
                    n_val -= 1
                elif n_train > 1:
                    n_train -= 1

            for idx, cluster_idx in enumerate(indices):
                cluster_id, members = cls_clusters[cluster_idx]
                if idx < n_train:
                    assigned_partition = "train"
                elif idx < n_train + n_val:
                    assigned_partition = "val"
                else:
                    assigned_partition = "test"

                for m in members:
                    split_assignments[m] = {
                        "partition": assigned_partition,
                        "cluster_id": cluster_id,
                        "class_name": cls,
                        "sha256": self.images_metadata[m]["sha256"]
                    }
                    partition_counts[assigned_partition] += 1
                    class_partition_distribution[cls][assigned_partition] += 1

        self.split_manifest = {
            "metadata": {
                "generated_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
                "random_seed": random_seed,
                "split_ratios": {"train": train_ratio, "val": val_ratio, "test": test_ratio},
                "total_images": len(split_assignments),
                "total_clusters": len(self.clusters),
                "partition_counts": partition_counts
            },
            "class_distribution": dict(class_partition_distribution),
            "assignments": split_assignments
        }

        print(f"\n[LEAKAGE-SAFE SPLIT SUMMARY]")
        print(f"  Train samples: {partition_counts['train']} ({partition_counts['train']/len(split_assignments)*100:.1f}%)")
        print(f"  Val samples:   {partition_counts['val']} ({partition_counts['val']/len(split_assignments)*100:.1f}%)")
        print(f"  Test samples:  {partition_counts['test']} ({partition_counts['test']/len(split_assignments)*100:.1f}%)")

        return self.split_manifest

    def save_manifest_and_provenance(self, output_dir: Optional[str] = None):
        """Save dataset split manifest, provenance, and audit reports."""
        target_dir = output_dir or BASE_DIR
        os.makedirs(target_dir, exist_ok=True)

        manifest_path = os.path.join(target_dir, "dataset_split_manifest.json")
        provenance_path = os.path.join(target_dir, "dataset_provenance.json")
        audit_path = os.path.join(target_dir, "dataset_audit_report.json")

        # 1. Save split manifest
        if self.split_manifest:
            with open(manifest_path, "w") as f:
                json.dump(self.split_manifest, f, indent=2)
            print(f"[INFO] Saved reproducible split manifest to: {manifest_path}")

        # 2. Save comprehensive dataset provenance
        provenance_payload = {
            "dataset_title": "Indian Medicinal Leaves Dataset (30 Classes)",
            "primary_sources": [
                {
                    "name": "Hugging Face Hub (sanjeevani-ds/medicinal_leaves)",
                    "url": "https://huggingface.co/datasets/sanjeevani-ds/medicinal_leaves",
                    "repository_path": "Output folder"
                },
                {
                    "name": "Mendeley Data (Sachin et al., 2021)",
                    "doi": "10.17632/t256x42ms8.1",
                    "description": "Comprehensive leaf image dataset for Indian medicinal plants"
                }
            ],
            "total_species_classes": len(self.classes),
            "classes": self.classes,
            "botanical_validation": self.class_validation,
            "total_valid_images": len(self.images_metadata),
            "corrupt_files_detected": len(self.corrupt_files),
            "corrupt_files_details": self.corrupt_files,
            "exact_duplicate_sets": len(self.exact_duplicates),
            "near_duplicate_pairs": len(self.near_duplicates),
            "specimen_clusters": len(self.clusters),
            "anti_leakage_guarantee": "Strict cluster-level atomic partition assignment with D4 dihedral near-duplicate clustering",
            "last_audited": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        }

        with open(provenance_path, "w") as f:
            json.dump(provenance_payload, f, indent=2)
        print(f"[INFO] Saved dataset provenance report to: {provenance_path}")

        # 3. Save updated audit report
        leakage_status = self.verify_existing_split_leakage()
        audit_payload = {
            "dataset_name": "Indian Medicinal Leaves Dataset (30 Classes)",
            "total_classes": len(self.classes),
            "class_list": self.classes,
            "total_images": len(self.images_metadata),
            "corrupt_files_count": len(self.corrupt_files),
            "exact_duplicates_count": len(self.exact_duplicates),
            "near_duplicates_count": len(self.near_duplicates),
            "leakage_audit": leakage_status,
            "provenance_recorded": True,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        }

        with open(audit_path, "w") as f:
            json.dump(audit_payload, f, indent=2)
        print(f"[INFO] Saved updated dataset audit report to: {audit_path}")


def run_pipeline():
    """Command line entrypoint for running the dataset pipeline."""
    pipeline = DatasetPipeline()
    stats = pipeline.scan_and_audit()
    dupes = pipeline.detect_duplicates_and_clusters(hamming_distance_threshold=4)
    leakage = pipeline.verify_existing_split_leakage()
    
    print("\n" + "=" * 65)
    print("EXISTING PARTITION AUDIT:")
    print(f"  Exact cross-split leakage: {leakage['exact_cross_leakage_count']}")
    print(f"  Near-duplicate cross-split leakage: {leakage['near_cross_leakage_count']}")
    print("=" * 65)

    pipeline.generate_reproducible_split()
    pipeline.save_manifest_and_provenance()
    print("\n[SUCCESS] Dataset pipeline executed successfully.")


if __name__ == "__main__":
    run_pipeline()
