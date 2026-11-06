# start_demo.ps1
# One-click staging script for recording the ST7072CEM screencast video demonstration.
# Prepares terminal, opens the live Streamlit Cloud app, and launches Jupyter Notebook.

$baseDir = "C:\Users\Administrator\Documents\college"
Set-Location $baseDir

Write-Host "===========================================================================" -ForegroundColor Cyan
Write-Host " ST7072CEM SCREENCAST VIDEO RECORDING LAUNCHER" -ForegroundColor Yellow
Write-Host " Student: Dhan Bahadur Gurung | Coventry ID: 17624480" -ForegroundColor White
Write-Host "===========================================================================" -ForegroundColor Cyan

# 1. Activate Virtual Environment
Write-Host "`n[1/3] Activating Python Virtual Environment..." -ForegroundColor Green
$venvActivate = Join-Path $baseDir ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    & $venvActivate
    Write-Host "  Virtual environment active: $env:VIRTUAL_ENV" -ForegroundColor Gray
}

# 2. Open Live Deployed Streamlit Cloud App in Browser
Write-Host "[2/3] Opening Live Deployed Streamlit Web Dashboard in Browser..." -ForegroundColor Green
$liveUrl = "https://arniko-highway-landslide-ml-axfr7wkd7kqywquzypd2xa.streamlit.app/"
Start-Process $liveUrl
Write-Host "  Opened: $liveUrl" -ForegroundColor Gray

# 3. Print Ready Instructions
Write-Host "`n[3/3] System Ready for Recording!" -ForegroundColor Green
Write-Host "---------------------------------------------------------------------------" -ForegroundColor White
Write-Host "RECORDING STEPS (Press Win + Alt + R to start recording):" -ForegroundColor Yellow
Write-Host "  Step 1: Speak Scene 1 (Intro, Title, Student ID: 17624480)" -ForegroundColor White
Write-Host "  Step 2: Show project files in VS Code / File Explorer" -ForegroundColor White
Write-Host "  Step 3: Run pipeline test in terminal:  python tests\run_pipeline.py" -ForegroundColor Cyan
Write-Host "  Step 4: Switch to browser tab to showcase Live Deployed Web Dashboard" -ForegroundColor Cyan
Write-Host "  Step 5: Drag sliders in Live Risk Simulator to show real-time ML inference" -ForegroundColor Cyan
Write-Host "  Step 6: Conclude with academic contributions and 99.2% Sensitivity" -ForegroundColor White
Write-Host "---------------------------------------------------------------------------" -ForegroundColor White
Write-Host "`nPress any key to execute pipeline test now, or run it manually during recording..." -ForegroundColor Magenta
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
python tests\run_pipeline.py

