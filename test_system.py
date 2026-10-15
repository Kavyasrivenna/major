"""
Automated Test Suite for PhytoMed AI System
===========================================
Validates knowledge base integrity, computer vision segmentation,
PyTorch deep learning inference, Grad-CAM explainability,
and Flask REST API endpoints.
"""

import os
import io
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

    def test_api_endpoints(self):
        """Verify REST API identification endpoint and JSON queries."""
        # Test /api/classes
        r_classes = self.app.get("/api/classes")
        self.assertEqual(r_classes.status_code, 200)
        data = r_classes.get_json()
        self.assertIn("total", data)
        self.assertGreater(data["total"], 0)

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
        self.assertTrue(res["prediction"]["confidence"] > 0)

    def test_zip_download_route(self):
        """Verify /download-zip endpoint serves the project zip."""
        r_zip = self.app.get("/download-zip")
        self.assertEqual(r_zip.status_code, 200)
        self.assertEqual(r_zip.headers["Content-Type"], "application/zip")


if __name__ == "__main__":
    unittest.main()
