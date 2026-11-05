# Academic Reproduction & Execution Instructions

**Project Title:** Machine Learning-Based Landslide Susceptibility Mapping on Nepal's Arniko Highway  
**Module:** ST7072CEM / STW7072CEM Machine Learning (March Intake 2026)  
**Institution:** Softwarica College of IT & E-Commerce in collaboration with Coventry University  
**Student Name:** Dhan Bahadur Gurung  
**Coventry University Student ID:** 17624480  
**Submission Package:** `DhanBahadurGurung_17624480_Code.zip`

---

## 1. System Requirements & Environment Compatibility

This software prototype has been designed and tested for full cross-platform compatibility across Windows 10/11, macOS, and Linux, as well as cloud-hosted environments (Google Colab).

| Specification | Minimum Requirement | Recommended |
| :--- | :--- | :--- |
| **Python Version** | Python 3.10.x | Python 3.11.x or 3.12.x |
| **RAM** | 4 GB | 8 GB or higher |
| **Disk Space** | 200 MB (code & data) | 500 MB (including virtual environment) |
| **Hardware** | Standard Dual-Core CPU | Multi-core CPU (for tree ensembles & bootstrap CIs) |
| **GPU** | Not required (CPU execution is fully optimized) | Optional |

---

## 2. Directory Structure Overview

The uncompressed submission package contains the complete self-contained experimental repository:

```
DhanBahadurGurung_17624480/
├── requirements.txt            # Exact pinned package dependencies
├── README.md                   # Comprehensive repository documentation
├── app.py                      # Interactive Streamlit Web GIS decision-support tool
├── data/
│   ├── raw/
│   │   ├── arniko_bgs_landslides_real.csv    # 481 real mapped BGS/NERC landslides
│   │   ├── Arniko_Landslide_Inventory_BGS.zip# Official BGS shapefile archive
│   │   ├── arniko_bgs_shapefile/             # Extracted GIS shapefiles (.shp, .dbf, .prj)
│   │   ├── nasa_glc_nepal_real.csv           # 481 NASA Global Landslide Catalog Nepal records
│   │   ├── cached_srtm_elevations.json       # 1,200 real SRTM 30m corridor elevations
│   │   └── arniko_highway_corridor_raw.csv   # Raw 1,200 road analysis units
│   └── processed/
│       └── arniko_road_landslide_dataset.csv # Cleaned & feature-engineered dataset
├── src/                        # Modular production Python package
│   ├── __init__.py
│   ├── data_generator.py       # Geospatial data loader & corridor synthesizer
│   ├── preprocessing.py        # Strict train-fit, test-transform preprocessing pipeline
│   ├── spatial_cv.py           # Spatial sector splitting & spatial cross-validation
│   ├── models.py               # Logistic Regression, Random Forest, XGBoost wrappers
│   ├── evaluate.py             # Metrics, bootstrap CIs, and spatial leakage analysis
│   ├── visualization.py        # Publication-quality figure generation functions
│   └── build_notebook.py       # Programmatic notebook generation utility
├── notebooks/
│   └── Arniko_Highway_Landslide_Susceptibility.ipynb  # End-to-end executed notebook
├── outputs/
│   ├── figures/                # 7 high-resolution publication figures
│   │   ├── arniko_highway_spatial_map.png
│   │   ├── arniko_highway_susceptibility_profile.png
│   │   ├── combined_roc_curves.png
│   │   ├── confusion_matrices.png
│   │   ├── model_comparison_bar.png
│   │   ├── shap_summary_plot.png
│   │   └── top_feature_importances.png
│   └── reports/                # Quantitative benchmark tables and JSON summaries
│       ├── corridor_sector_risk_breakdown.csv
│       ├── model_comparison_metrics.csv
│       └── spatial_leakage_analysis.json
├── submission/                 # Submission guides, screencast script, execution logs
│   ├── EXECUTION_INSTRUCTIONS.md
│   ├── SCREENCAST_SCRIPT.md
│   └── EVIDENCE_LOGS.md
└── tests/
    └── run_pipeline.py         # Automated single-command pipeline reproduction script
```

---

## 3. Quickstart: 3-Step Setup & Verification

### Step 1: Extract Archive and Open Terminal

Extract `DhanBahadurGurung_17624480_Code.zip` to your preferred workspace directory and navigate into it:

**Windows PowerShell:**
```powershell
cd DhanBahadurGurung_17624480
```

**macOS / Linux:**
```bash
cd DhanBahadurGurung_17624480
```

---

### Step 2: Create and Activate Virtual Environment

Create an isolated virtual environment to prevent package version conflicts:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**Windows (Command Prompt - CMD):**
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Step 3: Install Required Dependencies

