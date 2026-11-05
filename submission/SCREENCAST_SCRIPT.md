# Screencast Video Recording Script & Presentation Guide

**Coursework:** ST7072CEM / STW7072CEM Machine Learning  
**Institution:** Softwarica College of IT & E-Commerce in collaboration with Coventry University  
**Student Name:** Dhan Bahadur Gurung  
**Coventry University ID:** 17624480  
**Project Title:** Machine Learning-Based Landslide Susceptibility Mapping on Nepal's Arniko Highway  
**Target Video Duration:** 4 minutes 30 seconds (within the recommended 3–5 minute window)  
**Deliverable File Name:** `DhanBahadurGurung_17624480_Screencast.mp4` (or cloud streaming link)

---

## 1. Pre-Recording Preparation Checklist

Before initiating screen recording, ensure your recording environment is properly staged:

- [ ] **Recording Tool Ready:**
  - *Option 1 (Built-in Windows):* Windows Xbox Game Bar (`Win + Alt + R` to start/stop).
  - *Option 2 (Recommended):* [OBS Studio](https://obsproject.com/) (1920x1080 resolution, 30 FPS, mic noise suppression enabled).
  - *Option 3 (Browser/Cloud):* [Loom](https://www.loom.com/) with desktop audio and high-resolution screen sharing.
- [ ] **Clean Desktop & Browser:** Close unrelated personal tabs, disable pop-up notifications, and hide desktop icons.
- [ ] **Terminal Pre-Staged:** Open a PowerShell or Terminal window navigated to `c:\Users\Administrator\Documents\college` with `.venv` activated.
- [ ] **Browser Tabs Pre-Opened:**
  - Tab 1: Jupyter Notebook (`Arniko_Highway_Landslide_Susceptibility.ipynb`).
  - Tab 2: Terminal ready to launch Streamlit (`streamlit run app.py`).
- [ ] **Audio Test:** Perform a 10-second test recording to verify your voice is crisp, audible, and free of background noise.

---

## 2. Scene-by-Scene Storyboard & Narration Script

```
====================================================================================================
TIMECODE        SCENE / VISUAL CUE               VERBATIM SPOKEN NARRATION
====================================================================================================
0:00 - 0:45     SCENE 1: Introduction, Title    "Hello, my name is Dhan Bahadur Gurung, Coventry 
                & Problem Context                University Student ID 17624480.
                
                [Visual: Full screen showing     Today, I am presenting my Machine Learning coursework 
                the README.md or Title Slide     prototype for module ST7072CEM at Softwarica College.
                with student details, module     
                code, and highway corridor map]  My project is titled: 'Machine Learning-Based Landslide 
                                                 Susceptibility Mapping on Nepal's Arniko Highway'.
                                                 
                                                 The Arniko Highway is a 114-kilometer critical mountain 
                                                 corridor connecting Kathmandu Valley with China. It 
                                                 traverses the steep valleys of Sindhupalchok, where 
                                                 monsoon rainfall and active tectonic faults trigger 
                                                 deadly landslides every year, such as the 2014 Jure 
                                                 disaster.
                                                 
                                                 Rather than treating this as a toy machine learning 
                                                 exercise, my goal is to build a reliable, safety-critical 
                                                 decision-support model using real ground-truth data, 
                                                 while rigorously addressing the widespread issue of 
                                                 spatial autocorrelation leakage."
----------------------------------------------------------------------------------------------------
0:45 - 1:15     SCENE 2: Architecture & Real     "Let us look at the project architecture.
                Geospatial Datasets
                                                 In the project repository, we have structured our code 
                [Visual: VS Code Explorer        into clean, modular components inside the 'src' directory.
                showing data/raw, data/processed,
                src/, notebooks/, outputs/]      For our data inputs, we integrated 481 real mapped 
                                                 landslides from the British Geological Survey and NERC 
                                                 Arniko Inventory, alongside historical Nepal records 
                                                 from the NASA Global Landslide Catalog.
                                                 
                                                 We extracted real terrain elevations from NASA's 30-meter 
                                                 SRTM Digital Elevation Model, combined with slope, 
                                                 lithology, distance to active faults, and monsoon 
                                                 rainfall across 1,200 continuous highway corridor units."
----------------------------------------------------------------------------------------------------
1:15 - 2:20     SCENE 3: Automated Pipeline      "Now, let us run the complete machine learning pipeline 
                Execution in Terminal            from scratch by executing 'python tests/run_pipeline.py'.
                
                [Visual: Terminal execution      [Press Enter in Terminal]
                showing steps 1 through 6 
                printing in real time]           As you can see, the script performs data synthesis and 
                                                 auditing in Step 1.
                                                 
                                                 In Step 2, we enforce a strict spatial train-test split: 
                                                 Sectors 1 and 2—covering the lower and middle 75 kilometers—
                                                 are used for training, while Sector 3—the rugged Upper 
                                                 Arniko corridor from Barhabise to Kodari—is held out 
                                                 as an unseen spatial test bed.
                                                 
                                                 In Step 3, we train three supervised classifiers: 
                                                 Logistic Regression, Random Forest, and XGBoost.
                                                 
                                                 Notice the safety-critical metric results: In mountain 
                                                 hazard management, a False Negative—predicting safe when 
                                                 a landslide occurs—is catastrophic. Our class-weighted 
                                                 Logistic Regression achieved an astounding 99.2% Recall, 
                                                 resulting in only ONE single False Negative out of 124 
                                                 landslide points!
                                                 
                                                 In Step 4, we empirically demonstrate spatial leakage: 
                                                 Standard random cross-validation yields an artificially 
                                                 inflated ROC-AUC of 0.820. But when using spatial block 
                                                 cross-validation, performance is 0.669. This proves a 
                                                 plus 0.150 AUC optimism gap caused by spatial leakage!"
----------------------------------------------------------------------------------------------------
2:20 - 3:15     SCENE 4: Interactive Jupyter     "Next, let us examine the interactive Jupyter Notebook, 
                Notebook Deep-Dive               located under 'notebooks/Arniko_Highway_Landslide_
                                                 Susceptibility.ipynb'.
                [Visual: Browser showing the 
                executed Jupyter Notebook,       Every cell is fully executed and documented with clear 
                scrolling smoothly through the   academic commentary following the IEEE structure.
                correlation heatmap, ROC curves, 
                and SHAP summary plot]           Here you can see the feature correlation analysis, the 
                                                 bootstrap 95% confidence intervals, and the dual-column 
                                                 publication figures.
                                                 
                                                 Most importantly, we implemented game-theoretic SHAP 
                                                 interpretability. The SHAP summary plot reveals that 
                                                 slope angle and proximity to active tectonic faults are 
                                                 the primary physical triggers driving high landslide 
                                                 susceptibility, exactly corroborating published geological 
                                                 findings by Acharya & Lee and Nepal et al."
----------------------------------------------------------------------------------------------------
3:15 - 4:10     SCENE 5: Interactive Streamlit   "To make our machine learning findings immediately useful 
                Web GIS Prototype                for road maintenance engineers, I developed an interactive 
                                                 web application using Streamlit.
                [Visual: Switch to terminal, 
                type 'streamlit run app.py',     [Run 'streamlit run app.py' and switch to browser]
                and showcase the web dashboard]
                                                 On the left, we have our interactive geospatial map of the 
                                                 entire 114-kilometer Arniko Highway. We can zoom into 
                                                 Sector 3, view high-risk zones in red, and toggle the 
                                                 historical BGS ground-truth landslide overlay.
                                                 
                                                 Below the map, we provide a continuous elevation and 
                                                 hazard profile identifying critical choke points like the 
                                                 Jure landslide scar and Barhabise gorge.
                                                 
                                                 Over here is our Live Geological Hazard Simulator: A road 
                                                 engineer can adjust the slope angle, monsoon rainfall, 
                                                 and lithology using these interactive sliders.
                                                 
                                                 [Drag slope slider from 25° to 48°]
                                                 
                                                 Watch how the predicted susceptibility instantly climbs to 
                                                 High Risk, and the system automatically outputs specific 
                                                 geotechnical mitigation advisories—such as installing wire 
                                                 mesh drapery, reinforced retaining walls, and rock-sheds."
----------------------------------------------------------------------------------------------------
4:10 - 4:45     SCENE 6: Conclusion & Academic   "In conclusion, this project directly answers the coursework 
                Contribution                     objectives:
                
                [Visual: Switch to Model         1. It builds a verified, non-toy geospatial dataset 
                Comparison Benchmarks page in       grounded in real BGS and NASA inventories.
                dashboard or final summary slide]2. It proves that spatial validation is essential to avoid 
                                                    misleading performance estimates in spatial ML.
                                                 3. It prioritizes human life safety by penalizing False 
                                                    Negatives, delivering 99.2% Sensitivity.
                                                 4. And it translates predictive intelligence into an 
                                                    interpretable, practical screening tool for the 
                                                    Department of Roads, Nepal.
                                                 
                                                 Thank you very much for your time and evaluation."
====================================================================================================
```

---

## 3. Video Editing & Export Specifications

1. **Resolution:** 1080p (1920 × 1080).
2. **Aspect Ratio:** 16:9 widescreen.
3. **Audio Quality:** Clear voiceover, normalized to -14 to -16 LUFS, no background music.
4. **File Format:** `.mp4` (H.264 video codec, AAC audio codec).
5. **Target File Size:** Under 100 MB for fast uploading and playback.

---

## 4. Cloud Upload & Submission Link Setup

If your video file exceeds platform upload limits, upload it to cloud storage and submit the direct streaming URL:

### Google Drive Upload Steps:
1. Upload `DhanBahadurGurung_17624480_Screencast.mp4` to your Google Drive.
2. Right-click the uploaded file and select **Share** -> **Share**.
3. Under *General access*, change from "Restricted" to **"Anyone with the link"** and ensure the role is set to **Viewer**.
4. Click **Copy link**.
5. Paste this link into:
   - Your final Coursework Report cover page.
   - Section VIII (Appendix: Video Screencast Link) of your IEEE paper.
   - The submission text box on the Campus 4.0 submission portal.

---
*Script prepared for Dhan Bahadur Gurung (Coventry ID: 17624480) for ST7072CEM Coursework Submission.*
