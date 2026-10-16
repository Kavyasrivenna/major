"""
Flask Application Server & REST API
===================================
Main server providing the interactive web interface, leaf image inference API,
Grad-CAM explainability generation, botanical encyclopedia search,
and one-click project ZIP download.
"""

import os
import uuid
import cv2
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify, send_file, url_for

import database
import cv_utils
from model import PlantInferenceEngine
import create_zip

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "static", "uploads")
MODELS_DIR = os.path.join(BASE_DIR, "models")
ZIP_PATH = os.path.join(BASE_DIR, "medicinal_plant_leaf_identification_system_updated.zip")

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024  # 32 MB max upload limit

# Initialize Deep Learning Inference Engine
inference_engine = PlantInferenceEngine()


# -------------------------------------------------------------
# WEB ROUTES
# -------------------------------------------------------------

@app.route("/")
def index():
    """Main identification studio & monograph dashboard."""
    return render_template("index.html")


@app.route("/encyclopedia")
def encyclopedia():
    """Browse and search the botanical pharmacopoeia encyclopedia."""
    plants = database.get_all_species()
    return render_template("encyclopedia.html", plants=plants)


@app.route("/species/<species_id>")
def plant_details(species_id):
    """Detailed standalone monograph page for an individual plant."""
    plant = database.get_plant_by_id(species_id)
    if not plant:
        return render_template("index.html"), 404
    return render_template("details.html", plant=plant)


@app.route("/about")
def about():
    """Methodology, system architecture, and viva examination guide."""
    return render_template("about.html")


@app.route("/download-zip")
def download_zip():
    """Download the complete project ZIP archive."""
    if not os.path.exists(ZIP_PATH):
        create_zip.create_project_zip(ZIP_PATH)
    return send_file(
        ZIP_PATH,
        mimetype="application/zip",
        as_attachment=True,
        download_name="medicinal_plant_leaf_identification_system_updated.zip"
    )


# -------------------------------------------------------------
# REST API ENDPOINTS
# -------------------------------------------------------------

@app.route("/api/identify", methods=["POST"])
def api_identify():
    """
    Accepts an uploaded leaf image, segments the blade, computes morphological descriptors,
    runs PyTorch classification, generates Grad-CAM heatmaps, and retrieves authoritative
    pharmacological records.
    """
    if "leaf_image" not in request.files:
        return jsonify({"error": "No leaf_image file found in multipart request"}), 400

    file = request.files["leaf_image"]
    if file.filename == "":
        return jsonify({"error": "Empty filename received. Please select an image file to upload."}), 400

    # 1. Format / Extension Validation
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext and ext not in allowed_extensions:
        return jsonify({
            "error": f"Unsupported file extension '{ext}'. Please upload an image file in JPG, PNG, WebP, or BMP format."
        }), 400

    # 2. Image Decoding & Integrity Validation
    try:
        pil_img = Image.open(file.stream)
        pil_img.verify()
    except Exception as img_err:
        return jsonify({
            "error": "The uploaded file could not be decoded as a valid image. It may be corrupted or not an image file."
        }), 400

    # Re-open after verify() to access pixel data
    try:
        file.stream.seek(0)
        pil_img = Image.open(file.stream).convert("RGB")
        
        # Verify minimum dimensions
        w, h = pil_img.size
        if w < 16 or h < 16:
            return jsonify({
                "error": f"Image dimensions ({w}x{h} px) are too small for morphological and neural network classification. Minimum size is 16x16 px."
            }), 400

        img_np = np.array(pil_img)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # 1. OpenCV Leaf Segmentation & Contour Extraction
        segmented_bgr, mask, contour = cv_utils.segment_leaf(img_bgr)
        morphology_metrics = cv_utils.extract_leaf_features(img_bgr, contour)
        contour_annotated_bgr = cv_utils.create_contour_overlay(img_bgr, contour)

        # Save annotated/segmented image
        scan_id = uuid.uuid4().hex[:10]
        seg_filename = f"seg_{scan_id}.jpg"
        seg_path = os.path.join(UPLOADS_DIR, seg_filename)
        cv2.imwrite(seg_path, contour_annotated_bgr)

        # 2. PyTorch Deep Learning Inference & Grad-CAM
        results = inference_engine.predict(
            pil_image=pil_img,
            top_k=3,
            generate_explainability=True
        )

        # Save Grad-CAM visualization
        gradcam_bgr = results.get("gradcam_overlay_bgr")
        gradcam_url = None
        if gradcam_bgr is not None:
            cam_filename = f"cam_{scan_id}.jpg"
            cam_path = os.path.join(UPLOADS_DIR, cam_filename)
            cv2.imwrite(cam_path, gradcam_bgr)
            gradcam_url = url_for("static", filename=f"uploads/{cam_filename}")

        seg_url = url_for("static", filename=f"uploads/{seg_filename}")

        response_payload = {
            "prediction": results["top_prediction"],
            "top_k": results["top_k"],
            "is_uncertain": results.get("is_uncertain", False),
            "uncertainty_message": results.get("uncertainty_message"),
            "monograph": results["monograph"],
            "morphology": morphology_metrics,
            "segmented_image_url": seg_url,
            "gradcam_image_url": gradcam_url,
            "checkpoint_status": results.get("checkpoint_status")
        }
        return jsonify(response_payload)

    except Exception as e:
        print(f"[ERROR] Inference pipeline failure: {e}")
        return jsonify({"error": f"Inference processing error: {str(e)}"}), 500


@app.route("/api/species/<species_id>", methods=["GET"])
def api_get_species(species_id):
    """Retrieve pharmacological monograph for a specific species ID."""
    monograph = database.get_plant_by_id(species_id)
    if not monograph:
        return jsonify({"error": f"Species '{species_id}' not found"}), 404
    return jsonify(monograph)


@app.route("/api/search", methods=["GET"])
def api_search():
    """Search database by query string."""
    q = request.args.get("q", "")
    results = database.search_plants(q)
    return jsonify({"query": q, "count": len(results), "results": results})


@app.route("/api/classes", methods=["GET"])
def api_get_classes():
    """List all registered species IDs and basic metadata."""
    classes = []
    for plant in database.get_all_species():
        classes.append({
            "id": plant["id"],
            "scientific_name": plant["scientific_name"],
            "common_names": plant["common_names"],
            "is_medicinal": plant["is_medicinal"],
            "medicinal_status": plant["medicinal_status"]
        })
    return jsonify({"total": len(classes), "classes": classes})


if __name__ == "__main__":
    print("\n" + "="*60)
    print("[+] PhytoMed AI: Medicinal Plant Identification & Monograph System")
    print("="*60)
    print("Serving web interface at: http://127.0.0.1:5000")
    print("REST API endpoint at:     http://127.0.0.1:5000/api/identify")
    print("="*60 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
