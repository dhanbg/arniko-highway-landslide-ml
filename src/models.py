"""
models.py
Defines the three supervised learning algorithms specified in the proposal:
1. Logistic Regression (interpretable linear baseline)
2. Random Forest (ensemble bagging capturing non-linear interactions)
3. XGBoost (gradient boosting benchmark)

Includes class weighting mechanisms to address real-world landslide imbalance.
"""

from typing import Dict, Any
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

def get_model_instances(class_weight_ratio: float = 1.0, random_state: int = 42) -> Dict[str, Any]:
    """
    Instantiate the three baseline candidate models with appropriate parameters
    and class weighting for imbalance mitigation.
    
    Parameters:
        class_weight_ratio (float): Ratio of negative to positive samples (for scale_pos_weight).
        random_state (int): Random seed.
        
    Returns:
        Dict[str, Any]: Dictionary mapping model names to initialized classifier instances.
    """
    models = {
        "Logistic_Regression": LogisticRegression(
            C=1.0,
            class_weight="balanced",
            solver="lbfgs",
            max_iter=1000,
            random_state=random_state
        ),
        "Random_Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            min_samples_split=5,
            min_samples_leaf=2,
            class_weight="balanced",
            n_jobs=-1,
            random_state=random_state
        ),
        "XGBoost": xgb.XGBClassifier(
            n_estimators=150,
            max_depth=4,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            scale_pos_weight=class_weight_ratio,
            eval_metric="logloss",
            random_state=random_state
        )
    }
    return models


def get_hyperparameter_grids() -> Dict[str, Dict[str, list]]:
    """Return hyperparameter search grids for tuning under Spatial CV."""
    grids = {
        "Logistic_Regression": {
            "C": [0.01, 0.1, 1.0, 10.0],
            "penalty": ["l2"]
        },
        "Random_Forest": {
            "n_estimators": [100, 200, 300],
            "max_depth": [5, 8, 12, None],
            "min_samples_split": [2, 5, 10]
        },
        "XGBoost": {
            "n_estimators": [100, 150, 250],
            "max_depth": [3, 4, 6],
            "learning_rate": [0.01, 0.05, 0.1],
            "subsample": [0.7, 0.8, 1.0]
        }
    }
    return grids
