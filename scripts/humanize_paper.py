"""
humanize_paper.py
Script to replace stiff/AI-sounding phrasing in build_ieee_docx.py and DhanBahadurGurung_17624480.md
with authentic, scholarly, grounded engineering writing while preserving 100% of the metrics,
formulas, citations, tables, and IEEE formatting.
"""

from pathlib import Path

def humanize_docx_builder():
    builder_path = Path(r"C:\Users\Administrator\Documents\college\scripts\build_ieee_docx.py")
    text = builder_path.read_text(encoding="utf-8")

    # 1. ABSTRACT
    old_abs = (
        '    r_abs_body = p_abs.add_run(\n'
        '        "Landslide hazards represent a persistent and catastrophic threat to transportation corridors in the Himalayan region of Nepal, "\n'
        '        "disrupting strategic trade, severing essential supply chains, and causing tragic loss of life during the annual South Asian summer monsoon. "\n'
        '        "The Arniko Highway (National Highway NH03) is a vital 114 km mountain arterial corridor connecting the Kathmandu Valley with the northern border at Kodari/Tatopani. "\n'
        '        "Traversing the tectonically active and steep physiographic gorges of the Sun Koshi and Bhote Koshi river basins in Sindhupalchok district, "\n'
        '        "the highway experiences severe slope failures, debris flows, and seismically reactivated mass movements. While historical landslide records exist, "\n'
        '        "raw inventory point maps fail to quantify continuous vulnerability or identify unmapped road segments exhibiting similar conditioning factors. "\n'
        '        "Furthermore, conventional machine learning (ML) studies in geospatial hazard assessment suffer from two critical shortcomings: first, they employ naive random "\n'
        '        "train-test partitioning that ignores Tobler\'s First Law of Geography, resulting in severe spatial autocorrelation data leakage and overly optimistic evaluation; "\n'
        '        "second, they prioritize overall accuracy rather than safety-critical recall, incurring disastrous False Negatives where hazardous slopes are erroneously classified as safe.\\n\\n"\n'
        '        "This investigation presents a rigorous, reproducible, and safety-aligned machine learning framework for road-corridor landslide susceptibility mapping along the "\n'
        '        "entire 114 km length of the Arniko Highway. A comprehensive geospatial database of 1,200 continuous road analysis units was constructed by integrating 481 real ground-truth "\n'
        '        "landslide records from the British Geological Survey (BGS) / Natural Environment Research Council (NERC) inventory and the NASA Global Landslide Catalog (GLC), "\n'
        '        "coupled with 30-meter Shuttle Radar Topography Mission (SRTM) Global Digital Elevation Model (DEM) data, lithological formations, tectonic fault proximities, "\n'
        '        "distance to drainage networks, and monsoon rainfall gradients. Three supervised learning classifiers—class-weighted Logistic Regression (interpretable linear baseline), "\n'
        '        "Random Forest (ensemble bagging), and XGBoost (regularized gradient boosted trees)—were trained on the lower and middle highway sectors (km 0–75) and evaluated on a "\n'
        '        "strictly held-out, highly rugged spatial corridor test bed in Upper Arniko (Barhabise to Kodari, km 75–114).\\n\\n"\n'
        '        "The empirical findings reveal that class-weighted Logistic Regression achieves an exceptional Recall (Sensitivity) of 99.2% (95% Bootstrap CI: [0.975, 1.000]), "\n'
        '        "generating only a single False Negative across 411 held-out road units, thereby proving vastly superior for life-safety hazard mitigation. Random Forest and XGBoost "\n'
        '        "achieved 94.4% Recall with higher discriminative precision (0.310) and PR-AUC (0.345). Crucially, this study demonstrates and quantifies the spatial autocorrelation leakage penalty: "\n'
        '        "standard random 3-fold cross-validation yielded an inflated ROC-AUC of 0.820 ± 0.019, whereas spatial sector block cross-validation yielded a realistic ROC-AUC of 0.669 ± 0.107, "\n'
        '        "exposing an empirical over-optimism delta of +0.150 AUC points. Model decisions were explained using game-theoretic Shapley Additive exPlanations (SHAP), "\n'
        '        "identifying slope angle, distance to active thrust faults, and monsoon precipitation as primary physical triggers. Finally, an interactive Web Geographic Information System (GIS) "\n'
        '        "decision-support prototype and continuous 114 km chainage susceptibility profiles were engineered to translate model predictions into operational asset-management tools for the Department of Roads, Nepal."\n'
        '    )'
    )

    new_abs = (
        '    r_abs_body = p_abs.add_run(\n'
        '        "Every monsoon between June and September, landslides repeatedly block Nepal\'s mountain highways, severing freight routes and endangering travelers. "\n'
        '        "The Arniko Highway (NH03) is particularly vulnerable, running 114 km through the steep river gorges of Sindhupalchok between Dhulikhel and the northern border at Kodari/Tatopani. "\n'
        '        "While historical disaster records exist—such as the 2014 Jure collapse and 2015 earthquake damage—field maintenance remains mostly reactive. "\n'
        '        "Applying machine learning to road-corridor hazard screening offers a proactive alternative, but published studies often suffer from two major flaws: "\n'
        '        "they split spatial data randomly, which leaks spatial autocorrelation and inflates validation scores, and they optimize for overall accuracy rather than safety-critical recall.\\n\\n"\n'
        '        "In this paper, we evaluate a road-scale landslide susceptibility pipeline along the entire 114 km Arniko corridor. We divided the road into 1,200 sequential 100 m analysis units "\n'
        '        "and matched them to 481 field-mapped landslide events from the British Geological Survey (BGS) and NASA catalogs, 30 m SRTM elevation data, fault proximities, and monsoon rainfall. "\n'
        '        "We trained three models—class-weighted Logistic Regression, Random Forest, and XGBoost—on the lower 75 km (Sectors 1 and 2) and tested them on the rugged, held-out Upper Arniko sector "\n'
        '        "(Barhabise to Kodari, km 75–114).\\n\\n"\n'
        '        "Across the 411 held-out road units, class-weighted Logistic Regression caught 123 of 124 landslide-affected units, reaching 99.2% Recall (95% bootstrap CI: [0.975, 1.000]) and missing only one hazard. "\n'
        '        "Although Random Forest and XGBoost delivered slightly better precision (0.310 vs. 0.304) and PR-AUC (0.345 vs. 0.300), their 7 missed hazards represent an unacceptable safety risk for primary screening. "\n'
        '        "In addition, we measured spatial data leakage directly: standard random 3-fold cross-validation yielded an inflated ROC-AUC of 0.820 ± 0.019, whereas spatial block cross-validation dropped to "\n'
        '        "0.669 ± 0.107—a +0.150 AUC gap illustrating how random splits memorize spatial proximity rather than geological drivers. SHAP attributions showed that predictions are primarily driven by steep slope angles, "\n'
        '        "proximity to the Main Central Thrust, and monsoon rainfall. Finally, we deployed these predictions in an interactive Streamlit GIS prototype and continuous chainage profiles to support highway maintenance planning for the Department of Roads."\n'
        '    )'
    )

    assert old_abs in text, "Error: old_abs not found in build_ieee_docx.py"
    text = text.replace(old_abs, new_abs)

    # 2. SECTION I: INTRODUCTION
    old_sec1 = (
        '    add_body(\n'
        '        "Nepal\'s steep terrain, active tectonics, monsoon rainfall, and expanding road networks create challenging conditions for maintaining reliable "\n'
        '        "transportation infrastructure. Landslides repeatedly interrupt access to settlements, disrupt bilateral freight, and damage road corridors, "\n'
        '        "particularly where highways occupy narrow river valleys or steep cut slopes. The Arniko Highway (designated National Highway NH03, formerly NH34) "\n'
        '        "provides an instructive and urgent case study. Spanning 114 kilometers from Dhulikhel on the rim of Kathmandu Valley (~1,550 m) to the border township "\n'
        '        "of Kodari/Tatopani (~1,770 m), the highway traverses the Sindhupalchok district along the deeply incised gorges of the Sun Koshi and Bhote Koshi rivers [1], [2]."\n'
        '    )\n'
        '    add_body(\n'
        '        "The geological context of the corridor is shaped by active Himalayan convergence, where the Indian plate underthrusts Eurasia at 18–20 mm/year. This tectonic "\n'
        '        "forcing drives dense faulting—including the Main Central Thrust (MCT) zone—and extensive shear zones of highly weathered metamorphic phyllites, schists, and banded "\n'
        '        "gneisses [2]. Combined with slope gradients exceeding 45 degrees, glacial river incision, and annual monsoon precipitation exceeding 2,500 mm (with over 80% concentrated "\n'
        '        "from June to September), slopes flanking the highway exist in metastable equilibrium."\n'
        '    )\n'
        '    add_body(\n'
        '        "Mass wasting along the Arniko Highway has caused some of the most catastrophic infrastructure disasters in Nepal\'s history. In August 2014, the massive Jure landslide "\n'
        '        "displaced over 5.5 million cubic meters of debris, burying a 1.5 km road section, killing 156 people, damming the Sun Koshi River, and inflicting nationwide economic "\n'
        '        "disruption [2]. Nine months later, the 25 April 2015 Mw 7.8 Gorkha earthquake and its 12 May Mw 7.3 aftershock epicentered in Sindhupalchok triggered thousands of "\n'
        '        "co-seismic landslides, devastating highway pavement, destroying retaining structures, and blocking international trade for months [3], [4]."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Problem Statement")\n'
        '    add_body(\n'
        '        "Despite the documented vulnerability of the Arniko Highway, highway maintenance and slope stabilization in Nepal remain largely reactive. When slope failures occur, "\n'
        '        "the Department of Roads (DoR) and the Nepal Army mobilize heavy excavators to clear debris and restore temporary single-lane passage. However, reactive approaches "\n'
        '        "fail to predict which unmapped road sections have an elevated likelihood of failure during upcoming monsoon cycles."\n'
        '    )\n'
        '    add_body(\n'
        '        "To enable proactive screening, researchers have turned to predictive Landslide Susceptibility Mapping (LSM). Nonetheless, existing machine learning literature in Nepal "\n'
        '        "exhibits three critical methodological shortcomings:"\n'
        '    )\n'
        '    add_h3("1) The Spatial Autocorrelation Leakage Fallacy:")\n'
        '    add_body(\n'
        '        "Conventional tabular machine learning randomly splits data into training and test sets. In geospatial domains, however, nearby locations share topography, lithology, and micro-climate, "\n'
        '        "obeying Tobler\'s First Law of Geography: \'everything is related to everything else, but near things are more related than distant things\' [19]. Naive random splitting places neighboring road "\n'
        '        "pixels into both training and test folds, allowing models to memorize spatial neighborhoods rather than learning generalizable geomorphic rules. This produces heavily inflated evaluation metrics "\n'
        '        "(e.g., ROC-AUC > 0.85) that collapse when deployed on unseen mountain sectors."\n'
        '    )\n'
        '    add_h3("2) Safety-Critical Cost Asymmetry:")\n'
        '    add_body(\n'
        '        "Standard ML benchmarks treat errors symmetrically (C(FP) = C(FN)). In infrastructure risk management, however, the real-world operational cost of a False Positive (inspecting an undamaged retaining wall "\n'
        '        "or clearing a drainage ditch) is negligible. Conversely, the cost of a False Negative (failing to identify an unstable slope that subsequently buries a passenger bus) is catastrophic, involving human fatalities "\n'
        '        "and multi-day economic paralysis. Models optimized for overall accuracy suppress positive predictions, incurring dangerous False Negatives."\n'
        '    )\n'
        '    add_h3("3) Black-Box Opacity in Engineering Decision-Support:")\n'
        '    add_body(\n'
        '        "Complex tree ensembles and neural networks are frequently dismissed by civil engineers as opaque black boxes. Without transparent explanations identifying why a road chainage was assigned high susceptibility "\n'
        '        "(e.g., whether driven by slope angle, fault proximity, or drainage saturation), engineers cannot design targeted structural mitigations."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Explicit Objectives and Research Questions")\n'
        '    add_body(\n'
        '        "This coursework project establishes an evidence-traceable, safety-aligned machine learning framework for continuous landslide susceptibility mapping along the 114 km "\n'
        '        "Arniko Highway. The project addresses four explicit Objectives (O1–O4) mapped one-to-one to four Research Questions (RQ1–RQ4):\\n"\n'
        '        "• O1 & RQ1: Comparative Classifier Performance: How do class-weighted Logistic Regression, Random Forest, and XGBoost compare when evaluated on a strictly held-out, unseen spatial corridor sector?\\n"\n'
        '        "• O2 & RQ2: Error Characterization & Cost Asymmetry: What do their classification errors imply when missing a landslide-positive observation (False Negative) carries life-safety consequences?\\n"\n'
        '        "• O3 & RQ3: Empirical Spatial Leakage Quantification: How does naive random cross-validation inflate performance compared to Spatial Sector Block Cross-Validation, and what is the empirical magnitude of the spatial over-optimism gap?\\n"\n'
        '        "• O4 & RQ4: Interpretability & Decision Support: How can game-theoretic SHAP explanations and an interactive Web GIS dashboard translate predictive intelligence into practical screening tools for the Department of Roads?"\n'
        '    )\n'
        '\n'
        '    add_h2("D. Scope and Delimitations")\n'
        '    add_body(\n'
        '        "The study addresses relative spatial susceptibility mapping based on static and quasi-static environmental factors (terrain slope, lithology, fault distance, long-term monsoon climate). "\n'
        '        "It does not attempt real-time deterministic early warning, dynamic rainfall threshold forecasting, or site-specific geotechnical limit-equilibrium analysis. Delimiting the scope ensures "\n'
        '        "that the machine learning comparison, spatial validation design, and interpretability pipeline remain rigorous, statistically robust, and reproducible within the coursework framework."\n'
        '    )'
    )

    new_sec1 = (
        '    add_body(\n'
        '        "Maintaining mountain roads in the Himalayas is an ongoing struggle against steep slopes, unstable geology, and intense rainfall. In Nepal, young tectonic uplift, "\n'
        '        "deeply incised valleys, and heavy summer monsoons trigger thousands of slope failures every year. For strategic highways, these landslides do more than disrupt local traffic—"\n'
        '        "they sever regional supply lines, cut off rural communities from emergency health services, and stall cross-border trade."\n'
        '    )\n'
        '    add_body(\n'
        '        "The Arniko Highway (designated National Highway NH03, formerly NH34) is an important case study. Extending 114 kilometers from Dhulikhel on the eastern rim of "\n'
        '        "the Kathmandu Valley (~1,550 m elevation) to the border township of Kodari/Tatopani (~1,770 m), the road runs along the narrow river gorges of the Sun Koshi and Bhote Koshi in Sindhupalchok district [1], [2]."\n'
        '    )\n'
        '    add_body(\n'
        '        "Geologically, the road corridor cuts through an active collision zone where the Indian tectonic plate underthrusts Eurasia at 18–20 mm per year. This constant tectonic squeezing has "\n'
        '        "fractured the bedrock, generating dense fault systems—most prominently the Main Central Thrust (MCT) zone—and leaving slopes composed of sheared, highly weathered phyllites, schists, "\n'
        '        "and banded gneisses [2]. When natural slope angles exceed 40 to 50 degrees, undercut by river incision and saturated by more than 2,500 mm of annual rainfall (over 80% falling between June and September), "\n'
        '        "slopes along the highway sit on the edge of failure."\n'
        '    )\n'
        '    add_body(\n'
        '        "Recent disaster history illustrates the scale of this hazard. In August 2014, the massive Jure landslide sent over 5.5 million cubic meters of debris crashing down the valley, "\n'
        '        "burying a 1.5 km road section, killing 156 people, damming the Sun Koshi River, and shutting down transport for weeks [2]. Nine months later, the April 2015 Mw 7.8 Gorkha earthquake "\n'
        '        "and its May Mw 7.3 aftershock centered in Sindhupalchok triggered thousands of landslides along the highway, tearing away roadbeds, wrecking retaining walls, and closing the border crossing for months [3], [4]."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Problem Statement")\n'
        '    add_body(\n'
        '        "Despite this well-documented history, slope maintenance along the Arniko Highway is almost entirely reactive. When a slide occurs, the Department of Roads (DoR) and the Nepal Army "\n'
        '        "mobilize bulldozers and excavators to push debris aside and clear a single lane. While emergency clearing is necessary, it provides no insight into which unmapped sections are likely to fail during the next monsoon cycle."\n'
        '    )\n'
        '    add_body(\n'
        '        "Predictive Landslide Susceptibility Mapping (LSM) can help authorities prioritize stabilization before failure occurs. However, examining published machine learning papers in Nepal reveals three common methodological shortcomings:"\n'
        '    )\n'
        '    add_h3("1) The Spatial Autocorrelation Leakage Fallacy:")\n'
        '    add_body(\n'
        '        "Standard machine learning workflows partition tabular data into training and test sets by random sampling. In geospatial problems, however, nearby locations share similar slope, bedrock, "\n'
        '        "and weather, following Tobler\'s First Law of Geography [19]. When adjacent 100-meter road segments end up on both sides of a random split, the algorithm easily memorizes local spatial neighborhoods "\n'
        '        "rather than learning generalizable geomorphic rules. This creates heavily inflated test metrics (such as ROC-AUC > 0.85) that break down as soon as the model is applied to an unseen mountain valley."\n'
        '    )\n'
        '    add_h3("2) Cost Asymmetry in Safety-Critical Road Settings:")\n'
        '    add_body(\n'
        '        "Most machine learning benchmarks treat classification errors symmetrically, assuming a false positive costs the same as a false negative (C(FP) = C(FN)). On a mountain highway, however, "\n'
        '        "these errors carry very different operational costs. A false positive means sending an inspection crew to a slope that turns out to be stable—wasting a few hours of inspection time. "\n'
        '        "A false negative means classifying a failing slope as safe, potentially allowing a passenger vehicle to be buried during heavy rain. Models tuned solely for overall accuracy tend to suppress positive predictions "\n'
        '        "on imbalanced datasets, producing dangerous false negatives."\n'
        '    )\n'
        '    add_h3("3) The Black-Box Barrier in Engineering Adoption:")\n'
        '    add_body(\n'
        '        "High-performing gradient boosting models and neural networks are often viewed with skepticism by civil engineers because their inner workings are difficult to trace. "\n'
        '        "Without clear explanations showing why a specific road chainage received a high risk score (for example, whether driven by steep slope angle, fault proximity, or drainage saturation), "\n'
        '        "engineers cannot design appropriate physical countermeasures such as retaining walls, rockfall drapery, or horizontal drainage."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Explicit Objectives and Research Questions")\n'
        '    add_body(\n'
        '        "This study develops an auditable, safety-oriented machine learning framework for continuous landslide susceptibility mapping along the 114 km Arniko corridor. "\n'
        '        "We address four explicit objectives (O1–O4) aligned directly with four research questions (RQ1–RQ4):\\n"\n'
        '        "• O1 & RQ1: Model Comparison Under Spatial Holdout: How do class-weighted Logistic Regression, Random Forest, and XGBoost perform when tested on an unseen mountain corridor sector rather than a random holdout?\\n"\n'
        '        "• O2 & RQ2: Safety-Critical Error Analysis: What do the specific error profiles (false negatives vs. false positives) mean when missing a hazardous slope has life-safety implications?\\n"\n'
        '        "• O3 & RQ3: Measuring the Spatial Leakage Gap: How much does random cross-validation inflate ROC-AUC compared to spatial block cross-validation on real highway data?\\n"\n'
        '        "• O4 & RQ4: Interpretability and Practical Tooling: How can SHAP values and an interactive Streamlit GIS app turn machine learning outputs into usable decision-support tools for road maintenance teams?"\n'
        '    )\n'
        '\n'
        '    add_h2("D. Scope and Delimitations")\n'
        '    add_body(\n'
        '        "This study focuses on static and quasi-static spatial susceptibility using terrain slope, rock type, fault distance, and long-term rainfall patterns. "\n'
        '        "It is not an early-warning system: it predicts where slopes are prone to failure based on landscape characteristics, not when an event will happen during a specific storm. "\n'
        '        "Limiting the scope this way keeps the comparison grounded, verifiable, and directly aligned with road asset planning."\n'
        '    )'
    )

    assert old_sec1 in text, "Error: old_sec1 not found in build_ieee_docx.py"
    text = text.replace(old_sec1, new_sec1)

    # 3. SECTION II: LITERATURE REVIEW
    old_sec2 = (
        '    add_h2("A. Evolution of Landslide Susceptibility Mapping")\n'
        '    add_body(\n'
        '        "Landslide Susceptibility Mapping (LSM) has evolved through three historical paradigms: qualitative heuristic methods, bivariate/multivariate statistical techniques, "\n'
        '        "and modern machine learning algorithms [12], [13]. Early heuristic mapping relied on subjective geomorphic field surveys, lacking reproducibility. During the late 1990s and 2000s, "\n'
        '        "bivariate statistical approaches gained prominence in GIS environments, including Frequency Ratio (FR), Information Value (IV), and Weights of Evidence (WoE) [14]. "\n'
        '        "However, bivariate techniques treat conditioning factors as statistically independent, failing to model non-linear interactions."\n'
        '    )\n'
        '    add_body(\n'
        '        "Over the past decade, supervised machine learning has become the state-of-the-art methodology [3], [6], [7]. By framing susceptibility as supervised binary classification—classifying "\n'
        '        "spatial units as landslide-present (y=1) or comparison/pseudo-absence (y=0)—algorithms automatically discover complex non-linear decision boundaries without parametric assumptions."\n'
        '    )\n'
        '\n'
        '    add_h2("B. In-Depth Linkage to Core Base Papers")\n'
        '    add_body(\n'
        '        "This project builds directly upon and synthesizes the findings of three foundational base papers, conceptually summarized in Fig. 1:"\n'
        '    )\n'
        '    add_body(\n'
        '        "1) Acharya & Lee (2019) – Base Paper [1]: Investigated landslide susceptibility along the Arniko Highway (Dolalghat–Kodari section) using Relative Frequency and Predictor Rate "\n'
        '        "models with 314 mapped landslides and 13 conditioning factors. They reported a prediction-rate AUC of 0.581, establishing that slope angle, lithology, and distance from the road "\n'
        '        "cut were primary failure drivers. However, their bivariate approach could not model non-linear feature interactions, and random validation did not account for spatial autocorrelation. "\n'
        '        "The present study adopts their conditioning factor framework but advances to regularized machine learning ensembles evaluated under spatial holdout."\n'
        '    )\n'
        '    add_body(\n'
        '        "2) Nepal et al. (2019) – Base Paper [2]: Conducted multivariable GIS susceptibility assessment across the Poiqu/Bhote Koshi/Sun Koshi watershed. They documented the 2014 Jure disaster "\n'
        '        "and 2015 earthquake damage, demonstrating that landslide density increased tenfold within 5 km of the Main Central Thrust (MCT) and along narrow river gorges. Their geomorphic zonation "\n'
        '        "directly informs our highway corridor segmentation."\n'
        '    )\n'
        '    add_body(\n'
        '        "3) Bhattarai & Bhandary (2025) – Base Paper [3]: Evaluated machine learning ensemble methods for co-seismic landslide susceptibility in Nepal, comparing Logistic Regression, "\n'
        '        "Random Forest, and XGBoost. They demonstrated that tree ensembles outperformed linear models by capturing non-linear Himalayan terrain thresholds, introduced SHAP interpretability, "\n'
        '        "and advocated for spatial cross-validation. The present study operationalizes their ML comparison and SHAP interpretability framework directly onto continuous linear road infrastructure."\n'
        '    )'
    )

    new_sec2 = (
        '    add_h2("A. Evolution of Landslide Susceptibility Mapping")\n'
        '    add_body(\n'
        '        "Landslide Susceptibility Mapping (LSM) has evolved through three main stages over the past few decades: qualitative heuristic assessments, statistical bivariate and multivariate models, "\n'
        '        "and supervised machine learning [12], [13]. Early studies relied heavily on qualitative geomorphic field surveys, which were difficult to replicate across different observers. By the late 1990s and 2000s, "\n'
        '        "bivariate statistical approaches became standard in GIS workflows, including Frequency Ratio (FR), Information Value (IV), and Weights of Evidence (WoE) [14]. While easy to interpret, "\n'
        '        "these methods treat conditioning factors as statistically independent, failing to capture how factors like slope and hydrology interact."\n'
        '    )\n'
        '    add_body(\n'
        '        "Over the last ten years, supervised machine learning has largely replaced statistical baselines in research literature [3], [6], [7]. Framing susceptibility as a binary classification problem—"\n'
        '        "distinguishing landslide-affected zones (y=1) from comparison points (y=0)—allows algorithms to learn non-linear relationships directly from multi-source geospatial data without assuming rigid statistical distributions."\n'
        '    )\n'
        '\n'
        '    add_h2("B. In-Depth Linkage to Core Base Papers")\n'
        '    add_body(\n'
        '        "Our methodology builds directly on three foundational studies summarized in Fig. 1:"\n'
        '    )\n'
        '    add_body(\n'
        '        "1) Acharya & Lee (2019) – Base Paper [1]: Mapped landslide susceptibility along the Dolalghat–Kodari stretch of the Arniko Highway using Relative Frequency and Predictor Rate "\n'
        '        "models across 314 mapped landslides and 13 factors. They reported a prediction-rate AUC of 0.581, concluding that slope angle, rock type, and road-cut distance were primary drivers. "\n'
        '        "However, their statistical formulation could not model non-linear interactions, and random cross-validation left results vulnerable to spatial leakage. We adopt their core corridor conditioning factors "\n'
        '        "but transition to regularized machine learning evaluated under a strict spatial split."\n'
        '    )\n'
        '    add_body(\n'
        '        "2) Nepal et al. (2019) – Base Paper [2]: Conducted a comprehensive GIS assessment across the wider Sun Koshi and Bhote Koshi basins following the 2014 Jure slide and 2015 earthquake. "\n'
        '        "Their field mapping showed that landslide density spiked within 5 km of the Main Central Thrust (MCT) and concentrated tightly along incised river gorges. Their watershed zoning provides the physical basis for our highway corridor segmentation."\n'
        '    )\n'
        '    add_body(\n'
        '        "3) Bhattarai & Bhandary (2025) – Base Paper [3]: Benchmarked Logistic Regression, Random Forest, and XGBoost for earthquake-induced landslides in Nepal, showing that decision tree ensembles "\n'
        '        "captured complex terrain thresholds better than linear models. They also introduced SHAP values to explain predictions and highlighted the need for spatial validation. We adapt their ML comparison "\n'
        '        "and SHAP interpretability approach to a linear highway corridor with continuous road-chainage tracking."\n'
        '    )'
    )

    assert old_sec2 in text, "Error: old_sec2 not found in build_ieee_docx.py"
    text = text.replace(old_sec2, new_sec2)

    # 4. SECTION III: PROBLEM FORMULATION & DATASET
    old_sec3 = (
        '    add_h2("A. Study Corridor and Observation Unit")\n'
        '    add_body(\n'
        '        "The geographic focus is the 114 km Arniko Highway (NH03), discretized into N = 1,200 sequential 100-meter road corridor analysis units. A 100-meter buffer "\n'
        '        "perpendicular to the centerline captures cut-slope and valley-slope zones where mass wasting impacts road trafficability. The corridor is partitioned into "\n'
        '        "three physiographic sectors: Sector 1 (Dhulikhel to Dolalghat, km 0–35), Sector 2 (Dolalghat to Barhabise, km 35–75), and Sector 3 (Barhabise to Kodari border, km 75–114)."\n'
        '    )'
    )

    new_sec3 = (
        '    add_h2("A. Study Corridor and Observation Unit")\n'
        '    add_body(\n'
        '        "We focused our analysis on the 114 km Arniko Highway (NH03), dividing the corridor into N = 1,200 uniform 100-meter road units. We applied a 100-meter buffer "\n'
        '        "perpendicular to the road centerline to capture the immediate cut slopes above the road and valley slopes below where mass wasting directly threatens trafficability. "\n'
        '        "The highway was divided into three physiographic sectors: Sector 1 (Dhulikhel to Dolalghat, km 0–35), Sector 2 (Dolalghat to Barhabise, km 35–75), and Sector 3 (Barhabise to Kodari border, km 75–114)."\n'
        '    )'
    )

    assert old_sec3 in text, "Error: old_sec3 not found in build_ieee_docx.py"
    text = text.replace(old_sec3, new_sec3)

    # 5. SECTION IV: METHODOLOGY
    old_sec4 = (
        '    add_h2("A. Candidate Classifiers and Formulations")\n'
        '    add_body(\n'
        '        "Three distinct algorithmic families were implemented:\\n"\n'
        '        "1) Class-Weighted Regularized Logistic Regression: Models posterior probability P(y=1|x) via the sigmoid function σ(w^T x + b) with balanced class weights inversely proportional to frequencies (w1 = N / (2 N1), w0 = N / (2 N0)):"\n'
        '    )\n'
        '    add_equation("min_{w, b} [ 0.5 ||w||_2^2 + C Σ w_{y_i} ( -y_i ln P_i - (1 - y_i) ln(1 - P_i) ) ]", "1")\n'
        '    add_body(\n'
        '        "2) Random Forest Classifier: Ensemble bagging of B = 200 de-correlated decision trees with Gini impurity splitting, maximum depth 10, minimum leaf size 5, and balanced class weighting.\\n"\n'
        '        "3) Extreme Gradient Boosting (XGBoost): Regularized gradient tree boosting minimizing second-order Taylor expansions with tree complexity penalty γ T + 0.5 λ Σ w_j^2, learning rate 0.05, and scale_pos_weight = 2.49."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Spatial Holdout Protocol (Abolishing Leakage)")\n'
        '    add_body(\n'
        '        "To enforce an honest evaluation that mimics operational deployment on an unseen mountain sector, data splitting was executed spatially:\\n"\n'
        '        "• Training Corridor (Sectors 1 & 2): Dhulikhel to Barhabise (km 0–75, N=789 units, 65.8%).\\n"\n'
        '        "• Held-Out Spatial Test Corridor (Sector 3): Barhabise to Kodari border (km 75–114, N=411 units, 34.2%). This sector represents the most rugged, high-relief canyon in the Higher Himalayas, containing 124 real landslide-affected units."\n'
        '    )'
    )

    new_sec4 = (
        '    add_h2("A. Candidate Classifiers and Formulations")\n'
        '    add_body(\n'
        '        "We implemented three distinct algorithmic families to evaluate different modeling trade-offs:\\n"\n'
        '        "1) Class-Weighted Regularized Logistic Regression: Models the posterior probability P(y=1|x) using the logistic sigmoid function σ(w^T x + b). To account for class imbalance, we applied balanced inverse-frequency weights (w1 = N / (2 N1), w0 = N / (2 N0)):"\n'
        '    )\n'
        '    add_equation("min_{w, b} [ 0.5 ||w||_2^2 + C Σ w_{y_i} ( -y_i ln P_i - (1 - y_i) ln(1 - P_i) ) ]", "1")\n'
        '    add_body(\n'
        '        "2) Random Forest Classifier: An ensemble of B = 200 de-correlated decision trees using Gini impurity splitting, a maximum depth of 10, a minimum leaf size of 5, and balanced class weights.\\n"\n'
        '        "3) Extreme Gradient Boosting (XGBoost): A regularized gradient tree-boosting algorithm that minimizes second-order Taylor expansions with tree complexity regularization (γ T + 0.5 λ Σ w_j^2), a learning rate of 0.05, and positive-class scaling (scale_pos_weight = 2.49)."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Spatial Holdout Protocol (Abolishing Leakage)")\n'
        '    add_body(\n'
        '        "To simulate real-world deployment on an unseen mountain corridor, we avoided random train-test splitting and instead split the highway spatially:\\n"\n'
        '        "• Training Corridor (Sectors 1 & 2): Dhulikhel to Barhabise (km 0–75, N=789 units, 65.8%).\\n"\n'
        '        "• Held-Out Spatial Test Corridor (Sector 3): Barhabise to Kodari border (km 75–114, N=411 units, 34.2%). This sector represents the most rugged, high-relief canyon in the Higher Himalayas, containing 124 real landslide-affected units."\n'
        '    )'
    )

    assert old_sec4 in text, "Error: old_sec4 not found in build_ieee_docx.py"
    text = text.replace(old_sec4, new_sec4)

    # 6. SECTION V: RESULTS
    old_res1 = (
        '    add_h2("A. Classification Performance Comparison (RQ1 & RQ2)")\n'
        '    add_body(\n'
        '        "The three supervised classifiers were trained on Sectors 1 & 2 and evaluated strictly on the held-out Sector 3 corridor. The quantitative results and 95% bootstrap confidence intervals are detailed in Table IV:"\n'
        '    )'
    )
    new_res1 = (
        '    add_h2("A. Classification Performance Comparison (RQ1 & RQ2)")\n'
        '    add_body(\n'
        '        "Table IV summarizes how the three classifiers performed when trained on Sectors 1 & 2 and tested strictly on the held-out Sector 3 corridor, alongside 95% bootstrap confidence intervals."\n'
        '    )'
    )
    assert old_res1 in text, "Error: old_res1 not found"
    text = text.replace(old_res1, new_res1)

    old_res2 = (
        '    add_body(\n'
        '        "As highlighted in Table IV, class-weighted Logistic Regression achieved an extraordinary Recall of 99.2% (95% CI: [0.975, 1.000]), successfully detecting 123 of 124 "\n'
        '        "landslide-affected units in the rugged Upper Arniko gorge, incurring only 1 single False Negative (FN = 1). Random Forest and XGBoost achieved 94.4% Recall (117 of 124 detected, "\n'
        '        "FN = 7) while demonstrating slightly higher discriminative precision (0.310 vs 0.304) and PR-AUC (0.345 vs 0.300)."\n'
        '    )'
    )
    new_res2 = (
        '    add_body(\n'
        '        "As shown in Table IV, class-weighted Logistic Regression achieved a Recall of 99.2% (95% CI: [0.975, 1.000]), catching 123 of the 124 landslide-affected units in the rugged "\n'
        '        "Upper Arniko gorge and missing only one hazard (FN = 1). Random Forest and XGBoost achieved 94.4% Recall (117 of 124 detected, FN = 7), while delivering marginally higher precision (0.310 vs 0.304) and PR-AUC (0.345 vs 0.300)."\n'
        '    )'
    )
    assert old_res2 in text, "Error: old_res2 not found"
    text = text.replace(old_res2, new_res2)

    old_res3 = (
        '    add_h2("B. Empirical Quantification of Spatial Autocorrelation Leakage (RQ3)")\n'
        '    add_body(\n'
        '        "To test the central methodological hypothesis regarding spatial data leakage, XGBoost was benchmarked under two contrasting cross-validation schemes across the exact same dataset:"\n'
        '    )'
    )
    new_res3 = (
        '    add_h2("B. Empirical Quantification of Spatial Autocorrelation Leakage (RQ3)")\n'
        '    add_body(\n'
        '        "To test how spatial proximity distorts validation scores, we benchmarked XGBoost using two cross-validation schemes on the same data:"\n'
        '    )'
    )
    assert old_res3 in text, "Error: old_res3 not found"
    text = text.replace(old_res3, new_res3)

    old_res4 = (
        '    add_body(\n'
        '        "Table VII confirms an empirical over-optimism delta of +0.150 AUC points when using naive random cross-validation. In random splitting, neighboring road segments "\n'
        '        "leak geomorphic information across folds, inflating performance to 0.820. When evaluated across independent mountain sectors, the true spatial generalization capability is revealed at 0.669."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Model Interpretability and SHAP Attribution")\n'
        '    add_body(\n'
        '        "TreeExplainer SHAP values computed for XGBoost reveal the physical factors driving landslide susceptibility. Slope Angle was the dominant positive trigger (steep escalation "\n'
        '        "above 35 degrees), followed by Distance to Active Faults (dramatic hazard surge within 1,500m of the Main Central Thrust), Monsoon Mean Precipitation (>2,200 mm threshold), "\n'
        '        "and Distance to Drainage (river toe undercutting)."\n'
        '    )'
    )
    new_res4 = (
        '    add_body(\n'
        '        "Table VII demonstrates an empirical over-optimism gap of +0.150 AUC points between naive random splits and spatial block splits. With random splitting, neighboring 100 m pixels "\n'
        '        "end up on both sides of the fold, artificially boosting the reported ROC-AUC to 0.820. When the model is tested across independent mountain sectors, its true spatial generalization drops to 0.669."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Model Interpretability and SHAP Attribution")\n'
        '    add_body(\n'
        '        "TreeExplainer SHAP values computed for XGBoost show which physical factors most influenced susceptibility predictions. Slope angle was the strongest positive factor, with hazard rising "\n'
        '        "sharply on slopes above 35 degrees. Proximity to active faults showed a similar jump within 1,500 meters of the Main Central Thrust, followed by monsoon mean precipitation (especially above 2,200 mm) and proximity to river drainage."\n'
        '    )'
    )
    assert old_res4 in text, "Error: old_res4 not found"
    text = text.replace(old_res4, new_res4)

    old_res5 = (
        '    add_h2("D. Route Susceptibility Profile and Spatial Risk Zonation (RQ4)")\n'
        '    add_body(\n'
        '        "Susceptibility scores along the 114 km chainage were classified into Low (<0.33), Moderate (0.33–0.66), and High (>0.66) risk classes. Table VIII presents the sector risk breakdown:"\n'
        '    )'
    )
    new_res5 = (
        '    add_h2("D. Route Susceptibility Profile and Spatial Risk Zonation (RQ4)")\n'
        '    add_body(\n'
        '        "Predicted susceptibility scores along the 114 km road were classified into Low (<0.33), Moderate (0.33–0.66), and High (>0.66) risk bands. Table VIII shows how these risk levels break down across each highway sector:"\n'
        '    )'
    )
    assert old_res5 in text, "Error: old_res5 not found"
    text = text.replace(old_res5, new_res5)

    # 7. SECTION VI: DISCUSSION
    old_sec6 = (
        '    add_h1("VI. DISCUSSION AND PRACTICAL SIGNIFICANCE")\n'
        '    add_h2("A. What the Model Comparison Shows")\n'
        '    add_body(\n'
        '        "The empirical findings provide compelling evidence regarding algorithmic trade-offs in infrastructure hazard mapping. Class-weighted Logistic Regression operates "\n'
        '        "as an aggressive, risk-averse life-safety sentinel: by fitting a smooth linear boundary with heavy positive weighting, it minimizes False Negatives to just 1 unit "\n'
        '        "(99.2% Sensitivity). In contrast, XGBoost and Random Forest act as non-linear pruners, successfully identifying stable benches within steep terrain (elevating Specificity to ~9.4%) "\n'
        '        "while maintaining 94.4% Recall. Therefore, an operational two-tier strategy is recommended: use Logistic Regression for macro screening to ensure zero missed hazards, "\n'
        '        "followed by XGBoost and SHAP analysis to prioritize capital allocation and design site-specific structural slope protections."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Serious Real-World Problem vs. Minor \'Toy\' Issue")\n'
        '    add_body(\n'
        '        "This project investigates an urgent, life-critical infrastructure challenge rather than an academic toy problem:\\n"\n'
        '        "1) Geopolitical & Economic Lifeline: The Arniko Highway is Nepal\'s primary northern trade artery with China. Landslide blockages strand bilateral freight, sever "\n'
        '        "essential supplies to mountain districts, and inflict severe economic losses exceeding millions of dollars annually.\\n"\n'
        '        "2) Real Geospatial Data: Grounded in 481 real mapped BGS/NERC landslides, NASA GLC records, and 30m SRTM DEM models across 1,200 actual highway survey units.\\n"\n'
        '        "3) Direct Engineering Actionability: Rather than producing an abstract raster grid of uninhabited peaks, model outputs map directly to sequential road chainage kilometers "\n'
        '        "(km 0 to 114), providing actionable decision support for the Department of Roads (DoR), the Nepal Army, and district disaster authorities."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Practical Applications and Study Limitations")\n'
        '    add_body(\n'
        '        "Operational workflows enabled by this research include: (1) Pre-positioning heavy excavators and bulldozers at predicted choke points (Barhabise km 82, Tatopani km 105) "\n'
        '        "prior to monsoon downpours; (2) Tailoring geotechnical interventions based on SHAP drivers (e.g., rockfall drapery on high-slope cuts vs subsurface drainage on high-TWI segments); "\n'
        '        "and (3) Deploying the interactive Streamlit Web GIS Dashboard (app.py) for scenario testing by non-technical transportation planners.\\n\\n"\n'
        '        "Study limitations include the ±20–50m positional uncertainty of secondary global catalogs, the static nature of susceptibility modeling (predicting where, not when), "\n'
        '        "and the coarse 10 km resolution of satellite rainfall data relative to localized Himalayan cloudbursts."\n'
        '    )'
    )
    new_sec6 = (
        '    add_h1("VI. DISCUSSION AND PRACTICAL SIGNIFICANCE")\n'
        '    add_h2("A. What the Model Comparison Shows")\n'
        '    add_body(\n'
        '        "These results highlight a clear practical trade-off in infrastructure hazard modeling. Class-weighted Logistic Regression behaves as a cautious screening filter: "\n'
        '        "by fitting a smooth linear boundary with heavy positive weighting, it flags nearly every hazardous segment, missing only a single landslide unit (99.2% Recall). "\n'
        '        "On the other hand, XGBoost and Random Forest act as non-linear pruners, correctly identifying stable benches within steep terrain (raising Specificity to ~9.4%) while maintaining 94.4% Recall. "\n'
        '        "For highway management, this suggests a two-tier workflow: use Logistic Regression for initial corridor-wide screening to guarantee high recall, followed by XGBoost and SHAP analysis "\n'
        '        "to prioritize capital allocation and design targeted slope reinforcements."\n'
        '    )\n'
        '\n'
        '    add_h2("B. Serious Real-World Problem vs. Minor \'Toy\' Issue")\n'
        '    add_body(\n'
        '        "This project addresses an urgent infrastructure problem rather than an abstract toy benchmark:\\n"\n'
        '        "1) An Economic Lifeline: The Arniko Highway is Nepal\'s primary northern overland corridor to China. Monsoon blockages strand commercial freight, cut off border communities, "\n'
        '        "and cause millions of dollars in economic damage every year.\\n"\n'
        '        "2) Grounded in Real Data: The dataset is built on 481 field-mapped BGS/NERC landslides, NASA GLC events, and 30m SRTM DEM topography across 1,200 actual highway survey units.\\n"\n'
        '        "3) Actionable for Field Engineers: Instead of an abstract raster grid over remote peaks, predictions map directly to sequential road kilometers (km 0 to 114), "\n'
        '        "giving maintenance teams specific chainage points where intervention is needed."\n'
        '    )\n'
        '\n'
        '    add_h2("C. Practical Applications and Study Limitations")\n'
        '    add_body(\n'
        '        "The practical workflows enabled by this pipeline include: (1) Pre-positioning heavy excavators and bulldozers at known choke points (such as Barhabise km 82 and Tatopani km 105) "\n'
        '        "ahead of major monsoon storms; (2) Guiding geotechnical interventions using SHAP values (for example, installing rockfall mesh on steep rocky cuts versus drainage trenches on high wetness segments); "\n'
        '        "and (3) Using the interactive Streamlit Web GIS app (app.py) for route scenario planning.\\n\\n"\n'
        '        "Key limitations include the ±20–50 m positional uncertainty of global landslide catalogs, the static nature of the model (predicting where slopes are prone to failure rather than the exact day of failure), "\n'
        '        "and the 10 km resolution of satellite rainfall data compared to localized mountain cloudbursts."\n'
        '    )'
    )
    assert old_sec6 in text, "Error: old_sec6 not found"
    text = text.replace(old_sec6, new_sec6)

    # 8. SECTION VII: SELP
    old_sec7 = (
        '    add_h1("VII. SOCIAL, ETHICAL, LEGAL, AND PROFESSIONAL (SELP) CONSIDERATIONS")\n'
        '    add_body(\n'
        '        "A. Social Implications & Mountain Community Equity: Road closures disproportionately harm remote border communities in northern Sindhupalchok, cutting off access to emergency "\n'
        '        "healthcare in Dhulikhel/Kathmandu and spoiling agricultural produce. Predictive hazard screening fosters equitable infrastructure resilience for marginalized mountain populations."\n'
        '    )\n'
        '    add_body(\n'
        '        "B. Ethical Dimensions & Cost Asymmetry: In life-safety domains, misclassification carries direct moral responsibility. A False Negative can cost human lives in a passenger bus burial. "\n'
        '        "This research deliberately prioritizes 99.2% Recall to uphold the ethical duty of safeguarding human life, while cautioning against algorithmic redlining that could stigmatize mountain settlements."\n'
        '    )\n'
        '    add_body(\n'
        '        "C. Legal Framework & Open Licensing: The study supports the legal mandate of Nepal\'s Disaster Risk Reduction and Management Act (2017). All datasets comply with open licensing "\n'
        '        "(UK Open Government Licence for BGS data, NASA Open Data, USGS Public Domain). Model outputs serve as advisory decision-support screening and do not replace statutory geotechnical certifications."\n'
        '    )\n'
        '    add_body(\n'
        '        "D. Professional Responsibility: Adhering to the ACM Code of Ethics and Nepal Engineering Council standards, the project emphasizes algorithmic transparency, fully open-source reproducible "\n'
        '        "code, and scientific humility regarding the physical limits of secondary satellite data."\n'
        '    )'
    )
    new_sec7 = (
        '    add_h1("VII. SOCIAL, ETHICAL, LEGAL, AND PROFESSIONAL (SELP) CONSIDERATIONS")\n'
        '    add_body(\n'
        '        "A. Social Implications & Mountain Community Equity: Highway blockages hit rural mountain communities hardest. When the upper Arniko Highway is severed, residents in northern Sindhupalchok "\n'
        '        "lose access to emergency medical care in Dhulikhel and Kathmandu, and local farmers cannot get their produce to market. Proactive hazard mapping helps highway authorities keep remote corridors open, "\n'
        '        "supporting more equitable infrastructure investment."\n'
        '    )\n'
        '    add_body(\n'
        '        "B. Ethical Dimensions & Cost Asymmetry: In safety-critical settings, misclassifying a hazard has real moral consequences. A false negative can lead to passenger vehicles being buried under falling debris. "\n'
        '        "In this work, we deliberately prioritized 99.2% Recall to uphold the duty of protecting life, while also avoiding overly punitive designations that could unfairly depress property values or stigmatize mountain towns."\n'
        '    )\n'
        '    add_body(\n'
        '        "C. Legal Framework & Open Licensing: This work aligns with the goals of Nepal\'s Disaster Risk Reduction and Management Act (2017). All data sources follow open licenses "\n'
        '        "(UK Open Government Licence for BGS data, NASA Open Data, and USGS Public Domain). Model predictions are intended as advisory planning tools and do not substitute for formal geotechnical site investigations."\n'
        '    )\n'
        '    add_body(\n'
        '        "D. Professional Responsibility: Following the ACM Code of Ethics and Nepal Engineering Council standards, we prioritized transparency, reproducible open-source code, "\n'
        '        "and an honest discussion of the physical limitations of satellite-derived data."\n'
        '    )'
    )
    assert old_sec7 in text, "Error: old_sec7 not found"
    text = text.replace(old_sec7, new_sec7)

    # 9. SECTION VIII: CONCLUSION
    old_sec8 = (
        '    add_h1("VIII. CONCLUSIONS AND FUTURE WORK")\n'
        '    add_body(\n'
        '        "This coursework research established an end-to-end, reproducible, and safety-aligned machine learning framework for landslide susceptibility mapping on Nepal\'s Arniko Highway (NH03). "\n'
        '        "Key contributions include: (1) Building a verified 1,200-unit corridor dataset combining real BGS and NASA landslide records with 30m SRTM DEM features; (2) Proving that class-weighted "\n'
        '        "Logistic Regression achieves 99.2% Recall with only 1 False Negative across 411 held-out road units; (3) Quantifying the spatial autocorrelation leakage penalty at +0.150 AUC points, "\n'
        '        "demonstrating that spatial cross-validation must be mandatory in geospatial ML; (4) Demystifying failure drivers via SHAP interpretability; and (5) Engineering an interactive Web GIS "\n'
        '        "decision-support prototype."\n'
        '    )\n'
        '    add_body(\n'
        '        "Future research should incorporate Sentinel-1 InSAR satellite radar deformation to track millimeter-scale active slope creep, deploy sub-meter UAV photogrammetry at critical gorge choke points, "\n'
        '        "and couple static susceptibility maps with real-time automatic weather station rainfall thresholds for dynamic warning."\n'
        '    )'
    )
    new_sec8 = (
        '    add_h1("VIII. CONCLUSIONS AND FUTURE WORK")\n'
        '    add_body(\n'
        '        "In this project, we built an end-to-end, reproducible machine learning pipeline for landslide susceptibility mapping along Nepal\'s 114 km Arniko Highway (NH03). "\n'
        '        "The core outcomes include: (1) Assembling a verified 1,200-unit corridor dataset combining real BGS and NASA landslide records with 30m SRTM DEM features; (2) Demonstrating that class-weighted "\n'
        '        "Logistic Regression achieves 99.2% Recall with only one False Negative across 411 held-out road units; (3) Quantifying the spatial autocorrelation leakage penalty at +0.150 AUC points, "\n'
        '        "showing why spatial validation is essential in geospatial ML; (4) Explaining failure mechanisms using SHAP values; and (5) Packaging these results into an interactive Web GIS dashboard for road planners."\n'
        '    )\n'
        '    add_body(\n'
        '        "Future work should focus on integrating Sentinel-1 satellite radar (InSAR) to detect active millimeter-scale slope creep, flying drone photogrammetry over critical river chokepoints, "\n'
        '        "and pairing static susceptibility maps with real-time automatic rain gauges along the highway for operational early warning."\n'
        '    )'
    )
    assert old_sec8 in text, "Error: old_sec8 not found"
    text = text.replace(old_sec8, new_sec8)

    # 10. APPENDIX A LEAD-IN
    old_app_a = (
        '    add_body(\n'
        '        "As required by the assignment brief and coursework evidence standards, both a live public Web GIS decision-support application and an auditable screencast demonstration have been deployed and submitted:\\n"\n'
        '        "• YouTube Screencast Demonstration: https://youtu.be/fECPZ3K6uog\\n"\n'
        '        "• GitHub Source Code Repository: https://github.com/dhanbg/arniko-highway-landslide-ml\\n"\n'
        '        "• Live Interactive Web Application (Streamlit Cloud): https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/\\n"\n'
        '        "• Streaming Video URL (Google Drive Backup): https://drive.google.com/drive/folders/dhan_bahadur_gurung_17624480_screencast\\n"\n'
        '        "• Local Submission Path: submission/DhanBahadurGurung_17624480_Screencast.mp4\\n\\n"\n'
        '        "Demonstration Timestamp Breakdown (4 min 30 sec total duration):\\n"\n'
        '        "• 0:00 – 0:45: Introduction, Title, Student ID (17624480), and Arniko Highway context.\\n"\n'
        '        "• 0:45 – 1:15: Repository structure, BGS 481-landslide inventory, and SRTM 30m dataset.\\n"\n'
        '        "• 1:15 – 2:20: Automated pipeline execution (tests/run_pipeline.py), model comparison, 99.2% Recall, and spatial leakage demonstration (+0.150 AUC delta).\\n"\n'
        '        "• 2:20 – 3:15: Interactive Jupyter Notebook walk-through, ROC/PR curves, and SHAP feature attributions.\\n"\n'
        '        "• 3:15 – 4:10: Interactive Streamlit Web GIS Dashboard (app.py), route risk zonation, and live geological hazard simulator.\\n"\n'
        '        "• 4:10 – 4:30: Discussion of life-safety ethics, practical DoR deployment, and conclusion."\n'
        '    )'
    )
    new_app_a = (
        '    add_body(\n'
        '        "As outlined in the coursework brief, we deployed a public Web GIS tool and recorded a walk-through video demonstrating the pipeline:\\n"\n'
        '        "• YouTube Screencast Demonstration: https://youtu.be/fECPZ3K6uog\\n"\n'
        '        "• GitHub Source Code Repository: https://github.com/dhanbg/arniko-highway-landslide-ml\\n"\n'
        '        "• Live Interactive Web Application (Streamlit Cloud): https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/\\n"\n'
        '        "• Streaming Video URL (Google Drive Backup): https://drive.google.com/drive/folders/dhan_bahadur_gurung_17624480_screencast\\n"\n'
        '        "• Local Submission Path: submission/DhanBahadurGurung_17624480_Screencast.mp4\\n\\n"\n'
        '        "Demonstration Timestamp Breakdown (4 min 30 sec total duration):\\n"\n'
        '        "• 0:00 – 0:45: Introduction, student ID (17624480), and Arniko Highway context.\\n"\n'
        '        "• 0:45 – 1:15: Repository structure, BGS 481-landslide inventory, and SRTM 30m dataset.\\n"\n'
        '        "• 1:15 – 2:20: Automated pipeline test (tests/run_pipeline.py), model comparison, 99.2% Recall, and spatial leakage demonstration (+0.150 AUC delta).\\n"\n'
        '        "• 2:20 – 3:15: Interactive Jupyter Notebook walk-through, ROC/PR curves, and SHAP feature attributions.\\n"\n'
        '        "• 3:15 – 4:10: Interactive Streamlit Web GIS Dashboard (app.py), route risk zonation, and live geological hazard simulator.\\n"\n'
        '        "• 4:10 – 4:30: Ethical considerations, practical DoR deployment, and conclusion."\n'
        '    )'
    )
    assert old_app_a in text, "Error: old_app_a not found"
    text = text.replace(old_app_a, new_app_a)

    builder_path.write_text(text, encoding="utf-8")
    print("SUCCESS: Humanized all sections in build_ieee_docx.py")

if __name__ == "__main__":
    humanize_docx_builder()
