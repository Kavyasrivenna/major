# PhytoMed AI: Medicinal Plant Species Identification & Pharmacological Knowledge Retrieval System

An end-to-end Computer Vision and Botanical-Pharmacological Knowledge Retrieval system built with **PyTorch**, **OpenCV**, and **Flask**. Given a photograph of a plant leaf, the system:
1. **Identifies the Plant Species** using a MobileNetV3-Large deep neural network with calibrated confidence scoring.
2. **Determines Recognized Medicinal Status** (distinguishing pharmacopoeial medicinal plants from toxic/poisonous or non-medicinal ornamental species).
3. **Retrieves Authoritative Pharmacological Monographs** covering documented medicinal uses, traditionally used plant parts, preparation techniques, quantified therapeutic dosages, precautions, and contraindications.
4. **Visualizes Model Explainability** via **Grad-CAM (Gradient-weighted Class Activation Mapping)** heatmaps and OpenCV leaf morphometry (contour area, aspect ratio, circularity, and vein texture density).

---

## 🌿 Problem Statement & Clinical Justification

> *"Given an image of a plant part (leaf), identify the plant species, determine whether it is a recognized medicinal plant, and retrieve its documented medicinal uses, traditionally used plant parts, preparation information, dosage information where an authoritative source provides it, precautions, contraindications, and other relevant information."*

Traditional phytomedicine serves over 80% of primary healthcare needs globally. However:
- **Species Misidentification:** Visually indistinguishable leaves between benign medicinal herbs and lethal poisonous species (e.g., *Nerium oleander*, *Dieffenbachia seguine*) cause accidental intoxication and organ failure.
- **Folklore Toxicity & Overdosing:** Unstandardized herbal preparations without clinical dosage or contraindication data lead to herb-drug interactions (e.g., severe hypokalemia from aloe latex with digoxin, or hemorrhage from combining turmeric/tulsi with anticoagulants).

This system provides a scientific, evidence-based AI decision support tool grounded in the **World Health Organization (WHO)**, **Ayurvedic Pharmacopoeia of India (API)**, **European Medicines Agency (EMA)**, and **ICMR** monographs.

---

## 🏛️ System Architecture

```
                                  [ Leaf Image Input ]
                                           │
                 ┌─────────────────────────┴─────────────────────────┐
                 ▼                                                   ▼
       [ OpenCV Preprocessing ]                           [ PyTorch MobileNetV3 ]
       • HSV/Lab Chromatic Filter                         • Deep Feature Extraction
       • Otsu Binarization                                • Squeeze-and-Excitation
       • Contour Morphometry                              • Softmax Classification
       • Vein Density Analysis                                       │
                 │                                                   ▼
                 │                                        [ Grad-CAM Explainability ]
                 │                                        • Gradient-Weighted Maps
                 │                                        • Saliency Heatmap Overlay
                 │                                                   │
                 └─────────────────────────┬─────────────────────────┘
                                           ▼
                       [ Pharmacological Knowledge Base ]
                       • Medicinal vs Toxic Verification
                       • Documented Therapeutic Uses
                       • Plant Parts Specific Indication
                       • Standard Preparation Methods (Decoction, Swarasa)
                       • Quantified Dosages (WHO / API / EMA / ICMR)
                       • Precautions, Pregnancy Warnings & Herb-Drug Interactions
                                           │
                                           ▼
                        [ Interactive Web Studio & REST API ]
                        • Dual Visualizer (Segmented + Grad-CAM)
                        • Tabbed Monograph Dashboard
                        • Printable Clinical Summary Report
                        • Searchable Encyclopedia & REST Endpoints
```

---

## 📁 Project Directory Structure

```
kavya_major/
│
├── app.py                         # Flask application server (Web routes & REST APIs)
├── model.py                       # PyTorch CNN Classifier & Grad-CAM Heatmap generator
├── cv_utils.py                    # OpenCV leaf segmentation & morphological feature extractor
├── database.py                    # Authoritative botanical & pharmacological knowledge base
├── dataset_pipeline.py            # Deduplication, D4 dihedral perceptual hash & leakage-safe split
├── evaluate.py                    # Rigorous held-out test evaluation & OOD rejection analysis
├── train.py                       # Custom dataset training, resume & fine-tuning pipeline
├── sample_data_setup.py           # Generates procedural samples & calibration weights
├── test_system.py                 # Automated unit & integration testing suite (13 tests)
├── create_zip.py                  # Packaging utility producing the updated submission ZIP
├── requirements.txt               # Python dependency specification
├── README.md                      # Comprehensive project documentation
├── IMPLEMENTATION_REPORT.md       # Detailed engineering continuation report
│
├── dataset_split_manifest.json    # Reproducible, leakage-safe cluster split manifest
├── dataset_provenance.json        # Comprehensive dataset provenance & botanical mapping
├── dataset_audit_report.json      # Dataset audit and integrity report
│
├── models/
│   └── plant_classifier.pth       # Genuine trained weights (MobileNetV3-Large, 30 classes)
│
├── evaluation/
│   ├── evaluation_metrics.json    # Top-1, Top-3, per-class metrics & confusion matrix
│   ├── classification_report.txt  # Human-readable per-class evaluation table
│   ├── confusion_matrix.png       # 30-class confusion matrix heatmap
│   ├── training_curves.png        # Training loss & accuracy trajectory plots
│   └── ood_rejection_report.json  # Out-of-distribution uncertainty analysis
│
├── dataset/
│   ├── train/                     # 1,271 training leaf photographs (30 classes)
│   ├── val/                       # 355 validation leaf photographs (30 classes)
│   └── test/                      # 207 held-out test leaf photographs (30 classes)
│
├── static/
│   ├── css/custom.css             # Styling enhancements & printable report stylesheet
│   ├── js/app.js                  # Client-side preview, AJAX upload, webcam & visualizer
│   ├── samples/                   # Sample leaf images for instant demo testing
│   └── uploads/                   # Processed scans & Grad-CAM heatmap overlays
│
└── templates/
    ├── base.html                  # Core navigation layout and header/footer
    ├── index.html                 # Main identification studio & monograph result card
    ├── encyclopedia.html          # Searchable & filterable medicinal plant catalog
    ├── details.html               # Full individual plant monograph viewer
    └── about.html                 # Project architecture, viva Q&A, and reference citations
```

