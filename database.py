"""
Authoritative Botanical and Pharmacological Knowledge Base
==========================================================
Provides structured, evidence-based monographs for recognized medicinal plants
and control non-medicinal/toxic species.

Data synthesized from:
- World Health Organization (WHO) Monographs on Selected Medicinal Plants (Volumes 1-4)
- Ayurvedic Pharmacopoeia of India (API), Ministry of AYUSH, Govt. of India
- Indian Council of Medical Research (ICMR) Medicinal Plants Monographs
- European Medicines Agency (EMA) Committee on Herbal Medicinal Products (HMPC)
- German Commission E Monographs & USDA Phytochemical Databases
"""

from typing import Dict, List, Optional, Any

PLANT_DATABASE: Dict[str, Dict[str, Any]] = {
    "ocimum_sanctum": {
        "id": "ocimum_sanctum",
        "scientific_name": "Ocimum sanctum L. (syn. Ocimum tenuiflorum)",
        "common_names": ["Tulsi", "Holy Basil", "Sacred Basil", "Kaphari"],
        "botanical_family": "Lamiaceae (Mint family)",
        "genus": "Ocimum",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 2 (2002)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 18"
        ],
        "documented_medicinal_uses": [
            "Adaptogenic and stress-modulating activity (reduces cortisol and oxidative markers)",
            "Upper respiratory tract infection relief (antimicrobial, bronchodilator, mucolytic)",
            "Antipyretic and immunomodulatory activity in viral fevers and bronchitis",
            "Mild hypoglycemic effect: reduces fasting and postprandial blood glucose",
            "Cardioprotective and antihyperlipidemic through lipid peroxidation inhibition",
            "Topical antibacterial activity against skin pathogens and oral plaque"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Folia)", "indication": "Cough, cold, bronchitis, asthma, digestive spasms, cutaneous infections"},
            {"part": "Whole Plant (Panchanga)", "indication": "Fever, metabolic disorders, generalized debility, immune support"},
            {"part": "Seeds (Semina)", "indication": "Genitourinary tract irritation, demulcent in cystitis"},
            {"part": "Root (Radix)", "indication": "Malarial fever decoctions, diaphoretic preparations"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Swarasa)", "details": "Fresh leaves crushed and pressed; consumed alone or with raw honey."},
            {"method": "Leaf Infusion / Herbal Tea (Phanta)", "details": "2-4 g dried leaves steeped in 150 ml boiling water for 10-15 minutes in a covered vessel."},
            {"method": "Decoction (Kashayam)", "details": "Coarse powder or fresh leaves boiled down to 1/4th volume with black pepper and ginger for respiratory distress."},
            {"method": "Poultice / Paste (Kalka)", "details": "Fresh leaves ground with minimal sterile water applied topically for fungal dermatoses and ringworm."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Leaf Juice (Swarasa)",
                "dose": "10 to 20 ml twice daily"
            },
            {
                "source": "WHO Monograph on Selected Medicinal Plants (Vol. 2)",
                "preparation": "Dried leaf powder / Infusion",
                "dose": "1.0 - 2.5 g dried leaves in 150 ml water, 2 to 3 times daily"
            },
            {
                "source": "ICMR Clinical Reference Guidelines",
                "preparation": "Standardized Aqueous/Ethanolic Extract",
                "dose": "300 - 600 mg daily in divided doses"
            }
        ],
        "precautions_warnings": [
            "Pregnancy: Tulsi exhibits potential mild anti-implantation and antifertility effects in animal models; excessive therapeutic dosages are avoided during the first trimester.",
            "Lactation: Safety data during breastfeeding has not been established; use culinary amounts only.",
            "Hypoglycemia: Patients on oral hypoglycemic agents or insulin must monitor blood sugar closely to avoid synergistic hypoglycemia.",
            "Bleeding Disorders: Eugenol content may slightly inhibit platelet aggregation; discontinue 2 weeks prior to scheduled surgery."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Known hypersensitivity to Lamiaceae family plants.",
            "Drug Interactions: Anticoagulants/Antiplatelets (Warfarin, Heparin, Clopidogrel) - potential increased risk of bruising; Oral Antidiabetic agents (Metformin, Glimepiride) - monitor glucose levels."
        ],
        "active_phytochemicals": [
            "Eugenol (up to 70% in volatile oil)",
            "Ursolic acid and Oleanolic acid (triterpenoids)",
            "Rosmarinic acid",
            "Caryophyllene",
            "Linalool",
            "Apigenin and Luteolin (flavonoids)"
        ],
        "botanical_morphology": "Erect aromatic subshrub 30-60 cm; leaves opposite, ovate or elliptic-oblong, 2.5-5 cm long, margin faintly dentate to serrate, pubescent on both surfaces with conspicuous glandular dots.",
        "native_region": "Indian Subcontinent and widespread across tropical Southeastern Asia.",
        "iucn_conservation_status": "Least Concern (Cultivated widely)"
    },

    "azadirachta_indica": {
        "id": "azadirachta_indica",
        "scientific_name": "Azadirachta indica A. Juss. (syn. Melia azadirachta)",
        "common_names": ["Neem", "Indian Lilac", "Margosa Tree", "Nimba"],
        "botanical_family": "Meliaceae (Mahogany family)",
        "genus": "Azadirachta",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "WHO Traditional Medicine Strategy & ICMR Monographs",
            "United States Pharmacopeia - Herbal Compendium (USP-HC)"
        ],
        "documented_medicinal_uses": [
            "Broad-spectrum antimicrobial and antifungal (inhibits Candida, Trichophyton, Epidermophyton)",
            "Dermatological therapeutics: Eczema, psoriasis, acne vulgaris, pruritus, chronic wounds",
            "Potent anti-inflammatory and hepatoprotective actions mediated through antioxidant pathways",
            "Anti-hyperglycemic properties: stimulates insulin secretion and peripheral glucose utilization",
            "Gingivitis and oral plaque reduction (in herbal toothpaste and mouthwash)",
            "Antiparasitic action against scabies, pediculosis (lice), and intestinal helminths"
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
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Leaf Powder (Churna)",
                "dose": "1 to 3 g daily in divided doses"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Leaf Juice (Swarasa)",
                "dose": "5 to 10 ml once daily"
            },
            {
                "source": "ICMR Guidelines on Phytomedicines",
                "preparation": "Stem Bark Decoction",
                "dose": "20 to 50 ml twice daily after meals"
            }
        ],
        "precautions_warnings": [
            "Toxic in Infants and Young Children: Neem seed oil can cause toxic encephalopathy, Reye-like syndrome, and metabolic acidosis in infants. Internal administration to infants is strictly contraindicated.",
            "Fertility: Has documented spermicidal and anti-ovulatory properties; avoid if attempting conception.",
            "Renal and Hepatic Monitoring: High internal doses over prolonged periods may cause nephrotoxicity or hepatotoxicity; restrict continuous intake to 2-3 weeks.",
            "Pregnancy: Leaf and bark decoctions are contraindicated during pregnancy due to potential abortifacient actions."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy, lactation, infant oral ingestion, auto-immune diseases (may over-stimulate immune system).",
            "Drug Interactions: Antidiabetic medications (potential profound hypoglycemia), Immunosuppressants (cyclosporine, tacrolimus) - may counteract therapeutic immunosuppression."
        ],
        "active_phytochemicals": [
            "Azadirachtin (limonoid / tetranortriterpenoid)",
            "Nimbin, Nimbidin, and Nimbolide",
            "Salannin and Gedunin",
            "Quercetin and beta-sitosterol"
        ],
        "botanical_morphology": "Large evergreen tree (15-20 m tall); leaves alternate, pinnate, 20-40 cm long, with 20-30 medium to dark green leaflets; leaflet blades strongly asymmetric, lanceolate to ovate-lanceolate, serrated margins.",
        "native_region": "Native to Indian subcontinent and Myanmar; naturalized throughout tropical and subtropical dry areas worldwide.",
        "iucn_conservation_status": "Least Concern"
    },

    "aloe_barbadensis": {
        "id": "aloe_barbadensis",
        "scientific_name": "Aloe barbadensis Miller (syn. Aloe vera (L.) Burm. f.)",
        "common_names": ["Aloe Vera", "Ghritkumari", "Kanya", "Indian Alces"],
        "botanical_family": "Asphodelaceae (Aloaceae)",
        "genus": "Aloe",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 1 (1999)",
            "European Medicines Agency (EMA) Monograph on Aloe Barbadensis",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "US Pharmacopeia (USP)"
        ],
        "documented_medicinal_uses": [
            "Topical wound healing accelerator (burns, radiation-induced dermatitis, surgical incisions)",
            "Deep dermal hydration and barrier repair in erythema, sunburn, and xerosis",
            "Anti-inflammatory action via prostaglandin synthesis and bradykininase inhibition",
            "Gastrointestinal soothing: relief in mild gastritis, peptic irritation, and reflux",
            "Laxative activity (specifically the yellow latex containing anthraquinone glycosides)",
            "Adjunctive glycemic regulation in pre-diabetic and type 2 diabetic profiles"
        ],
        "traditionally_used_parts": [
            {"part": "Inner Leaf Gel (Pulp)", "indication": "Burns, cuts, cosmetic hydration, gastritis, digestive tonic"},
            {"part": "Leaf Latex (Exudate / Bitters)", "indication": "Short-term treatment of occasional constipation (stimulant laxative)"},
            {"part": "Whole Leaf Extract", "indication": "Detoxification, metabolic management, joint stiffness"}
        ],
        "preparation_information": [
            {"method": "Pure Inner Fillet Gel", "details": "Fresh mature leaf washed, thick green epidermis pared away; clear parenchymatous gel scooped and blended, devoid of yellow aloin-rich latex."},
            {"method": "Aloe Juice / Expressed Gel", "details": "Inner gel diluted with water or lemon juice; consumed fresh or refrigerated."},
            {"method": "Standardized Dry Latex Extract", "details": "Decanted and dried bitter yellow exudate standardized for aloin content (regulated for pharmaceutical laxative tablets)."}
        ],
        "dosage_information": [
            {
                "source": "WHO Monographs on Selected Medicinal Plants (Vol. 1)",
                "preparation": "Topical Hydrogel",
                "dose": "Apply fresh gel or 10-70% formulation liberally 2 to 3 times daily"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Leaf Pulp (Pulp/Gel)",
                "dose": "10 to 20 g daily"
            },
            {
                "source": "European Medicines Agency (EMA)",
                "preparation": "Standardized Anthraquinone Latex (Oral Laxative)",
                "dose": "10 - 30 mg hydroxyanthracene derivatives (as aloin) once daily at bedtime (maximum 1 week continuous use)"
            }
        ],
        "precautions_warnings": [
            "Distinction between Gel and Latex: The clear inner gel is safe for general use. The yellow latex (aloin) is a potent anthraquinone stimulant laxative and must not be taken indiscriminately.",
            "Pregnancy & Lactation: Oral latex is contraindicated during pregnancy due to reflex stimulation of uterine contractions and risk of miscarriage. Active metabolites pass into breast milk causing diarrhea in infants.",
            "Electrolyte Depletion: Chronic oral latex consumption causes severe hypokalemia, cardiac arrhythmia, and melanosis coli.",
            "Topical Sensitivity: Rare contact dermatitis in individuals allergic to Liliaceae/Asphodelaceae plants; conduct patch test."
        ],
        "contraindications_interactions": [
            "Absolute Contraindications (Oral Latex): Intestinal obstruction, Crohn's disease, ulcerative colitis, appendicitis, unexplained abdominal pain, children under 12 years.",
            "Drug Interactions: Cardiac glycosides (Digoxin) - hypokalemia increases digitalis toxicity; Diuretics (Furosemide) - worsens potassium wasting; Oral Antidiabetic agents - additive hypoglycemic risk."
        ],
        "active_phytochemicals": [
            "Acemannan (immunomodulatory acetylated polymannose)",
            "Aloin A and B (barbaloin - anthraquinone glycosides in latex)",
            "Aloe-emodin and Chrysophanol",
            "Bradykinase (anti-inflammatory peptidase)",
            "Glucomannan, vitamins A, C, E, B12, and amino acids"
        ],
        "botanical_morphology": "Acaulescent succulent perennial herb 60-100 cm; leaves thick, fleshy, rosette-forming, lanceolate, 40-50 cm long, 6-8 cm wide, glaucous green with spiny pinkish-white serrated margins containing gelatinous central parenchyma.",
        "native_region": "Arid regions of Arabian Peninsula; cultivated extensively across tropical and Mediterranean climates.",
        "iucn_conservation_status": "Least Concern"
    },

    "curcuma_longa": {
        "id": "curcuma_longa",
        "scientific_name": "Curcuma longa L. (syn. Curcuma domestica Valeton)",
        "common_names": ["Turmeric", "Haldi", "Haridra", "Indian Saffron"],
        "botanical_family": "Zingiberaceae (Ginger family)",
        "genus": "Curcuma",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 1 (1999)",
            "European Medicines Agency (EMA) Monograph on Curcuma longa",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "German Commission E Monographs"
        ],
        "documented_medicinal_uses": [
            "Profound anti-inflammatory activity via NF-kB and COX-2 inhibition (osteoarthritis, rheumatoid arthritis)",
            "Antioxidant free-radical scavenger protecting against cellular lipid peroxidation",
            "Choleretic and cholagogue: stimulates bile production and enhances lipid digestion",
            "Neuroprotective: enhances brain-derived neurotrophic factor (BDNF) and crosses blood-brain barrier",
            "Dermatological wound antiseptic and antibacterial topically for cuts, burns, and acne",
            "Cardiovascular endothelial protection and platelet homeostasis modulation"
        ],
        "traditionally_used_parts": [
            {"part": "Rhizome (Rhizoma)", "indication": "Joint inflammation, dyspepsia, biliary disorders, skin wounds, respiratory allergies"},
            {"part": "Leaves (Folia)", "indication": "Aromatic food wrapper with mild carminative and antifungal properties"}
        ],
        "preparation_information": [
            {"method": "Rhizome Powder (Churna)", "details": "Boiled, dried, and pulverized orange rhizomes; consumed with milk and pinch of black pepper (piperine enhances curcumin bioavailability by up to 2000%)."},
            {"method": "Topical Paste (Lepa)", "details": "Powder mixed with water, rose water, or sesame oil for application on inflammatory swellings and wounds."},
            {"method": "Decoction (Kwatha)", "details": "5-10 g crushed dried rhizome simmered in 200 ml water down to 50 ml."},
            {"method": "Golden Milk (Haridra Dugdha)", "details": "Half teaspoon powder simmered in warm cow or plant milk with ghee and crushed piper nigrum."}
        ],
        "dosage_information": [
            {
                "source": "WHO Monographs on Selected Medicinal Plants (Vol. 1)",
                "preparation": "Crude Rhizome Powder",
                "dose": "1.5 to 3.0 g daily in divided doses"
            },
            {
                "source": "European Medicines Agency (EMA)",
                "preparation": "Standardized Powdered Herbal Substance",
                "dose": "0.5 to 1.0 g, 2 to 3 times daily for digestive disorders"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Rhizome Powder (Churna)",
                "dose": "1 to 3 g twice daily with warm water or milk"
            }
        ],
        "precautions_warnings": [
            "Biliary Obstruction: Curcuma stimulates bile production; strictly contraindicated in mechanical bile duct obstruction and cholangitis.",
            "Gallstones: Consult physician before use; high doses may cause gallbladder contractions and colic.",
            "Bleeding Tendencies: Curcumin inhibits platelet aggregation; withhold high medicinal doses 2 weeks prior to surgical procedures.",
            "Gastric Hyperacidity: Very large doses may cause mild gastric irritation, nausea, or acid rebound."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Obstruction of biliary tract, acute biliary colic, severe liver disease.",
            "Drug Interactions: Anticoagulants / Antiplatelet drugs (Warfarin, Aspirin, Plavix) - synergistic hemorrhagic potential; Antidiabetic drugs - enhanced hypoglycemic response."
        ],
        "active_phytochemicals": [
            "Curcuminoids (Curcumin / Diferuloylmethane, Demethoxycurcumin, Bisdemethoxycurcumin - 3-5%)",
            "Volatile Essential Oil (Turmerone, ar-turmerone, Zingiberene)",
            "Polysaccharides (Ukonan A-D)",
            "Ferulic acid and caffeic acid"
        ],
        "botanical_morphology": "Perennial rhizomatous herb 1 m tall; leaves large, oblong-lanceolate, 70-100 cm long, green on both sides with long petiole; rhizomes oblong, ovate, pyriform, golden-yellow inside, intensely aromatic.",
        "native_region": "Native to tropical South Asia (India); requires humid tropical climate and well-drained loamy soils.",
        "iucn_conservation_status": "Least Concern"
    },

    "withania_somnifera": {
        "id": "withania_somnifera",
        "scientific_name": "Withania somnifera (L.) Dunal",
        "common_names": ["Ashwagandha", "Indian Ginseng", "Winter Cherry", "Asgandh"],
        "botanical_family": "Solanaceae (Nightshade family)",
        "genus": "Withania",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 4 (2009)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "United States Pharmacopeia - Dietary Supplements Compendium (USP-DSC)",
            "ICMR Monographs on Indian Medicinal Plants"
        ],
        "documented_medicinal_uses": [
            "Adaptogen: Promotes homeostasis, reduces perceived stress, and lowers serum cortisol levels",
            "Neurocognitive enhancement: Supports memory consolidation, attention, and executive function",
            "Sleep architecture improvement: Reduces sleep latency and promotes non-REM deep rest",
            "Anabolic / Athletic performance: Increases VO2 max, muscle strength, and recovery rate",
            "Male endocrine support: Enhances spermatogenesis, sperm motility, and testosterone synthesis",
            "Immunomodulation: Stimulates macrophage phagocytosis, lymphocytes, and hematopoiesis"
        ],
        "traditionally_used_parts": [
            {"part": "Root (Radix)", "indication": "General debility, nervous exhaustion, insomnia, arthritis, cognitive decline, reproductive vitality"},
            {"part": "Leaves (Folia)", "indication": "Topical poultice for painful joint swellings, carbuncles, scrofula, and skin ulcers"},
            {"part": "Berries / Seeds", "indication": "Milk coagulant (rennet substitute), mild diuretic"}
        ],
        "preparation_information": [
            {"method": "Root Powder (Churna)", "details": "Fine powder of dried mature roots boiled with cow's milk and ghee or honey."},
            {"method": "Root Decoction (Kashayam)", "details": "10 g root pieces simmered in 16 parts water down to 4 parts."},
            {"method": "Standardized Aqueous/Hydroalcoholic Root Extract", "details": "Concentrated dry extract standardized to 2.5% or 5% withanolides (KSM-66, Sensoril)."},
            {"method": "Leaf Paste (Kalka)", "details": "Fresh leaves crushed and heated with castor oil, applied topically on inflamed joints."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Crude Root Powder (Churna)",
                "dose": "3 to 6 g daily with warm milk or honey"
            },
            {
                "source": "WHO Monographs on Selected Medicinal Plants (Vol. 4)",
                "preparation": "Standardized Root Extract (Withanolides)",
                "dose": "300 to 600 mg daily in divided doses"
            },
            {
                "source": "ICMR Clinical Guidelines",
                "preparation": "Root Decoction",
                "dose": "50 to 100 ml twice daily"
            }
        ],
        "precautions_warnings": [
            "Pregnancy: Spasmolytic and potential abortifacient activities observed in high doses; contraindicated during gestation.",
            "Thyroid Disorders: Ashwagandha stimulates thyroid hormone (T3 and T4) synthesis; patients with hyperthyroidism should avoid it, and hypothyroid patients should monitor levels.",
            "Sedation: May potentiate sedatives, barbiturates, and anxiolytics; caution when operating machinery.",
            "Autoimmune Conditions: May stimulate immune activity; exercise caution in lupus, rheumatoid arthritis, Hashimoto's."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy, severe hepatic impairment, thyrotoxicosis.",
            "Drug Interactions: Benzodiazepines, Barbiturates, Alcohol (enhanced CNS depression); Thyroid hormone medications (Levothyroxine) - additive elevation; Immunosuppressive therapy."
        ],
        "active_phytochemicals": [
            "Withanolides (steroidal lactones: Withaferin A, Withanolide A and D)",
            "Withanosides (glycowithanolides I-VI)",
            "Alkaloids (Somniferine, Withanine, Tropine, Pseudotropine)",
            "Sitoindosides VII to X"
        ],
        "botanical_morphology": "Erect stellate-tomentose subshrub 30-150 cm; leaves simple, alternate or subopposite, ovate, 5-10 cm long, margin entire to wavy, dull green; flowers greenish-yellow; berries globose, bright red inside an inflated persistent calyx.",
        "native_region": "Dry and subtropical regions of India, Pakistan, Mediterranean, and parts of Africa.",
        "iucn_conservation_status": "Least Concern"
    },

    "centella_asiatica": {
        "id": "centella_asiatica",
        "scientific_name": "Centella asiatica (L.) Urban (syn. Hydrocotyle asiatica)",
        "common_names": ["Gotu Kola", "Mandukaparni", "Brahmi (South India)", "Indian Pennywort"],
        "botanical_family": "Apiaceae (Umbelliferae)",
        "genus": "Centella",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 1 (1999)",
            "European Medicines Agency (EMA) Community Herbal Monograph",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. IV",
            "Pharmacopée Française / European Pharmacopoeia (Ph. Eur.)"
        ],
        "documented_medicinal_uses": [
            "Neurotropic / Nootropic: Enhances dendrite branching, memory retention, and mental clarity",
            "Venous insufficiency therapeutics: Improves microcirculation and strengthens capillary walls in varicose veins",
            "Dermal collagen synthesis accelerator: Stimulates type I collagen in burn scars, keloids, and surgical wounds",
            "Anxiolytic action: Modulates GABAergic neurotransmission without causing sedation",
            "Anti-ulcerogenic: Promotes mucosal healing and restores gastric epithelial barrier integrity",
            "Neuroprotective against beta-amyloid toxicity and oxidative stress"
        ],
        "traditionally_used_parts": [
            {"part": "Whole Herb (Panchanga)", "indication": "Cognitive deficits, mental fatigue, anxiety, skin disorders, memory enhancement"},
            {"part": "Fresh Leaves (Patra)", "indication": "Dietary salad herb for longevity, eyesight, and digestive rejuvenation"}
        ],
        "preparation_information": [
            {"method": "Fresh Herb Juice (Swarasa)", "details": "Fresh whole plant washed, crushed, and strained; consumed with milk and honey."},
            {"method": "Infusion (Phanta)", "details": "1-2 g dried leaves steeped in 150 ml boiling water for 10 minutes."},
            {"method": "Standardized Titrated Extract (TECA)", "details": "Pharmaceutical extract containing 40% asiaticoside and 60% madecassic/asiatic acid for venous and dermatological therapeutics."},
            {"method": "Medicated Ghee (Brahmi Ghrita)", "details": "Juice processed with cow's ghee and select herbs according to Classical Ayurvedic texts for neuropsychiatric indications."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Plant Juice (Swarasa)",
                "dose": "10 to 20 ml once daily"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Dried Herb Powder (Churna)",
                "dose": "3 to 6 g daily in divided doses"
            },
            {
                "source": "European Medicines Agency (EMA)",
                "preparation": "Standardized Extract (Venous insufficiency)",
                "dose": "60 to 180 mg daily of standardized triterpenoid fraction"
            }
        ],
        "precautions_warnings": [
            "Hepatic Safety: Excessive prolonged oral usage over 6 continuous weeks without interruption should be avoided to prevent liver enzyme elevation.",
            "Pregnancy: Emmenagogue activity reported in excessive traditional doses; avoid during pregnancy.",
            "Hypnotic Interaction: May have additive central nervous system depressant effects if taken with sleeping medications.",
            "Skin Sensitization: Rare contact dermatitis from topical creams in hypersensitive individuals."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Severe hepatic failure, allergy to Apiaceae family.",
            "Drug Interactions: Sedatives (benzodiazepines, zolpidem), hepatotoxic medications, cholesterol-lowering drugs (may interfere with lipid metabolism)."
        ],
        "active_phytochemicals": [
            "Triterpenoid saponins (Asiaticoside, Madecassoside)",
            "Triterpene acids (Asiatic acid, Madecassic acid, Madasiatic acid)",
            "Flavonoids (Quercetin, Kaempferol, Astragalin)",
            "Centelloside and Brahminoside"
        ],
        "botanical_morphology": "Slender, creeping, stoloniferous perennial herb rooting at nodes; leaves orbicular-reniform (kidney-shaped), 1.5-5 cm in diameter, margin crenate, cupped, with long channeled petioles.",
        "native_region": "Wet, marshy, pantropical regions of Asia, Africa, Australasia, and the Americas.",
        "iucn_conservation_status": "Least Concern"
    },

    "adhatoda_vasica": {
        "id": "adhatoda_vasica",
        "scientific_name": "Justicia adhatoda L. (syn. Adhatoda vasica Nees)",
        "common_names": ["Vasaka", "Malabar Nut", "Adosa", "Basa"],
        "botanical_family": "Acanthaceae (Acanthus family)",
        "genus": "Justicia",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 4 (2009)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 1"
        ],
        "documented_medicinal_uses": [
            "Potent bronchodilator: Relaxes bronchial smooth muscle and relieves bronchospasm in asthma",
            "Expectorant & Mucolytic: Liquefies viscous tracheobronchial mucus (origin of pharmaceutical Bromhexine and Ambroxol)",
            "Antitussive: Suppresses persistent coughing without depressing the central respiratory center",
            "Hemostatic: Controls intrinsic capillary bleeding, epistaxis, and dysfunctional uterine menorrhagia",
            "Antitubercular synergist: Enhances rifampicin pulmonary bioavailability against Mycobacterium tuberculosis",
            "Antibacterial activity against respiratory tract pathogens (Streptococcus pneumoniae, Klebsiella pneumoniae)"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Vasa Patra)", "indication": "Cough, asthma, bronchitis, hemoptysis, chronic pharyngitis"},
            {"part": "Root (Moola)", "indication": "Fever, chronic respiratory ailments, asthma, leucorrhoea"},
            {"part": "Flowers (Pushpa)", "indication": "Antispasmodic, ophthalmia, bleeding disorders"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Vasa Swarasa)", "details": "Fresh leaves steamed or heated slightly, crushed, and juice extracted; taken with honey."},
            {"method": "Decoction (Kashayam)", "details": "10-15 g dried leaves boiled in 400 ml water down to 100 ml; taken warm."},
            {"method": "Fermented Liquid (Vasarishta)", "details": "Classical Ayurvedic self-generated hydroalcoholic preparation for chronic bronchial ailments."},
            {"method": "Herbal Confection (Vasa Avaleha)", "details": "Juice boiled with sugar candy, pippali, and ghee into a viscous electuary for long-term pulmonary support."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Leaf Juice (Swarasa)",
                "dose": "10 to 20 ml twice daily with honey"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Leaf Powder (Churna)",
                "dose": "2 to 4 g twice daily"
            },
            {
                "source": "WHO Monograph on Selected Medicinal Plants (Vol. 4)",
                "preparation": "Standardized Extract (calculated as Vasicine)",
                "dose": "2 to 4 mg of vasicine, 2 to 3 times daily"
            }
        ],
        "precautions_warnings": [
            "Uterine Stimulant: Vasicine possesses documented oxytocic and abortifacient actions; strictly contraindicated during pregnancy.",
            "High Dose Emesis: Excessive doses of fresh juice irritate gastric mucosa, causing nausea and vomiting.",
            "Pediatrics: Dose must be adjusted strictly according to weight; avoid unregulated administration in infants."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy (causes uterine contractions and premature labor).",
            "Drug Interactions: Bronchodilators (Theophylline, Salbutamol) - additive effect; Anticoagulants (may affect bleeding time)."
        ],
        "active_phytochemicals": [
            "Vasicine (quinazoline alkaloid - bronchodilator)",
            "Vasicinone (bronchodilator and antitussive)",
            "Adhatodine and Vasicinol",
            "Betaine and Vasakin",
            "Essential oil containing limonene"
        ],
        "botanical_morphology": "Dense evergreen shrub 2-4 m high; leaves opposite, elliptic-lanceolate, 10-20 cm long, 3-8 cm wide, acuminate, entire, dark green above and paler beneath, distinctive bitter taste and pungent smell.",
        "native_region": "Indigenous to plains and sub-Himalayan tracts of India, Sri Lanka, Nepal, and Southeast Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    "catharanthus_roseus": {
        "id": "catharanthus_roseus",
        "scientific_name": "Catharanthus roseus (L.) G. Don (syn. Vinca rosea L.)",
        "common_names": ["Madagascar Periwinkle", "Sadabahar", "Nayantara", "Rosy Periwinkle"],
        "botanical_family": "Apocynaceae (Dogbane family)",
        "genus": "Catharanthus",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial & Oncology Source Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Model List of Essential Medicines (Vincristine / Vinblastine source)",
            "United States Pharmacopeia (USP) - Vinca Alkaloids",
            "British Pharmacopoeia (BP) & European Pharmacopoeia",
            "Ayurvedic Pharmacopoeia & Traditional Folk Medicine Records"
        ],
        "documented_medicinal_uses": [
            "Oncology source: Botanical source of FDA-approved anti-neoplastic drugs Vincristine (leukemia, lymphomas) and Vinblastine (Hodgkin's lymphoma, testicular cancer)",
            "Folk Antidiabetic: Traditional use of leaf decoction for type 2 diabetes (stimulates beta-cell insulin secretion)",
            "Antihypertensive: Vasodilatory indole alkaloids lower systemic vascular resistance",
            "Wound healing and antimicrobial topically for minor dermal excoriations",
            "Antidote in traditional folklore for wasp and hornet stings"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Folia)", "indication": "Traditional glycemic regulation, hypertension, wasp stings; extraction of pharmaceutical alkaloids"},
            {"part": "Root (Radix)", "indication": "Industrial extraction of Ajmalicine (antihypertensive and cerebral vasodilator)"},
            {"part": "Whole Plant", "indication": "Industrial isolation of therapeutic dimeric indole-indoline alkaloids"}
        ],
        "preparation_information": [
            {"method": "Pharmaceutical Isolation (Clinical Oncology)", "details": "Purified crystalline vincristine sulfate and vinblastine sulfate for intravenous chemotherapy under strict medical supervision."},
            {"method": "Folk Leaf Infusion (Not Recommended for self-medication)", "details": "2-3 fresh leaves soaked in warm water overnight; consumed early morning in traditional folklore."},
            {"method": "Leaf Paste (External)", "details": "Fresh leaves crushed and applied to insect bites and stings."}
        ],
        "dosage_information": [
            {
                "source": "Clinical Oncology Monograph (USP / BP)",
                "preparation": "Purified Vincristine Sulfate (IV)",
                "dose": "Strictly prescribed: 1.4 mg/m² IV weekly by oncologist (NEVER by self-medication)"
            },
            {
                "source": "Traditional Ethnomedicinal Practice (Caution Required)",
                "preparation": "Fresh Leaf Decoction",
                "dose": "Max 2 to 4 leaves boiled in 100 ml water; limited usage due to narrow therapeutic index"
            }
        ],
        "precautions_warnings": [
            "HIGH TOXICITY RISK: Catharanthus contains powerful cytotoxic alkaloids. Unstandardized ingestion can cause severe bone marrow suppression, myelosuppression, neurotoxicity, and hair loss.",
            "Pregnancy & Lactation: Highly teratogenic and embryotoxic; strictly contraindicated.",
            "Self-Medication Warning: Patients should NEVER attempt self-treatment for cancer or diabetes using crude extracts.",
            "Inadvertent Intrathecal Administration: Vincristine administered intrathecally is fatal."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy, lactation, liver disease, pre-existing leukopenia or neurodegenerative disease.",
            "Drug Interactions: CYP3A4 inhibitors (Ketoconazole, Erythromycin) - drastically increase alkaloid toxicity; Ototoxic / Nephrotoxic agents."
        ],
        "active_phytochemicals": [
            "Vincristine and Vinblastine (bisindole alkaloids - tubulin binders)",
            "Ajmalicine (Raubasine - cerebral circulation)",
            "Serpentine and Catharanthine",
            "Vindoline and Vindolinine"
        ],
        "botanical_morphology": "Evergreen herbaceous subshrub 30-100 cm tall; leaves opposite, oval to oblong, 2.5-9 cm long, glossy green with pale midrib, short petiole; flowers with salverform corolla having 5 lobes, pink, rose, or white with reddish eye.",
        "native_region": "Endemic to Madagascar; naturalized widely in tropical and subtropical regions worldwide.",
        "iucn_conservation_status": "Least Concern"
    },

    "moringa_oleifera": {
        "id": "moringa_oleifera",
        "scientific_name": "Moringa oleifera Lam.",
        "common_names": ["Moringa", "Drumstick Tree", "Shigru", "Horseradish Tree", "Miracle Tree"],
        "botanical_family": "Moringaceae",
        "genus": "Moringa",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial & Nutra-Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "WHO / FAO Nutritional & Phytomedicinal Compendium",
            "ICMR Monographs on Indian Medicinal Plants"
        ],
        "documented_medicinal_uses": [
            "Super-nutritional restorative: High concentrations of bioavailable vitamins A, C, E, calcium, iron, and complete proteins",
            "Anti-hyperglycemic and insulin-sensitizing via chlorogenic acid and isothiocyanates",
            "Antihypertensive: Vasodilatory beta-sitosterol and glycosides decrease arterial blood pressure",
            "Anti-hyperlipidemic: Significantly lowers serum cholesterol, LDL, and triglycerides",
            "Anti-inflammatory: Relieves joint pain and swelling in osteoarthritis and rheumatoid ailments",
            "Galactagogue: Stimulates prolactin secretion and boosts breast milk production in nursing mothers"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Shigru Patra)", "indication": "Malnutrition, anemia, diabetes, hypertension, arthritis, lactation enhancement"},
            {"part": "Pods / Fruit (Phala)", "indication": "Nutritious culinary vegetable, digestive tonic, anthelmintic"},
            {"part": "Seeds (Beeja)", "indication": "Water purification (coagulant), antimicrobial, joint inflammation, oil source"},
            {"part": "Bark / Root (Tvaka / Moola)", "indication": "Deep inflammatory disorders, rubefacient, abortifacient (toxic root bark)"}
        ],
        "preparation_information": [
            {"method": "Leaf Powder", "details": "Shade-dried green leaves pulverized; incorporated into water, smoothies, or curries."},
            {"method": "Fresh Leaf Decoction", "details": "10-20 g fresh leaves boiled in 200 ml water; taken warm."},
            {"method": "Seed Powder for Coagulation", "details": "Crushed dry seeds stirred in turbid water to settle particulates and bacteria."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Dried Leaf Powder (Churna)",
                "dose": "2 to 5 g daily"
            },
            {
                "source": "WHO / FAO Dietary Recommendations",
                "preparation": "Nutritional Leaf Supplement",
                "dose": "5 to 10 g daily for addressing micronutrient deficiency"
            },
            {
                "source": "ICMR Guidelines",
                "preparation": "Seed Powder / Stem Bark Extract",
                "dose": "1 to 2 g under professional supervision"
            }
        ],
        "precautions_warnings": [
            "Root Bark Warning: Root and root bark contain spirochin alkaloid which has paralyzing neurotoxic properties and is strongly abortifacient. Avoid root/bark preparations.",
            "Pregnancy: Leaf consumption in culinary amounts is safe, but high medicinal leaf extracts or root extracts must be avoided due to uterine stimulation.",
            "Laxative Effect: High initial doses of leaf powder may cause loose stools and mild abdominal cramps."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy (for root and root bark preparations).",
            "Drug Interactions: Antidiabetic medications (potential additive hypoglycemia), Antihypertensive drugs (additive hypotension), Levothyroxine (may interfere with absorption)."
        ],
        "active_phytochemicals": [
            "Isothiocyanates (Moringin)",
            "Quercetin and Kaempferol",
            "Chlorogenic acid",
            "Beta-sitosterol",
            "Niazimicin and Pterygospermin"
        ],
        "botanical_morphology": "Fast-growing deciduous tree 10-12 m; leaves tripinnate, 30-60 cm long, with numerous small elliptic to obovate leaflets (1-2 cm long), pale green beneath; flowers white, fragrant; fruit long pendulous triangular ribbed capsule (pod).",
        "native_region": "Native to foothills of the Himalayas in Northwestern India; cultivated pantropically.",
        "iucn_conservation_status": "Least Concern"
    },

    "mentha_arvensis": {
        "id": "mentha_arvensis",
        "scientific_name": "Mentha arvensis L. (syn. Mentha canadensis)",
        "common_names": ["Field Mint", "Corn Mint", "Pudina", "Japanese Mint"],
        "botanical_family": "Lamiaceae (Mint family)",
        "genus": "Mentha",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "WHO Monographs on Selected Medicinal Plants, Vol. 2 (2002)",
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. II",
            "European Medicines Agency (EMA) Monograph on Mentha Oil",
            "German Commission E Monographs"
        ],
        "documented_medicinal_uses": [
            "Gastrointestinal antispasmodic: Relaxes smooth muscle of GI tract via calcium channel blockade (irritable bowel syndrome, dyspepsia)",
            "Carminative: Relieves flatulence, aerophagia, and sensation of abdominal fullness",
            "Topical antipruritic and analgesic: Menthol stimulates cold-sensitive TRPM8 receptors providing cooling pain relief",
            "Decongestant: Inhalational vapor clears nasal congestion and relieves catarrh",
            "Antiemetic: Suppresses nausea, vomiting, and motion sickness",
            "Antibacterial and antifungal in oral hygiene against bad breath and gingivitis"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Folia)", "indication": "Indigestion, nausea, fever, headache, oral halitosis, abdominal colic"},
            {"part": "Volatile Oil (Menthol / Peppermint Oil)", "indication": "Topical analgesia, tension headache, IBS enteric capsules, vapor inhalation"}
        ],
        "preparation_information": [
            {"method": "Leaf Infusion (Pudina Phanta)", "details": "1.5-3 g dried leaves infused in 150 ml boiling water for 10 minutes in a covered vessel."},
            {"method": "Fresh Leaf Chutney / Juice", "details": "Leaves ground with cumin, black salt, and lemon as digestive carminative appetizer."},
            {"method": "Volatile Oil (Enteric-coated)", "details": "Commercial standardized capsules for lower GI release in IBS."},
            {"method": "Steam Inhalation", "details": "3-4 drops of mint essential oil in a bowl of hot steaming water."}
        ],
        "dosage_information": [
            {
                "source": "WHO Monographs on Selected Medicinal Plants (Vol. 2)",
                "preparation": "Dried Leaf Infusion",
                "dose": "1.5 to 3.0 g dried leaf in 150 ml water, 3 times daily"
            },
            {
                "source": "European Medicines Agency (EMA)",
                "preparation": "Mentha Oil (Enteric-coated for IBS)",
                "dose": "0.2 to 0.4 ml (187-374 mg) 3 times daily before meals"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Fresh Leaf Juice (Swarasa)",
                "dose": "5 to 10 ml twice daily"
            }
        ],
        "precautions_warnings": [
            "GERD / Acid Reflux: Menthol relaxes the lower esophageal sphincter; can aggravate gastroesophageal reflux and heartburn.",
            "Infant Facial Application: Never apply menthol or mint oil directly to the face or nostrils of infants or small children; can induce reflex laryngospasm and respiratory arrest.",
            "Gallbladder Diseases: Use cautiously in patients with gallstones or biliary obstruction."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Gastroesophageal reflux disease (GERD), severe biliary tract obstruction, hepatic failure, application to face of infants.",
            "Drug Interactions: Antacids and H2-blockers (may dissolve enteric coating of mint capsules prematurely), Cytochrome P450 substrates (mild modulation)."
        ],
        "active_phytochemicals": [
            "Menthol (70-80% in volatile oil)",
            "Menthone and Isomenthone",
            "Menthyl acetate",
            "Limonene and Pulegone (trace)",
            "Rosmarinic acid and flavonoids (luteolin, eriodictyol)"
        ],
        "botanical_morphology": "Perennial aromatic herb 30-60 cm with creeping rhizomes; stems quadrangular, purplish; leaves opposite, ovate-lanceolate, 2.5-5 cm long, margin serrate, glandular-punctate beneath, releasing characteristic mint scent when bruised.",
        "native_region": "Temperate and subtropical regions of Europe, Central and Eastern Asia.",
        "iucn_conservation_status": "Least Concern"
    },

    "dieffenbachia_seguine": {
        "id": "dieffenbachia_seguine",
        "scientific_name": "Dieffenbachia seguine (Jacq.) Schott (syn. Dieffenbachia picta)",
        "common_names": ["Dumb Cane", "Tropic Snow", "Leopard Lily"],
        "botanical_family": "Araceae (Arum family)",
        "genus": "Dieffenbachia",
        "is_medicinal": False,
        "medicinal_status": "Toxic / Hazardous Ornamental Plant (Non-Medicinal)",
        "status_badge_color": "rose",
        "authoritative_sources": [
            "American Association of Poison Control Centers (AAPCC) Toxic Plant Guidelines",
            "Clinical Toxicology of Commercial Products (Gosselin et al.)",
            "National Institute for Occupational Safety and Health (NIOSH) Database"
        ],
        "documented_medicinal_uses": [
            "NO RECOGNIZED THERAPEUTIC MEDICINAL USES in modern pharmacopoeias.",
            "Historical note: Used historically as an instrument of punishment to render victims mute (hence 'Dumb Cane') due to laryngeal edema.",
            "Common indoor decorative houseplant valued solely for variegated foliage, not medicine."
        ],
        "traditionally_used_parts": [
            {"part": "None", "indication": "All plant parts contain toxic calcium oxalate raphides and proteolytic enzymes. INGESTION IS DANGEROUS."}
        ],
        "preparation_information": [
            {"method": "NOT APPLICABLE", "details": "Plant is toxic. Ingestion or topical handling can cause severe mucosal burns. No medicinal preparation is recognized."}
        ],
        "dosage_information": [
            {
                "source": "Poison Control Medical Reference",
                "preparation": "Toxic Exposure Threshold",
                "dose": "Chewing even half a leaf causes intense stinging, stomatitis, and dysphagia. DOSE IS ZERO (CONTRAINDICATED)."
            }
        ],
        "precautions_warnings": [
            "SEVERE TOXICITY WARNING: Plant contains needle-sharp insoluble calcium oxalate crystals (raphides) stored in specialized idioblast cells, bundled with proteolytic enzymes (dumbcaine).",
            "When chewed, the raphides are forcefully ejected into the buccal mucosa, tongue, and pharynx, causing immediate intense burning sensation, profound salivation, tongue swelling, and transient loss of speech.",
            "Laryngeal Edema Risk: Severe swelling may obstruct the airway, leading to asphyxiation, particularly in young children and pets.",
            "Ocular Exposure: Sap in the eyes causes severe keratoconjunctivitis and corneal abrasions."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: ALL INTERNAL CONSUMPTION IS STRICTLY PROHIBITED.",
            "Handling Precautions: Wear protective gloves when pruning or propagating; wash hands thoroughly; keep strictly away from domestic animals and children."
        ],
        "active_phytochemicals": [
            "Insoluble Calcium oxalate raphides (mechanical micro-needles)",
            "Dumbcaine (proteolytic trypsin-like enzyme causing histamine release)",
            "Cyanogenic glycosides (trace)",
            "Steroidal sapogenins"
        ],
        "botanical_morphology": "Robust perennial herb 1-2 m tall with thick cane-like fleshy stem; leaves alternate, large, oblong-elliptic, 25-50 cm long, deep green variegated with creamy white or yellow irregular blotches and spots.",
        "native_region": "Tropical Americas and the West Indies; widely cultivated worldwide as a potted ornamental.",
        "iucn_conservation_status": "Least Concern (Cultivated Ornamental)"
    },

    "nerium_oleander": {
        "id": "nerium_oleander",
        "scientific_name": "Nerium oleander L.",
        "common_names": ["Oleander", "Kaner", "Rose Bay", "Adelfa"],
        "botanical_family": "Apocynaceae (Dogbane family)",
        "genus": "Nerium",
        "is_medicinal": False,
        "medicinal_status": "Extremely Toxic / Poisonous Plant (Non-Medicinal)",
        "status_badge_color": "rose",
        "authoritative_sources": [
            "International Programme on Chemical Safety (IPCS / INCHEM) Monograph",
            "WHO Poisons Information Monograph (PIM 366)",
            "TOXNET / Hazardous Substances Data Bank (HSDB)"
        ],
        "documented_medicinal_uses": [
            "NO SAFE RECOGNIZED MEDICINAL USES in legitimate modern healthcare.",
            "Historical/folk note: Extremely dangerous folk uses for cardiac dropsy and skin ailments were abandoned due to high fatality rates.",
            "Oleandrin has been studied in in-vitro cancer research, but whole-plant ingestion is lethal."
        ],
        "traditionally_used_parts": [
            {"part": "None", "indication": "ALL PARTS (leaves, flowers, stems, roots, sap, and even smoke from burning wood) ARE HIGHLY LETHAL."}
        ],
        "preparation_information": [
            {"method": "STRICTLY FORBIDDEN", "details": "Contains potent cardiac glycosides. Do not prepare or ingest under any circumstance."}
        ],
        "dosage_information": [
            {
                "source": "WHO Poisons Information Monograph (PIM 366)",
                "preparation": "Lethal Toxicity Threshold",
                "dose": "Ingestion of even a single leaf can be lethal to an adult human or child. DOSE IS ZERO."
            }
        ],
        "precautions_warnings": [
            "LETHAL POISON WARNING: Contains high concentrations of potent cardiotoxins (Oleandrin and Neriine) that inhibit the cardiac sodium-potassium ATPase pump.",
            "Symptoms of Ingestion: Severe gastrointestinal nausea, projectile vomiting, bloody diarrhea, bradycardia, visual halos (xanthopsia), ventricular arrhythmias, heart block, and fatal cardiac arrest.",
            "Environmental Hazard: Honey made from oleander nectar is poisonous; meat roasted on oleander twigs has caused mass poisonings.",
            "Medical Emergency: Anyone suspected of ingesting oleander requires immediate emergency hospitalization, gastric lavage, activated charcoal, and Digoxin-specific Fab antibodies (Digibind)."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: COMPLETE CONTRAINDICATION FOR ALL INGESTION OR MEDICINAL ATTEMPTS.",
            "Interactions: Fatal synergism with digitalis, beta-blockers, and calcium channel blockers."
        ],
        "active_phytochemicals": [
            "Oleandrin (potent cardiac glycoside)",
            "Neriine and Adynerin",
            "Folinerin and Rosagenin",
            "Flavonoids (Rutin) and triterpenoids"
        ],
        "botanical_morphology": "Erect evergreen shrub 2-5 m tall; leaves in whorls of 3, narrow lanceolate, 10-22 cm long, 1.5-3 cm wide, leathery, dark green with prominent pale midrib and parallel secondary veins; flowers showy, white, pink, or crimson.",
        "native_region": "Mediterranean basin and coastal Southwest Asia; widely planted along highways as drought-tolerant ornamental.",
        "iucn_conservation_status": "Least Concern"
    },

    "monstera_deliciosa": {
        "id": "monstera_deliciosa",
        "scientific_name": "Monstera deliciosa Liebm.",
        "common_names": ["Swiss Cheese Plant", "Split-Leaf Philodendron", "Ceriman", "Fruit Salad Plant"],
        "botanical_family": "Araceae (Arum family)",
        "genus": "Monstera",
        "is_medicinal": False,
        "medicinal_status": "Ornamental Foliage Plant (Non-Medicinal)",
        "status_badge_color": "slate",
        "authoritative_sources": [
            "Royal Botanic Gardens Kew - Plants of the World Online (POWO)",
            "University of California Davis Toxic Plant Database"
        ],
        "documented_medicinal_uses": [
            "NO FORMAL PHARMACOPOEIAL MEDICINAL USES.",
            "Popular indoor ornamental valued for dramatic fenestrated foliage and air purification.",
            "Traditional folk craft: Aerial roots used for weaving ropes and baskets in native Mexican folklore."
        ],
        "traditionally_used_parts": [
            {"part": "Ripe Fruit Only", "indication": "Fully ripe fruit is edible with a flavor resembling banana and pineapple (all other parts are toxic)."}
        ],
        "preparation_information": [
            {"method": "Ornamental / Edible Ripe Fruit Only", "details": "Leaves and stems must NEVER be consumed. Fruit must be allowed to ripen on the stem until scales fall off naturally before eating."}
        ],
        "dosage_information": [
            {
                "source": "Botanical Toxicology Reference",
                "preparation": "Leaf Ingestion",
                "dose": "NOT A MEDICINE. Foliage is unsuited for internal medical therapy."
            }
        ],
        "precautions_warnings": [
            "Contains calcium oxalate crystals throughout foliage and stems that cause severe oral irritation, drooling, and dysphagia if chewed.",
            "Unripe fruit contains high oxalate levels causing throat irritation; eat only when scales shed spontaneously.",
            "Keep away from cats and dogs."
        ],
        "contraindications_interactions": [
            "Contraindication: Ingestion of leaves, petioles, or unripened fruit is contraindicated.",
            "No known pharmacological interactions."
        ],
        "active_phytochemicals": [
            "Calcium oxalate raphides",
            "Amylases and proteases in ripening fruit",
            "Polysaccharides"
        ],
        "botanical_morphology": "Epiphytic or hemiepiphytic climbing liana with stout aerial roots; leaves huge, cordate, 25-90 cm long, coriaceous, pinnatifid with deep lateral lobes and perforated with elliptical holes (fenestrations).",
        "native_region": "Tropical rainforests of Southern Mexico and Central America.",
        "iucn_conservation_status": "Least Concern"
    },

    "ficus_religiosa": {
        "id": "ficus_religiosa",
        "scientific_name": "Ficus religiosa L.",
        "common_names": ["Sacred Fig", "Peepal", "Bodhi Tree", "Ashvattha"],
        "botanical_family": "Moraceae (Mulberry family)",
        "genus": "Ficus",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial Medicinal Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "Ayurvedic Pharmacopoeia of India (API), Part I, Vol. I",
            "ICMR Monographs on Indian Medicinal Plants, Vol. 11",
            "Unani Pharmacopoeia of India"
        ],
        "documented_medicinal_uses": [
            "Astringent and hemostatic: Arrests capillary bleeding, epistaxis, and hematuria",
            "Wound healing: Accelerates granulation and epithelization in burns and chronic ulcers",
            "Antidiabetic: Bark extract improves insulin resistance and downregulates glycogenolysis",
            "Anti-inflammatory and analgesic: Relieves pain in arthritic joints and inflammatory bowel conditions",
            "Oral health: Bark decoction gargle tightens loose gums, relieves toothache and stomatitis",
            "Respiratory support: Bark and tender leaf decoction for bronchial asthma and persistent cough"
        ],
        "traditionally_used_parts": [
            {"part": "Stem Bark (Tvaka)", "indication": "Bleeding disorders, diabetes, diarrhea, skin diseases, oral ulcers"},
            {"part": "Tender Leaves / Shoots", "indication": "Constipation, skin blemishes, nosebleeds, heart palpitations"},
            {"part": "Latex (Kshira)", "indication": "Cracked heels, boils, warts, minor cuts"},
            {"part": "Fruit (Figs)", "indication": "Digestive weakness, asthma, respiratory irritation"}
        ],
        "preparation_information": [
            {"method": "Bark Decoction (Kashayam)", "details": "20-30 g coarse bark boiled in 400 ml water reduced to 100 ml; taken orally or as gargle."},
            {"method": "Leaf Infusion", "details": "Tender heart-shaped leaves crushed and soaked in water overnight for cooling bowel regulation."},
            {"method": "Bark Powder (Churna)", "details": "Dried bark pulverized and taken with honey or warm milk."},
            {"method": "Topical Bark Paste", "details": "Powder mixed with coconut oil or honey applied on chronic wounds and burns."}
        ],
        "dosage_information": [
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Stem Bark Powder (Churna)",
                "dose": "3 to 6 g daily in divided doses"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Bark Decoction (Kwatha)",
                "dose": "50 to 100 ml twice daily"
            },
            {
                "source": "ICMR Guidelines",
                "preparation": "Tender Leaf Juice",
                "dose": "5 to 10 ml with honey"
            }
        ],
        "precautions_warnings": [
            "Mild laxative effect: Large doses of leaves may cause diarrhea.",
            "Pregnancy: Safe in culinary amounts; high medicinal doses of bark decoctions should be supervised by a practitioner.",
            "Latex contact: White sap may cause mild contact dermatitis in individuals with latex allergy."
        ],
        "contraindications_interactions": [
            "Contraindication: Severe diarrhea or dysentery (for tender leaf preparations).",
            "Drug Interactions: Antidiabetic medications (monitor glucose levels due to additive hypoglycemia)."
        ],
        "active_phytochemicals": [
            "Tannins and flavonoids (Quercetin, Kaempferol)",
            "Beta-sitosterol and Stigmasterol",
            "Lupan-3-one and Lupeol",
            "Vitamin K (hemostatic cofactor)"
        ],
        "botanical_morphology": "Large semi-evergreen banyan tree up to 30 m; leaves distinctly heart-shaped (cordate), 10-18 cm long, with an extraordinary elongated drip tip (tail) 2-6 cm long; petiole slender, causing leaves to flutter in the gentlest breeze.",
        "native_region": "Indian subcontinent and Indochina; revered across Hindu and Buddhist traditions.",
        "iucn_conservation_status": "Least Concern"
    },

    "carica_papaya": {
        "id": "carica_papaya",
        "scientific_name": "Carica papaya L.",
        "common_names": ["Papaya", "Pawpaw", "Papita", "Erandakarkati"],
        "botanical_family": "Caricaceae",
        "genus": "Carica",
        "is_medicinal": True,
        "medicinal_status": "Recognized Pharmacopoeial & Clinical Leaf Extract Plant",
        "status_badge_color": "emerald",
        "authoritative_sources": [
            "ICMR Guidelines & Clinical Studies on Dengue Thrombocytopenia",
            "Ayurvedic Pharmacopoeia of India (API)",
            "British Herbal Pharmacopoeia (BHP)"
        ],
        "documented_medicinal_uses": [
            "Thrombocytopenia management: Clinically proven to stimulate thrombopoietin and accelerate platelet recovery in Dengue and viral fevers",
            "Proteolytic digestive aid: Papain and chymopapain break down proteins and ease gastric fullness",
            "Anti-inflammatory: Modulates inflammatory cytokines and relieves arthritic stiffness",
            "Anthelmintic: Carpaine alkaloid and latex enzymes exhibit lethal activity against intestinal parasites and pinworms",
            "Topical wound debridement: Clears necrotic tissue and purulent discharge in chronic sloughy ulcers",
            "Hepatoprotective and antioxidant support during systemic viral infections"
        ],
        "traditionally_used_parts": [
            {"part": "Leaves (Folia)", "indication": "Dengue fever, low platelet count, malaria, digestive sluggishness"},
            {"part": "Unripe Fruit Latex", "indication": "Meat tenderizer, digestive enzyme, topical ringworm and wart treatment"},
            {"part": "Seeds (Semina)", "indication": "Intestinal parasites, anthelmintic, liver detoxifier"},
            {"part": "Ripe Fruit", "indication": "Constipation, digestive debility, vitamin A & C supplementation"}
        ],
        "preparation_information": [
            {"method": "Fresh Leaf Juice (Dengue Protocol)", "details": "Fresh disease-free mature leaves thoroughly washed; thick fibrous central veins removed; blades crushed in a mortar without water and juice squeezed through sterile gauze."},
            {"method": "Standardized Commercial Tablet / Syrup", "details": "Standardized aqueous leaf extract formulation (e.g., Caripill) clinically validated for dengue thrombocytopenia."},
            {"method": "Crushed Seed Paste", "details": "Dried seeds ground and taken with honey for intestinal worms."}
        ],
        "dosage_information": [
            {
                "source": "ICMR Clinical Trial Recommendations (Dengue)",
                "preparation": "Fresh Expressed Leaf Juice",
                "dose": "Adults: 25 to 30 ml twice daily for 5 consecutive days; Children (6-12 yrs): 5 to 10 ml twice daily"
            },
            {
                "source": "Clinical Reference Guidelines (Standardized Extract)",
                "preparation": "Standardized Leaf Extract Tablet (1100 mg)",
                "dose": "One tablet 3 times daily for 5 days"
            },
            {
                "source": "Ayurvedic Pharmacopoeia of India (API)",
                "preparation": "Leaf Infusion",
                "dose": "50 to 100 ml daily"
            }
        ],
        "precautions_warnings": [
            "Severe Taste Bitterness: Fresh leaf juice is intensely bitter and can cause nausea in sensitive individuals; follow with a spoonful of honey or jaggery.",
            "Pregnancy: Unripe papaya and unripe fruit latex contain high concentrations of latex enzymes that trigger uterine contractions and miscarriage. Fully ripe fruit is safe, but medicinal leaf extract is contraindicated in pregnancy.",
            "Latex Allergy: Cross-reactivity in individuals with latex-fruit syndrome (banana, avocado, latex allergy)."
        ],
        "contraindications_interactions": [
            "Absolute Contraindication: Pregnancy (risk of uterine contraction from latex components), latex allergy.",
            "Drug Interactions: Anticoagulants (Warfarin) - may increase INR and bleeding risk; Oral antidiabetics - potential additive hypoglycemia."
        ],
        "active_phytochemicals": [
            "Carpaine and Pseudocarpaine (piperidine alkaloids)",
            "Papain and Chymopapain (endopeptidases)",
            "Flavonoids (Quercetin, Kaempferol, Myricetin)",
            "Glucosinolates (Benzyl isothiocyanate)",
            "Ascorbic acid, tocopherols, and beta-carotene"
        ],
        "botanical_morphology": "Fast-growing single-stemmed giant arborescent herb 3-10 m; leaves spirally clustered at apex, large, 50-70 cm across, deeply palmate-lobed with 7-9 segments, lobes pinnatifid, petioles hollow and 50-100 cm long.",
        "native_region": "Native to tropical Americas; cultivated ubiquitously across tropical and subtropical regions.",
        "iucn_conservation_status": "Least Concern"
    }
}

# Helper lookup functions
def get_plant_by_id(plant_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve full monograph for a given species ID."""
    return PLANT_DATABASE.get(plant_id)

def get_all_species() -> List[Dict[str, Any]]:
    """Return a list of all plant monographs in the database."""
    return list(PLANT_DATABASE.values())

def search_plants(query: str) -> List[Dict[str, Any]]:
    """Search database by common name, scientific name, indication, or family."""
    query = query.lower().strip()
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
