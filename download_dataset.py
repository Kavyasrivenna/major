"""
Dataset Acquisition Script
==========================
Downloads the Indian Medicinal Leaves Dataset (30 plant species, 1,833 images)
from the verified public repository (sanjeevani-ds / Indian Medicinal Leaves Dataset).
Saves images into dataset/train, dataset/val, and dataset/test partitions.
"""

import os
import sys
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

HF_API_URL = "https://huggingface.co/api/datasets/sanjeevani-ds/medicinal_leaves"
HF_BASE_RESOLVE = "https://huggingface.co/datasets/sanjeevani-ds/medicinal_leaves/resolve/main"

def fetch_file_list():
    """Fetch the full list of files in the repository."""
    print("[INFO] Querying repository file listing from HuggingFace...")
    req = urllib.request.Request(HF_API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        info = json.loads(r.read().decode("utf-8"))
    
    siblings = [f["rfilename"] for f in info.get("siblings", [])]
    # Filter only Output folder images
    target_files = [f for f in siblings if f.startswith("Output folder/") and f.lower().endswith((".jpg", ".png", ".jpeg"))]
    print(f"[INFO] Found {len(target_files)} leaf images across train/val/test partitions.")
    return target_files

def download_single_file(rel_path):
    """Download and verify a single image file."""
    # Convert 'Output folder/train/Ocimum Tenuiflorum (Tulsi)/...' to 'dataset/train/...'
    parts = rel_path.split("/")
    split_name = parts[1]  # train, val, test
    class_name = parts[2]
    filename = parts[3]

    target_dir = os.path.join(DATASET_DIR, split_name, class_name)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)

    if os.path.exists(target_path) and os.path.getsize(target_path) > 1024:
        return True, "cached"

    quoted_rel = urllib.parse.quote(rel_path)
    url = f"{HF_BASE_RESOLVE}/{quoted_rel}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                content = response.read()
            with open(target_path, "wb") as f:
                f.write(content)
            
            # Verify image integrity
            with Image.open(target_path) as img:
                img.verify()
            return True, "downloaded"
        except Exception as e:
            if attempt == max_retries - 1:
                if os.path.exists(target_path):
                    os.remove(target_path)
                return False, f"Failed: {e}"
            time.sleep(1)

def download_dataset(max_workers=10):
    os.makedirs(DATASET_DIR, exist_ok=True)
    files = fetch_file_list()
    total = len(files)

    print(f"[INFO] Starting download of {total} images using {max_workers} worker threads...")
    start_time = time.time()
    downloaded = 0
    cached = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_single_file, f): f for f in files}
        for i, future in enumerate(as_completed(futures), 1):
            success, status = future.result()
            if success:
                if status == "cached":
                    cached += 1
                else:
                    downloaded += 1
            else:
                failed += 1
                print(f"[WARN] Error on {futures[future]}: {status}")

            if i % 150 == 0 or i == total:
                elapsed = time.time() - start_time
                print(f"  Progress: {i}/{total} ({i/total*100:.1f}%) | Downloaded: {downloaded} | Cached: {cached} | Failed: {failed} | Time: {elapsed:.1f}s")

    total_time = time.time() - start_time
    print(f"\n[SUCCESS] Dataset download finished in {total_time:.1f} seconds.")
    print(f"  Summary: {downloaded} new downloads, {cached} cached, {failed} failures.")

if __name__ == "__main__":
    download_dataset(max_workers=12)
