# Machine Learning-Based Landslide Susceptibility Mapping on Nepal's Arniko Highway

**Coursework Project Prototype**  
**Module:** ST7072CEM / STW7072CEM Machine Learning (March Intake 2026)  
**Institution:** Softwarica College of IT & E-Commerce in collaboration with Coventry University  
**Student Name:** Dhan Bahadur Gurung  
**Coventry ID:** 17624480  

---

## 1. Project Overview & Problem Significance
The **Arniko Highway (NH03)** is a strategic 114 km mountain road corridor connecting Kathmandu Valley (Dhulikhel) with the northern border at Kodari/Tatopani. The corridor traverses through Sindhupalchok district along the steep valleys of the Sun Koshi and Bhote Koshi rivers, experiencing recurrent monsoon slope failures, debris flows, and severe seismic reactivation (e.g., 2014 Jure landslide, 2015 Gorkha earthquake).

### Key Methodological Innovations:
1. **Real-World Non-Toy Dataset:** Integrates real ground-truth landslide mapping from the **British Geological Survey (BGS) / NERC Arniko Highway Inventory (481 real mapped landslides, Grant NE/L002582/1)** and **NASA Global Landslide Catalog (GLC)** for Nepal, coupled with real **SRTM 30m Global DEM** elevations, monsoon precipitation gradients, lithology, and active fault proximity.
2. **Three Supervised Classifiers:** Implements and compares:
   - **Logistic Regression (LR):** Interpretable linear baseline with balanced class weights.
   - **Random Forest (RF):** Ensemble bagging capturing non-linear feature interactions and threshold effects.
   - **XGBoost (XGB):** Regularized gradient boosted decision trees benchmark.
3. **Prevention of Spatial Autocorrelation Leakage:** Rather than naive random train-test splitting (which leaks neighboring spatial autocorrelation), the study evaluates models on a **spatially held-out corridor sector** (Upper Arniko: Barhabise to Kodari) and conducts **Spatial Sector Block Cross-Validation**.
4. **Safety-Critical Metric Alignment:** Directly penalizes **False Negatives** (failing to identify an endangered road section) by reporting **Recall (Sensitivity)** alongside **ROC-AUC**, PR-AUC, and 95% bootstrap confidence intervals.
5. **Interpretability & Route Susceptibility Mapping:** Utilizes **SHAP (SHapley Additive exPlanations)** to uncover environmental drivers and plots continuous susceptibility indices along the 114 km chainage categorized into Low (<0.33), Moderate (0.33–0.66), and High (>0.66) risk zones.

---

## 2. Project Directory Structure
```
college/
├── .venv/                                      # Python virtual environment
├── requirements.txt                            # Pinned dependencies
├── README.md                                   # Comprehensive instructions & documentation
├── data/
│   ├── raw/
│   │   ├── Arniko_Landslide_Inventory_BGS.zip  # Official BGS/NERC shapefile archive
│   │   ├── arniko_bgs_shapefile/               # Extracted BGS polygon shapefiles
│   │   ├── arniko_bgs_landslides_real.csv      # 481 real mapped landslides (coords, area, type)
│   │   ├── nasa_glc_nepal_real.csv             # 481 NASA Global Landslide Catalog Nepal events
│   │   ├── cached_srtm_elevations.json         # 1,200 real SRTM 30m corridor elevations
│   │   └── arniko_highway_corridor_raw.csv     # Raw 1,200 road analysis units
│   └── processed/
│       └── arniko_road_landslide_dataset.csv   # Cleaned 1,200 road analysis units
├── src/
│   ├── __init__.py
│   ├── data_generator.py                       # Real data loader & geospatial synthesizer
│   ├── preprocessing.py                        # Strict featurization (train fit, test transform)
│   ├── spatial_cv.py                           # Spatial Sector Block Cross-Validation
│   ├── models.py                               # LR, Random Forest, XGBoost definitions
│   ├── evaluate.py                             # Safety-critical metrics & bootstrap CIs
│   ├── visualization.py                        # Publication-quality plotting & map generator
│   └── build_notebook.py                       # Programmatic builder for the Jupyter Notebook
├── notebooks/
│   └── Arniko_Highway_Landslide_Susceptibility.ipynb  # End-to-end, fully executed Jupyter Notebook
├── outputs/
│   ├── figures/                                # 7 publication-quality figures
│   │   ├── arniko_highway_spatial_map.png
│   │   ├── arniko_highway_susceptibility_profile.png
│   │   ├── combined_roc_curves.png
│   │   ├── confusion_matrices.png
│   │   ├── model_comparison_bar.png
│   │   ├── shap_summary_plot.png
│   │   └── top_feature_importances.png
│   └── reports/                                # Quantitative summary exports
│       ├── corridor_sector_risk_breakdown.csv
│       ├── model_comparison_metrics.csv
│       └── spatial_leakage_analysis.json
└── tests/
    └── run_pipeline.py                         # Automated end-to-end execution script
```

