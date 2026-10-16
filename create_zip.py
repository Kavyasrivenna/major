"""
Project ZIP Packaging Utility
=============================
Archives the complete medicinal plant identification and knowledge retrieval
codebase, templates, database, genuine pre-trained weights, evaluation reports,
manifests, and documentation into a clean, submission-ready ZIP file:
medicinal_plant_leaf_identification_system_updated.zip
"""

import os
import zipfile
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_FILENAME = "medicinal_plant_leaf_identification_system_updated.zip"
ZIP_OUTPUT_PATH = os.path.join(BASE_DIR, ZIP_FILENAME)

# Files and directories to include in the submission zip
INCLUDE_FILES = [
    "app.py",
    "model.py",
    "cv_utils.py",
    "database.py",
    "dataset_pipeline.py",
    "evaluate.py",
    "train.py",
    "audit_dataset.py",
    "download_dataset.py",
    "sample_data_setup.py",
    "test_system.py",
    "create_zip.py",
    "requirements.txt",
    "README.md",
    "IMPLEMENTATION_REPORT.md",
    "dataset_split_manifest.json",
    "dataset_provenance.json",
    "dataset_audit_report.json"
]

INCLUDE_DIRS = [
    "templates",
    "static",
    "models",
    "evaluation"
]

EXCLUDE_EXTENSIONS = [".pyc", ".log", ".tmp", ".pyo"]
EXCLUDE_DIRS = ["__pycache__", ".git", ".idea", ".vscode", "scratch", "venv", "dataset"]

def create_project_zip(output_path: str = ZIP_OUTPUT_PATH) -> str:
    print("=" * 65)
    print(f"[INFO] Creating updated project archive at: {output_path}")
    print("=" * 65)
    count = 0
    total_bytes = 0

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add root files
        for filename in INCLUDE_FILES:
            filepath = os.path.join(BASE_DIR, filename)
            if os.path.exists(filepath):
                zipf.write(filepath, arcname=os.path.join("medicinal_plant_project", filename))
                count += 1
                total_bytes += os.path.getsize(filepath)
                print(f"  + Added file: {filename}")
            else:
                print(f"  - Notice: file '{filename}' not found on disk, skipping.")

        # Add directories
        for dirname in INCLUDE_DIRS:
            dirpath = os.path.join(BASE_DIR, dirname)
            if not os.path.exists(dirpath):
                continue
            for root, dirs, files in os.walk(dirpath):
                # Filter out excluded directories
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

                # If static/uploads, skip dynamically uploaded images
                if os.path.normpath(root).endswith(os.path.normpath(os.path.join("static", "uploads"))):
                    continue

                for file in files:
                    if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, BASE_DIR)
                    arcname = os.path.join("medicinal_plant_project", rel_path)
                    zipf.write(full_path, arcname=arcname)
                    count += 1
                    total_bytes += os.path.getsize(full_path)
                    print(f"  + Added asset: {rel_path}")

    mb = total_bytes / (1024 * 1024)
    zip_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n[SUCCESS] Packaged {count} files ({mb:.2f} MB uncompressed, {zip_size_mb:.2f} MB compressed) into:")
    print(f"  -> '{output_path}'")

    # Verify ZIP integrity
    print("\n[+] Verifying ZIP archive integrity...")
    with zipfile.ZipFile(output_path, "r") as test_zipf:
        bad_file = test_zipf.testzip()
        if bad_file:
            print(f"[ERROR] Corrupted file found in ZIP: {bad_file}")
            raise zipfile.BadZipFile(f"Corrupt file in archive: {bad_file}")
        namelist = test_zipf.namelist()
        print(f"[VERIFIED] Archive tested successfully: {len(namelist)} entries found, zero CRC errors.")

    return output_path

if __name__ == "__main__":
    create_project_zip()
