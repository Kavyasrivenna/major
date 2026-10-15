/**
 * PhytoMed AI - Client-side Interactive Engine
 * Handles image upload, webcam capture, sample execution, AJAX inference,
 * Grad-CAM visualization display, and monograph rendering.
 */

document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const dropZone = document.getElementById("dropZone");
    const leafInput = document.getElementById("leafInput");
    const uploadPlaceholder = document.getElementById("uploadPlaceholder");
    const previewContainer = document.getElementById("previewContainer");
    const imagePreview = document.getElementById("imagePreview");
    const changeImageBtn = document.getElementById("changeImageBtn");
    const analyzeBtn = document.getElementById("analyzeBtn");

    // Camera elements
    const cameraBtn = document.getElementById("cameraBtn");
    const cameraModal = document.getElementById("cameraModal");
    const webcamVideo = document.getElementById("webcamVideo");
    const captureBtn = document.getElementById("captureBtn");
    const closeCameraBtn = document.getElementById("closeCameraBtn");
    let videoStream = null;

    // State containers
    const initialState = document.getElementById("initialState");
    const loadingState = document.getElementById("loadingState");
    const loadingStatusText = document.getElementById("loadingStatusText");
    const resultsContainer = document.getElementById("resultsContainer");

    let currentFile = null;

    // Tab Navigation
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabPanels = document.querySelectorAll(".tab-panel");

    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetTab = btn.getAttribute("data-tab");
            tabButtons.forEach(b => b.classList.remove("active"));
            tabPanels.forEach(p => p.classList.add("hidden"));

            btn.classList.add("active");
            const panel = document.getElementById(targetTab);
            if (panel) panel.classList.remove("hidden");
        });
    });

    // Drag and Drop Events
    if (dropZone) {
        dropZone.addEventListener("click", () => leafInput.click());

        ["dragenter", "dragover"].forEach(eventName => {
            dropZone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.add("border-emerald-500", "bg-emerald-50/50");
            });
        });

        ["dragleave", "drop"].forEach(eventName => {
            dropZone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.remove("border-emerald-500", "bg-emerald-50/50");
            });
        });

        dropZone.addEventListener("drop", (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files && files.length > 0) {
                handleSelectedFile(files[0]);
            }
        });
    }

    if (leafInput) {
        leafInput.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                handleSelectedFile(e.target.files[0]);
            }
        });
    }

    if (changeImageBtn) {
        changeImageBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            leafInput.click();
        });
    }

    function handleSelectedFile(file) {
        if (!file.type.startsWith("image/")) {
            alert("Please select a valid image file (JPG, PNG, WEBP).");
            return;
        }
        currentFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            uploadPlaceholder.classList.add("hidden");
            previewContainer.classList.remove("hidden");
            analyzeBtn.disabled = false;
        };
        reader.readAsDataURL(file);
    }

    // Camera WebRTC Stream Handling
    if (cameraBtn) {
        cameraBtn.addEventListener("click", async () => {
            if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                alert("Camera access is not supported or permitted in this browser context.");
                return;
            }
            try {
                videoStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
                webcamVideo.srcObject = videoStream;
                cameraModal.classList.remove("hidden");
            } catch (err) {
                console.error("Camera access error:", err);
                alert("Unable to open camera: " + err.message);
            }
        });

        closeCameraBtn.addEventListener("click", () => {
            stopCamera();
            cameraModal.classList.add("hidden");
        });

        captureBtn.addEventListener("click", () => {
            const canvas = document.getElementById("cameraCanvas");
            canvas.width = webcamVideo.videoWidth || 640;
            canvas.height = webcamVideo.videoHeight || 480;
            const ctx = canvas.getContext("2d");
            ctx.drawImage(webcamVideo, 0, 0, canvas.width, canvas.height);

            canvas.toBlob((blob) => {
                const photoFile = new File([blob], "camera_leaf.jpg", { type: "image/jpeg" });
                handleSelectedFile(photoFile);
                stopCamera();
                cameraModal.classList.add("hidden");
            }, "image/jpeg", 0.95);
        });
    }

    function stopCamera() {
        if (videoStream) {
            videoStream.getTracks().forEach(track => track.stop());
            videoStream = null;
        }
    }

    // Instant Sample Selector
    const sampleButtons = document.querySelectorAll(".sample-btn");
    sampleButtons.forEach(btn => {
        btn.addEventListener("click", async () => {
            const speciesId = btn.getAttribute("data-species");
            const sampleImg = btn.querySelector("img");
            if (!sampleImg) return;

            // Fetch sample image as Blob
            try {
                const response = await fetch(sampleImg.src);
                const blob = await response.blob();
                const file = new File([blob], `${speciesId}.jpg`, { type: "image/jpeg" });
                handleSelectedFile(file);
                // Trigger analysis directly
                triggerLeafAnalysis();
            } catch (err) {
                console.error("Error loading sample image:", err);
            }
        });
    });

    // Analyze Button Click
    if (analyzeBtn) {
        analyzeBtn.addEventListener("click", () => {
            triggerLeafAnalysis();
        });
    }

    async function triggerLeafAnalysis() {
        if (!currentFile) {
            alert("Please select or upload a leaf image first.");
            return;
        }

        // Show loading state
        if (initialState) initialState.classList.add("hidden");
        if (resultsContainer) resultsContainer.classList.add("hidden");
        if (loadingState) loadingState.classList.remove("hidden");

        const steps = [
            "Performing Otsu & Lab chromatic leaf segmentation...",
            "Computing contour perimeter, circularity, and venation...",
            "Evaluating MobileNetV3 deep feature descriptors...",
            "Computing Grad-CAM gradient visual attention heatmap...",
            "Retrieving authoritative WHO / API pharmacopoeial monograph..."
        ];

        let stepIndex = 0;
        const progressInterval = setInterval(() => {
            if (stepIndex < steps.length && loadingStatusText) {
                loadingStatusText.textContent = steps[stepIndex];
                stepIndex++;
            }
        }, 350);

        const formData = new FormData();
        formData.append("leaf_image", currentFile);

        try {
            const res = await fetch("/api/identify", {
                method: "POST",
                body: formData
            });

            clearInterval(progressInterval);

            if (!res.ok) {
                const errData = await res.json();
                throw new Error(errData.error || "Server analysis error");
            }

            const data = await res.json();
            renderResults(data);
        } catch (err) {
            clearInterval(progressInterval);
            console.error("Analysis failed:", err);
            alert("Identification error: " + err.message);
            if (loadingState) loadingState.classList.add("hidden");
            if (initialState) initialState.classList.remove("hidden");
        }
    }

    function renderResults(data) {
        if (loadingState) loadingState.classList.add("hidden");
        if (resultsContainer) resultsContainer.classList.remove("hidden");

        const top = data.prediction;
        const mono = data.monograph;
        const morph = data.morphology;

        // Common & Scientific Name
        document.getElementById("resCommonName").textContent = mono ? mono.common_names.join(" / ") : top.scientific_name;
        document.getElementById("resScientificName").textContent = mono ? mono.scientific_name : top.scientific_name;
        document.getElementById("resFamily").textContent = mono ? `Botanical Family: ${mono.botanical_family} | Genus: ${mono.genus}` : "";

        // Confidence
        document.getElementById("resConfidence").textContent = top.confidence;
        document.getElementById("resConfidenceBar").style.width = `${Math.min(100, Math.max(10, top.confidence))}%`;

        // Medicinal Status Badge
        const badge = document.getElementById("medicinalBadge");
        const badgeIcon = document.getElementById("badgeIcon");
        const badgeText = document.getElementById("badgeText");
        const statusAccentBar = document.getElementById("statusAccentBar");

        if (top.is_medicinal) {
            badge.className = "inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-300 shadow-sm";
            badgeIcon.className = "fa-solid fa-shield-halved mr-1.5 text-emerald-600";
            badgeText.textContent = top.medicinal_status || "Recognized Pharmacopoeial Medicinal Plant";
            statusAccentBar.className = "absolute top-0 left-0 right-0 h-1.5 bg-emerald-500";
        } else {
            badge.className = "inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-rose-100 text-rose-800 border border-rose-300 shadow-sm";
            badgeIcon.className = "fa-solid fa-skull-crossbones mr-1.5 text-rose-600";
            badgeText.textContent = top.medicinal_status || "Toxic / Non-Medicinal Plant";
            statusAccentBar.className = "absolute top-0 left-0 right-0 h-1.5 bg-rose-500";
        }

        // Top Candidates List
        const candidatesContainer = document.getElementById("topCandidatesList");
        candidatesContainer.innerHTML = "";
        data.top_k.forEach((cand, idx) => {
            const candDiv = document.createElement("div");
            candDiv.className = `p-2.5 rounded-xl border ${idx === 0 ? 'bg-emerald-50/70 border-emerald-300 font-semibold' : 'bg-slate-50 border-slate-200'}`;
            candDiv.innerHTML = `
                <div class="flex justify-between items-center">
                    <span class="truncate font-bold text-slate-800">${cand.common_names[0] || cand.species_id}</span>
                    <span class="text-xs font-black text-emerald-700">${cand.confidence}%</span>
                </div>
                <p class="text-[10px] text-slate-500 italic truncate">${cand.scientific_name}</p>
            `;
            candidatesContainer.appendChild(candDiv);
        });

        // Previews: Segmented & Grad-CAM
        document.getElementById("segmentedPreview").src = data.segmented_image_url || imagePreview.src;
        document.getElementById("gradcamPreview").src = data.gradcam_image_url || imagePreview.src;

        // Morphology metrics
        if (morph) {
            document.getElementById("morphCircularity").textContent = morph.circularity;
            document.getElementById("morphAspectRatio").textContent = morph.aspect_ratio;
            document.getElementById("morphVeins").textContent = morph.vein_texture_density;
            document.getElementById("morphShape").textContent = morph.morphology_class;
        }

        if (mono) {
            // Tab 1: Uses
            const usesList = document.getElementById("resUsesList");
            usesList.innerHTML = "";
            mono.documented_medicinal_uses.forEach(use => {
                const li = document.createElement("li");
                li.className = "flex items-start bg-slate-50 p-2.5 rounded-xl border border-slate-100";
                li.innerHTML = `<i class="fa-solid fa-circle-check text-emerald-500 text-xs mt-0.5 mr-2.5 shrink-0"></i><span>${use}</span>`;
                usesList.appendChild(li);
            });

            // Tab 2: Used Parts
            const partsTable = document.getElementById("resPartsTable");
            partsTable.innerHTML = "";
            mono.traditionally_used_parts.forEach(part => {
                const tr = document.createElement("tr");
                tr.className = "hover:bg-slate-50";
                tr.innerHTML = `<td class="p-2.5 font-bold text-slate-800">${part.part}</td><td class="p-2.5 text-slate-600">${part.indication}</td>`;
                partsTable.appendChild(tr);
            });

            // Tab 3: Preparations
            const prepList = document.getElementById("resPrepList");
            prepList.innerHTML = "";
            mono.preparation_information.forEach(prep => {
                const pdiv = document.createElement("div");
                pdiv.className = "p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs";
                pdiv.innerHTML = `<p class="font-bold text-slate-900 mb-1 flex items-center"><i class="fa-solid fa-mortar-pestle text-emerald-600 mr-1.5"></i>${prep.method}</p><p class="text-slate-600">${prep.details}</p>`;
                prepList.appendChild(pdiv);
            });

            // Tab 4: Dosages
            const dosageList = document.getElementById("resDosageList");
            dosageList.innerHTML = "";
            mono.dosage_information.forEach(d => {
                const ddiv = document.createElement("div");
                ddiv.className = "p-3 bg-emerald-50/40 rounded-xl border border-emerald-200 flex flex-col sm:flex-row sm:items-center justify-between text-xs gap-2";
                ddiv.innerHTML = `
                    <div>
                        <span class="text-[9px] font-bold text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded uppercase tracking-wider">${d.source}</span>
                        <p class="font-bold text-slate-800 mt-1">${d.preparation}</p>
                    </div>
                    <div class="sm:text-right">
                        <span class="text-sm font-extrabold text-emerald-700">${d.dose}</span>
                    </div>
                `;
                dosageList.appendChild(ddiv);
            });

            // Tab 5: Precautions & Contraindications
            const precList = document.getElementById("resPrecautionsList");
            precList.innerHTML = "";
            mono.precautions_warnings.forEach(p => {
                const li = document.createElement("li");
                li.className = "flex items-start";
                li.innerHTML = `<i class="fa-solid fa-triangle-exclamation text-amber-500 text-xs mt-0.5 mr-2 shrink-0"></i><span>${p}</span>`;
                precList.appendChild(li);
            });

            const contraList = document.getElementById("resContraindicationsList");
            contraList.innerHTML = "";
            mono.contraindications_interactions.forEach(c => {
                const li = document.createElement("li");
                li.className = "flex items-start";
                li.innerHTML = `<i class="fa-solid fa-ban text-rose-500 text-xs mt-0.5 mr-2 shrink-0"></i><span>${c}</span>`;
                contraList.appendChild(li);
            });

            // Tab 6: Phytochemistry
            const chemsList = document.getElementById("resChemsList");
            chemsList.innerHTML = "";
            mono.active_phytochemicals.forEach(ch => {
                const li = document.createElement("li");
                li.textContent = ch;
                chemsList.appendChild(li);
            });
            document.getElementById("resHabitat").textContent = mono.native_region || "-";
            document.getElementById("resIUCN").textContent = mono.iucn_conservation_status || "-";
            document.getElementById("resMorphologyDesc").textContent = mono.botanical_morphology || "-";
        }

        // Scroll smoothly to results
        resultsContainer.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    // Print Report Button
    const printReportBtn = document.getElementById("printReportBtn");
    if (printReportBtn) {
        printReportBtn.addEventListener("click", () => {
            window.print();
        });
    }

    // Search and Filter functionality in Encyclopedia page
    const encyclopediaSearch = document.getElementById("encyclopediaSearch");
    const filterButtons = document.querySelectorAll(".filter-btn");
    const plantCards = document.querySelectorAll(".plant-card");
    const noResults = document.getElementById("noResults");
    const searchCount = document.getElementById("searchCount");

    if (encyclopediaSearch && plantCards.length > 0) {
        let currentFilter = "all";

        function filterCatalog() {
            const query = encyclopediaSearch.value.toLowerCase().trim();
            let visibleCount = 0;

            plantCards.forEach(card => {
                const name = (card.getAttribute("data-name") || "").toLowerCase();
                const family = (card.getAttribute("data-family") || "").toLowerCase();
                const uses = (card.getAttribute("data-uses") || "").toLowerCase();
                const isMedicinal = card.getAttribute("data-medicinal") === "true";

                // Text search match
                const matchesQuery = query === "" || name.includes(query) || family.includes(query) || uses.includes(query);

                // Category filter match
                let matchesCategory = true;
                if (currentFilter === "medicinal") {
                    matchesCategory = isMedicinal;
                } else if (currentFilter === "toxic") {
                    matchesCategory = !isMedicinal;
                } else if (currentFilter === "respiratory") {
                    matchesCategory = uses.includes("respiratory") || uses.includes("cough") || uses.includes("asthma") || uses.includes("bronchitis");
                } else if (currentFilter === "digestive") {
                    matchesCategory = uses.includes("digest") || uses.includes("gastric") || uses.includes("dyspepsia") || uses.includes("ulcer");
                } else if (currentFilter === "diabetes") {
                    matchesCategory = uses.includes("diabet") || uses.includes("glycem") || uses.includes("sugar");
                }

                if (matchesQuery && matchesCategory) {
                    card.classList.remove("hidden");
                    visibleCount++;
                } else {
                    card.classList.add("hidden");
                }
            });

            if (searchCount) searchCount.textContent = `${visibleCount} species`;
            if (noResults) {
                if (visibleCount === 0) noResults.classList.remove("hidden");
                else noResults.classList.add("hidden");
            }
        }

        encyclopediaSearch.addEventListener("input", filterCatalog);

        filterButtons.forEach(btn => {
            btn.addEventListener("click", () => {
                filterButtons.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                currentFilter = btn.getAttribute("data-filter");
                filterCatalog();
            });
        });
    }
});