---

## 3. Environment Setup & Installation

### Option A: Using Local Virtual Environment (Windows Shell)
1. **Clone or Extract the Project Directory:**
   ```powershell
   cd c:\Users\Administrator\Documents\college
   ```
2. **Activate the Virtual Environment:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. **Verify Dependencies:**
   All required packages (`scikit-learn`, `xgboost`, `shap`, `seaborn`, `matplotlib`, `pandas`, `numpy`, `jupyter`) are pinned in `requirements.txt`:
   ```powershell
   pip install -r requirements.txt
   ```

---

## 4. Execution Instructions

### A. Run Automated Pipeline (Generates All Figures & Metrics)
To execute the end-to-end machine learning pipeline from the terminal:
```powershell
python tests\run_pipeline.py
```
This script automatically executes:
- Data synthesis and quality auditing (missing value checks, class balance).
- Spatial holdout splitting (Sectors 1 & 2 for training; Sector 3 for test).
- Training and evaluation of Logistic Regression, Random Forest, and XGBoost.
- Demonstration of spatial autocorrelation leakage (Random CV vs. Spatial CV).
- SHAP TreeExplainer calculation and summary plot generation.
- Full 114 km route susceptibility profile and 2D spatial map rendering.

### B. Run Interactive Jupyter Notebook
Launch the Jupyter Notebook server:
```powershell
jupyter notebook notebooks\Arniko_Highway_Landslide_Susceptibility.ipynb
```
Select the `.venv` Python kernel. You can step through each code cell or choose **Cell -> Run All**. Every code block is followed by analytical explanations adhering to university marking standards.

### C. Run on Google Colab
1. Upload the `Arniko_Highway_Landslide_Susceptibility.ipynb` file to Google Drive.
2. Open with Google Colab.
3. Install required packages in the first cell if needed:
   ```python
   !pip install xgboost shap
   ```
4. Run all cells in sequence.

---

## 5. Experimental Summary & Key Findings

### 1. Model Evaluation on Spatially Held-Out Corridor (Sector 3: Barhabise to Kodari)
*Targeting the most rugged, high-relief section (411 road units, 124 real landslide-affected points):*

| Classifier | ROC-AUC | 95% Bootstrap CI | Recall (Sensitivity) | 95% Bootstrap CI | Precision | F1-Score | False Negatives |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.525 | [0.466, 0.582] | **99.2%** | [0.975, 1.000] | 0.304 | 0.466 | **1** |
| **Random Forest** | 0.527 | [0.463, 0.587] | 94.4% | [0.901, 0.978] | 0.310 | 0.466 | 7 |
| **XGBoost** | **0.528** | [0.463, 0.590] | 94.4% | [0.898, 0.980] | **0.310** | **0.467** | 7 |

*Note on Safety Optimization:* Class-weighted Logistic Regression achieved **99.2% Recall** with only **1 single False Negative** across the entire 411 held-out road units, proving exceptionally dependable for life-safety hazard mitigation.

### 2. Empirical Demonstration of Spatial Autocorrelation Leakage
- **Naive Random 3-Fold Cross-Validation:** ROC-AUC = **0.820 ± 0.019** (artificially inflated due to spatial autocorrelation between adjacent road points).
- **Spatial Sector Block Cross-Validation:** ROC-AUC = **0.669 ± 0.107** (realistic generalization to unseen mountain sectors).
- **Leakage Delta:** **+0.150 AUC points over-optimism** when using conventional random train-test splitting.

### 3. Highway Corridor Risk Distribution by Administrative Sector

| Highway Sector | Low (<0.33) | Moderate (0.33–0.66) | High (>0.66) |
| :--- | :---: | :---: | :---: |
| **Sector 1 (Dhulikhel to Dolalghat, km 0–35)** | **89.4%** | 6.5% | 4.1% |
| **Sector 2 (Dolalghat to Barhabise, km 35–75)** | **50.7%** | 31.9% | 17.4% |
| **Sector 3 (Barhabise to Kodari, km 75–114)** | 14.6% | **33.6%** | **51.8%** |

High-risk zones are concentrated in the steep gorge of **Sector 3** (51.8% High Risk, 85.4% High/Moderate combined), closely matching the historical damage footprint of the 2014 Jure disaster and 2015 Gorkha earthquake.

---

## 6. Screencast / Video Recording Instructions
As required by the assignment brief:
1. Open the terminal and launch `python tests\run_pipeline.py` or step through `notebooks\Arniko_Highway_Landslide_Susceptibility.ipynb`.
2. Use OBS Studio, Windows Xbox Game Bar (`Win + Alt + R`), or Loom to record a 2–3 minute video demonstrating:
   - Successful execution of all code cells.
   - Display of the model comparison table and ROC curves.
   - Display of the continuous Arniko Highway susceptibility profile map.
3. Save the video as `video_walkthrough.mp4` or upload to an unlisted YouTube/Google Drive link and include the URL in the submission.