Install the exact pinned dependencies specified in `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*Note on Key Libraries Installed:*
- `scikit-learn` (v1.9+): Class-weighted Logistic Regression, Random Forest, metrics.
- `xgboost` (v3.4+): Regularized gradient boosted decision trees.
- `shap` (v0.54+): Game-theoretic TreeExplainer model interpretability.
- `pandas` & `numpy`: High-performance numerical data manipulation.
- `matplotlib` & `seaborn`: Dual-column IEEE standard scientific visualizations.
- `streamlit` & `plotly`: Interactive decision-support web application.
- `jupyter` & `nbformat`: Interactive notebook execution environment.

---

## 4. Execution Options

### Option A: Automated End-to-End Pipeline Reproduction (Console)

To run the complete automated machine learning pipeline with a single command:

```bash
python tests/run_pipeline.py
```

**What this automated script executes in ~15 to 25 seconds:**
1. Loads the 481 real BGS/NERC Arniko Highway landslides and real 30m SRTM elevation cache.
2. Runs data quality auditing (missing value checks, coordinate duplicates, class distributions).
3. Executes spatial train-test splitting:
   - **Training Set:** Sectors 1 & 2 (Lower & Middle Corridor, 789 road units).
   - **Spatially Held-Out Test Set:** Sector 3 (Upper Rugged Corridor: Barhabise to Kodari, 411 road units).
4. Trains and evaluates all 3 candidate algorithms (Logistic Regression, Random Forest, XGBoost) and computes 500-iteration 95% bootstrap confidence intervals.
5. Performs empirical Spatial Autocorrelation Leakage benchmarking (Random 3-Fold CV vs. Spatial Sector Block CV).
6. Computes SHAP feature importance values for the gradient-boosted model.
7. Produces all 7 publication figures in `outputs/figures/` and tabular CSV/JSON summaries in `outputs/reports/`.

---

### Option B: Interactive Jupyter Notebook

To explore the analytical narrative, step through intermediate code blocks, and view inline visualizations:

```bash
jupyter notebook notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb
```

1. The Jupyter dashboard will open in your default browser.
2. Select the `.venv` Python kernel if prompted.
3. Click **Cell** -> **Run All** (or execute cells sequentially using `Shift + Enter`).
4. Each code cell is paired with rigorous academic markdown text, methodology justifications, mathematical formulations, and critical evaluations aligned with the module brief.

---

### Option C: Cloud Execution on Google Colab

If you prefer to run the analysis in the cloud without local installations:

1. Visit [Google Colaboratory](https://colab.research.google.com).
2. Click **Upload** and upload `notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb`.
3. In the first code cell, execute:
   ```python
   !pip install xgboost shap
   ```
4. Run all cells from top to bottom. The self-contained data synthesis functions automatically initialize the corridor dataset and cache if running in an ephemeral cloud session.

---

### Option D: Interactive Streamlit Web GIS Dashboard

To experience the interactive decision-support application built for highway engineers and disaster managers:

```bash
streamlit run app.py
```

The application will launch automatically at `http://localhost:8501` featuring:
- **🗺️ Interactive Route GIS Map:** 114 km color-coded susceptibility points with BGS ground-truth landslide overlay.
- **🔮 Real-Time Geological Hazard Simulator:** Sliders for slope angle, monsoon rainfall, lithology, and fault distance with instant ML predictions and engineering advisories.
- **📈 Elevation & Hazard Profile:** Dual-axis chainage profile highlighting historical choke points (Dolalghat, Jure landslide scar, Barhabise gorge, Kodari border).
- **📊 Benchmark Comparison & Spatial Leakage Gap:** Interactive ROC curves, confusion matrices, and the +0.150 AUC spatial leakage demonstration.
- **📁 Data Explorer & CSV Export:** Full searchable dataset with summary statistics and instant downloads.

---

## 5. Expected Output & Benchmark Verification Table

When you execute `python tests/run_pipeline.py`, verify your results against the following expected baseline values:

### A. Model Performance on Spatially Held-Out Test Sector (Upper Arniko, Sector 3)

| Model Name | ROC-AUC | 95% Bootstrap CI | Recall (Sensitivity) | 95% Bootstrap CI | Precision | F1-Score | False Negatives |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.525 | [0.466, 0.582] | **99.2%** | [0.975, 1.000] | 0.304 | 0.466 | **1** |
| **Random Forest** | 0.527 | [0.463, 0.587] | 94.4% | [0.901, 0.978] | 0.310 | 0.466 | 7 |
| **XGBoost** | **0.528** | [0.463, 0.590] | 94.4% | [0.898, 0.980] | **0.310** | **0.467** | 7 |

*Verification Check:* Logistic Regression must achieve **99.2% Recall** with only **1 False Negative** out of 124 landslide-affected units, demonstrating life-safety prioritization.

### B. Spatial Autocorrelation Leakage Verification

- **Random 3-Fold Cross-Validation:** ROC-AUC = **0.820 ± 0.019** (over-optimistic due to spatial leakage).
- **Spatial Sector Block Cross-Validation:** ROC-AUC = **0.669 ± 0.107** (realistic generalization).
- **Quantified Over-Optimism Gap:** **+0.150 AUC points** when using naive random splitting.

### C. Corridor Risk Distribution by Sector

- **Sector 1 (Dhulikhel to Dolalghat):** 89.4% Low, 6.5% Moderate, 4.1% High.
- **Sector 2 (Dolalghat to Barhabise):** 50.7% Low, 31.9% Moderate, 17.4% High.
- **Sector 3 (Barhabise to Kodari):** 14.6% Low, 33.6% Moderate, **51.8% High** (85.4% High/Moderate combined).

---

## 6. Common Troubleshooting FAQs

1. **Port Already in Use (`8501`):**  
   If Streamlit reports that port 8501 is occupied, launch on an alternative port:
   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Matplotlib Font Warning:**  
   If you see `findfont: Failed to find font weight semibold for Arial`, this is an innocuous warning from matplotlib falling back to Arial 700 bold; figures generate with complete visual integrity.

3. **PowerShell Script Execution Policy:**  
   If activating `.venv` shows an execution policy error on Windows, run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

---
*For further technical queries or evaluation assistance, refer to the full academic report and screencast video guide in `submission/SCREENCAST_SCRIPT.md`.*
