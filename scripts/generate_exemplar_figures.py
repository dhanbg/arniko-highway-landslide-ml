"""
generate_exemplar_figures.py
Generates additional publication-grade figures aligned with the Softwarica ST7072CEM exemplar paper:
1. conceptual_base_papers.png: Conceptual summaries of base papers [1] Acharya & Lee (2019), [2] Nepal et al. (2019), and [3] Bhattarai & Bhandary (2025).
2. spatial_partition_audit.png: Data partition and class label distribution (Sectors 1 & 2 Train vs. Sector 3 Spatial Holdout Test).
3. model_result_cards.png: Individual model confusion matrix + metrics result cards for LR, RF, and XGBoost.
4. dashboard_overview_card.png: Visual overview of the Streamlit GIS Decision Support system.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import seaborn as sns

output_dir = os.path.join(os.path.dirname(__file__), "..", "outputs", "figures")
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------------
# Figure 1: Conceptual Summaries of Base Papers
# -------------------------------------------------------------------------
def generate_base_paper_summary():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), dpi=300)
    plt.subplots_adjust(wspace=0.25)
    
    # Panel A: Acharya & Lee (2019)
    ax = axes[0]
    ax.set_facecolor("#F8F9FA")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.text(0.5, 9.2, "A | Acharya & Lee (2019)", fontsize=13, fontweight="bold", color="#1A365D")
    ax.text(0.5, 8.4, "Arniko Highway: Bivariate Susceptibility", fontsize=10, fontstyle="italic", color="#4A5568")
    
    # Diagram boxes
    p1 = patches.FancyBboxPatch((0.5, 5.0), 3.8, 2.2, boxstyle="round,pad=0.2", facecolor="#EBF8FF", edgecolor="#3182CE", lw=1.5)
    ax.add_patch(p1)
    ax.text(2.4, 6.1, "481 Mapped\nLandslides", ha="center", va="center", fontsize=10, fontweight="bold", color="#2B6CB0")
    
    ax.annotate("", xy=(5.2, 6.1), xytext=(4.3, 6.1), arrowprops=dict(arrowstyle="->", lw=2, color="#4A5568"))
    
    p2 = patches.FancyBboxPatch((5.2, 5.0), 4.2, 2.2, boxstyle="round,pad=0.2", facecolor="#EBF8FF", edgecolor="#3182CE", lw=1.5)
    ax.add_patch(p2)
    ax.text(7.3, 6.1, "11 Conditioning\nFactors (RF & PR)", ha="center", va="center", fontsize=10, fontweight="bold", color="#2B6CB0")
    
    ax.annotate("", xy=(5.0, 3.2), xytext=(5.0, 4.8), arrowprops=dict(arrowstyle="->", lw=2, color="#4A5568"))
    
    p3 = patches.FancyBboxPatch((2.0, 1.2), 6.0, 1.8, boxstyle="round,pad=0.2", facecolor="#FEFCBF", edgecolor="#D69E2E", lw=1.5)
    ax.add_patch(p3)
    ax.text(5.0, 2.1, "Prediction-Rate AUC = 0.581\nBivariate statistical model", ha="center", va="center", fontsize=10.5, fontweight="bold", color="#744210")

    # Panel B: Nepal et al. (2019)
    ax = axes[1]
    ax.set_facecolor("#F8F9FA")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.text(0.5, 9.2, "B | Nepal et al. (2019)", fontsize=13, fontweight="bold", color="#1A365D")
    ax.text(0.5, 8.4, "Bhote Koshi Basin: Multivariable GIS", fontsize=10, fontstyle="italic", color="#4A5568")
    
    # Bar representation of earthquake damage
    categories = ["Arniko Highway", "Pasang Lhamu"]
    values = [35, 89]
    colors = ["#3182CE", "#DD6B20"]
    y_pos = [5.5, 3.2]
    for cat, val, col, y in zip(categories, values, colors, y_pos):
        ax.barh(y, val / 15.0, height=1.2, left=3.5, color=col, edgecolor="#2D3748", lw=1)
        ax.text(0.5, y, cat, va="center", fontsize=10.5, fontweight="bold", color="#2D3748")
        ax.text(3.7 + val/15.0, y, f"{val} landslides", va="center", fontsize=10, fontweight="bold", color=col)
    ax.text(0.5, 1.2, "2015 Gorkha Earthquake Coseismic Damage\nDocumented structural vulnerability along corridor", fontsize=9.5, fontstyle="italic", color="#4A5568")

    # Panel C: Bhattarai & Bhandary (2025)
    ax = axes[2]
    ax.set_facecolor("#F8F9FA")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.text(0.5, 9.2, "C | Bhattarai & Bhandary (2025)", fontsize=13, fontweight="bold", color="#1A365D")
    ax.text(0.5, 8.4, "Nepal Himalaya: ML Ensemble Comparison", fontsize=10, fontstyle="italic", color="#4A5568")
    
    ml_models = ["XGBoost", "Random Forest", "Logistic Reg."]
    aucs = [0.881, 0.844, 0.742]
    cols = ["#38A169", "#48BB78", "#A0AEC0"]
    y_pos = [6.2, 4.4, 2.6]
    for m, a, c, y in zip(ml_models, aucs, cols, y_pos):
        ax.barh(y, a * 6.5, height=1.1, left=3.0, color=c, edgecolor="#2D3748", lw=1)
        ax.text(0.3, y, m, va="center", fontsize=10, fontweight="bold", color="#2D3748")
        ax.text(3.2 + a * 6.5, y, f"AUC {a:.3f}", va="center", fontsize=9.5, fontweight="bold", color="#2D3748")
    ax.text(0.5, 0.8, "Pioneered spatial validation & SHAP in Nepal\nEnsembles capture high-relief terrain thresholds", fontsize=9.5, fontstyle="italic", color="#4A5568")

    plt.tight_layout()
    fig_path = os.path.join(output_dir, "conceptual_base_papers.png")
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {fig_path}")

# -------------------------------------------------------------------------
# Figure 2: Auditable Data Partition and Class Composition
# -------------------------------------------------------------------------
def generate_spatial_partition_audit():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
    
    # Left: Road Analysis Units Count by Partition
    ax = axes[0]
    partitions = ["Training Corridor\n(Sectors 1 & 2: km 0–75)", "Spatial Test Corridor\n(Sector 3: km 75–114)"]
    counts = [789, 411]
    colors = ["#2B6CB0", "#38A169"]
    bars = ax.bar(partitions, counts, color=colors, width=0.5, edgecolor="#1A365D", lw=1.5)
    ax.set_ylabel("Number of 100m Road Units", fontsize=11, fontweight="bold")
    ax.set_title("Corridor Road Units by Spatial Partition", fontsize=12, fontweight="bold", pad=12)
    ax.set_ylim(0, 950)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 20, f"{h:,} units\n({h/1200*100:.1f}%)", ha="center", va="bottom", fontsize=10.5, fontweight="bold")

    # Right: Class Composition (Landslide vs Pseudo-Absence)
    ax = axes[1]
    categories = ["Training Corridor\n(Sectors 1 & 2)", "Spatial Test Corridor\n(Sector 3)"]
    positives = [220, 124]
    negatives = [569, 287]
    
    x = np.arange(len(categories))
    width = 0.35
    
    r1 = ax.bar(x - width/2, negatives, width, label="Comparison / Pseudo-Absence (y=0)", color="#4A5568", edgecolor="#1A202C", lw=1.2)
    r2 = ax.bar(x + width/2, positives, width, label="Historically Landslide-Affected (y=1)", color="#E53E3E", edgecolor="#742A2A", lw=1.2)
    
    ax.set_ylabel("Number of Road Units", fontsize=11, fontweight="bold")
    ax.set_title("Class Composition Across Spatial Partitions", fontsize=12, fontweight="bold", pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10.5, fontweight="bold")
    ax.set_ylim(0, 700)
    ax.legend(frameon=True, facecolor="#F7FAFC", edgecolor="#CBD5E0", fontsize=9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    
    for bar in r1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 15, f"{h}", ha="center", va="bottom", fontsize=10, fontweight="bold", color="#4A5568")
    for bar in r2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 15, f"{h}", ha="center", va="bottom", fontsize=10, fontweight="bold", color="#E53E3E")

    plt.tight_layout()
    fig_path = os.path.join(output_dir, "spatial_partition_audit.png")
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {fig_path}")

# -------------------------------------------------------------------------
# Figure 3: Model Performance Cards with Confusion Matrices (LR, RF, XGB)
# -------------------------------------------------------------------------
def generate_model_result_cards():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2), dpi=300)
    
    models_data = [
        {
            "name": "Logistic Regression",
            "cm": np.array([[6, 281], [1, 123]]),
            "acc": 0.3139,
            "prec": 0.3045,
            "rec": 0.9919,
            "f1": 0.4659,
            "auc": 0.5250,
            "thresh": 0.50,
            "fn": 1,
            "color": "#3182CE"
        },
        {
            "name": "Random Forest",
            "cm": np.array([[27, 260], [7, 117]]),
            "acc": 0.3504,
            "prec": 0.3095,
            "rec": 0.9435,
            "f1": 0.4661,
            "auc": 0.5268,
            "thresh": 0.46,
            "fn": 7,
            "color": "#38A169"
        },
        {
            "name": "XGBoost",
            "cm": np.array([[27, 260], [7, 117]]),
            "acc": 0.3504,
            "prec": 0.3103,
            "rec": 0.9435,
            "f1": 0.4671,
            "auc": 0.5283,
            "thresh": 0.46,
            "fn": 7,
            "color": "#DD6B20"
        }
    ]
    
    for i, m in enumerate(models_data):
        ax = axes[i]
        cm = m["cm"]
        
        # Plot confusion matrix heatmap
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax,
                    annot_kws={"size": 15, "weight": "bold"},
                    xticklabels=["Predicted Safe", "Predicted Landslide"],
                    yticklabels=["Actual Safe", "Actual Landslide"],
                    linewidths=1.5, linecolor="#CBD5E0")
        
        ax.set_title(f"{m['name']}\nHeld-Out Test (Sector 3, N=411)", fontsize=12, fontweight="bold", pad=10, color="#1A365D")
        ax.set_xlabel("Predicted Label", fontsize=10, fontweight="bold")
        ax.set_ylabel("Actual Label", fontsize=10, fontweight="bold")
        
        # Metrics summary box below
        metrics_text = (
            f"ROC-AUC: {m['auc']:.4f}\n"
            f"Recall (Sensitivity): {m['rec']*100:.1f}%\n"
            f"Precision: {m['prec']:.4f} | F1: {m['f1']:.4f}\n"
            f"False Negatives: {m['fn']} | True Positives: {cm[1,1]}"
        )
        ax.text(0.5, -0.32, metrics_text, transform=ax.transAxes, ha="center", va="top",
                fontsize=9.5, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.5", facecolor="#F7FAFC", edgecolor=m['color'], lw=1.5))
    
    plt.tight_layout()
    fig_path = os.path.join(output_dir, "model_result_cards.png")
    plt.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {fig_path}")

if __name__ == "__main__":
    generate_base_paper_summary()
    generate_spatial_partition_audit()
    generate_model_result_cards()

