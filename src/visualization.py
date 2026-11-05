"""
visualization.py
Visualization suite for landslide susceptibility modeling along Nepal's Arniko Highway:
1. Model performance benchmarks (ROC curves, metric comparisons, confusion matrices)
2. Model interpretability (feature importance and SHAP analysis)
3. Susceptibility mapping along the 114 km road corridor (chainage profile, 2D spatial maps, sector risk breakdown)
"""

from typing import Dict, List, Any, Tuple
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc, confusion_matrix

# Set aesthetic visual styling
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 11

ROAD_MILESTONES = [
    (0.0, "Dhulikhel"),
    (28.0, "Panchkhal"),
    (42.0, "Dolalghat (River Confluence)"),
    (58.0, "Sukute / Balephi"),
    (75.0, "Barhabise"),
    (88.0, "Larcha"),
    (103.0, "Tatopani"),
    (114.0, "Kodari Border"),
]

def plot_model_comparison_metrics(metrics_df: pd.DataFrame, output_path: str = None) -> plt.Figure:
    """Plot grouped bar chart comparing ROC-AUC, PR-AUC, Recall, and F1 across models."""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    plot_df = metrics_df[["Model", "ROC_AUC", "PR_AUC", "Recall_Sensitivity", "F1_Score"]].melt(
        id_vars="Model", var_name="Metric", value_name="Score"
    )
    
    palette = {"Logistic_Regression": "#4A90E2", "Random_Forest": "#50E3C2", "XGBoost": "#F5A623"}
    sns.barplot(data=plot_df, x="Metric", y="Score", hue="Model", palette=palette, ax=ax)
    
    ax.set_ylim(0, 1.05)
    ax.set_title("Arniko Highway Landslide Model Comparison (Spatial Validation Holdout)", fontweight="bold")
    ax.set_ylabel("Validation Score")
    ax.set_xlabel("Evaluation Metric (Safety-Critical Focus on Recall)")
    ax.legend(title="Classifier", frameon=True)
    
    for p in ax.patches:
        h = p.get_height()
        if h > 0:
            ax.annotate(f"{h:.2f}", (p.get_x() + p.get_width() / 2., h),
                        ha="center", va="bottom", fontsize=8.5, xytext=(0, 2),
                        textcoords="offset points")
            
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig


def plot_combined_roc_curves(
    roc_data: Dict[str, Tuple[np.ndarray, np.ndarray, float]],
    output_path: str = None
) -> plt.Figure:
    """Plot combined ROC curves for all models."""
    fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=300)
    
    colors = {"Logistic_Regression": "#1f77b4", "Random_Forest": "#2ca02c", "XGBoost": "#d62728"}
    
    for model_name, (fpr, tpr, score) in roc_data.items():
        color = colors.get(model_name, "#333333")
        ax.plot(fpr, tpr, lw=2.2, color=color, label=f"{model_name.replace('_', ' ')} (AUC = {score:.3f})")
        
    ax.plot([0, 1], [0, 1], color="gray", lw=1.2, linestyle="--", label="Random Chance (AUC = 0.500)")
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.02])
    ax.set_xlabel("False Positive Rate (1 - Specificity)")
    ax.set_ylabel("True Positive Rate (Recall / Sensitivity)")
    ax.set_title("Receiver Operating Characteristic (ROC) - Spatial Holdout Evaluation", fontweight="bold")
    ax.legend(loc="lower right", frameon=True, fontsize=10)
    
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig


def plot_confusion_matrices(
    confusion_dict: Dict[str, np.ndarray],
    output_path: str = None
) -> plt.Figure:
    """Plot side-by-side confusion matrices for all classifiers."""
    n_models = len(confusion_dict)
    fig, axes = plt.subplots(1, n_models, figsize=(5 * n_models, 4.2), dpi=300)
    if n_models == 1:
        axes = [axes]
        
    for ax, (model_name, cm) in zip(axes, confusion_dict.items()):
        sns.heatmap(
            cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax,
            xticklabels=["Stable", "Landslide"], yticklabels=["Stable", "Landslide"]
        )
        ax.set_title(f"{model_name.replace('_', ' ')}", fontweight="bold")
        ax.set_ylabel("Ground Truth")
        ax.set_xlabel("Predicted Label")
        
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig


def plot_feature_importances(
    feature_names: List[str],
    importances: np.ndarray,
    model_name: str = "XGBoost",
    top_n: int = 10,
    output_path: str = None
) -> plt.Figure:
    """Plot horizontal bar chart of top predictor variables."""
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)
    
    feat_df = pd.DataFrame({"Feature": feature_names, "Importance": importances})
    feat_df = feat_df.sort_values(by="Importance", ascending=False).head(top_n)
    
    # Clean feature names for clean presentation
    feat_df["Clean_Name"] = feat_df["Feature"].str.replace("_", " ").str.title()
    
    sns.barplot(data=feat_df, x="Importance", y="Clean_Name", color="#3470A3", ax=ax)
    ax.set_title(f"Top {top_n} Conditioning Factors ({model_name.replace('_', ' ')})", fontweight="bold")
    ax.set_xlabel("Relative Importance / Gini Gain")
    ax.set_ylabel("Geospatial / Environmental Predictor")
    
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig


