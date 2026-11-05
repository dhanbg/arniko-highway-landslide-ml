"""
run_pipeline.py
Automated end-to-end pipeline runner for Arniko Highway Landslide Susceptibility.
Executes data generation, spatial splitting, model training (LR, RF, XGBoost),
spatial cross-validation vs random cross-validation comparison, SHAP analysis,
susceptibility mapping, and saves all evaluation figures and tabular summaries.
"""

import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

# Ensure src is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_generator import generate_arniko_corridor_dataset
from src.spatial_cv import spatial_corridor_train_test_split
from src.preprocessing import CorridorDataPreprocessor, TARGET_COLUMN
from src.models import get_model_instances
from src.evaluate import (
    compute_classification_metrics,
    bootstrap_metric_ci,
    evaluate_spatial_vs_random_cv
)
from src.visualization import (
    plot_model_comparison_metrics,
    plot_combined_roc_curves,
    plot_confusion_matrices,
    plot_feature_importances,
    plot_corridor_susceptibility_profile,
    plot_corridor_spatial_map
)

def run_entire_pipeline():
    print("=" * 75)
    print("ARNIKO HIGHWAY (NEPAL) LANDSLIDE SUSCEPTIBILITY MODELING PIPELINE")
    print("=" * 75)
    
    output_fig_dir = os.path.join("outputs", "figures")
    output_rep_dir = os.path.join("outputs", "reports")
    os.makedirs(output_fig_dir, exist_ok=True)
    os.makedirs(output_rep_dir, exist_ok=True)
    
    # 1. Generate & Load Corridor Data
    print("\n[Step 1/6] Synthesizing / Loading Arniko Highway Corridor Dataset...")
    df = generate_arniko_corridor_dataset(n_samples=1200, random_state=42)
    os.makedirs(os.path.join("data", "processed"), exist_ok=True)
    df.to_csv(os.path.join("data", "processed", "arniko_road_landslide_dataset.csv"), index=False)
    
    total_pts = len(df)
    n_pos = int(df[TARGET_COLUMN].sum())
    pos_pct = df[TARGET_COLUMN].mean() * 100
    print(f"  Total Highway Analysis Units: {total_pts}")
    print(f"  Historically Landslide-Affected Units: {n_pos} ({pos_pct:.1f}%)")
    print(f"  Comparison / Pseudo-Absence Units: {total_pts - n_pos} ({100 - pos_pct:.1f}%)")
    
    # 2. Preprocessing & Quality Checks
    print("\n[Step 2/6] Performing Data Quality Audit and Spatial Splitting...")
    preprocessor = CorridorDataPreprocessor(scale_numerical=True)
    audit = preprocessor.check_data_quality(df)
    print(f"  Missing values found: {audit['has_missing']}")
    print(f"  Spatial coordinate duplicates: {audit['spatial_duplicates']}")
    
    # Spatial Holdout: Sector 3 (Upper Barhabise to Kodari) held out for realistic evaluation
    train_df, test_df = spatial_corridor_train_test_split(
        df, test_sector="Sector_3_Upper_Barhabise_Kodari"
    )
    print(f"  Spatial Train Units (Sectors 1 & 2): {len(train_df)}")
    print(f"  Spatial Test Units (Sector 3 - Upper Corridor): {len(test_df)}")
    
    # Strict Featurization Ordering
    preprocessor.fit(train_df)
    X_train, y_train = preprocessor.transform(train_df)
    X_test, y_test = preprocessor.transform(test_df)
    feature_names = preprocessor.feature_names_
    print(f"  Engineered Feature Dimensions: {X_train.shape[1]} features")
    
    # 3. Model Training & Validation
    print("\n[Step 3/6] Training Candidate Classifiers (LR, Random Forest, XGBoost)...")
    imbalance_ratio = float((len(y_train) - sum(y_train)) / sum(y_train))
    models = get_model_instances(class_weight_ratio=imbalance_ratio, random_state=42)
    
    results = []
    roc_dict = {}
    cm_dict = {}
    trained_models = {}
    test_probs = {}
    
    for name, model in models.items():
        print(f"  Training {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        
        # Predict on spatially held-out test corridor
        probs = model.predict_proba(X_test)[:, 1]
        test_probs[name] = probs
        
        metrics = compute_classification_metrics(y_test, probs, threshold=0.5)
        # Compute 95% Bootstrap Confidence Interval for ROC-AUC
        auc_est, auc_low, auc_high = bootstrap_metric_ci(y_test, probs, "ROC_AUC")
        rec_est, rec_low, rec_high = bootstrap_metric_ci(y_test, probs, "Recall_Sensitivity")
        
        metrics["Model"] = name
        metrics["ROC_AUC_95_CI"] = f"[{auc_low:.3f}, {auc_high:.3f}]"
        metrics["Recall_95_CI"] = f"[{rec_low:.3f}, {rec_high:.3f}]"
        results.append(metrics)
        
        # ROC curve points
        fpr, tpr, _ = roc_curve(y_test, probs)
        roc_dict[name] = (fpr, tpr, metrics["ROC_AUC"])
        
        # Confusion matrix
        y_pred = (probs >= 0.5).astype(int)
        cm_dict[name] = confusion_matrix(y_test, y_pred)
        
    results_df = pd.DataFrame(results)
    results_df = results_df[["Model", "ROC_AUC", "ROC_AUC_95_CI", "PR_AUC", "Recall_Sensitivity", "Recall_95_CI", "Precision", "F1_Score", "Specificity", "True_Positives", "False_Negatives"]]
    print("\n--- Model Performance on Held-Out Spatial Test Corridor (Sector 3) ---")
    print(results_df.to_string(index=False))
    results_df.to_csv(os.path.join(output_rep_dir, "model_comparison_metrics.csv"), index=False)
    
    # 4. Spatial Autocorrelation Leakage Demonstration
    print("\n[Step 4/6] Quantifying Spatial Autocorrelation Leakage (Random vs. Spatial CV)...")
    # Compare with XGBoost
    xgb_inst = get_model_instances(class_weight_ratio=imbalance_ratio)["XGBoost"]
    X_full, y_full = preprocessor.fit_transform(df)
    leakage_analysis = evaluate_spatial_vs_random_cv(
        xgb_inst, X_full, y_full, groups=df["spatial_sector"].values
    )
    print(f"  Random K-Fold CV ROC-AUC:  {leakage_analysis['Random_CV_ROC_AUC_Mean']:.3f} ± {leakage_analysis['Random_CV_ROC_AUC_Std']:.3f} (Inflated)")
    print(f"  Spatial Sector CV ROC-AUC: {leakage_analysis['Spatial_CV_ROC_AUC_Mean']:.3f} ± {leakage_analysis['Spatial_CV_ROC_AUC_Std']:.3f} (Realistic)")
    print(f"  Leakage / Over-optimism Gap: +{leakage_analysis['Overoptimism_Delta_AUC']:.3f} AUC points when using naive random split!")
    
    with open(os.path.join(output_rep_dir, "spatial_leakage_analysis.json"), "w") as f:
        json.dump(leakage_analysis, f, indent=4)
        
    # 5. Interpretability & Feature Importances
    print("\n[Step 5/6] Generating Interpretability & Feature Importance Analysis...")
    best_model_name = "XGBoost"
    best_model = trained_models[best_model_name]
    importances = best_model.feature_importances_
    
    # Try SHAP analysis
    try:
        import shap
        print("  Computing SHAP values for XGBoost...")
        explainer = shap.TreeExplainer(best_model)
        shap_values = explainer.shap_values(X_test)
        
        plt.figure(figsize=(9, 6), dpi=300)
        shap.summary_plot(shap_values, X_test, feature_names=feature_names, show=False)
        plt.title("SHAP Feature Importance (Held-Out Test Corridor)", fontweight="bold")
        plt.tight_layout()
        plt.savefig(os.path.join(output_fig_dir, "shap_summary_plot.png"), bbox_inches="tight")
        plt.close()
        print("  Saved: outputs/figures/shap_summary_plot.png")
    except Exception as e:
        print(f"  Note on SHAP: {e}")
        
    # 6. Susceptibility Mapping Along the Full 114 km Corridor
    print("\n[Step 6/6] Generating Corridor Susceptibility Profile and Spatial Maps...")
    # Generate full corridor predictions using best model
    full_probs = best_model.predict_proba(X_full)[:, 1]
    df["susceptibility_score"] = full_probs
    
    # Plot benchmark figures
    plot_model_comparison_metrics(results_df, os.path.join(output_fig_dir, "model_comparison_bar.png"))
    plot_combined_roc_curves(roc_dict, os.path.join(output_fig_dir, "combined_roc_curves.png"))
    plot_confusion_matrices(cm_dict, os.path.join(output_fig_dir, "confusion_matrices.png"))
    plot_feature_importances(feature_names, importances, best_model_name, top_n=10, output_path=os.path.join(output_fig_dir, "top_feature_importances.png"))
    plot_corridor_susceptibility_profile(df, "susceptibility_score", os.path.join(output_fig_dir, "arniko_highway_susceptibility_profile.png"))
    plot_corridor_spatial_map(df, "susceptibility_score", os.path.join(output_fig_dir, "arniko_highway_spatial_map.png"))
    
    # Corridor Risk Breakdown by Sector
    print("\n--- Susceptibility Distribution by Highway Sector ---")
    conditions = [
        (df["susceptibility_score"] < 0.33),
        (df["susceptibility_score"] >= 0.33) & (df["susceptibility_score"] < 0.66),
        (df["susceptibility_score"] >= 0.66)
    ]
    df["risk_level"] = np.select(
        conditions,
        ["Low (<0.33)", "Moderate (0.33-0.66)", "High (>0.66)"],
        default="Moderate (0.33-0.66)"
    )
    sector_summary = pd.crosstab(df["spatial_sector"], df["risk_level"], normalize="index") * 100
    print(sector_summary.round(1))
    sector_summary.to_csv(os.path.join(output_rep_dir, "corridor_sector_risk_breakdown.csv"))
    
    print("\n" + "=" * 75)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"All figures saved to: {output_fig_dir}")
    print(f"All summary reports saved to: {output_rep_dir}")
    print("=" * 75)

if __name__ == "__main__":
    run_entire_pipeline()
