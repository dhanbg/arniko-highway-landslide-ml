"""
create_submission_zip.py
Automated packaging script for ST7072CEM Coursework Submission.
Packages all required code, notebooks, datasets, figures, and execution guides into
a clean, validated ZIP archive named strictly in accordance with Coventry / Softwarica guidelines:
'DhanBahadurGurung_17624480_Code.zip'.
"""

import os
import sys
import zipfile
import shutil
from pathlib import Path

def create_submission_package():
    base_dir = Path(__file__).resolve().parent.parent
    submission_dir = base_dir / "submission"
    submission_dir.mkdir(parents=True, exist_ok=True)
    
    zip_filename = "DhanBahadurGurung_17624480_Code.zip"
    zip_output_path = submission_dir / zip_filename
    root_folder_in_zip = "DhanBahadurGurung_17624480"
    
    print("=" * 75)
    print("ST7072CEM COURSEWORK SUBMISSION PACKAGE GENERATOR")
    print(f"Student: Dhan Bahadur Gurung | Coventry ID: 17624480")
    print(f"Target Archive: {zip_output_path}")
    print("=" * 75)
    
    # Items to include (relative to project base_dir)
    include_paths = [
        "README.md",
        "requirements.txt",
        "app.py",
        "DhanBahadurGurung_17624480.md",
        "submission/DhanBahadurGurung_17624480.pdf",
        "submission/DhanBahadurGurung_17624480.docx",
        "data/raw/arniko_bgs_landslides_real.csv",
        "data/raw/Arniko_Landslide_Inventory_BGS.zip",
        "data/raw/arniko_bgs_shapefile",
        "data/raw/cached_srtm_elevations.json",
        "data/raw/nasa_glc_nepal_real.csv",
        "data/raw/arniko_highway_corridor_raw.csv",
        "data/processed/arniko_road_landslide_dataset.csv",
        "src",
        "notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb",
        "outputs/figures",
        "outputs/reports",
        "submission/EXECUTION_INSTRUCTIONS.md",
        "submission/SCREENCAST_SCRIPT.md",
        "submission/EVIDENCE_LOGS.md",
        "submission/README_SUBMISSION.md",
        "tests/run_pipeline.py",
        "scripts/create_submission_zip.py",
        "scripts/build_ieee_docx.py"
    ]
    
    # Ignore patterns
    ignore_extensions = {".pyc", ".pyo", ".pyd"}
    ignore_dirs = {".venv", "__pycache__", ".git", ".agents", ".claude", "scratch"}

    # Remove previous zip if it exists
    if zip_output_path.exists():
        zip_output_path.unlink()
        print(f"Removed existing archive: {zip_output_path}")

    files_added = 0
    total_uncompressed_bytes = 0

    print("\n[Step 1/3] Packaging project files into ZIP archive...")
    with zipfile.ZipFile(zip_output_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for rel_path_str in include_paths:
            full_path = base_dir / rel_path_str
            if not full_path.exists():
                print(f"  [WARNING] Path not found, skipping: {rel_path_str}")
                continue
                
            if full_path.is_file():
                arcname = f"{root_folder_in_zip}/{rel_path_str.replace('\\', '/')}"
                zipf.write(full_path, arcname=arcname)
                files_added += 1
                total_uncompressed_bytes += full_path.stat().st_size
                print(f"  [+] File: {rel_path_str}")
            elif full_path.is_dir():
                for root, dirs, files in os.walk(full_path):
                    # Filter out ignored dirs
                    dirs[:] = [d for d in dirs if d not in ignore_dirs]
                    
                    for f in files:
                        file_p = Path(root) / f
                        if file_p.suffix in ignore_extensions:
                            continue
                        if file_p.name == zip_filename:
                            continue
                            
                        rel_file = file_p.relative_to(base_dir)
                        arcname = f"{root_folder_in_zip}/{str(rel_file).replace('\\', '/')}"
                        zipf.write(file_p, arcname=arcname)
                        files_added += 1
                        total_uncompressed_bytes += file_p.stat().st_size
                print(f"  [+] Directory: {rel_path_str}")

    compressed_bytes = zip_output_path.stat().st_size
    print("\n[Step 2/3] Verifying ZIP archive integrity...")
    with zipfile.ZipFile(zip_output_path, "r") as test_zip:
        bad_file = test_zip.testzip()
        if bad_file:
            raise RuntimeError(f"Corrupt file detected in zip archive: {bad_file}")
        namelist = test_zip.namelist()

    # Step 3: Print summary
    print("\n[Step 3/3] Packaging Verification Summary:")
    print(f"  Total Files Archived: {files_added}")
    print(f"  Uncompressed Size:    {total_uncompressed_bytes / (1024 * 1024):.2f} MB")
    print(f"  Compressed ZIP Size:  {compressed_bytes / (1024 * 1024):.2f} MB")
    print(f"  Compression Ratio:    {(1 - (compressed_bytes / total_uncompressed_bytes)) * 100:.1f}% space saved")
    print(f"  Archive Location:     {zip_output_path}")

    # Verify key deliverables exist inside archive
    critical_checkpoints = [
        f"{root_folder_in_zip}/notebooks/Arniko_Highway_Landslide_Susceptibility.ipynb",
        f"{root_folder_in_zip}/app.py",
        f"{root_folder_in_zip}/src/models.py",
        f"{root_folder_in_zip}/tests/run_pipeline.py",
        f"{root_folder_in_zip}/requirements.txt",
        f"{root_folder_in_zip}/submission/SCREENCAST_SCRIPT.md",
        f"{root_folder_in_zip}/submission/EXECUTION_INSTRUCTIONS.md"
    ]
    all_present = all(cp in namelist for cp in critical_checkpoints)
    if all_present:
        print("\n>>> ALL CRITICAL DELIVERABLES VERIFIED INSIDE SUBMISSION ARCHIVE <<<")
    else:
        print("\n>>> WARNING: SOME CRITICAL FILES ARE MISSING FROM ARCHIVE <<<")

    print("=" * 75)
    return str(zip_output_path)

if __name__ == "__main__":
    create_submission_package()
