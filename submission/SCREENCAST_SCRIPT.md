# Screencast Video Recording Script & Teleprompter Guide

**Coursework:** ST7072CEM / STW7072CEM Machine Learning  
**Institution:** Softwarica College of IT & E-Commerce in collaboration with Coventry University  
**Student Name:** Dhan Bahadur Gurung  
**Coventry University ID:** 17624480  
**Project Title:** Machine Learning-Based Landslide Susceptibility Mapping on Nepal's Arniko Highway  
**Target Video Duration:** 3 to 4.5 minutes (perfectly compliant with assignment guidelines)  
**Deliverable File Name:** `DhanBahadurGurung_17624480_Screencast.mp4` (or cloud streaming URL)  
**Live Deployed App:** https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/  
**GitHub Repository:** https://github.com/dhanbg/arniko-highway-landslide-ml  

---

## 1. Quick Recording Setup

1. **Screen Resolution:** 1920 × 1080 (1080p).
2. **Audio:** Built-in headset microphone or external mic (test for 10 seconds before recording).
3. **Recording Shortcut:** Press `Win + Alt + R` (built-in Windows Xbox Game Bar recorder) or use OBS Studio.
4. **Pre-Staged Tabs:**
   - **Tab 1 (Browser):** Live Streamlit App (`https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/`).
   - **Tab 2 (Browser / VS Code):** Executed Jupyter Notebook (`notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb`).
   - **Window 2 (Terminal):** PowerShell open in `C:\Users\Administrator\Documents\college` with `.venv` active.

---

## 2. Word-For-Word Spoken Narration Script

