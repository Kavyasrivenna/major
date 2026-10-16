"""
Authoritative Botanical and Pharmacological Knowledge Base
==========================================================
Provides evidence-based monographs for all 30 classes from the Indian Medicinal Leaves
Dataset and additional control non-medicinal / toxic reference species.

Synthesizes data from:
- World Health Organization (WHO) Monographs on Selected Medicinal Plants (Volumes 1-4)
- Ayurvedic Pharmacopoeia of India (API), Ministry of AYUSH, Govt. of India
- Indian Council of Medical Research (ICMR) Medicinal Plants Monographs
- European Medicines Agency (EMA) Committee on Herbal Medicinal Products (HMPC)
- American Association of Poison Control Centers (AAPCC) & Toxnet / PubChem
"""

from typing import Dict, List, Optional, Any

PLANT_DATABASE: Dict[str, Dict[str, Any]] = {
    # -------------------------------------------------------------
    # 1. Alpinia Galanga (Rasna)
    # -------------------------------------------------------------
    "alpinia_galanga": {
        "id": "alpinia_galanga",
        "dataset_class": "Alpinia Galanga (Rasna)",
        "scientific_name": "Alpinia galanga (L.) Willd.",
        "botanical_family": "Zingiberaceae (Ginger family)",
        "genus": "Alpinia",
        "synonyms": ["Languas galanga (L.) Stuntz", "Maranta galanga L."],
        "common_names": ["Rasna", "Greater Galangal", "Kulanjan", "Blue Ginger", "Mahabaracandra"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial (API & ICMR)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 2",
            "WHO Monographs on Selected Medicinal Plants, Vol. 4"
        ],
        "documented_medicinal_uses": [
            "Potent anti-inflammatory and anti-arthritic activity (relieves rheumatoid arthritis and sciatica)",
            "Bronchodilatory and mucolytic action in bronchial asthma and chronic cough",
            "Carminative and digestive stimulant (treats dyspepsia, flatulence, and colic)",
            "Antimicrobial and antifungal activity against respiratory and enteric pathogens"
        ],
        "traditionally_used_parts": [
            {"part": "Rhizome", "indication": "Arthritis, rheumatism, bronchial catarrh, dyspepsia"},
            {"part": "Leaves", "indication": "Topical poultice for rheumatic swellings and fever baths"}
        ],
        "preparation_information": [
            {"method": "Rhizome Decoction (Kashayam)", "details": "10-15 g crushed dried rhizome simmered in 400 ml water reduced to 100 ml."},
            {"method": "Rhizome Powder (Churna)", "details": "Dry rhizome finely pulverized; consumed with warm water or ginger tea."},
            {"method": "Medicated Oil (Rasnadi Taila)", "details": "Rhizome extract infused in sesame oil for topical arthritic massage."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Rhizome Powder (Churna)", "dose": "1 to 3 g daily in divided doses"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Rhizome Decoction (Kwatha)", "dose": "50 to 100 ml twice daily"},
            {"source": "ICMR Monograph", "preparation": "Hydroalcoholic Extract", "dose": "250 to 500 mg twice daily"}
        ],
        "precautions_warnings": [
            "Gastric Acidity: High doses may irritate gastric mucosa and cause heartburn.",
            "Pregnancy: Avoid therapeutic high-dose extracts during pregnancy; culinary levels are considered safe.",
            "Lactation: Safety not systematically established; limit to culinary use."
        ],
        "contraindications_interactions": [
            "Contraindication: Active gastric or duodenal peptic ulcers.",
            "Interactions: Antacids (may reduce efficacy due to stomach acid stimulation); Anticoagulants (mild additive platelet inhibition)."
        ],
        "active_phytochemicals": ["1'-Acetoxychavicol acetate (ACA)", "Galangin (flavonol)", "1,8-Cineole (eucalyptol)", "Methyl cinnamate"],
        "botanical_morphology": "Perennial rhizomatous reed-like herb up to 2 m tall; leaves lanceolate, 25-35 cm long, smooth and shiny green with fragrant aroma when crushed.",
        "native_region": "Tropical South and Southeast Asia (Indonesia, Malaysia, India).",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 2. Amaranthus Viridis (Arive-Dantu)
    # -------------------------------------------------------------
    "amaranthus_viridis": {
        "id": "amaranthus_viridis",
        "dataset_class": "Amaranthus Viridis (Arive-Dantu)",
        "scientific_name": "Amaranthus viridis L.",
        "botanical_family": "Amaranthaceae",
        "genus": "Amaranthus",
        "synonyms": ["Amaranthus gracilis Desf."],
        "common_names": ["Arive-Dantu", "Slender Amaranth", "Green Amaranth", "Tanduliyaka", "Cholai"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Nutra-Medicinal Herb",
        "status_badge_color": "emerald",
        "evidence_category": "Traditional Phytomedicine & Nutrition",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. V",
            "Indian Journal of Traditional Knowledge (IJTK)",
            "FAO Traditional Vegetable Monograph Series"
        ],
        "documented_medicinal_uses": [
            "Nutritional restorative rich in bioavailable calcium, iron, beta-carotene, and protein",
            "Diuretic and cooling agent in urinary tract irritation and burning micturition",
            "Hepatoprotective and antioxidant properties mitigating oxidative tissue injury",
            "Mild emollient and anti-inflammatory poultice for skin eruptions and boils"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves and Tender Shoots", "indication": "Nutritional vegetable, anemia, urinary dysuria, constipation"},
            {"part": "Roots", "indication": "Traditional decoction for eczema and inflammatory dermatoses"}
        ],
        "preparation_information": [
            {"method": "Culinary Leaf Vegetable", "details": "Fresh leaves steamed or sautéed with lentils as dietary vegetable."},
            {"method": "Expressed Whole Plant Juice (Swarasa)", "details": "Fresh plant washed, crushed, and filtered; taken with cumin."},
            {"method": "Root Paste", "details": "Fresh roots ground and applied topically on inflammatory boils."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Whole Plant Juice", "dose": "10 to 20 ml twice daily"},
            {"source": "Traditional Ayurvedic Practice", "preparation": "Cooked Green Leaves", "dose": "50 to 100 g as dietary vegetable"},
            {"source": "Clinical Reference", "preparation": "Standardized Leaf Extract", "dose": "Dosage information not verified for standardized extract; culinary use standard."}
        ],
        "precautions_warnings": [
            "Oxalate Content: Contains soluble oxalates; patients with calcium oxalate kidney stones should consume in moderation.",
            "Nitrate Accumulation: Avoid harvesting from over-fertilized soils where nitrates may concentrate."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe calcium-oxalate nephrolithiasis.",
            "Interactions: None well-documented; may enhance dietary iron absorption."
        ],
        "active_phytochemicals": ["Rutin", "Quercetin", "Amaranthin", "Beta-carotene", "Ascorbic acid", "Dietary fiber"],
        "botanical_morphology": "Erect annual herb 30-80 cm; leaves ovate to rhombic-ovate, 2-7 cm long, slender petiole, small greenish flowers in dense terminal spikes.",
        "native_region": "Pantropical and subtropical regions worldwide.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 3. Artocarpus Heterophyllus (Jackfruit)
    # -------------------------------------------------------------
    "artocarpus_heterophyllus": {
        "id": "artocarpus_heterophyllus",
        "dataset_class": "Artocarpus Heterophyllus (Jackfruit)",
        "scientific_name": "Artocarpus heterophyllus Lam.",
        "botanical_family": "Moraceae (Mulberry family)",
        "genus": "Artocarpus",
        "synonyms": ["Artocarpus integrifolius L.f.", "Artocarpus philippensis"],
        "common_names": ["Jackfruit", "Panasa", "Kathal", "Jak"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Medicinal & Nutritional Tree",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. VI",
            "ICMR Indian Medicinal Plants Compendium",
            "Journal of Ethnopharmacology Monographs"
        ],
        "documented_medicinal_uses": [
            "Hypoglycemic action: Mature leaf extract significantly improves glycemic index and glucose tolerance",
            "Astringent and antidiarrheal action of bark and tender leaves",
            "Wound healing and anti-inflammatory properties of bark decoction",
            "Immunomodulatory and antioxidant action via high polyphenolic flavones"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Diabetes management, diarrhea, skin wounds, fever wash"},
            {"part": "Bark", "indication": "Dysentery, skin ulcers, astringent gargle"},
            {"part": "Latex / Sap", "indication": "Topical paste for abscesses, snakebites, and glandular swelling"},
            {"part": "Seeds", "indication": "Nutritious roasted edible seed, aphrodisiac tonic"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction", "details": "10-15 g mature dried leaves boiled in 300 ml water reduced to 100 ml."},
            {"method": "Bark Powder (Churna)", "details": "Dried stem bark pulverized and taken with honey for diarrhea."},
            {"method": "Leaf Ash Paste", "details": "Traditional ash of roasted leaves mixed with coconut oil applied to burns and cuts."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Stem Bark Powder", "dose": "3 to 6 g daily in divided doses"},
            {"source": "Ethnomedicinal Reference", "preparation": "Mature Leaf Decoction (Glycemic support)", "dose": "50 to 75 ml once daily before breakfast"},
            {"source": "Standard Monograph", "preparation": "Clinical Dosage Status", "dose": "Dosage information not verified for commercial purified extract."}
        ],
        "precautions_warnings": [
            "Hypoglycemia: May augment prescription antidiabetic drugs; monitor blood sugar.",
            "Latex Contact: The white milky latex may cause mild contact dermatitis in sensitive individuals."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe acute constipation (due to strong astringent tannins in bark).",
            "Interactions: Additive interaction with oral hypoglycemic agents."
        ],
        "active_phytochemicals": ["Artocarpin", "Artocarpetin", "Cycloartocarpin", "Morin", "Jacalin (lectin)", "Dietary fibers"],
        "botanical_morphology": "Massive evergreen monoecious tree 10-20 m; leaves alternate, coriaceous, elliptic to obovate, 8-20 cm long, dark glossy green, entire; produces massive cauliflorous fruit syncarps.",
        "native_region": "Indigenous to Western Ghats of India; widely cultivated in tropical Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 4. Azadirachta Indica (Neem)
    # -------------------------------------------------------------
    "azadirachta_indica": {
        "id": "azadirachta_indica",
        "dataset_class": "Azadirachta Indica (Neem)",
        "scientific_name": "Azadirachta indica A. Juss.",
        "botanical_family": "Meliaceae (Mahogany family)",
        "genus": "Azadirachta",
        "synonyms": ["Melia azadirachta L."],
        "common_names": ["Neem", "Indian Lilac", "Margosa Tree", "Nimba", "Vepa"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO & API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "WHO Traditional Medicine Compendium & ICMR Monographs",
            "United States Pharmacopeia - Herbal Compendium (USP-HC)"
        ],
        "documented_medicinal_uses": [
            "Broad-spectrum antimicrobial and antifungal (Candida, Trichophyton, Epidermophyton)",
            "Dermatological therapeutics: Eczema, psoriasis, acne vulgaris, pruritus, chronic wounds",
            "Anti-inflammatory and hepatoprotective actions via antioxidant pathways",
            "Anti-hyperglycemic properties: promotes peripheral glucose utilization",
            "Gingivitis and oral plaque reduction (in herbal toothpaste and mouthwash)",
            "Antiparasitic against scabies, pediculosis (lice), and intestinal helminths"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Patra)", "indication": "Skin infections, leprosy, boils, intestinal worms, hyperglycemia, blood purifier"},
            {"part": "Bark (Tvaka)", "indication": "Intermittent fevers, malaria, gastric ulcers, astringent, bitter tonic"},
            {"part": "Seed / Oil (Taila)", "indication": "Lice, scabies, ringworm, chronic rheumatism, topical insect repellant"},
            {"part": "Flowers (Pushpa)", "indication": "Digestive disorders, intestinal parasites, biliousness"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction (Kashayam)", "details": "5-10 g fresh leaves boiled in 400 ml water reduced to 100 ml; taken orally or used as antiseptic wash."},
            {"method": "Leaf Paste (Kalka)", "details": "Fresh leaves crushed into fine paste applied topically on affected skin lesions for 30 minutes."},
            {"method": "Expressed Leaf Juice (Swarasa)", "details": "Fresh leaves crushed with clean water, filtered through muslin cloth; consumed early morning."},
            {"method": "Neem Oil (Cold-pressed)", "details": "For external dermatological application diluted 1:5 in carrier oil (coconut or sesame)."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Leaf Powder (Churna)", "dose": "1 to 3 g daily in divided doses"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice (Swarasa)", "dose": "5 to 10 ml once daily"},
            {"source": "ICMR Guidelines on Phytomedicines", "preparation": "Stem Bark Decoction", "dose": "20 to 50 ml twice daily after meals"}
        ],
        "precautions_warnings": [
            "Toxic in Infants and Young Children: Neem seed oil can cause toxic encephalopathy, Reye-like syndrome, and metabolic acidosis in infants. Internal administration to infants is strictly contraindicated.",
            "Fertility: Documented spermicidal and anti-ovulatory properties; avoid if attempting conception.",
            "Renal and Hepatic Monitoring: High internal doses over prolonged periods may cause nephrotoxicity or hepatotoxicity; restrict continuous intake to 2-3 weeks.",
            "Pregnancy: Leaf and bark decoctions are contraindicated during pregnancy due to potential abortifacient actions."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy, lactation, infant oral ingestion, auto-immune diseases (may over-stimulate immune system).",
            "Drug Interactions: Antidiabetic medications (potential profound hypoglycemia), Immunosuppressants (cyclosporine, tacrolimus) - may counteract therapeutic immunosuppression."
        ],
        "active_phytochemicals": ["Azadirachtin (limonoid)", "Nimbin, Nimbidin, and Nimbolide", "Salannin and Gedunin", "Quercetin and beta-sitosterol"],
        "botanical_morphology": "Large evergreen tree (15-20 m tall); leaves alternate, pinnate, 20-40 cm long, with 20-30 medium to dark green leaflets; leaflet blades strongly asymmetric, lanceolate to ovate-lanceolate, serrated margins.",
        "native_region": "Native to Indian subcontinent and Myanmar; naturalized throughout tropical and subtropical dry areas worldwide.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 5. Basella Alba (Basale)
    # -------------------------------------------------------------
    "basella_alba": {
        "id": "basella_alba",
        "dataset_class": "Basella Alba (Basale)",
        "scientific_name": "Basella alba L. (syn. Basella rubra L.)",
        "botanical_family": "Basellaceae",
        "genus": "Basella",
        "synonyms": ["Basella rubra L.", "Basella lucida L."],
        "common_names": ["Basale", "Malabar Spinach", "Indian Spinach", "Upodika", "Pui Shak"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Nutra-Medicinal Herb",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Nutra-Medicinal (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. VI",
            "Indian Journal of Natural Products and Resources",
            "WHO Traditional Food Plants Compendium"
        ],
        "documented_medicinal_uses": [
            "Demulcent and mucosal protectant in peptic ulcers and gastrointestinal irritation",
            "Laxative and bowel regulator for chronic constipation due to abundant mucilage",
            "Cooling antipyretic in heat stroke, burning sensation, and stomatitis",
            "Topical emollient for burn injuries, scalds, and urticarial skin irritations"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves and Tender Stems", "indication": "Constipation, gastritis, mouth ulcers, burn dressings, anemia"},
            {"part": "Roots", "indication": "Traditional decoction for biliousness and morning sickness"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Swarasa)", "details": "Fresh succulent leaves crushed with minimal water and strained; consumed with sugar candy."},
            {"method": "Culinary Preparation", "details": "Leaves cooked into mild soups and stews for digestive recovery."},
            {"method": "Topical Leaf Poultice", "details": "Fresh bruised mucilaginous leaves applied directly to burns and scalds."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice", "dose": "10 to 20 ml twice daily with honey or ghee"},
            {"source": "Dietary Standard", "preparation": "Cooked Herb", "dose": "50 to 100 g daily as dietary therapeutic vegetable"},
            {"source": "Standard Extract", "preparation": "Purified Formulation", "dose": "Dosage information not verified for standardized industrial extracts."}
        ],
        "precautions_warnings": [
            "Loose Stools: Due to its high mucilage and laxative nature, excessive intake may cause diarrhea.",
            "Kidney Stones: Contains moderate oxalates; consume with plenty of water in stone-forming patients."
        ],
        "contraindications_interactions": [
            "Contraindication: Acute diarrhea and dysentery.",
            "Interactions: May slow absorption of oral medications taken concurrently; separate administration by 1-2 hours."
        ],
        "active_phytochemicals": ["Mucilage (polysaccharides)", "Betacyanins (in red form)", "Carotenoids", "Vitamins A, C, E, Iron", "Saponins"],
        "botanical_morphology": "Fleshy, twining perennial liana; stems succulent and green or purplish; leaves alternate, succulent, ovate or cordate, 5-12 cm long, glossy dark green with mucilaginous sap.",
        "native_region": "Tropical Asia and Africa; cultivated extensively throughout the tropics.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 6. Brassica Juncea (Indian Mustard)
    # -------------------------------------------------------------
    "brassica_juncea": {
        "id": "brassica_juncea",
        "dataset_class": "Brassica Juncea (Indian Mustard)",
        "scientific_name": "Brassica juncea (L.) Czern.",
        "botanical_family": "Brassicaceae (Mustard family)",
        "genus": "Brassica",
        "synonyms": ["Sinapis juncea L."],
        "common_names": ["Indian Mustard", "Brown Mustard", "Sarson", "Rai", "Rajika"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial (API & German Commission E)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "German Commission E Monographs on Mustard Seed",
            "British Herbal Pharmacopoeia (BHP)"
        ],
        "documented_medicinal_uses": [
            "Rubefacient and counter-irritant for musculoskeletal joint pain, sciatica, and lumbago",
            "Emetic in emergency toxic ingestion management (traditional mustard seed water)",
            "Decongestant poultice for acute bronchitis, chest congestion, and pleurisy",
            "Antimicrobial and carminative digestive condiment enhancing gastric secretion"
        ],
        "traditionally_used_parts": [
            {"part": "Seeds", "indication": "Topical counter-irritant plaster, rheumatism, digestive appetizer, emetic"},
            {"part": "Fixed Oil (Mustard Oil)", "indication": "Topical joint massage, skin disinfectant, ear drops (warm)"},
            {"part": "Tender Leaves", "indication": "Nutritious winter green vegetable (Sarson ka Saag)"}
        ],
        "preparation_information": [
            {"method": "Mustard Plaster / Poultice (Sinapism)", "details": "Coarsely ground seeds mixed with warm water (not boiling) into a paste; applied between cloth layers on chest or joint for max 15 minutes."},
            {"method": "Seed Powder (Churna)", "details": "Ground seeds used in tiny quantities as carminative digestive spice."},
            {"method": "Medicated Massage Oil", "details": "Mustard oil warmed with garlic and camphor for topical joint rubbing."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Seed Powder (Churna)", "dose": "0.5 to 1.5 g as digestive; 3 to 6 g as emetic with warm water"},
            {"source": "German Commission E", "preparation": "External Mustard Plaster", "dose": "Apply poultice for 10-15 minutes maximum (children: 5-10 minutes); discontinue if burning occurs"},
            {"source": "Clinical Reference", "preparation": "Leaf Extract", "dose": "No verified dosage found in the available sources for isolated leaf extract."}
        ],
        "precautions_warnings": [
            "Blistering and Chemical Burns: Prolonged application of mustard paste beyond 15 minutes causes erythema, severe blisters, and skin necrosis.",
            "Pediatrics: Contraindicated as plaster in infants and children under 6 years due to delicate skin.",
            "Renal Irritation: Excessive internal consumption of mustard seed oil may cause gastrointestinal and renal irritation."
        ],
        "contraindications_interactions": [
            "Contraindication: Broken skin, mucosal ulcerations, varicose veins, kidney disease.",
            "Interactions: None well-documented with pharmaceutical drugs at culinary doses."
        ],
        "active_phytochemicals": ["Sinigrin (glucosinolate producing allyl isothiocyanate upon myrosinase hydrolysis)", "Erucic acid", "Sinapic acid", "Flavonoids"],
        "botanical_morphology": "Erect annual herb 60-150 cm; lower leaves lyrate-pinnatifid, 10-25 cm long with large terminal lobe; upper leaves smaller, lanceolate; bright yellow 4-petaled flowers; slender silique pods.",
        "native_region": "Central and Eastern Asia; cultivated across India, China, and Europe.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 7. Carissa Carandas (Karanda)
    # -------------------------------------------------------------
    "carissa_carandas": {
        "id": "carissa_carandas",
        "dataset_class": "Carissa Carandas (Karanda)",
        "scientific_name": "Carissa carandas L.",
        "botanical_family": "Apocynaceae (Dogbane family)",
        "genus": "Carissa",
        "synonyms": ["Carissa congesta Wight"],
        "common_names": ["Karanda", "Karamcha", "Bengal Currant", "Karamarda", "Kalakkai"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Traditional & Folk Medicinal Shrub",
        "status_badge_color": "emerald",
        "evidence_category": "Traditional & Ethnomedicinal (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. VI",
            "ICMR Indian Medicinal Plants Compendium",
            "Journal of Natural Remedies"
        ],
        "documented_medicinal_uses": [
            "Antipyretic: Leaf and root decoction traditionally administered for periodic intermittent fevers",
            "Cardiotonic and hypotensive activity demonstrated by root triterpenoid glycosides",
            "Astringent and antiscorbutic ripe and unripe fruit rich in vitamin C and iron",
            "Antidiabetic and hepatoprotective properties documented in leaf extracts"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Fever, diarrhea, diabetes, earache (leaf juice)"},
            {"part": "Root", "indication": "Bitter stomachic, anthelmintic, scabies, cardiac stimulant"},
            {"part": "Fruit", "indication": "Anemia, anorexia, biliousness, astringent digestive pickle"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction", "details": "10 g dried leaves boiled in 200 ml water reduced to 50 ml."},
            {"method": "Root Paste", "details": "Root rubbed with lime juice applied topically to expel intestinal and cutaneous maggots."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Root Powder", "dose": "1 to 3 g daily"},
            {"source": "Ethnomedicinal Reference", "preparation": "Leaf Decoction", "dose": "25 to 50 ml twice daily"},
            {"source": "Modern Pharmacology", "preparation": "Purified Formulation", "dose": "No verified dosage found in the available sources for pharmaceutical isolates."}
        ],
        "precautions_warnings": [
            "Cardiac Glycosides: Roots contain lignans and cardiac steroidal glycosides; high root doses can cause bradycardia and arrhythmias.",
            "Unripe fruit is very sour and acidic; may aggravate gastric hyperacidity."
        ],
        "contraindications_interactions": [
            "Contraindication: Arrhythmias or pre-existing cardiac conduction defects (for root preparations).",
            "Interactions: Potential synergism with digoxin and beta-blockers."
        ],
        "active_phytochemicals": ["Carissone", "Carindone", "Lupeol", "Ursolic acid", "Cardiac glycosides (glucoside of odoroside)", "Ascorbic acid"],
        "botanical_morphology": "Spiny, much-branched evergreen shrub or small tree 3-5 m; branches with sharp paired dichotomous thorns; leaves opposite, oval-elliptic, 3-7 cm long, coriaceous, shining dark green.",
        "native_region": "Indigenous to Indian subcontinent and Southeast Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 8. Citrus Limon (Lemon)
    # -------------------------------------------------------------
    "citrus_limon": {
        "id": "citrus_limon",
        "dataset_class": "Citrus Limon (Lemon)",
        "scientific_name": "Citrus limon (L.) Osbeck",
        "botanical_family": "Rutaceae (Citrus family)",
        "genus": "Citrus",
        "synonyms": ["Citrus medica var. limon L."],
        "common_names": ["Lemon", "Nimbu", "Jambira", "Limbu"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (WHO, API, EMA)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. III",
            "European Medicines Agency (EMA) Community Herbal Monograph on Citrus Oil",
            "British Pharmacopoeia (BP) & United States Pharmacopeia (USP)"
        ],
        "documented_medicinal_uses": [
            "Antiscorbutic and systemic alkalizing agent high in bioavailable ascorbic acid (Vitamin C)",
            "Choleretic and hepatic stimulant enhancing digestive bile secretion",
            "Antiurolithic action: High urinary citrate inhibits calcium oxalate kidney stone nucleation",
            "Antioxidant and endothelial vascular protector via bioflavonoids (hesperidin, eriocitrin)",
            "Topical antimicrobial and astringent for acne, seborrhea, and mild skin hyperpigmentation"
        ],
        "traditionally_used_parts": [
            {"part": "Fruit Juice", "indication": "Scurvy, kidney stones, dyspepsia, dehydration, vomiting"},
            {"part": "Peel / Pericarp", "indication": "Aromatic carminative, essential oil extraction, capillary fragility"},
            {"part": "Leaves", "indication": "Traditional antispasmodic infusion, mild febrifuge, and sedative"}
        ],
        "preparation_information": [
            {"method": "Fresh Fruit Juice", "details": "Freshly squeezed juice diluted in warm water with honey."},
            {"method": "Dried Peel Infusion", "details": "2-3 g dried outer pericarp steeped in 150 ml boiling water for 10 minutes."},
            {"method": "Leaf Infusion", "details": "4-6 fresh fragrant leaves steeped in hot water as a calming bedtime tea."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Fruit Juice (Swarasa)", "dose": "5 to 10 ml twice daily with water"},
            {"source": "British Pharmacopoeia (BP)", "preparation": "Fresh Lemon Juice (Therapeutic posology)", "dose": "30 to 60 ml daily for urinary citrate alkalization"},
            {"source": "European Medicines Agency (EMA)", "preparation": "Expressed Lemon Oil", "dose": "0.1 to 0.3 ml daily for digestive and flavoring use"}
        ],
        "precautions_warnings": [
            "Dental Enamel Erosion: Frequent consumption of undiluted lemon juice can cause demineralization of tooth enamel; rinse mouth with water after drinking.",
            "Phototoxicity: Lemon peel essential oil contains furanocoumarins (bergapten); topical application followed by sun exposure causes phytophotodermatitis.",
            "GERD: May trigger symptoms in acute gastroesophageal reflux."
        ],
        "contraindications_interactions": [
            "Contraindication: Active gastric erosion or severe heartburn.",
            "Interactions: Can mildly enhance iron absorption from plant foods."
        ],
        "active_phytochemicals": ["Citric acid (5-8%)", "Ascorbic acid (Vitamin C)", "Hesperidin and Eriocitrin (flavanones)", "Limonene (up to 70% in peel oil)", "Citral"],
        "botanical_morphology": "Small thorny evergreen tree 3-6 m; leaves alternate, elliptic to ovate, 6-12 cm long, margin faintly serrate, aromatic with pellucid oil glands; winged or narrowly margined petiole.",
        "native_region": "Native to Northeastern India and Southeast Asia; cultivated globally in warm temperate and subtropical zones.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 9. Ficus Auriculata (Roxburgh fig)
    # -------------------------------------------------------------
    "ficus_auriculata": {
        "id": "ficus_auriculata",
        "dataset_class": "Ficus Auriculata (Roxburgh fig)",
        "scientific_name": "Ficus auriculata Lour.",
        "botanical_family": "Moraceae (Mulberry family)",
        "genus": "Ficus",
        "synonyms": ["Ficus roxburghii Wall. ex Miq.", "Ficus macrophylla Roxb."],
        "common_names": ["Roxburgh Fig", "Broadleaf Fig", "Timla", "Gular (Himalayan)", "Elephant Ear Fig"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Traditional Himalayan Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Traditional Himalayan Phytomedicine",
        "authoritative_sources": [
            "Indian Council of Forestry Research and Education (ICFRE) Monographs",
            "Ethnomedicinal Flora of the Himalayas (CSIR)",
            "Journal of Traditional and Complementary Medicine"
        ],
        "documented_medicinal_uses": [
            "Hepatoprotective and digestive tonic in jaundice and liver sluggishness",
            "Astringent and antidiarrheal action of stem bark and leaf decoction",
            "Wound healing and antimicrobial properties topically applied for cuts and sores",
            "Nutritional fodder and edible wild fruit rich in calcium, iron, and fiber"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Diarrhea, dysentery, diabetes, wound washing"},
            {"part": "Stem Bark", "indication": "Jaundice, diabetes, diarrhea, skin disorders"},
            {"part": "Latex", "indication": "Boils, cuts, toothache, and warts"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction", "details": "10-15 g dried leaves boiled in 300 ml water reduced to 75 ml."},
            {"method": "Bark Powder", "details": "Dried bark pulverized and consumed with warm water or buttermilk."},
            {"method": "Latex Topical Application", "details": "Fresh milky sap dabbed directly on skin abrasions."}
        ],
        "dosage_information": [
            {"source": "Ethnomedicinal Himalayan Practice", "preparation": "Stem Bark Decoction", "dose": "30 to 50 ml twice daily"},
            {"source": "Traditional Practice", "preparation": "Leaf Powder", "dose": "2 to 4 g daily"},
            {"source": "Pharmacopoeial Status", "preparation": "Standardized Clinical Posology", "dose": "No verified dosage found in the available sources; traditional practice standard."}
        ],
        "precautions_warnings": [
            "Latex contact may cause skin irritation in individuals with Ficus/latex allergy.",
            "Mild astringent effect may worsen severe constipation."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe chronic constipation.",
            "Interactions: Monitor if taken alongside prescription antidiabetic medications."
        ],
        "active_phytochemicals": ["Flavonoids (Rutin, Quercetin)", "Triterpenoids (Lupeol)", "Tannins", "Berlapgenin", "Polysaccharides"],
        "botanical_morphology": "Low spreading evergreen tree 5-10 m; leaves remarkably large (elephant ear-like), 15-40 cm long, ovate-orbicular to broad cordate, 5-7 basal veins, margin wavy or dentate.",
        "native_region": "Himalayan foothills, Northern India, Nepal, Southern China, and Indochina.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 10. Ficus Religiosa (Peepal Tree)
    # -------------------------------------------------------------
    "ficus_religiosa": {
        "id": "ficus_religiosa",
        "dataset_class": "Ficus Religiosa (Peepal Tree)",
        "scientific_name": "Ficus religiosa L.",
        "botanical_family": "Moraceae (Mulberry family)",
        "genus": "Ficus",
        "synonyms": ["Urostigma religiosum (L.) Gasp."],
        "common_names": ["Peepal", "Sacred Fig", "Bodhi Tree", "Ashvattha", "Arani"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 11",
            "Unani Pharmacopoeia of India"
        ],
        "documented_medicinal_uses": [
            "Astringent and hemostatic: Arrests capillary bleeding, epistaxis, and hematuria",
            "Wound healing: Accelerates granulation and epithelization in burns and chronic ulcers",
            "Antidiabetic: Bark extract improves insulin sensitivity and reduces glycogenolysis",
            "Oral health: Bark decoction gargle tightens gums, relieves toothache and stomatitis",
            "Respiratory support: Bark and tender leaf decoction for bronchial asthma and cough"
        ],
        "traditionally_used_parts": [
            {"part": "Stem Bark (Tvaka)", "indication": "Bleeding disorders, diabetes, diarrhea, skin diseases, oral ulcers"},
            {"part": "Tender Leaves / Shoots", "indication": "Constipation, skin blemishes, nosebleeds, palpitations"},
            {"part": "Latex (Kshira)", "indication": "Cracked heels, boils, warts, minor cuts"},
            {"part": "Fruit (Figs)", "indication": "Digestive weakness, asthma, respiratory irritation"}
        ],
        "preparation_information": [
            {"method": "Bark Decoction (Kashayam)", "details": "20-30 g coarse bark boiled in 400 ml water reduced to 100 ml; taken orally or as gargle."},
            {"method": "Leaf Infusion", "details": "Tender heart-shaped leaves crushed and soaked in water overnight for cooling bowel regulation."},
            {"method": "Bark Powder (Churna)", "details": "Dried bark pulverized and taken with honey or warm milk."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Stem Bark Powder (Churna)", "dose": "3 to 6 g daily in divided doses"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Bark Decoction (Kwatha)", "dose": "50 to 100 ml twice daily"},
            {"source": "ICMR Guidelines", "preparation": "Tender Leaf Juice", "dose": "5 to 10 ml with honey"}
        ],
        "precautions_warnings": [
            "Tender leaves have mild laxative properties; high doses may cause diarrhea.",
            "White latex may cause contact dermatitis in individuals with latex allergies."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe acute diarrhea (for leaf preparations).",
            "Interactions: Potential additive hypoglycemia with prescription antidiabetic medications."
        ],
        "active_phytochemicals": ["Tannins and flavonoids (Quercetin, Kaempferol)", "Beta-sitosterol and Stigmasterol", "Lupan-3-one and Lupeol", "Vitamin K"],
        "botanical_morphology": "Large semi-evergreen tree up to 30 m; leaves distinctly heart-shaped (cordate), 10-18 cm long, with an extraordinary elongated drip tip (tail) 2-6 cm long; slender petiole fluttering in the wind.",
        "native_region": "Indian subcontinent and Indochina; revered across Hindu and Buddhist traditions.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 11. Hibiscus Rosa-sinensis
    # -------------------------------------------------------------
    "hibiscus_rosa_sinensis": {
        "id": "hibiscus_rosa_sinensis",
        "dataset_class": "Hibiscus Rosa-sinensis",
        "scientific_name": "Hibiscus rosa-sinensis L.",
        "botanical_family": "Malvaceae (Mallow family)",
        "genus": "Hibiscus",
        "synonyms": ["Hibiscus boryanus DC."],
        "common_names": ["Hibiscus", "China Rose", "Japa", "Gudhal", "Shoeblackplant"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. IV",
            "ICMR Indian Medicinal Plants Compendium",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Trichological regenerative: Promotes hair follicle proliferation, prevents premature greying and dandruff",
            "Cardioprotective and antihypertensive: Calyx/flower anthocyanins induce peripheral vasodilation and lower blood pressure",
            "Menstrual regulation: Traditionally used for menorrhagia, dysmenorrhea, and menstrual balance",
            "Demulcent and cooling: Soothes urinary tract cystitis, burning sensation, and oral aphthous ulcers"
        ],
        "traditionally_used_parts": [
            {"part": "Flowers (Pushpa)", "indication": "Hypertension, dysmenorrhea, alopecia, cystitis, cardiac tonic"},
            {"part": "Leaves (Patra)", "indication": "Hair conditioning paste, burning micturition, emollient poultice"}
        ],
        "preparation_information": [
            {"method": "Medicated Hair Oil (Japapushpa Taila)", "details": "Fresh flowers and leaves processed into coconut or sesame oil for scalp application."},
            {"method": "Flower Infusion / Herbal Tea", "details": "3-5 fresh red flowers steeped in 150 ml hot water with a dash of lime."},
            {"method": "Leaf Paste", "details": "Fresh leaves crushed into mucilaginous paste for natural conditioning hair wash."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Flower Powder", "dose": "5 to 10 g daily in divided doses"},
            {"source": "Clinical Reference", "preparation": "Flower Infusion", "dose": "50 to 100 ml twice daily"},
            {"source": "Standard Monograph", "preparation": "Leaf Paste (External)", "dose": "Apply liberally to scalp 30 minutes before bathing"}
        ],
        "precautions_warnings": [
            "Pregnancy: Flowers have documented mild emmenagogue and anti-implantation properties; avoid internal therapeutic doses during pregnancy.",
            "Hypotension: May potentiate antihypertensive medications; monitor blood pressure."
        ],
        "contraindications_interactions": [
            "Contraindication: Pregnancy (for internal medicinal doses).",
            "Interactions: Additive blood pressure lowering when taken with ACE inhibitors or beta-blockers."
        ],
        "active_phytochemicals": ["Anthocyanins (Cyanidin-3-sophoroside)", "Flavonoids (Quercetin, Kaempferol)", "Mucilage (acidic polysaccharides)", "Ascorbic acid"],
        "botanical_morphology": "Evergreen woody shrub 2-5 m tall; leaves alternate, ovate to lanceolate, 5-12 cm long, glossy dark green with serrate margins; solitary large showy trumpet-shaped 5-petaled flowers with long projecting staminal column.",
        "native_region": "Tropical East Asia; cultivated pantropically as an ornamental and medicinal shrub.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 12. Jasminum (Jasmine)
    # -------------------------------------------------------------
    "jasminum": {
        "id": "jasminum",
        "dataset_class": "Jasminum (Jasmine)",
        "scientific_name": "Jasminum officinale L. / Jasminum grandiflorum L.",
        "botanical_family": "Oleaceae (Olive family)",
        "genus": "Jasminum",
        "synonyms": ["Jasminum grandiflorum L.", "Jasminum officinale var. grandiflorum"],
        "common_names": ["Jasmine", "Jati", "Chameli", "Malati", "Royal Jasmine"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Traditional (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "International Journal of Aromatherapy",
            "WHO Traditional Medicine Records"
        ],
        "documented_medicinal_uses": [
            "Oral health and stomatitis: Leaf decoction gargle heals mouth ulcers, gingivitis, and aphthous stomatitis",
            "Wound antiseptic and debridement: Accelerates cicatrization and epithelization in chronic indolent ulcers",
            "Anxiolytic and sedative aromatherapy: Inhalation of jasmine volatile oil reduces anxiety and uplifts mood",
            "Lactation suppression: Topical flower compress traditionally applied to arrest excessive milk production"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Jati Patra)", "indication": "Mouth ulcers, dental caries, skin wounds, eye wash"},
            {"part": "Flowers (Pushpa)", "indication": "Anxiety, insomnia, lactation suppression (topical), aromatic perfume"},
            {"part": "Root", "indication": "Ringworm, sedative decoction in traditional insomnia"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction Gargle", "details": "10-15 g fresh leaves boiled in 300 ml water down to 100 ml; used warm as mouthwash."},
            {"method": "Medicated Ghee / Oil (Jatyadi Ghrita / Taila)", "details": "Classical Ayurvedic formulation prepared from Jati leaves for deep wound and ulcer healing."},
            {"method": "Flower Compress", "details": "Fresh bruised flowers applied to breasts for lactation weaning."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Leaf Powder", "dose": "1 to 3 g daily"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Leaf Decoction (Kwatha)", "dose": "25 to 50 ml as oral gargle or internal dose"},
            {"source": "Topical Monograph", "preparation": "Jatyadi Taila", "dose": "Apply topically twice daily on cleansed wounds"}
        ],
        "precautions_warnings": [
            "Contact Sensitivity: Essential oil may rarely cause allergic contact dermatitis in sensitive individuals; perform skin patch test.",
            "Lactation: Breastfeeding mothers should not apply flower compresses to the breasts as it inhibits prolactin and suppresses milk production."
        ],
        "contraindications_interactions": [
            "Contraindication: Women wishing to maintain breastfeeding should avoid topical flower application to breasts.",
            "Interactions: None known with oral pharmaceuticals."
        ],
        "active_phytochemicals": ["Secoiridoid glycosides (Jasminoside, Oleuropein)", "Benzyl acetate", "Linalool", "Jasmone", "Indole", "Flavonoids"],
        "botanical_morphology": "Climbing or sprawling woody deciduous or semi-evergreen shrub 2-4 m; leaves opposite, pinnate with 5-9 elliptic leaflets (terminal leaflet largest); clusters of intensely fragrant white 5-lobed flowers.",
        "native_region": "Central and South Asia (Iran, Afghanistan, India, Western China).",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 13. Mangifera Indica (Mango)
    # -------------------------------------------------------------
    "mangifera_indica": {
        "id": "mangifera_indica",
        "dataset_class": "Mangifera Indica (Mango)",
        "scientific_name": "Mangifera indica L.",
        "botanical_family": "Anacardiaceae (Cashew family)",
        "genus": "Mangifera",
        "synonyms": ["Mangifera domestica Gaertn."],
        "common_names": ["Mango", "Amra", "Aam", "Mavina Mara"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Tree",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API & ICMR)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 16",
            "Phytotherapy Research Monographs"
        ],
        "documented_medicinal_uses": [
            "Antidiabetic action: Tender leaf infusion inhibits alpha-glucosidase and improves insulin resistance",
            "Antidiarrheal and hemostatic: Stem bark and seed kernel arrest chronic diarrhea, dysentery, and menorrhagia",
            "Powerful antioxidant and cardioprotector via high concentrations of the xanthone Mangiferin",
            "Oral health: Leaf chewing or ash powder strengthens gums and acts as an antiseptic toothpowder"
        ],
        "traditionally_used_parts": [
            {"part": "Tender Leaves", "indication": "Diabetes, diarrhea, throat wash, dental care, asthma"},
            {"part": "Stem Bark", "indication": "Astringent, dysentery, menorrhagia, cutaneous ulcers"},
            {"part": "Seed Kernel", "indication": "Intestinal worms, chronic diarrhea, leucorrhoea"}
        ],
        "preparation_information": [
            {"method": "Tender Leaf Infusion", "details": "4-6 tender purple-tinted leaves soaked in hot water overnight, strained and drunk in the morning."},
            {"method": "Bark Decoction", "details": "15-20 g coarse stem bark boiled in 400 ml water down to 100 ml."},
            {"method": "Seed Kernel Powder", "details": "Dried seed kernel pulverized and taken with buttermilk for dysentery."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Stem Bark Powder", "dose": "3 to 6 g daily in divided doses"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Seed Kernel Powder", "dose": "1 to 2 g twice daily"},
            {"source": "Ethnomedicinal Reference", "preparation": "Tender Leaf Infusion", "dose": "50 to 100 ml once daily in the morning"}
        ],
        "precautions_warnings": [
            "Urushiol Contact: Mango peel, stem sap, and bark contain trace alkylresorcinols and urushiol; can cause contact cheilitis or dermatitis in Poison Ivy-sensitive individuals.",
            "Antidiabetic synergy: Monitor blood glucose if combined with metformin or sulfonylureas."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe hypersensitivity to Anacardiaceae family plants.",
            "Interactions: Potential additive hypoglycemia with prescription antidiabetic medications."
        ],
        "active_phytochemicals": ["Mangiferin (C-glucosylxanthone)", "Tannins", "Gallic acid", "Quercetin", "Lupeol", "Beta-carotene"],
        "botanical_morphology": "Large evergreen tree 10-30 m; leaves alternate, simple, oblong-lanceolate, 15-30 cm long, coriaceous, deep shiny green above (copper-purple when tender); large branched terminal panicles.",
        "native_region": "Native to tropical South Asia (India, Myanmar, Bangladesh); cultivated worldwide.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 14. Mentha (Mint)
    # -------------------------------------------------------------
    "mentha": {
        "id": "mentha",
        "dataset_class": "Mentha (Mint)",
        "scientific_name": "Mentha arvensis L. / Mentha spicata L.",
        "botanical_family": "Lamiaceae (Mint family)",
        "genus": "Mentha",
        "synonyms": ["Mentha canadensis L.", "Mentha cordifolia Opiz"],
        "common_names": ["Mint", "Field Mint", "Pudina", "Spearmint", "Japanese Mint"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO, API, EMA)",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 2 (2002)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "European Medicines Agency (EMA) Community Herbal Monograph"
        ],
        "documented_medicinal_uses": [
            "Gastrointestinal antispasmodic and carminative: Relaxes GI smooth muscle (IBS, dyspepsia, colic)",
            "Topical antipruritic and analgesic: Menthol stimulates TRPM8 cold receptors for soothing pain relief",
            "Respiratory decongestant: Steam vapor relieves nasal catarrh, sinus pressure, and mild bronchitis",
            "Antiemetic and digestive appetizer: Suppresses nausea, vomiting, and morning sickness"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Indigestion, flatulence, nausea, headache, fever, halitosis"},
            {"part": "Volatile Oil (Menthol)", "indication": "Topical tension headache, IBS enteric capsules, steam inhalation"}
        ],
        "preparation_information": [
            {"method": "Leaf Infusion (Pudina Phanta)", "details": "2-3 g dried leaves infused in 150 ml boiling water for 10 minutes in a closed vessel."},
            {"method": "Fresh Leaf Juice / Chutney", "details": "Fresh leaves crushed with black salt and lemon as carminative appetizer."},
            {"method": "Steam Inhalation", "details": "2-3 drops of mint oil in a bowl of hot steaming water."}
        ],
        "dosage_information": [
            {"source": "WHO Monographs on Selected Medicinal Plants (Vol. 2)", "preparation": "Dried Leaf Infusion", "dose": "1.5 to 3.0 g in 150 ml water, 3 times daily"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice (Swarasa)", "dose": "5 to 10 ml twice daily"},
            {"source": "European Medicines Agency (EMA)", "preparation": "Mentha Oil (Enteric-coated)", "dose": "0.2 to 0.4 ml 3 times daily before meals"}
        ],
        "precautions_warnings": [
            "GERD / Acid Reflux: Menthol relaxes the lower esophageal sphincter; can worsen reflux and heartburn.",
            "Infant Facial Application: Never apply menthol or mint oil directly to nostrils or face of infants; risks reflex laryngospasm.",
            "Biliary tract disorders: Caution in gallstones."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe gastroesophageal reflux (GERD), biliary obstruction, infant facial use.",
            "Interactions: Antacids (may dissolve enteric coating of mint capsules prematurely)."
        ],
        "active_phytochemicals": ["Menthol (up to 70-80% in volatile oil)", "Menthone", "Menthyl acetate", "Rosmarinic acid", "Luteolin"],
        "botanical_morphology": "Perennial aromatic creeping herb 30-60 cm; quadrangular purplish stems; leaves opposite, ovate-lanceolate, 2.5-6 cm long, sharply serrated margins, releasing strong mint aroma when bruised.",
        "native_region": "Temperate and subtropical Eurasia; cultivated ubiquitously.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 15. Moringa Oleifera (Drumstick)
    # -------------------------------------------------------------
    "moringa_oleifera": {
        "id": "moringa_oleifera",
        "dataset_class": "Moringa Oleifera (Drumstick)",
        "scientific_name": "Moringa oleifera Lam.",
        "botanical_family": "Moringaceae",
        "genus": "Moringa",
        "synonyms": ["Moringa pterygosperma Gaertn."],
        "common_names": ["Moringa", "Drumstick Tree", "Shigru", "Miracle Tree", "Sahijan"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial & Nutra-Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (API & WHO/FAO)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "WHO / FAO Nutritional Compendium on Underutilized Greens",
            "ICMR Monographs on Indian Medicinal Plants"
        ],
        "documented_medicinal_uses": [
            "High micronutrient restorative: Exceptionally rich in Vitamin A, C, calcium, iron, and amino acids",
            "Anti-hyperglycemic: Chlorogenic acid and isothiocyanates improve insulin sensitivity",
            "Hypolipidemic: Reduces serum cholesterol, LDL, and atherogenic triglycerides",
            "Galactagogue: Stimulates prolactin secretion to increase breast milk volume in lactating mothers",
            "Anti-inflammatory: Relieves joint swelling and stiffness in osteoarthritis"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Malnutrition, anemia, diabetes, arthritis, lactation enhancement"},
            {"part": "Pods / Fruit", "indication": "Nutritious culinary vegetable, digestive appetizer"},
            {"part": "Seeds", "indication": "Natural water clarification (coagulant), antimicrobial, oil source"},
            {"part": "Bark and Root", "indication": "Deep inflammatory disorders (Caution: potential abortifacient toxicity in root bark)"}
        ],
        "preparation_information": [
            {"method": "Leaf Powder", "details": "Shade-dried green leaves pulverized into fine emerald powder; added to water or smoothies."},
            {"method": "Fresh Leaf Decoction", "details": "10-20 g fresh leaves boiled in 200 ml water; taken warm."},
            {"method": "Culinary Pods", "details": "Cooked in curries and soups for nutritional rejuvenation."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Leaf Powder (Churna)", "dose": "2 to 5 g daily"},
            {"source": "WHO / FAO Dietary Recommendation", "preparation": "Nutritional Leaf Supplement", "dose": "5 to 10 g daily for micronutrient deficiency"},
            {"source": "ICMR Guidelines", "preparation": "Seed Extract", "dose": "1 to 2 g under professional supervision"}
        ],
        "precautions_warnings": [
            "Root Bark Warning: Root and root bark contain the alkaloid spirochin, which exhibits neurotoxic paralysis and abortifacient effects; avoid root bark preparations.",
            "Pregnancy: Leaves in culinary amounts are safe, but high medicinal leaf concentrates or root preparations should be avoided.",
            "Mild Laxative: High initial doses may cause loose stools."
        ],
        "contraindications_interactions": [
            "Contraindication: Pregnancy (for root and bark preparations).",
            "Interactions: Antidiabetic medications (potential additive hypoglycemia), Antihypertensives (additive blood pressure lowering)."
        ],
        "active_phytochemicals": ["Moringine and Moringinine", "Quercetin and Kaempferol", "Chlorogenic acid", "Beta-sitosterol", "Glucosinolates"],
        "botanical_morphology": "Fast-growing deciduous tree 10-12 m; tripinnate leaves 30-60 cm long with small elliptic leaflets (1-2 cm); yellowish-white fragrant flowers; long pendulous 3-valved ribbed pods.",
        "native_region": "Sub-Himalayan tracts of Northern India; cultivated throughout the tropics.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 16. Muntingia Calabura (Jamaica Cherry-Gasagase)
    # -------------------------------------------------------------
    "muntingia_calabura": {
        "id": "muntingia_calabura",
        "dataset_class": "Muntingia Calabura (Jamaica Cherry-Gasagase)",
        "scientific_name": "Muntingia calabura L.",
        "botanical_family": "Muntingiaceae",
        "genus": "Muntingia",
        "synonyms": ["Muntingia rosea Humb. & Bonpl."],
        "common_names": ["Jamaica Cherry", "Gasagase Hannu", "Calabur", "Singapore Cherry", "Panama Berry"],
        "is_medicinal": True,
        "medicinal_status": "Traditional / Folk Medicinal Tree",
        "status_badge_color": "amber",
        "evidence_category": "Traditional Ethnomedicine (Folk Use)",
        "authoritative_sources": [
            "Ethnomedicinal Field Studies (Karnataka & Kerala)",
            "Asian Pacific Journal of Tropical Biomedicine",
            "USDA GRIN Taxonomy Records"
        ],
        "documented_medicinal_uses": [
            "Antidiabetic folk remedy: Leaf tea traditionally consumed to lower blood sugar in rural communities",
            "Anti-inflammatory and antinociceptive: Relieves headache, body ache, and cold symptoms",
            "Antimicrobial activity: Leaf flavonoid extracts inhibit Staphylococcus aureus and E. coli",
            "Edible sweet berries rich in vitamin C and polyphenols"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Traditional herbal tea for diabetes, headache, and gastric spasms"},
            {"part": "Flowers", "indication": "Antispasmodic infusion for headache and infant colic"},
            {"part": "Fruit", "indication": "Nutritious edible berry, mild digestive tonic"}
        ],
        "preparation_information": [
            {"method": "Folk Leaf Tea", "details": "5-8 fresh leaves boiled in 250 ml water for 5 minutes; consumed as herbal tea in folk medicine."}
        ],
        "dosage_information": [
            {"source": "Pharmacopoeial Verification", "preparation": "Clinical Standard", "dose": "No verified dosage found in the available sources."},
            {"source": "Ethnomedicinal Observation", "preparation": "Folk Leaf Tea", "dose": "Dosage information not verified by official pharmacopoeias; folk use 1 cup daily."}
        ],
        "precautions_warnings": [
            "No formal safety evaluation in pregnant or lactating women has been completed.",
            "Do not substitute verified medical treatment of diabetes with unstandardized folk leaf teas."
        ],
        "contraindications_interactions": [
            "Contraindication: Pregnancy and lactation due to absence of authoritative safety data.",
            "Interactions: Unknown; potential theoretical synergy with oral antidiabetics."
        ],
        "active_phytochemicals": ["Flavonoids (Chrysin, Pinostrobin, Galangin)", "Tannins", "Saponins", "Anthocyanins"],
        "botanical_morphology": "Small fast-growing spreading tree 5-10 m; leaves alternate, oblong-lanceolate, 5-12 cm long, distinctly asymmetric at base, margins serrated, densely pubescent with stellate hairs beneath; white solitary flowers.",
        "native_region": "Tropical Americas; widely naturalized across India and Southeast Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 17. Murraya Koenigii (Curry)
    # -------------------------------------------------------------
    "murraya_koenigii": {
        "id": "murraya_koenigii",
        "dataset_class": "Murraya Koenigii (Curry)",
        "scientific_name": "Murraya koenigii (L.) Spreng.",
        "botanical_family": "Rutaceae (Citrus family)",
        "genus": "Murraya",
        "synonyms": ["Bergera koenigii L."],
        "common_names": ["Curry Leaf", "Kadi Patta", "Kaalasaaka", "Karivepaku", "Kariveppila"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. IV",
            "ICMR Indian Medicinal Plants Monographs",
            "Food and Chemical Toxicology"
        ],
        "documented_medicinal_uses": [
            "Hypoglycemic: Mahanimbine carbazole alkaloid stimulates insulin secretion and protects beta-cells",
            "Hypocholesterolemic and hepatoprotective: Prevents hepatic steatosis and lowers LDL cholesterol",
            "Trichological hair tonic: Strengthens hair roots, prevents premature greying and hair thinning",
            "Digestive stimulant and carminative: Relieves morning sickness, nausea, and dysentery"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Diabetes, dyslipidemia, premature greying, nausea, dysentery"},
            {"part": "Bark and Roots", "indication": "Traditional decoction for kidney pain and skin eruptions"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice", "details": "10-15 fresh leaves ground with buttermilk and a pinch of rock salt for morning sickness."},
            {"method": "Leaf Powder (Churna)", "details": "Shade-dried leaves ground into fine aromatic powder for metabolic regulation."},
            {"method": "Medicated Hair Oil", "details": "Leaves boiled in pure coconut oil until blackened; strained and applied to hair roots."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Leaf Powder", "dose": "2 to 4 g twice daily with buttermilk"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice", "dose": "10 to 20 ml once daily"},
            {"source": "Clinical Reference", "preparation": "Dietary Use", "dose": "10 to 15 fresh leaves chewed raw daily"}
        ],
        "precautions_warnings": [
            "Culinary amounts are completely safe for all populations.",
            "Large therapeutic extracts combined with antidiabetic medications may require dose adjustments."
        ],
        "contraindications_interactions": [
            "Contraindication: None documented at recommended dosages.",
            "Interactions: Mild additive effect with oral antidiabetic agents."
        ],
        "active_phytochemicals": ["Mahanimbine", "Koenimbine", "Girimbine (carbazole alkaloids)", "Caryophyllene", "Beta-carotene", "Iron"],
        "botanical_morphology": "Aromatic semi-deciduous small tree 4-6 m; leaves pinnate, 15-30 cm long with 11-25 alternate ovate-lanceolate asymmetric leaflets (2-4 cm); intensely aromatic when crushed; clusters of white flowers followed by black berries.",
        "native_region": "Native to Indian subcontinent and Indochina; widely cultivated.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 18. Nerium Oleander (Oleander) [TOXIC CONTROL]
    # -------------------------------------------------------------
    "nerium_oleander": {
        "id": "nerium_oleander",
        "dataset_class": "Nerium Oleander (Oleander)",
        "scientific_name": "Nerium oleander L.",
        "botanical_family": "Apocynaceae (Dogbane family)",
        "genus": "Nerium",
        "synonyms": ["Nerium indicum Mill.", "Nerium odorum Sol."],
        "common_names": ["Oleander", "Kaner", "Karavira", "Rose Bay", "Adelfa"],
        "is_medicinal": False,
        "medicinal_status": "Extremely Toxic / Poisonous Plant (Non-Medicinal)",
        "status_badge_color": "rose",
        "evidence_category": "Clinical Toxicology Warning (WHO & IPCS)",
        "authoritative_sources": [
            "International Programme on Chemical Safety (IPCS / INCHEM) Monograph PIM 366",
            "American Association of Poison Control Centers (AAPCC) Toxic Plant Guidelines",
            "TOXNET / Hazardous Substances Data Bank (HSDB)"
        ],
        "documented_medicinal_uses": [
            "NO SAFE RECOGNIZED MEDICINAL USES in modern healthcare.",
            "Historical note: Dangerous Ayurvedic and folk applications for severe skin disease and cardiac dropsy were abandoned due to extreme fatality rates.",
            "Oleandrin is researched in in-vitro cancer laboratories, but crude plant ingestion is lethal."
        ],
        "traditionally_used_parts": [
            {"part": "None", "indication": "ALL PARTS (leaves, stems, flowers, seeds, roots, sap, and smoke from burning wood) ARE POTENTIALLY FATAL."}
        ],
        "preparation_information": [
            {"method": "STRICTLY FORBIDDEN", "details": "Contains lethal cardiac glycosides. Do not prepare or ingest under any circumstance."}
        ],
        "dosage_information": [
            {"source": "WHO Poisons Information Monograph (PIM 366)", "preparation": "Lethal Toxicity Threshold", "dose": "Ingestion of even a single leaf can be fatal to an adult or child. DOSE IS ZERO (CONTRAINDICATED)."}
        ],
        "precautions_warnings": [
            "LETHAL POISON WARNING: Contains high concentrations of potent cardiotoxins (Oleandrin and Neriine) that block the sodium-potassium ATPase pump in heart muscle.",
            "Symptoms of Ingestion: Severe vomiting, bloody diarrhea, extreme bradycardia, visual yellow halos (xanthopsia), ventricular fibrillation, heart block, and fatal cardiac arrest.",
            "Medical Emergency: Anyone suspected of ingesting oleander requires immediate emergency hospitalization, gastric lavage, activated charcoal, and Digoxin-specific Fab antibody fragments (Digibind)."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: ALL INTERNAL CONSUMPTION IS STRICTLY CONTRAINDICATED.",
            "Interactions: Fatal synergism with digitalis, beta-blockers, and calcium channel blockers."
        ],
        "active_phytochemicals": ["Oleandrin (potent cardenolide)", "Neriine", "Adynerin", "Folinerin", "Rosagenin"],
        "botanical_morphology": "Erect evergreen shrub 2-5 m tall; leaves in whorls of 3, narrow lanceolate, 10-22 cm long, 1.5-3 cm wide, leathery, dark green with prominent pale midrib and parallel veins; showy pink, red, or white flowers.",
        "native_region": "Mediterranean basin and coastal Southwest Asia; widely planted along highways as drought-tolerant ornamental.",
        "iucn_conservation_status": "Least Concern (Highly Toxic)"
    },

    # -------------------------------------------------------------
    # 19. Nyctanthes Arbor-tristis (Parijata)
    # -------------------------------------------------------------
    "nyctanthes_arbor_tristis": {
        "id": "nyctanthes_arbor_tristis",
        "dataset_class": "Nyctanthes Arbor-tristis (Parijata)",
        "scientific_name": "Nyctanthes arbor-tristis L.",
        "botanical_family": "Oleaceae (sometimes placed in Verbenaceae)",
        "genus": "Nyctanthes",
        "synonyms": ["Nyctanthes dentata Blume"],
        "common_names": ["Parijata", "Night-flowering Jasmine", "Harsingar", "Shiuli", "Coral Jasmine"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Indian Medicinal Plants Monographs",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Sciatica and arthritic neuralgia: Fresh leaf decoction is considered a premier traditional therapeutic for sciatica and lumbago",
            "Antipyretic and anti-inflammatory: Effective in chronic and intermittent malarial or viral fevers",
            "Anthelmintic: Expels roundworms and threadworms in children",
            "Hepatoprotective and cholagogue action stimulating bile flow"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Sciatica, chronic arthritis, obstinate fevers, worm infestation, cough"},
            {"part": "Flowers", "indication": "Mild carminative, natural saffron-orange dye (corolla tube)"},
            {"part": "Seeds", "indication": "Alopecia and scalp dandruff paste"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction (Parijata Kwatha for Sciatica)", "details": "5-10 fresh leaves bruised and boiled in 200 ml water reduced to 50 ml; consumed warm twice daily."},
            {"method": "Leaf Juice with Honey", "details": "Fresh expressed juice taken with honey and a pinch of black pepper for fevers."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Leaf Powder", "dose": "1 to 3 g daily"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Leaf Decoction (Kwatha)", "dose": "20 to 50 ml twice daily before meals"},
            {"source": "Clinical Reference", "preparation": "Fresh Leaf Juice", "dose": "5 to 10 ml with honey"}
        ],
        "precautions_warnings": [
            "Intense Bitterness: Fresh juice is extremely bitter and can cause nausea; consume with honey.",
            "Pregnancy: Avoid therapeutic high-dose leaf decoction during pregnancy due to mild emmenagogue action."
        ],
        "contraindications_interactions": [
            "Contraindication: Pregnancy.",
            "Interactions: None well-documented with pharmaceuticals."
        ],
        "active_phytochemicals": ["Arbortristoside A, B, and C (iridoid glucosides)", "Nyctanthoside", "Mannitol", "Beta-sitosterol", "Crocin (in corolla tube)"],
        "botanical_morphology": "Large coarse shrub or small tree up to 10 m with quadrangular branches; leaves opposite, ovate, 6-12 cm long, acute, margin entire or distantly toothed, harshly scabrous (sandpaper-like); night-opening fragrant white flowers with bright orange-red tubes.",
        "native_region": "Native to tropical South Asia (India, Nepal, Thailand).",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 20. Ocimum Tenuiflorum (Tulsi)
    # -------------------------------------------------------------
    "ocimum_tenuiflorum": {
        "id": "ocimum_tenuiflorum",
        "dataset_class": "Ocimum Tenuiflorum (Tulsi)",
        "scientific_name": "Ocimum tenuiflorum L. (syn. Ocimum sanctum L.)",
        "botanical_family": "Lamiaceae (Mint family)",
        "genus": "Ocimum",
        "synonyms": ["Ocimum sanctum L."],
        "common_names": ["Tulsi", "Holy Basil", "Sacred Basil", "Kaphari"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO, API, ICMR)",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 2 (2002)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 18"
        ],
        "documented_medicinal_uses": [
            "Adaptogenic and stress-modulating: Lowers elevated cortisol and oxidative stress biomarkers",
            "Upper respiratory tract infection relief: Antimicrobial, bronchodilator, and mucolytic",
            "Antipyretic and immunomodulatory in viral fevers, bronchitis, and influenza",
            "Mild hypoglycemic effect: reduces fasting and postprandial blood glucose",
            "Cardioprotective and antihyperlipidemic through lipid peroxidation inhibition"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Cough, cold, asthma, bronchitis, digestive spasms, cutaneous infections"},
            {"part": "Whole Plant", "indication": "Fever, metabolic disorders, generalized debility, immune support"},
            {"part": "Seeds", "indication": "Genitourinary tract irritation, demulcent in cystitis"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Swarasa)", "details": "Fresh leaves crushed and pressed; taken with raw honey."},
            {"method": "Leaf Infusion (Phanta)", "details": "2-4 g dried leaves steeped in 150 ml boiling water for 10-15 minutes."},
            {"method": "Decoction (Kashayam)", "details": "Leaves boiled down to 1/4th volume with ginger and black pepper."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice", "dose": "10 to 20 ml twice daily"},
            {"source": "WHO Monograph on Selected Medicinal Plants (Vol. 2)", "preparation": "Dried Leaf Infusion", "dose": "1.0 to 2.5 g in 150 ml water, 2 to 3 times daily"},
            {"source": "ICMR Guidelines", "preparation": "Standardized Extract", "dose": "300 to 600 mg daily in divided doses"}
        ],
        "precautions_warnings": [
            "Pregnancy: Tulsi exhibits mild anti-implantation activity in animal models; avoid high medicinal doses in first trimester.",
            "Hypoglycemia: Patients on oral hypoglycemics or insulin must monitor blood sugar to avoid synergistic drops.",
            "Platelet Aggregation: Eugenol content may slightly prolong bleeding time; withhold 2 weeks prior to surgery."
        ],
        "contraindications_interactions": [
            "Contraindication: Hypersensitivity to Lamiaceae family plants.",
            "Interactions: Anticoagulants (Warfarin, Heparin) - increased bruising risk; Antidiabetic agents (Metformin) - additive hypoglycemia."
        ],
        "active_phytochemicals": ["Eugenol (up to 70% in volatile oil)", "Ursolic acid", "Rosmarinic acid", "Caryophyllene", "Linalool"],
        "botanical_morphology": "Erect aromatic subshrub 30-60 cm; leaves opposite, ovate or elliptic, 2.5-5 cm long, margin faintly serrate, pubescent on both surfaces with conspicuous glandular dots; purple or green tinged.",
        "native_region": "Indian subcontinent and widespread across tropical Southeast Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 21. Piper Betle (Betel)
    # -------------------------------------------------------------
    "piper_betle": {
        "id": "piper_betle",
        "dataset_class": "Piper Betle (Betel)",
        "scientific_name": "Piper betle L.",
        "botanical_family": "Piperaceae (Pepper family)",
        "genus": "Piper",
        "synonyms": ["Chavica betle (L.) Miq."],
        "common_names": ["Betel Leaf", "Paan", "Tambula", "Nagavalli", "Vethalapaakku"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Traditional (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. III",
            "ICMR Indian Medicinal Plants Compendium",
            "American Journal of Chinese Medicine"
        ],
        "documented_medicinal_uses": [
            "Potent oral antiseptic: Suppresses oral anaerobic bacteria, Streptococcus mutans, and dental plaque",
            "Digestive and carminative: Chewed after meals to stimulate salivary amylase and gastric secretions",
            "Topical anti-inflammatory poultice: Warmed leaves with castor oil applied to relieve pediatric chest congestion",
            "Wound antiseptic: Antimicrobial action accelerates healing in burns, eczema, and cutaneous wounds"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Bad breath, indigestion, cough, chest congestion poultice, boils"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Swarasa)", "details": "Fresh leaves crushed and pressed; taken with honey for pediatric cough."},
            {"method": "Warmed Leaf Poultice", "details": "Leaf smeared with castor oil, warmed gently, applied on chest for bronchial congestion."},
            {"method": "Traditional Chewing (Paan)", "details": "Fresh leaf chewed with areca nut and spices (Note: consume plain leaf without tobacco or areca nut to avoid carcinogenic risk)."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice (Swarasa)", "dose": "5 to 10 ml twice daily with honey"},
            {"source": "Traditional Practice", "preparation": "Fresh Raw Leaf", "dose": "1 to 2 leaves chewed after meals"}
        ],
        "precautions_warnings": [
            "Plain Leaf vs Commercial Paan: Pure Piper betle leaf is non-carcinogenic and antimicrobial. However, chewing betel leaf with Areca nut (supari) and slaked lime/tobacco is a proven Group 1 carcinogen (IARC) causing oral submucous fibrosis and oral squamous cell carcinoma. Never combine with tobacco or areca nut.",
            "Excessive consumption may cause mild salivation and tooth staining."
        ],
        "contraindications_interactions": [
            "Contraindication: Active oral submucous fibrosis, leukoplakia.",
            "Interactions: None documented for plain leaf at therapeutic amounts."
        ],
        "active_phytochemicals": ["Chavibetol", "Hydroxychavicol", "Eugenol", "Caryophyllene", "Terpinyl acetate"],
        "botanical_morphology": "Dioecious perennial evergreen climbing vine; stems semi-woody rooting at nodes; leaves alternate, broadly ovate to cordate, 10-18 cm long, glossy dark green, 5-7 prominent palmate veins from base.",
        "native_region": "Native to tropical Southeast Asia; cultivated widely across South Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 22. Plectranthus Amboinicus (Mexican Mint)
    # -------------------------------------------------------------
    "plectranthus_amboinicus": {
        "id": "plectranthus_amboinicus",
        "dataset_class": "Plectranthus Amboinicus (Mexican Mint)",
        "scientific_name": "Coleus amboinicus Lour. (syn. Plectranthus amboinicus)",
        "botanical_family": "Lamiaceae (Mint family)",
        "genus": "Coleus",
        "synonyms": ["Plectranthus amboinicus (Lour.) Spreng.", "Coleus aromaticus Benth."],
        "common_names": ["Mexican Mint", "Indian Borage", "Ajwain Leaf", "Karpuravalli", "Dodda Patre"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. IV",
            "ICMR Indian Medicinal Plants Compendium",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Pediatric cough and cold: Fresh leaf juice with honey is the premier household remedy for acute bronchitis and catarrh",
            "Potent bronchodilator: Relaxes tracheal smooth muscle and liquefies phlegm in asthmatic wheezing",
            "Antiurolithic action: Promotes dissolution of calcium oxalate urinary crystals and acts as a gentle diuretic",
            "Digestive carminative: Relieves abdominal colic, flatulence, and indigestion in infants and adults"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Cough, cold, asthma, bronchitis, urinary calculi, indigestion, insect stings"}
        ],
        "preparation_information": [
            {"method": "Fresh Expressed Leaf Juice (Swarasa)", "details": "Fresh succulent leaves warmed on low heat, crushed and pressed; juice taken with honey."},
            {"method": "Herbal Decoction", "details": "5-10 leaves boiled in 200 ml water with black pepper down to 50 ml."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Juice (Swarasa)", "dose": "5 to 10 ml twice daily (Adults); 2.5 to 5 ml with honey (Children)"},
            {"source": "Ethnomedicinal Reference", "preparation": "Dried Leaf Powder", "dose": "1 to 3 g daily in divided doses"}
        ],
        "precautions_warnings": [
            "Thymol and carvacrol content can cause mild throat tingling; always take fresh juice with honey.",
            "Generally safe with high safety margin in pediatric traditional usage."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe hypersensitivity to Lamiaceae family plants.",
            "Interactions: None well-documented with pharmaceuticals."
        ],
        "active_phytochemicals": ["Carvacrol (high percentage in volatile oil)", "Thymol", "Caryophyllene", "Rosmarinic acid", "Flavonoids (Salpigenin)"],
        "botanical_morphology": "Sprawling aromatic succulent herb 30-90 cm; stems fleshy, densely pubescent; leaves opposite, thick and fleshy, broadly ovate, 4-9 cm long, crenate margin, releasing intense oregano/thyme aroma when bruised.",
        "native_region": "Southern and Eastern Africa; cultivated across tropical India, Southeast Asia, and the Americas.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 23. Pongamia Pinnata (Indian Beech)
    # -------------------------------------------------------------
    "pongamia_pinnata": {
        "id": "pongamia_pinnata",
        "dataset_class": "Pongamia Pinnata (Indian Beech)",
        "scientific_name": "Millettia pinnata (L.) Panigrahi (syn. Pongamia pinnata)",
        "botanical_family": "Fabaceae (Legume family)",
        "genus": "Millettia",
        "synonyms": ["Pongamia pinnata (L.) Pierre", "Pongamia glabra Vent."],
        "common_names": ["Indian Beech", "Karanja", "Pongam Oil Tree", "Honge Mara", "Karanj"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant (External / Topical)",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants",
            "Toxnet / PubChem Botanical Database"
        ],
        "documented_medicinal_uses": [
            "Premier topical dermatological remedy: Karanja seed oil is clinically proven for eczema, psoriasis, scabies, and leprosy",
            "Potent anthelmintic and wound disinfectant accelerating healing of chronic purulent ulcers",
            "Anti-inflammatory and analgesic in acute rheumatic joint swellings",
            "Traditional twig used as chewing stick for periodontal disease and toothache"
        ],
        "traditionally_used_parts": [
            {"part": "Seed Oil (Karanja Taila)", "indication": "Scabies, psoriasis, eczema, ringworm, chronic wounds, joint inflammation"},
            {"part": "Stem Bark", "indication": "Bleeding piles, acute diarrhea, dermatosis wash"},
            {"part": "Leaves", "indication": "Poultice for rheumatic swellings and worm-infested ulcers"}
        ],
        "preparation_information": [
            {"method": "Karanja Seed Oil (External)", "details": "Cold-pressed bitter seed oil applied topically diluted with coconut oil for scabies and fungal dermatoses."},
            {"method": "Bark Decoction", "details": "10-15 g coarse bark boiled in 400 ml water reduced to 100 ml; used as antiseptic wash."},
            {"method": "Leaf Poultice", "details": "Fresh leaves crushed and heated; applied to painful arthritic joints."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Stem Bark Powder (Churna)", "dose": "1 to 3 g daily"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Karanja Seed Oil (External Application)", "dose": "Apply externally 2 times daily on clean lesions; NOT FOR INTERNAL CONSUMPTION"},
            {"source": "Clinical Toxicology", "preparation": "Seed Oil Internal Warning", "dose": "Crude seed oil internal ingestion is toxic (emetic and purgative); dose is ZERO internally."}
        ],
        "precautions_warnings": [
            "Internal Toxicity of Seed Oil: Karanja oil contains toxic furanoflavonoids (karanjin, pongapin); ingestion induces severe nausea, vomiting, and diarrhea. Strictly restricted to EXTERNAL use.",
            "Pregnancy: Avoid internal administration of bark decoctions during pregnancy."
        ],
        "contraindications_interactions": [
            "Contraindication: Internal consumption of seed oil is strictly contraindicated.",
            "Interactions: None known when applied topically."
        ],
        "active_phytochemicals": ["Karanjin (furanoflavonol)", "Pongapin", "Kanjone", "Pongaglabrone", "Glabrin"],
        "botanical_morphology": "Medium-sized deciduous or semi-evergreen tree 12-18 m; leaves alternate, imparipinnate, 20-30 cm long with 5-9 ovate-elliptic glossy green leaflets; fragrant pinkish-white pea-like flowers; thick woody pods.",
        "native_region": "Native to coastal and riverine tropical Asia, Australia, and Pacific Islands.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 24. Psidium Guajava (Guava)
    # -------------------------------------------------------------
    "psidium_guajava": {
        "id": "psidium_guajava",
        "dataset_class": "Psidium Guajava (Guava)",
        "scientific_name": "Psidium guajava L.",
        "botanical_family": "Myrtaceae (Myrtle family)",
        "genus": "Psidium",
        "synonyms": ["Psidium pyriferum L."],
        "common_names": ["Guava", "Amrud", "Peru", "Koyya", "Pera"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. VI",
            "WHO Traditional Medicine Strategy Compendium",
            "Journal of Ethnopharmacology Monographs"
        ],
        "documented_medicinal_uses": [
            "Potent antidiarrheal: Leaf tannins and quercetin inhibit intestinal motility and neutralize enteropathogens",
            "Antidiabetic: Leaf polyphenol tea inhibits alpha-glucosidase, blunting postprandial glucose spikes",
            "Oral health: Chewing fresh tender leaves heals bleeding gums, relieves toothache, and treats aphthous ulcers",
            "Cardiovascular protector: Reduces blood pressure and improves lipid profiles through high antioxidant flavonoids"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Acute diarrhea, diabetes, toothache, mouth ulcers, wound wash"},
            {"part": "Bark", "indication": "Astringent decoction for dysentery and chronic diarrhea"},
            {"part": "Fruit", "indication": "Nutritious edible fruit exceptionally high in Vitamin C and fiber"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction (Antidiarrheal Protocol)", "details": "10-15 g dried leaves boiled in 300 ml water reduced to 100 ml; taken in divided doses."},
            {"method": "Guava Leaf Tea (Glycemic Management)", "details": "1-2 teaspoons dried crushed leaves steeped in 200 ml boiling water for 10 minutes; consumed with meals."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Leaf Powder", "dose": "2 to 4 g daily in divided doses"},
            {"source": "Clinical Reference Guidelines", "preparation": "Leaf Decoction (Acute Diarrhea)", "dose": "50 to 100 ml 2 to 3 times daily"},
            {"source": "Clinical Trial Standard", "preparation": "Standardized Guava Leaf Tea (Bansoreil)", "dose": "1 cup (150 ml) after each main meal"}
        ],
        "precautions_warnings": [
            "Constipation: Excessive consumption of high-tannin leaf decoctions can induce constipation.",
            "Antidiabetic synergy: May enhance effects of metformin or insulin; monitor blood sugar."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe chronic constipation.",
            "Interactions: Antidiabetic medications (additive glucose reduction)."
        ],
        "active_phytochemicals": ["Quercetin and Quercitrin", "Guaijaverin", "Ellagic acid", "Catechin", "Caryophyllene (in essential oil)"],
        "botanical_morphology": "Small evergreen tree 3-8 m; bark smooth, copper-brown, peeling in thin flakes; leaves opposite, elliptic to oblong, 6-15 cm long, coriaceous, prominent parallel veins beneath; fragrant white 4-petaled flowers.",
        "native_region": "Tropical Americas; cultivated ubiquitously across tropical and subtropical regions.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 25. Punica Granatum (Pomegranate)
    # -------------------------------------------------------------
    "punica_granatum": {
        "id": "punica_granatum",
        "dataset_class": "Punica Granatum (Pomegranate)",
        "scientific_name": "Punica granatum L.",
        "botanical_family": "Lythraceae (Pomegranate family)",
        "genus": "Punica",
        "synonyms": ["Punica florida Salisb."],
        "common_names": ["Pomegranate", "Dadima", "Anaar", "Mathulai", "Dalim"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (WHO, API, EMA)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "WHO Monographs on Selected Medicinal Plants, Vol. 4",
            "European Medicines Agency (EMA) Herbal Compendium"
        ],
        "documented_medicinal_uses": [
            "Potent astringent and antidiarrheal: Fruit rind tannins and punicalagins halt acute diarrhea and amoebic dysentery",
            "Anthelmintic: Root bark pelletierine alkaloid paralyzes intestinal tapeworms and roundworms",
            "Cardiovascular and anti-atherogenic: Aril juice punicalagins inhibit LDL oxidation and lower systolic blood pressure",
            "Oral health and stomatitis: Rind decoction gargle heals bleeding gums, oral candidiasis, and pharyngitis"
        ],
        "traditionally_used_parts": [
            {"part": "Fruit Rind / Pericarp (Dadima Tvaka)", "indication": "Diarrhea, dysentery, bleeding hemorrhoids, oral ulcers, colitis"},
            {"part": "Seeds / Arils", "indication": "Cardiovascular tonic, anemia, thirst, anorexia"},
            {"part": "Leaves", "indication": "Eye wash in conjunctivitis, mild diarrhea"},
            {"part": "Root and Stem Bark", "indication": "Tapeworm expellant (anthelmintic)"}
        ],
        "preparation_information": [
            {"method": "Fruit Rind Decoction", "details": "10-15 g dried coarse rind boiled in 300 ml water reduced to 75 ml."},
            {"method": "Rind Powder (Churna)", "details": "Dried rind pulverized; consumed with buttermilk or honey for diarrhea."},
            {"method": "Fresh Aril Juice", "details": "Freshly extracted seed aril juice taken as a daily cardiovascular tonic."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Fruit Rind Powder", "dose": "2 to 4 g twice daily with buttermilk"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Rind Decoction (Kwatha)", "dose": "25 to 50 ml twice daily"},
            {"source": "Clinical Reference", "preparation": "Fresh Aril Juice", "dose": "100 to 200 ml daily"}
        ],
        "precautions_warnings": [
            "Root Bark Alkaloids: Pelletierine in root bark is toxic in high doses causing dizziness, visual disturbances, and motor paralysis; avoid unprescribed root bark.",
            "Constipation: Prolonged high doses of fruit rind can cause obstinate constipation due to high astringency."
        ],
        "contraindications_interactions": [
            "Contraindication: Chronic severe constipation.",
            "Interactions: Antihypertensives (mild additive ACE inhibition), Statins (minor CYP3A4 interaction in very large juice quantities)."
        ],
        "active_phytochemicals": ["Punicalagin and Punicalin (ellagitannins)", "Ellagic acid", "Pelletierine (alkaloid in root)", "Punicic acid (in seed oil)", "Anthocyanins"],
        "botanical_morphology": "Deciduous spiny shrub or small tree 3-6 m; leaves opposite or subopposite, glossy narrow oblong-lanceolate, 3-8 cm long; scarlet red 5-8 petaled flowers; globose crowned fruit with numerous ruby arils.",
        "native_region": "Native from Iran to Northern India; cultivated throughout Mediterranean and subtropical regions.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 26. Santalum Album (Sandalwood)
    # -------------------------------------------------------------
    "santalum_album": {
        "id": "santalum_album",
        "dataset_class": "Santalum Album (Sandalwood)",
        "scientific_name": "Santalum album L.",
        "botanical_family": "Santalaceae (Sandalwood family)",
        "genus": "Santalum",
        "synonyms": ["Sirium myrtifolium L."],
        "common_names": ["Sandalwood", "Chandana", "Shrikhanda", "Safed Chandan", "White Sandalwood"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Tree",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO, API, EMA)",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 4",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "German Commission E Monographs on Sandalwood Oil"
        ],
        "documented_medicinal_uses": [
            "Urinary antiseptic: Santalol inhibits uropathogens in acute uncomplicated cystitis and burning urethritis",
            "Cooling antipyretic: Paste applied to forehead relieves hyperpyrexia, sunstroke, and severe headache",
            "Dermatological antiseptic: Clears acne, prickly heat, erythema, and cutaneous hyperpigmentation",
            "Neuro-calming anxiolytic: Inhalation of alpha-santalol crosses blood-brain barrier exerting mild central sedation"
        ],
        "traditionally_used_parts": [
            {"part": "Heartwood", "indication": "Cystitis, burning sensation, fever, headache, acne, cardiac debility"},
            {"part": "Essential Oil (Chandana Taila)", "indication": "Urinary tract infections, aromatherapy, cosmetic formulations"}
        ],
        "preparation_information": [
            {"method": "Topical Sandalwood Paste", "details": "Heartwood rubbed with rose water on a stone slab to yield fine aromatic paste; applied on skin."},
            {"method": "Heartwood Powder", "details": "Pulverized heartwood taken with milk or honey for dysuria and burning micturition."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Heartwood Powder (Churna)", "dose": "1 to 3 g daily in divided doses with cold water or milk"},
            {"source": "German Commission E", "preparation": "Sandalwood Essential Oil", "dose": "1.0 to 1.5 g (approx 0.2 to 0.4 ml) daily for max 6 weeks for urinary tract infections"},
            {"source": "Topical Standard", "preparation": "Fresh Heartwood Paste", "dose": "Apply liberally to affected skin or forehead as needed"}
        ],
        "precautions_warnings": [
            "Renal Disease: Sandalwood oil should not be taken internally for more than 6 continuous weeks to avoid potential renal parenchymal irritation.",
            "Endangered Species Warning: Santalum album is vulnerable due to overexploitation; purchase only from certified sustainable/licensed sources."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe kidney disease (parenchymal renal inflammation).",
            "Interactions: None well-documented with oral pharmaceuticals."
        ],
        "active_phytochemicals": ["Alpha-santalol (up to 55%)", "Beta-santalol (up to 25%)", "Santene", "Santalic acid", "Triterpenes"],
        "botanical_morphology": "Small to medium hemi-parasitic evergreen tree 4-10 m; roots attach to host roots via haustoria; leaves opposite, elliptic to ovate-lanceolate, 4-8 cm long, thin, glabrous and shining green; heartwood intensely fragrant.",
        "native_region": "Indigenous to Southern India (Karnataka, Tamil Nadu) and Indonesia.",
        "iucn_conservation_status": "Vulnerable (Regulated and protected by Government statutes)"
    },

    # -------------------------------------------------------------
    # 27. Syzygium Cumini (Jamun)
    # -------------------------------------------------------------
    "syzygium_cumini": {
        "id": "syzygium_cumini",
        "dataset_class": "Syzygium Cumini (Jamun)",
        "scientific_name": "Syzygium cumini (L.) Skeels",
        "botanical_family": "Myrtaceae (Myrtle family)",
        "genus": "Syzygium",
        "synonyms": ["Eugenia jambolana Lam.", "Myrtus cumini L."],
        "common_names": ["Jamun", "Jambu", "Black Plum", "Java Plum", "Naval"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial & Clinical (API & ICMR)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 13",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Premier antidiabetic agent: Seed jamboline alkaloid arrests diastatic conversion of starch into sugar and improves insulin release",
            "Antidiarrheal and astringent: Stem bark and leaf decoction halts chronic diarrhea and dysentery",
            "Oral health: Bark decoction gargle tightens spongy bleeding gums and treats stomatitis",
            "Hepatoprotective and antioxidant activity via high anthocyanin and polyphenolic content"
        ],
        "traditionally_used_parts": [
            {"part": "Seeds (Jambu Beeja)", "indication": "Type 2 diabetes, glycosuria, polyuria, metabolic syndrome"},
            {"part": "Stem Bark (Tvaka)", "indication": "Diarrhea, dysentery, bleeding piles, oral ulcers"},
            {"part": "Leaves", "indication": "Diabetes tea, gingivitis wash, cutaneous ulcers"},
            {"part": "Fruit", "indication": "Digestive astringent, splenic enlargement, diabetes"}
        ],
        "preparation_information": [
            {"method": "Seed Powder (Churna)", "details": "Dried seeds pulverized into fine powder; taken with water or buttermilk before meals."},
            {"method": "Stem Bark Decoction", "details": "15-20 g coarse bark boiled in 400 ml water reduced to 100 ml."},
            {"method": "Leaf Infusion", "details": "10-15 tender leaves steeped in 200 ml hot water as diabetic tea."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Dried Seed Powder (Churna)", "dose": "1 to 3 g, 2 to 3 times daily before meals"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Stem Bark Decoction (Kwatha)", "dose": "50 to 100 ml twice daily"},
            {"source": "ICMR Guidelines", "preparation": "Aqueous Seed Extract", "dose": "500 to 1000 mg twice daily"}
        ],
        "precautions_warnings": [
            "Hypoglycemia: Potent blood sugar lowering effect; monitor blood sugar carefully if taken alongside prescription antidiabetics.",
            "Excessive unripe fruit or seed powder on an empty stomach may cause throat dryness and acidity."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe hypoglycemia, advanced constipation.",
            "Interactions: Synergistic interaction with Metformin, Glimepiride, and Insulin (risk of hypoglycemic episodes)."
        ],
        "active_phytochemicals": ["Jamboline and Jambosine", "Ellagic acid", "Anthocyanins (Delphinidin-3-glucoside)", "Gallic acid", "Beta-sitosterol"],
        "botanical_morphology": "Large fast-growing evergreen tree 15-30 m; bark rough, greyish-brown; leaves opposite, coriaceous, elliptic to oblong-ovate, 8-15 cm long, smooth and shiny green with close parallel lateral veins; purplish-black oblong berries.",
        "native_region": "Native to Indian subcontinent and Southeast Asia; naturalized in many tropical regions.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 28. Syzygium Jambos (Rose Apple)
    # -------------------------------------------------------------
    "syzygium_jambos": {
        "id": "syzygium_jambos",
        "dataset_class": "Syzygium Jambos (Rose Apple)",
        "scientific_name": "Syzygium jambos (L.) Alston",
        "botanical_family": "Myrtaceae (Myrtle family)",
        "genus": "Syzygium",
        "synonyms": ["Eugenia jambos L."],
        "common_names": ["Rose Apple", "Malabar Plum", "Gulab Jamun", "Jambu", "Pannerale"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Traditional & Folk Medicinal Tree",
        "status_badge_color": "emerald",
        "evidence_category": "Traditional Ethnomedicinal (API)",
        "authoritative_sources": [
            "Indian Council of Medical Research (ICMR) Compendium",
            "CRC Handbook of Medicinal Herbs",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Antidiabetic: Seed and leaf extracts exhibit alpha-glucosidase inhibitory activity",
            "Antimicrobial: Leaf extracts inhibit Gram-positive bacteria and dermatophytic fungi",
            "Astringent: Bark and leaf decoction traditionally used for diarrhea, dysentery, and sore throat",
            "Edible fragrant rose-flavored fruit with mild digestive and diuretic action"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves", "indication": "Diabetes, fever, sore throat gargle, wound wash"},
            {"part": "Seeds", "indication": "Diarrhea, dysentery, diabetes (Caution: seeds contain trace hydrocyanic acid)"},
            {"part": "Bark", "indication": "Astringent gargle, leucorrhoea, menorrhagia"}
        ],
        "preparation_information": [
            {"method": "Leaf Decoction", "details": "10 g dried leaves boiled in 300 ml water reduced to 75 ml."},
            {"method": "Bark Gargle", "details": "15 g bark boiled in water as astringent gargle for sore throat."}
        ],
        "dosage_information": [
            {"source": "Ethnomedicinal Reference", "preparation": "Stem Bark Decoction", "dose": "25 to 50 ml twice daily"},
            {"source": "Traditional Practice", "preparation": "Leaf Infusion", "dose": "50 to 100 ml daily"},
            {"source": "Pharmacopoeial Status", "preparation": "Standard Clinical Posology", "dose": "Dosage information not verified for pharmaceutical extracts."}
        ],
        "precautions_warnings": [
            "Seed Caution: Seeds contain trace amounts of cyanogenic glycosides producing hydrocyanic acid; seeds should not be consumed in excessive raw quantities.",
            "Roots and seeds should be used with caution."
        ],
        "contraindications_interactions": [
            "Contraindication: Excessive ingestion of raw seeds.",
            "Interactions: Monitor if taken with antidiabetic medications."
        ],
        "active_phytochemicals": ["Myricetin", "Quercetin", "Friedelin", "Betulinic acid", "Tannins", "Essential oil (rich in pinene, limonene)"],
        "botanical_morphology": "Evergreen tree 6-12 m with dense wide crown; leaves opposite, narrow lanceolate, 10-20 cm long, leathery and dark green; large creamy-white flowers with numerous long stamens; bell-shaped yellowish fruit smelling of rose water.",
        "native_region": "Native to Southeast Asia; widely cultivated across tropical India and the Americas.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 29. Tabernaemontana Divaricata (Crape Jasmine)
    # -------------------------------------------------------------
    "tabernaemontana_divaricata": {
        "id": "tabernaemontana_divaricata",
        "dataset_class": "Tabernaemontana Divaricata (Crape Jasmine)",
        "scientific_name": "Tabernaemontana divaricata (L.) R.Br. ex Roem. & Schult.",
        "botanical_family": "Apocynaceae (Dogbane family)",
        "genus": "Tabernaemontana",
        "synonyms": ["Ervatamia coronaria (Jacq.) Stapf", "Nerium divaricatum L."],
        "common_names": ["Crape Jasmine", "Pinwheel Flower", "Nandivardhanam", "Tagar", "East Indian Rosebay"],
        "is_medicinal": True,
        "medicinal_status": "Traditional Medicinal Plant with Toxic Potential",
        "status_badge_color": "amber",
        "evidence_category": "Traditional & Phytochemical Screening (API)",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. IV (under Tagara substitutes)",
            "ICMR Indian Medicinal Plants Compendium",
            "Journal of Ethnopharmacology"
        ],
        "documented_medicinal_uses": [
            "Ophthalmic folk remedy: Milky sap mixed with oil traditionally instilled for eye irritation and corneal opacity (Caution: unsterile eye use can cause infection)",
            "Analgesic and anti-inflammatory: Root paste chewed for toothache and applied to arthritic swellings",
            "Antimicrobial and wound healing action of leaf extracts",
            "Cholinesterase inhibition: Indole alkaloids researched for potential neurodegenerative therapy"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves and Latex", "indication": "External wound dressing, ophthalmia (folk use, caution required)"},
            {"part": "Roots", "indication": "Toothache, skin diseases, vermifuge, anthelmintic"}
        ],
        "preparation_information": [
            {"method": "Root Paste (External)", "details": "Root rubbed with water applied topically to aching tooth or inflamed joint."},
            {"method": "Leaf Decoction (External Wash)", "details": "Leaves boiled in water used as antiseptic wash for wounds."}
        ],
        "dosage_information": [
            {"source": "Pharmacopoeial Verification", "preparation": "Internal Dosage", "dose": "Dosage information not verified for safe internal administration."},
            {"source": "Traditional Practice (External Only)", "preparation": "Root Paste", "dose": "Apply small topical dab on aching tooth; do not swallow in quantity."}
        ],
        "precautions_warnings": [
            "Apocynaceae Toxicity Risk: Contains numerous indole alkaloids (coronaridine, voacangine, tabernaemontanine); ingestion of large amounts causes CNS depression, bradycardia, and hypotensive shock.",
            "Ophthalmic Warning: Never instil crude milky plant latex directly into eyes without sterile pharmaceutical processing.",
            "Pregnancy & Lactation: Strictly contraindicated internally."
        ],
        "contraindications_interactions": [
            "Contraindication: Internal oral consumption without medical supervision; pregnancy; bradycardia.",
            "Interactions: Potential synergism with central depressants and cardiac medications."
        ],
        "active_phytochemicals": ["Coronaridine", "Voacangine", "Tabernaemontanine", "Dregamine", "Ibogaine-type indole alkaloids"],
        "botanical_morphology": "Evergreen glabrous shrub 1.5-3 m with milky latex; leaves opposite, glossy elliptic-oblong, 8-15 cm long, acuminate tip; fragrant pure white pinwheel-shaped 5-petaled flowers (single or double forms).",
        "native_region": "Native to South and Southeast Asia (India, Myanmar, Thailand).",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # 30. Trigonella Foenum-graecum (Fenugreek)
    # -------------------------------------------------------------
    "trigonella_foenum_graecum": {
        "id": "trigonella_foenum_graecum",
        "dataset_class": "Trigonella Foenum-graecum (Fenugreek)",
        "scientific_name": "Trigonella foenum-graecum L.",
        "botanical_family": "Fabaceae (Legume family)",
        "genus": "Trigonella",
        "synonyms": ["Trigonella tibetana (Alef.) Vassilcz."],
        "common_names": ["Fenugreek", "Methi", "Methika", "Greek Hay", "Vendhayam"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO, API, EMA)",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 3",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "European Medicines Agency (EMA) Community Herbal Monograph"
        ],
        "documented_medicinal_uses": [
            "Potent hypoglycemic and insulin-sensitizing: 4-hydroxyisoleucine and galactomannan slow glucose absorption and stimulate pancreatic secretion",
            "Hypolipidemic: Saponins bind bile salts, significantly lowering LDL and triglycerides",
            "Galactagogue: Clinically established to enhance breast milk production in nursing mothers",
            "Gastrointestinal soothing: High mucilage content treats acid reflux, gastritis, and constipation",
            "Nutritional restorative: Leaves are an iron- and folate-rich dietary vegetable"
        ],
        "traditionally_used_parts": [
            {"part": "Seeds (Methika Beeja)", "indication": "Diabetes, hyperlipidemia, lactation deficiency, dyspepsia, joint pain"},
            {"part": "Leaves (Methi Saag)", "indication": "Nutritious vegetable, anemia, digestive cooling, poultice for boils"}
        ],
        "preparation_information": [
            {"method": "Seed Powder (Churna)", "details": "Dry seeds lightly roasted, pulverized; consumed with warm water or buttermilk before meals."},
            {"method": "Overnight Soaked Seeds", "details": "1-2 teaspoons whole seeds soaked in water overnight; water drunk and seeds chewed in morning."},
            {"method": "Cooked Green Leaves", "details": "Fresh leaves cooked as vegetable or incorporated into flatbreads (Thepla/Paratha)."}
        ],
        "dosage_information": [
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Seed Powder (Churna)", "dose": "3 to 6 g daily in divided doses"},
            {"source": "WHO Monographs on Selected Medicinal Plants (Vol. 3)", "preparation": "Defatted Powdered Seeds", "dose": "5 to 10 g daily in divided doses for diabetes and hypercholesterolemia"},
            {"source": "European Medicines Agency (EMA)", "preparation": "Seed Decoction / Infusion", "dose": "1.0 to 6.0 g powdered drug in 250 ml water, up to 3 times daily"}
        ],
        "precautions_warnings": [
            "Pregnancy: Oxytocic uterine stimulant properties documented in high medicinal seed doses; avoid high medicinal doses during pregnancy (culinary levels are safe).",
            "Hypoglycemia: Patients on sulfonylureas or insulin should monitor glucose levels closely.",
            "Urine Odor: High consumption imparts a characteristic harmless maple syrup odor to urine and perspiration."
        ],
        "contraindications_interactions": [
            "Contraindication: Pregnancy (for high-dose therapeutic seed extracts); Peanut/Chickpea allergy (cross-reactivity with Fabaceae).",
            "Interactions: Antidiabetic medications (additive hypoglycemia); Anticoagulants (trace coumarin content may mildly enhance bleeding risk)."
        ],
        "active_phytochemicals": ["4-Hydroxyisoleucine (amino acid stimulant of insulin)", "Diosgenin and Yamogenin (steroidal sapogenins)", "Galactomannan (mucilaginous fiber)", "Trigonelline (alkaloid)"],
        "botanical_morphology": "Erect aromatic annual herb 30-60 cm; leaves trifoliolate with 3 obovate-cuneate leaflets, 2-3 cm long, faintly toothed; small yellowish-white solitary pea-like flowers in leaf axils; slender beaked pods containing 10-20 angular yellowish-brown seeds.",
        "native_region": "Mediterranean region, Western Asia, and Indian subcontinent; cultivated extensively globally.",
        "iucn_conservation_status": "Least Concern"
    },

    # -------------------------------------------------------------
    # ADDITIONAL REFERENCE MONOGRAPHS (Previous & Negative Controls)
    # -------------------------------------------------------------
    "aloe_barbadensis": {
        "id": "aloe_barbadensis",
        "dataset_class": "Aloe Barbadensis (Aloe Vera)",
        "scientific_name": "Aloe barbadensis Miller (syn. Aloe vera (L.) Burm. f.)",
        "botanical_family": "Asphodelaceae",
        "genus": "Aloe",
        "synonyms": ["Aloe vera (L.) Burm. f."],
        "common_names": ["Aloe Vera", "Ghritkumari", "Kanya", "Indian Alces"],
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "evidence_category": "Pharmacopoeial Standard (WHO & API)",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 1",
            "European Medicines Agency (EMA) Monograph on Aloe",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I"
        ],
        "documented_medicinal_uses": [
            "Wound healing accelerator for burns, erythema, and cuts",
            "Dermal hydration, cosmetic soothing, and barrier repair",
            "Gastrointestinal soothing in mild gastritis and acid reflux (inner gel)",
            "Stimulant laxative (specifically the yellow aloin-rich latex)"
        ],
        "traditionally_used_parts": [
            {"part": "Inner Leaf Gel (Pulp)", "indication": "Burns, cosmetic hydration, gastritis, digestive tonic"},
            {"part": "Leaf Latex (Bitters)", "indication": "Short-term treatment of occasional constipation"}
        ],
        "preparation_information": [
            {"method": "Pure Inner Fillet Gel", "details": "Fresh mature leaf pared to remove green rind; parenchymatous gel scooped and blended, devoid of yellow aloin-rich latex."},
            {"method": "Standardized Dry Latex Extract", "details": "Concentrated yellow exudate standardized for aloin content."}
        ],
        "dosage_information": [
            {"source": "WHO Monographs on Selected Medicinal Plants (Vol. 1)", "preparation": "Topical Hydrogel", "dose": "Apply fresh gel or 10-70% formulation liberally 2 to 3 times daily"},
            {"source": "Ayurvedic Pharmacopoeia of India (API)", "preparation": "Fresh Leaf Pulp", "dose": "10 to 20 g daily"},
            {"source": "European Medicines Agency (EMA)", "preparation": "Standardized Anthraquinone Latex", "dose": "10 to 30 mg hydroxyanthracene derivatives once daily at bedtime (maximum 1 week)"}
        ],
        "precautions_warnings": [
            "Gel vs Latex Distinction: The clear inner gel is safe for general use. The yellow latex (aloin) is a potent anthraquinone stimulant laxative and must not be taken indiscriminately.",
            "Pregnancy: Oral latex is contraindicated during pregnancy due to reflex stimulation of uterine contractions.",
            "Chronic latex use causes hypokalemia and melanosis coli."
        ],
        "contraindications_interactions": [
            "Contraindication: Intestinal obstruction, Crohn's disease, ulcerative colitis, pregnancy.",
            "Interactions: Cardiac glycosides (Digoxin) - hypokalemia increases toxicity."
        ],
        "active_phytochemicals": ["Acemannan", "Aloin A and B (barbaloin)", "Aloe-emodin", "Bradykinase"],
        "botanical_morphology": "Succulent rosette herb; leaves thick, fleshy, lanceolate, 40-50 cm long, spiny margins containing gelatinous central parenchyma.",
        "native_region": "Arid regions of Arabian Peninsula; cultivated pantropically.",
        "iucn_conservation_status": "Least Concern"
    },

    "dieffenbachia_seguine": {
        "id": "dieffenbachia_seguine",
        "dataset_class": "Dieffenbachia Seguine (Dumb Cane)",
        "scientific_name": "Dieffenbachia seguine (Jacq.) Schott",
        "botanical_family": "Araceae (Arum family)",
        "genus": "Dieffenbachia",
        "synonyms": ["Dieffenbachia picta Schott"],
        "common_names": ["Dumb Cane", "Tropic Snow", "Leopard Lily"],
        "is_medicinal": False,
        "medicinal_status": "Toxic / Hazardous Ornamental Plant (Non-Medicinal)",
        "status_badge_color": "rose",
        "evidence_category": "Clinical Toxicology Warning (AAPCC)",
        "authoritative_sources": [
            "American Association of Poison Control Centers (AAPCC) Toxic Plant Guidelines",
            "Clinical Toxicology of Commercial Products",
            "NIOSH Pocket Guide to Chemical Hazards"
        ],
        "documented_medicinal_uses": [
            "NO RECOGNIZED THERAPEUTIC MEDICINAL USES in modern pharmacopoeias.",
            "Common indoor decorative houseplant valued solely for variegated foliage, not medicine."
        ],
        "traditionally_used_parts": [
            {"part": "None", "indication": "All plant parts contain toxic calcium oxalate raphides and proteolytic enzymes. INGESTION IS DANGEROUS."}
        ],
        "preparation_information": [
            {"method": "NOT APPLICABLE", "details": "Plant is toxic. Ingestion or handling sap can cause severe mucosal burns. No medicinal preparation is recognized."}
        ],
        "dosage_information": [
            {"source": "Poison Control Medical Reference", "preparation": "Toxic Exposure Threshold", "dose": "DOSE IS ZERO (CONTRAINDICATED). Ingestion causes immediate intense burning and laryngeal edema."}
        ],
        "precautions_warnings": [
            "SEVERE TOXICITY WARNING: Plant contains needle-sharp insoluble calcium oxalate crystals (raphides) bundled with proteolytic enzymes (dumbcaine).",
            "When chewed, raphides are forcefully ejected into buccal mucosa, causing severe pain, salivation, tongue swelling, and transient loss of speech.",
            "Laryngeal Edema Risk: Severe swelling may obstruct the airway, leading to asphyxiation."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: ALL INTERNAL CONSUMPTION IS STRICTLY PROHIBITED.",
            "Handling Precautions: Wear protective gloves when pruning; keep away from children and pets."
        ],
        "active_phytochemicals": ["Insoluble Calcium oxalate raphides", "Dumbcaine (proteolytic enzyme)", "Cyanogenic glycosides (trace)"],
        "botanical_morphology": "Robust perennial herb 1-2 m tall with fleshy cane-like stem; leaves alternate, large, oblong-elliptic, 25-50 cm long, deep green variegated with creamy white or yellow irregular blotches.",
        "native_region": "Tropical Americas and West Indies; grown worldwide as potted ornamental.",
        "iucn_conservation_status": "Least Concern (Toxic Ornamental)"
    },

    "monstera_deliciosa": {
        "id": "monstera_deliciosa",
        "dataset_class": "Monstera Deliciosa (Swiss Cheese Plant)",
        "scientific_name": "Monstera deliciosa Liebm.",
        "botanical_family": "Araceae",
        "genus": "Monstera",
        "synonyms": ["Philodendron pertusum"],
        "common_names": ["Swiss Cheese Plant", "Split-Leaf Philodendron", "Ceriman"],
        "is_medicinal": False,
        "medicinal_status": "Ornamental Foliage Plant (Non-Medicinal)",
        "status_badge_color": "slate",
        "evidence_category": "Botanical Toxicology Reference",
        "authoritative_sources": [
            "Royal Botanic Gardens Kew - Plants of the World Online (POWO)",
            "UC Davis Toxic Plant Database"
        ],
        "documented_medicinal_uses": [
            "NO FORMAL PHARMACOPOEIAL MEDICINAL USES.",
            "Popular indoor ornamental valued for dramatic fenestrated foliage and air purification."
        ],
        "traditionally_used_parts": [
            {"part": "Ripe Fruit Only", "indication": "Fully ripe fruit is edible (all other parts are toxic)."}
        ],
        "preparation_information": [
            {"method": "Ornamental Only", "details": "Leaves and stems must NEVER be consumed."}
        ],
        "dosage_information": [
            {"source": "Botanical Reference", "preparation": "Leaf Ingestion", "dose": "No verified dosage found in the available sources; NOT A MEDICINE."}
        ],
        "precautions_warnings": [
            "Contains calcium oxalate crystals throughout foliage causing severe oral irritation if chewed.",
            "Keep away from domestic cats and dogs."
        ],
        "contraindications_interactions": [
            "Contraindication: Ingestion of foliage is contraindicated."
        ],
        "active_phytochemicals": ["Calcium oxalate raphides", "Amylases"],
        "botanical_morphology": "Epiphytic climbing liana with stout aerial roots; leaves huge, cordate, 25-90 cm long, pinnatifid with deep lateral lobes and perforated with elliptical holes.",
        "native_region": "Tropical rainforests of Southern Mexico and Central America.",
        "iucn_conservation_status": "Least Concern"
    }
}

# -------------------------------------------------------------
# LOOKUP & CANONICAL RESOLUTION FUNCTIONS
# -------------------------------------------------------------

# Precompute lookup index by folder_name, common name, scientific name, and synonyms
_LOOKUP_MAP: Dict[str, str] = {}
for p_id, p_data in PLANT_DATABASE.items():
    _LOOKUP_MAP[p_id.lower()] = p_id
    _LOOKUP_MAP[p_id.lower().replace("_", " ")] = p_id

    if "dataset_class" in p_data:
        dc = p_data["dataset_class"].lower()
        _LOOKUP_MAP[dc] = p_id
        _LOOKUP_MAP[dc.replace("_", " ")] = p_id

    sc = p_data.get("scientific_name", "").lower()
    _LOOKUP_MAP[sc] = p_id
    _LOOKUP_MAP[sc.replace(" ", "_")] = p_id

    for syn in p_data.get("synonyms", []):
        s_low = syn.lower()
        _LOOKUP_MAP[s_low] = p_id
        _LOOKUP_MAP[s_low.replace(" ", "_")] = p_id
        # Also index first two words (e.g. 'ocimum sanctum')
        tokens = s_low.split()
        if len(tokens) >= 2:
            bi_name = f"{tokens[0]} {tokens[1]}"
            _LOOKUP_MAP[bi_name] = p_id
            _LOOKUP_MAP[bi_name.replace(" ", "_")] = p_id

    # Also index first two words of scientific name (binomial)
    sc_tokens = sc.split()
    if len(sc_tokens) >= 2:
        bi_sc = f"{sc_tokens[0]} {sc_tokens[1]}"
        _LOOKUP_MAP[bi_sc] = p_id
        _LOOKUP_MAP[bi_sc.replace(" ", "_")] = p_id

    for cn in p_data.get("common_names", []):
        c_low = cn.lower()
        _LOOKUP_MAP[c_low] = p_id
        _LOOKUP_MAP[c_low.replace(" ", "_")] = p_id

def get_plant_by_id(plant_id_or_name: str) -> Optional[Dict[str, Any]]:
    """Retrieve full monograph for a given species ID, dataset class name, synonym, or common name."""
    if not plant_id_or_name:
        return None
    key = str(plant_id_or_name).lower().strip()
    
    # Direct match
    resolved_id = _LOOKUP_MAP.get(key)
    if resolved_id and resolved_id in PLANT_DATABASE:
        return PLANT_DATABASE[resolved_id]

    # Space vs Underscore variants
    key_space = key.replace("_", " ").replace("-", " ")
    resolved_id = _LOOKUP_MAP.get(key_space)
    if resolved_id and resolved_id in PLANT_DATABASE:
        return PLANT_DATABASE[resolved_id]

    key_under = key.replace(" ", "_").replace("-", "_")
    resolved_id = _LOOKUP_MAP.get(key_under)
    if resolved_id and resolved_id in PLANT_DATABASE:
        return PLANT_DATABASE[resolved_id]
    
    # Substring search fallback with normalization
    clean_k = key_space.replace("(", "").replace(")", "")
    for k, v in _LOOKUP_MAP.items():
        k_clean = k.replace("_", " ").replace("(", "").replace(")", "")
        if clean_k in k_clean or k_clean in clean_k:
            return PLANT_DATABASE[v]
    return None

def get_all_species() -> List[Dict[str, Any]]:
    """Return a list of all plant monographs in the database."""
    return list(PLANT_DATABASE.values())

def search_plants(query: str) -> List[Dict[str, Any]]:
    """Search database by common name, scientific name, indication, or family."""
    query = query.lower().strip()
    if not query:
        return get_all_species()
    results = []
    for plant in PLANT_DATABASE.values():
        match = False
        if query in plant["scientific_name"].lower():
            match = True
        elif any(query in name.lower() for name in plant["common_names"]):
            match = True
        elif query in plant["botanical_family"].lower():
            match = True
        elif any(query in use.lower() for use in plant["documented_medicinal_uses"]):
            match = True
        elif any(query in part["indication"].lower() for part in plant["traditionally_used_parts"]):
            match = True
        elif any(query in chem.lower() for chem in plant["active_phytochemicals"]):
            match = True
        if match:
            results.append(plant)
    return results

def get_species_classes() -> List[str]:
    """Get list of registered species IDs."""
    return list(PLANT_DATABASE.keys())
