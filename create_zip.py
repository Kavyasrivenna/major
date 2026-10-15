"""
Project ZIP Packaging Utility
=============================
Archives the complete medicinal plant identification and knowledge retrieval
codebase, templates, database, pre-trained weights, sample images, and documentation
into a clean, submission-ready ZIP file.
"""

import os
import zipfile
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_FILENAME = "medicinal_plant_leaf_identification_system.zip"
ZIP_OUTPUT_PATH = os.path.join(BASE_DIR, ZIP_FILENAME)

# Files and directories to include in the submission zip
INCLUDE_FILES = [
    "app.py",
    "model.py",
    "cv_utils.py",
    "database.py",
    "train.py",
    "sample_data_setup.py",
    "test_system.py",
    "create_zip.py",
    "requirements.txt",
    "README.md",
]

INCLUDE_DIRS = [
    "templates",
    "static",
    "models"
]

EXCLUDE_EXTENSIONS = [".pyc", ".log", ".tmp"]
EXCLUDE_DIRS = ["__pycache__", ".git", ".idea", ".vscode", "scratch"]

def create_project_zip(output_path: str = ZIP_OUTPUT_PATH) -> str:
    print(f"[INFO] Creating project archive at: {output_path}")
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
                print(f"  + Added: {filename}")

        # Add directories
        for dirname in INCLUDE_DIRS:
            dirpath = os.path.join(BASE_DIR, dirname)
            if not os.path.exists(dirpath):
                continue
            for root, dirs, files in os.walk(dirpath):
                # Filter out excluded directories
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                for file in files:
                    if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, BASE_DIR)
                    arcname = os.path.join("medicinal_plant_project", rel_path)
                    zipf.write(full_path, arcname=arcname)
                    count += 1
                    total_bytes += os.path.getsize(full_path)
                    print(f"  + Added: {rel_path}")

    mb = total_bytes / (1024 * 1024)
    print(f"[SUCCESS] Packaged {count} files ({mb:.2f} MB) into '{output_path}'.")
    return output_path

if __name__ == "__main__":
    create_project_zip()