def plot_corridor_susceptibility_profile(
    df: pd.DataFrame,
    prob_col: str = "susceptibility_score",
    output_path: str = None
) -> plt.Figure:
    """
    Plot the continuous susceptibility profile along the 114 km Arniko Highway corridor
    with color-coded risk zones (Low, Moderate, High) and geographical milestone markers.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 8), sharex=True, dpi=300, gridspec_kw={"height_ratios": [2.5, 1.2]})
    
    sorted_df = df.sort_values(by="chainage_km").reset_index(drop=True)
    chainage = sorted_df["chainage_km"].values
    scores = sorted_df[prob_col].values
    
    # 1. Top Panel: Susceptibility Score & Risk Zones
    ax1.plot(chainage, scores, color="#2c3e50", lw=1.6, label="Susceptibility Index", zorder=3)
    ax1.axhspan(0.00, 0.33, color="#2ecc71", alpha=0.22, label="Low Susceptibility (< 0.33)")
    ax1.axhspan(0.33, 0.66, color="#f39c12", alpha=0.22, label="Moderate Susceptibility (0.33 - 0.66)")
    ax1.axhspan(0.66, 1.00, color="#e74c3c", alpha=0.25, label="High Susceptibility (> 0.66)")
    
    # Mark historical landslide occurrences
    historical_ls = sorted_df[sorted_df["landslide_label"] == 1]
    ax1.scatter(
        historical_ls["chainage_km"], historical_ls[prob_col],
        color="crimson", marker="x", s=45, lw=1.8, label="Historical Landslide Point", zorder=4
    )
    
    # Add milestone vertical dashed lines
    for km, name in ROAD_MILESTONES:
        ax1.axvline(km, color="#7f8c8d", linestyle=":", lw=1.0, alpha=0.7)
        ax1.text(km, 0.98, f" {name}", rotation=90, va="top", ha="right", fontsize=8, color="#2c3e50", fontweight="semibold")

    ax1.set_ylim(-0.02, 1.05)
    ax1.set_ylabel("Predicted Landslide Susceptibility Index")
    ax1.set_title("Arniko Highway (NH03) Continuous Landslide Susceptibility Profile", fontweight="bold", fontsize=13)
    ax1.legend(loc="upper left", framealpha=0.9, fontsize=9)
    
    # 2. Bottom Panel: Terrain Slope Profile along highway
    ax2.fill_between(chainage, sorted_df["slope_deg"].values, color="#95a5a6", alpha=0.4, label="Corridor Slope (°)")
    ax2.plot(chainage, sorted_df["slope_deg"].values, color="#7f8c8d", lw=1.0)
    ax2.set_ylabel("Slope (°)")
    ax2.set_xlabel("Highway Chainage (Distance from Dhulikhel towards Kodari / China Border in km)")
    ax2.set_xlim(0, 114)
    ax2.legend(loc="upper left", fontsize=8.5)

    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig


def plot_corridor_spatial_map(
    df: pd.DataFrame,
    prob_col: str = "susceptibility_score",
    output_path: str = None
) -> plt.Figure:
    """
    Plot 2D spatial map of the highway corridor coordinates (Lat/Long),
    color-coded into Low, Moderate, High susceptibility classes, with actual landslides overlaid.
    """
    fig, ax = plt.subplots(figsize=(9.5, 8.5), dpi=300)
    
    # Assign classes
    conditions = [
        (df[prob_col] < 0.33),
        (df[prob_col] >= 0.33) & (df[prob_col] < 0.66),
        (df[prob_col] >= 0.66)
    ]
    choices = ["Low", "Moderate", "High"]
    df["susceptibility_class"] = np.select(conditions, choices, default="Moderate")
    
    palette = {"Low": "#27ae60", "Moderate": "#f39c12", "High": "#c0392b"}
    
    # Plot road alignment points
    for c_name in ["Low", "Moderate", "High"]:
        subset = df[df["susceptibility_class"] == c_name]
        ax.scatter(
            subset["longitude"], subset["latitude"],
            c=palette[c_name], label=f"{c_name} Susceptibility", s=28, alpha=0.85, edgecolors="none"
        )
        
    # Mark road milestones
    sorted_df = df.sort_values(by="chainage_km")
    for km, name in ROAD_MILESTONES:
        closest_row = sorted_df.iloc[(sorted_df["chainage_km"] - km).abs().argsort()[:1]].iloc[0]
        ax.plot(closest_row["longitude"], closest_row["latitude"], marker="o", markersize=6, color="black")
        ax.text(closest_row["longitude"] + 0.006, closest_row["latitude"], name, fontsize=8, fontweight="bold", color="#1a252f")
        
    # Mark historical landslide events
    ls_pts = df[df["landslide_label"] == 1]
    ax.scatter(
        ls_pts["longitude"], ls_pts["latitude"],
        marker="x", c="black", s=30, lw=1.2, label="Historical Landslide Record", zorder=5
    )

    ax.set_title("Arniko Highway Spatial Landslide Susceptibility Map (Dhulikhel to Kodari)", fontweight="bold")
    ax.set_xlabel("Longitude (°E)")
    ax.set_ylabel("Latitude (°N)")
    ax.legend(loc="upper left", frameon=True, framealpha=0.9)
    
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, bbox_inches="tight")
    return fig
