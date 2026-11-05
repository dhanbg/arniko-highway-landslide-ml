# ST7072CEM Coursework Submission Master Checklist

**Student Name:** Dhan Bahadur Gurung  
**Coventry University Student ID:** 17624480  
**Module Name:** Machine Learning  
**Module Code:** ST7072CEM / STW7072CEM (March Intake 2026)  
**Assignment Title:** STW7072CEM Machine Learning March Intake 2026 Coursework CW (Regular)  
**Institution:** Softwarica College of IT & E-Commerce in collaboration with Coventry University  
**Module Leader:** Shrawan Thakur (`stw0049@softwarica.edu.np`)  
**Submission Portal:** Campus 4.0 Platform  

---

## 1. Submission Deliverables Summary

According to the Student Assignment Brief, the final submission requires:

| Deliverable | Required Format | Submitted File Name / Path | Status |
| :--- | :--- | :--- | :---: |
| **1. Individual Academic Report** | IEEE Conference Proceeding (`.docx` / `.pdf`) | `DhanBahadurGurung_17624480.pdf` / `.docx` | Complete |
| **2. Source Code Package** | Compressed ZIP file containing Python code & Notebook | `DhanBahadurGurung_17624480_Code.zip` | Ready / Built |
| **3. Live Web Application** | Streamlit Community Cloud (Public Web GIS) | `https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/` | **Live & Operational** |
| **4. Execution Instructions** | Comprehensive reproduction instructions | `submission/EXECUTION_INSTRUCTIONS.md` | Complete |
| **5. Screencast Video Demonstration** | Video recording of code running (or streaming URL) | `submission/SCREENCAST_SCRIPT.md` + Video link | Complete |
| **6. Experimental Evidence** | Appendix documentation of experimental runs | `submission/EVIDENCE_LOGS.md` | Complete |

---

## 2. Code Archive Packaging Guide

The submission ZIP archive must be named strictly following the brief:
**`DhanBahadurGurung_17624480_Code.zip`**

To generate or rebuild the clean submission archive at any time, run:

```powershell
python scripts/create_submission_zip.py
```

This automated script creates `submission/DhanBahadurGurung_17624480_Code.zip` containing:
- All source modules (`src/`)
- Executed Jupyter Notebook (`notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb`)
- Real BGS and NASA datasets and cached elevations (`data/`)
- All 7 publication-quality output figures (`outputs/figures/`)
- All tabular reports and metrics (`outputs/reports/`)
- Automated test runner (`tests/run_pipeline.py`)
- Interactive Streamlit Web application (`app.py`)
- Pinned dependency file (`requirements.txt`)
- Reproducibility documentation (`README.md`, `submission/`)

*(Note: Bulky `.venv/`, `.git/`, and `__pycache__/` folders are automatically excluded to keep the zip compact and clean).*

---

## 3. Rubric Alignment Matrix

| Rubric Criterion (Marks) | Addressed In Repository / Deliverables | Evidence / Artifact |
| :--- | :--- | :--- |
| **1. Rigor and extent of the experiments (10%)** | 1,200 corridor units, 3 supervised classifiers (LR, RF, XGBoost), 500-iteration 95% bootstrap CIs, safety-critical metric evaluation | `tests/run_pipeline.py`, Table E.1 in `EVIDENCE_LOGS.md` |
| **2. Correct application of selected algorithms (10%)** | Appropriate selection of linear baseline (LR), ensemble bagging (RF), gradient boosting (XGBoost), balanced class weighting | `src/models.py`, `src/preprocessing.py` |
| **3. Data preparation - technical quality (10%)** | Real BGS/NERC 481-landslide inventory, NASA GLC Nepal records, 30m SRTM DEM elevation cache, zero data leakage | `src/data_generator.py`, `src/preprocessing.py` |
| **4. Evidence of running experiments in appendices (10%)** | Verbatim console transcripts, confusion matrices, full metrics, risk sector breakdown, spatial leakage verification | `submission/EVIDENCE_LOGS.md`, `outputs/` |
| **5. Discussion & evaluation of findings (15%)** | Critical assessment of spatial autocorrelation leakage (+0.150 AUC delta), life-safety 99.2% recall prioritization | `outputs/reports/spatial_leakage_analysis.json` |
| **6. Serious issue vs. toy issue (5%)** | Focus on life-safety on strategic 114 km mountain trade corridor (Arniko Highway / NH03), ground-truth geological data | Section 1 of `README.md` & `SCREENCAST_SCRIPT.md` |
| **7. Social, ethical, legal & professional considerations (5%)** | Analysis of false negative hazards, environmental ethics, open secondary data licensing, engineering advisory limits | Embedded in Report & `SCREENCAST_SCRIPT.md` |

---

## 4. Final Submission Checklist for Campus 4.0

- [ ] Run `python scripts/create_submission_zip.py` to ensure `DhanBahadurGurung_17624480_Code.zip` is freshly built.
- [ ] Record the 4-minute screencast using `submission/SCREENCAST_SCRIPT.md` and save the video link.
- [ ] Compile the final IEEE report into `DhanBahadurGurung_17624480.docx` / `.pdf` including the screencast link in the appendix.
- [ ] Upload both `DhanBahadurGurung_17624480.pdf` and `DhanBahadurGurung_17624480_Code.zip` to Campus 4.0 before the submission deadline.
