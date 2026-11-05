"""
evaluate.py
Evaluation metrics, spatial cross-validation runner, bootstrap confidence intervals,
and comparison between random vs. spatial cross-validation to expose spatial autocorrelation.
"""

from typing import Dict, Any, List, Tuple
import numpy as np
import pandas as pd
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    recall_score,
    precision_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    precision_recall_curve
)
from sklearn.model_selection import KFold
from .spatial_cv import SpatialSectorKFold

def compute_classification_metrics(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float = 0.5
) -> Dict[str, float]:
    """
    Compute comprehensive classification metrics focusing on safety-critical evaluation.
    Recall is prioritized to avoid dangerous False Negatives along mountain road corridors.
    """
    y_pred = (y_prob >= threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel() if cm.shape == (2, 2) else (0, 0, 0, 0)
    
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    recall = recall_score(y_true, y_pred, zero_division=0)
    precision = precision_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    roc_auc = roc_auc_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 0.5
    pr_auc = average_precision_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 0.0

    return {
        "ROC_AUC": float(roc_auc),
        "PR_AUC": float(pr_auc),
        "Recall_Sensitivity": float(recall),
        "Precision": float(precision),
        "Specificity": float(specificity),
        "F1_Score": float(f1),
        "True_Positives": int(tp),
        "False_Negatives": int(fn),
        "False_Positives": int(fp),
        "True_Negatives": int(tn)
    }


def bootstrap_metric_ci(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    metric_name: str = "ROC_AUC",
    n_bootstraps: int = 500,
    alpha: float = 0.05,
    random_state: int = 42
) -> Tuple[float, float, float]:
    """
    Compute mean and 95% bootstrap confidence intervals for a given metric.
    Returns: (point_estimate, ci_lower, ci_upper)
    """
    np.random.seed(random_state)
    bootstrapped_scores = []
    n = len(y_true)
    
    for _ in range(n_bootstraps):
        idx = np.random.choice(n, size=n, replace=True)
        if len(np.unique(y_true[idx])) < 2:
            continue
        if metric_name == "ROC_AUC":
            score = roc_auc_score(y_true[idx], y_prob[idx])
        elif metric_name == "Recall_Sensitivity":
            score = recall_score(y_true[idx], (y_prob[idx] >= 0.5).astype(int), zero_division=0)
        elif metric_name == "F1_Score":
            score = f1_score(y_true[idx], (y_prob[idx] >= 0.5).astype(int), zero_division=0)
        else:
            score = roc_auc_score(y_true[idx], y_prob[idx])
        bootstrapped_scores.append(score)
        
    ci_lower = float(np.percentile(bootstrapped_scores, 100 * (alpha / 2)))
    ci_upper = float(np.percentile(bootstrapped_scores, 100 * (1 - alpha / 2)))
    point_est = float(np.mean(bootstrapped_scores))
    
    return point_est, ci_lower, ci_upper


def evaluate_spatial_vs_random_cv(
    model,
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray
) -> Dict[str, Any]:
    """
    Compares Standard Random K-Fold vs Spatial Sector K-Fold for the same model.
    Empirically demonstrates the impact of spatial autocorrelation leakage.
    """
    # 1. Random 3-Fold
    rf_cv = KFold(n_splits=3, shuffle=True, random_state=42)
    random_aucs = []
    random_recalls = []
    for tr_idx, val_idx in rf_cv.split(X, y):
        m = model.__class__(**model.get_params())
        m.fit(X[tr_idx], y[tr_idx])
        prob = m.predict_proba(X[val_idx])[:, 1]
        random_aucs.append(roc_auc_score(y[val_idx], prob))
        random_recalls.append(recall_score(y[val_idx], (prob >= 0.5).astype(int), zero_division=0))

    # 2. Spatial Sector 3-Fold
    spatial_aucs = []
    spatial_recalls = []
    unique_groups = np.unique(groups)
    for test_group in unique_groups:
        tr_mask = (groups != test_group)
        val_mask = (groups == test_group)
        m = model.__class__(**model.get_params())
        m.fit(X[tr_mask], y[tr_mask])
        prob = m.predict_proba(X[val_mask])[:, 1]
        spatial_aucs.append(roc_auc_score(y[val_mask], prob))
        spatial_recalls.append(recall_score(y[val_mask], (prob >= 0.5).astype(int), zero_division=0))

    return {
        "Random_CV_ROC_AUC_Mean": float(np.mean(random_aucs)),
        "Random_CV_ROC_AUC_Std": float(np.std(random_aucs)),
        "Spatial_CV_ROC_AUC_Mean": float(np.mean(spatial_aucs)),
        "Spatial_CV_ROC_AUC_Std": float(np.std(spatial_aucs)),
        "Overoptimism_Delta_AUC": float(np.mean(random_aucs) - np.mean(spatial_aucs)),
        "Spatial_CV_Recall_Mean": float(np.mean(spatial_recalls)),
    }