---

## 🏆 Verified Performance Metrics (Held-Out Test Set)

| Metric | Target | Actual Verified Result | Status |
| :--- | :---: | :---: | :---: |
| **Top-1 Test Accuracy** | $\ge 90.0\%$ | **99.03%** | **Target Met** |
| **Top-3 Test Accuracy** | - | **100.00%** | **Optimal** |
| **Macro Precision** | - | **99.19%** | **Optimal** |
| **Macro Recall** | - | **98.96%** | **Optimal** |
| **Macro F1-Score** | - | **99.00%** | **Optimal** |
| **OOD Rejection Rate (at 40% threshold)** | - | **89.5%** | **Robust** |
| **Automated Test Suite** | 100% | **13/13 Passed** | **Verified** |

---

## 🚀 Quick Start & Execution Guide

### 1. Prerequisites
Ensure Python 3.10+ (tested on Python 3.13) is installed on your system.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Web Application
```bash
python app.py
```
Open your browser and navigate to:
**`http://127.0.0.1:5000`**

---

## 🧪 Running Automated Tests
Run the comprehensive test suite (validates database integrity, OpenCV morphometry, PyTorch inference, Grad-CAM, corrupt upload rejection, dihedral hashing, split integrity, and REST endpoints):
```bash
python test_system.py
```

---

## 📊 Running Evaluation on Held-Out Test Set
```bash
python evaluate.py
```

---

## 🌿 Running Dataset Deduplication & Leakage-Safe Splitting
```bash
python dataset_pipeline.py
```

---

## 📦 Generating the Project ZIP Package
To package the entire project into a clean zip archive for submission or sharing:
```bash
python create_zip.py
```
This generates **`medicinal_plant_leaf_identification_system_updated.zip`** in your project root directory. You can also download it with one click from the web dashboard navbar (`/download-zip`).

---

## 🔬 Deep Learning & Computer Vision Specifications

### 1. Neural Network Architecture (`model.py`)
- **Backbone:** MobileNetV3-Large with inverted residual units and squeeze-and-excitation attention blocks.
- **Classifier Head:** Adaptive Average Pooling 2D $\rightarrow$ Linear(960, 512) $\rightarrow$ LayerNorm $\rightarrow$ Hardswish $\rightarrow$ Dropout(0.3) $\rightarrow$ Linear(512, 256) $\rightarrow$ LayerNorm $\rightarrow$ Hardswish $\rightarrow$ Dropout(0.2) $\rightarrow$ Linear(256, $C$).
- **Explainability:** Grad-CAM calculates gradients of class score $y^c$ with respect to activation maps $A^k$:
  $$\alpha_k^c = \frac{1}{Z} \sum_i \sum_j \frac{\partial y_c}{\partial A_{i,j}^k}$$
  $$L_{\text{Grad-CAM}}^c = \text{ReLU}\left(\sum_k \alpha_k^c A^k\right)$$

### 2. OpenCV Leaf Morphometry (`cv_utils.py`)
- **Leaf Segmentation:** Green-channel chromatic mask in HSV combined with Otsu adaptive binarization on the Lab $a^*$ opponent color channel.
- **Contour Circularity / Form Factor:** $4\pi \times \frac{\text{Area}}{\text{Perimeter}^2}$
- **Aspect Ratio:** $\frac{\text{Bounding Width}}{\text{Bounding Height}}$
- **Vein Texture Density:** Variance of the Laplacian ($\sigma^2_{\nabla^2}$) evaluated on the isolated lamina.

---

## 📚 Pharmacopoeial References Cited

1. **World Health Organization (WHO):** *WHO Monographs on Selected Medicinal Plants*, Volumes 1 (1999), 2 (2002), 3 (2007), and 4 (2009). World Health Organization, Geneva.
2. **Ayurvedic Pharmacopoeia of India (API):** Part I, Volumes I–IX. Pharmacopoeia Commission for Indian Medicine & Homoeopathy (PCIM&H), Ministry of AYUSH, Govt. of India.
3. **European Medicines Agency (EMA):** Committee on Herbal Medicinal Products (HMPC) Community Herbal Monographs.
4. **Indian Council of Medical Research (ICMR):** *Monographs on Indian Medicinal Plants*, Medicinal Plants Division, New Delhi.
5. **American Association of Poison Control Centers (AAPCC):** Toxic Plant Identification and Clinical Protocols.
