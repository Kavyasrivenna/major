"""
Computer Vision Utilities for Leaf Segmentation and Morphological Feature Extraction
=====================================================================================
Processes leaf images using OpenCV to isolate the leaf blade from noisy backgrounds,
compute botanical morphological descriptors (circularity, aspect ratio, venation contrast),
and generate visual diagnostic overlays.
"""

import cv2
import numpy as np
from typing import Tuple, Dict, Any, Optional

def segment_leaf(image_bgr: np.ndarray) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
    """
    Segment the leaf blade from background using multi-channel color thresholding
    and morphological cleanup.

    Returns:
        (segmented_bgr, binary_mask, largest_contour)
    """
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)

    # 1. Green color thresholding in HSV space
    lower_green = np.array([20, 25, 25])
    upper_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 2. Otsu thresholding on Lab 'a' channel (green-red opponent channel)
    # Green leaves have low values in 'a' channel
    a_channel = lab[:, :, 1]
    _, otsu_mask = cv2.threshold(a_channel, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Combine masks
    combined = cv2.bitwise_or(green_mask, otsu_mask)

    # Morphological noise removal
    kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel_large = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    opened = cv2.morphologyEx(combined, cv2.MORPH_OPEN, kernel_small, iterations=2)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_large, iterations=2)

    # Find largest contour (presumed leaf blade)
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        # Recreate clean single-contour mask
        final_mask = np.zeros_like(closed)
        cv2.drawContours(final_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
    else:
        largest_contour = None
        final_mask = closed

    # Apply mask with clean neutral background (soft white)
    bg = np.full_like(image_bgr, 245)
    mask_3ch = cv2.merge([final_mask, final_mask, final_mask]) / 255.0
    segmented = (image_bgr * mask_3ch + bg * (1.0 - mask_3ch)).astype(np.uint8)

    return segmented, final_mask, largest_contour

def extract_leaf_features(image_bgr: np.ndarray, contour: Optional[np.ndarray]) -> Dict[str, Any]:
    """
    Extract geometric, colorimetric, and venation texture metrics from leaf image.
    """
    h, w, _ = image_bgr.shape
    features: Dict[str, Any] = {
        "dimensions": f"{w} x {h} px",
        "aspect_ratio": 1.0,
        "circularity": 0.0,
        "solidity": 0.0,
        "extent": 0.0,
        "leaf_area_pct": 0.0,
        "vein_texture_density": 0.0,
        "color_profile": {
            "mean_green_intensity": 0,
            "mean_chlorophyll_hue": 0,
            "saturation_index": 0
        },
        "morphology_class": "Undetermined"
    }

    if contour is not None and len(contour) >= 5:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        total_pixels = h * w

        if perimeter > 0:
            # Form factor / Circularity: 4 * pi * Area / Perimeter^2
            circularity = (4.0 * np.pi * area) / (perimeter ** 2)
            features["circularity"] = round(float(circularity), 3)

        # Bounding rectangle
        bx, by, bw, bh = cv2.boundingRect(contour)
        aspect_ratio = float(bw) / float(bh) if bh > 0 else 1.0
        features["aspect_ratio"] = round(aspect_ratio, 3)

        # Extent: Area / Bounding Rect Area
        rect_area = bw * bh
        if rect_area > 0:
            features["extent"] = round(float(area / rect_area), 3)

        # Convex Hull and Solidity
        hull = cv2.convexHull(contour)
        hull_area = cv2.contourArea(hull)
        if hull_area > 0:
            features["solidity"] = round(float(area / hull_area), 3)

        features["leaf_area_pct"] = round(float((area / total_pixels) * 100), 1)

        # Leaf shape classification based on aspect ratio and circularity
        if circularity > 0.65:
            features["morphology_class"] = "Orbicular / Reniform (Rounded leaf)"
        elif aspect_ratio > 1.8:
            features["morphology_class"] = "Lanceolate / Linear (Elongated narrow leaf)"
        elif 0.8 <= aspect_ratio <= 1.5 and circularity > 0.4:
            features["morphology_class"] = "Ovate / Cordate (Heart or Egg-shaped)"
        else:
            features["morphology_class"] = "Elliptic / Oblong (Standard oval leaf)"

    # Vein texture prominence (Laplacian variance on green channel)
    green_channel = image_bgr[:, :, 1]
    laplacian = cv2.Laplacian(green_channel, cv2.CV_64F)
    features["vein_texture_density"] = round(float(laplacian.var()), 2)

    # Color analysis
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    mean_hsv = cv2.mean(hsv)
    mean_bgr = cv2.mean(image_bgr)
    features["color_profile"] = {
        "mean_green_intensity": int(mean_bgr[1]),
        "mean_chlorophyll_hue": int(mean_hsv[0]),
        "saturation_index": int(mean_hsv[1])
    }

    return features

def create_contour_overlay(image_bgr: np.ndarray, contour: Optional[np.ndarray]) -> np.ndarray:
    """
    Generate an annotated image displaying the detected leaf perimeter,
    bounding box, center of mass, and dimensions.
    """
    overlay = image_bgr.copy()
    if contour is not None and len(contour) >= 5:
        # Draw green contour line along leaf perimeter
        cv2.drawContours(overlay, [contour], -1, (16, 185, 129), 3)

        # Draw bounding rectangle in cyan
        bx, by, bw, bh = cv2.boundingRect(contour)
        cv2.rectangle(overlay, (bx, by), (bx + bw, by + bh), (245, 158, 11), 2)

        # Centroid
        m = cv2.moments(contour)
        if m["m00"] != 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
            cv2.circle(overlay, (cx, cy), 6, (239, 68, 68), -1)
            cv2.putText(overlay, f"Centroid ({cx}, {cy})", (cx + 10, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)

        # Annotate bounding box dimensions
        cv2.putText(overlay, f"{bw}x{bh}px", (bx, max(20, by - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (245, 158, 11), 2, cv2.LINE_AA)

    return overlay