```
========================================================================================================================
TIMECODE        SCENE / VISUAL ACTION                    VERBATIM SPOKEN NARRATION
========================================================================================================================
0:00 - 0:40     SCENE 1: Introduction & Title Slide     "Hello. My name is Dhan Bahadur Gurung, Coventry University 
                                                         Student ID 17624480.
                [Visual: Full screen showing 
                the title page of the PDF report         Today, I am presenting my Machine Learning coursework prototype 
                or README with student name, ID,         for module ST7072CEM at Softwarica College in collaboration 
                and Arniko corridor map]                 with Coventry University.

                                                         My research paper is titled: 'Machine Learning-Based Landslide 
                                                         Susceptibility Mapping on Nepal's Arniko Highway: Addressing 
                                                         Spatial Autocorrelation Leakage and Safety-Critical Decision 
                                                         Support.'

                                                         The Arniko Highway is a 114-kilometer vital arterial corridor 
                                                         connecting Kathmandu with China. It traverses steep mountain 
                                                         canyons in Sindhupalchok where monsoon rainfall and active 
                                                         faults trigger catastrophic landslides, such as the 2014 Jure 
                                                         disaster.

                                                         My project formulates a safety-critical, production-ready 
                                                         machine learning framework using real geospatial datasets, 
                                                         prioritizing zero missed hazards over naive accuracy."
------------------------------------------------------------------------------------------------------------------------
0:40 - 1:15     SCENE 2: Real Datasets & Architecture    "Let us examine the project repository and dataset integrity.

                [Visual: Switch to VS Code explorer      Unlike toy academic problems, this investigation is grounded in:
                showing data/raw, data/processed,        1. 481 real mapped landslide scarps from the British Geological 
                src/, and outputs/folders]                  Survey and NERC Arniko Inventory, combined with NASA Global 
                                                            Landslide Catalog records.
                                                         2. Real 30-meter SRTM Global Digital Elevation Data across 
                                                            1,200 continuous 100-meter corridor analysis units.
                                                         3. Multi-source environmental layers including lithological 
                                                            strength, distance to active thrust faults like the MCT, 
                                                            and GPM monsoon precipitation gradients.

                                                         All code is modularized inside the 'src' package with strict 
                                                         train-fit and test-transform separation."
------------------------------------------------------------------------------------------------------------------------
1:15 - 2:15     SCENE 3: Pipeline Terminal Execution     "Now, let us run the automated end-to-end machine learning 
                                                         pipeline in the terminal.
                [Visual: Switch to Terminal window, 
                run: python tests/run_pipeline.py        [Press Enter]
                and watch steps 1 to 6 print]
                                                         In Step 1 and 2, the pipeline audits 1,200 road units and 
                                                         enforces a strict Spatial Holdout Partition: Sectors 1 and 2 
                                                         from Dhulikhel to Barhabise—spanning 75 kilometers—are used 
                                                         for training, while Sector 3—the rugged Upper Arniko gorge 
                                                         to the Kodari border—is held out as an unseen spatial test bed.

                                                         In Step 3, we evaluate three candidate classifiers:
                                                         Notice our life-safety results: In road disaster management, 
                                                         a False Negative—missing a landslide slope—is fatal. 
                                                         Our class-weighted Logistic Regression achieved an exceptional 
                                                         99.2% Recall, detecting 123 out of 124 landslide units with 
                                                         only ONE single False Negative!

                                                         In Step 4, we empirically quantify spatial autocorrelation 
                                                         leakage: Naive random cross-validation yields an artificially 
                                                         inflated ROC-AUC of 0.820. In contrast, spatial sector block 
                                                         cross-validation yields 0.669. This exposes an empirical 
                                                         over-optimism gap of +0.150 AUC points, proving why spatial 
                                                         validation is mandatory."
------------------------------------------------------------------------------------------------------------------------
2:15 - 3:00     SCENE 4: Interactive Jupyter Notebook    "Next, let us briefly view the executed Jupyter Notebook 
                & SHAP Attribution                       under 'notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb'.

                [Visual: Scroll smoothly through the     Every cell is executed with clear markdown commentary, 95% 
                Jupyter Notebook, showing ROC/PR         bootstrap confidence intervals, and confusion matrices.
                curves and SHAP summary plot]
                                                         Crucially, we demystified the tree ensemble decisions using 
                                                         game-theoretic SHAP explanations. As seen in the SHAP beeswarm 
                                                         plot, Slope Angle is the dominant physical trigger—surging 
                                                         hazard above 35 degrees—followed by distance to active thrust 
                                                         faults and monsoon rainfall, directly corroborating published 
                                                         geological literature."
------------------------------------------------------------------------------------------------------------------------
3:00 - 4:05     SCENE 5: Live Cloud Web GIS Dashboard    "To translate these predictive findings into operational tools 
                                                         for the Department of Roads, I deployed an interactive Web GIS 
                [Visual: Switch to browser tab showing   dashboard live on Streamlit Community Cloud.
                https://arniko-highway-landslide-ml-
                axfr7wkd7kqywquzypd2xa.streamlit.app/]   Here on the live public URL:
                                                         
                                                         On the Corridor Map, we can explore all 114 kilometers with 
                                                         color-coded hazard scores, inspect high-risk units, and toggle 
                                                         historical BGS landslide overlays.

                                                         Under Route Profile, we see a continuous 114 km elevation 
                                                         cross-section highlighting historical disaster choke points 
                                                         like the 2014 Jure landslide scar and Barhabise canyon.

                                                         Here is our Live Geological Hazard Simulator: A road engineer 
                                                         can test hypothetical conditions in real time.
                                                         
                                                         [Drag Slope slider from 25° to 46°]
                                                         
                                                         Notice how the predicted susceptibility instantly updates to 
                                                         High Risk, and the system automatically generates site-specific 
                                                         engineering advisories—such as installing rockfall drapery mesh, 
                                                         subsurface drainage, and reinforced retaining structures."
------------------------------------------------------------------------------------------------------------------------
4:05 - 4:30     SCENE 6: Conclusions & Rubric Alignment  "In conclusion, this coursework project achieves all rubric 
                                                         criteria:
                [Visual: Switch back to PDF paper,       1. Real-world dataset rigor with 481 BGS landslides.
                showing IEEE 2-column layout and         2. 99.2% life-safety Recall minimizing catastrophic misses.
                Table IV model comparison]               3. Quantified proof of spatial autocorrelation leakage (+0.150).
                                                         4. Fully open-source code and a live deployed cloud prototype.

                                                         All deliverables, reproducible notebooks, and IEEE report files 
                                                         are packaged inside 'DhanBahadurGurung_17624480_Code.zip'.

                                                         Thank you very much for your time and evaluation."
========================================================================================================================
```

---

## 3. Post-Recording Quick Checklist

1. [ ] **Video Verification:** Open the saved video file and check that the audio is clear and the screen transitions are smooth.
2. [ ] **File Name:** Name the recording file:
   `DhanBahadurGurung_17624480_Screencast.mp4`
3. [ ] **Google Drive Backup:** Upload the `.mp4` to your Google Drive folder (`dhan_bahadur_gurung_17624480_screencast`), set sharing permissions to **"Anyone with the link can view"**, and verify the link opens without requiring login.
