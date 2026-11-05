"""
preprocessing.py
Data preprocessing, cleaning, feature encoding, and scaling module.
Implements strict featurization ordering to prevent leakage:
preprocessors are fitted strictly on the training partition and applied to test data.
"""

from typing import List, Tuple, Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

NUMERICAL_FEATURES = [
    "elevation_m",
    "slope_deg",
    "aspect_deg",
    "plan_curvature",
    "twi",
    "dist_to_river_m",
    "dist_to_fault_km",
    "rainfall_annual_mm",
]

CATEGORICAL_FEATURES = [
    "land_cover",
    "lithology",
]

METADATA_COLUMNS = [
    "sample_id",
    "chainage_km",
    "latitude",
    "longitude",
    "spatial_sector",
]

TARGET_COLUMN = "landslide_label"


class CorridorDataPreprocessor:
    """
    Encapsulates feature scaling, categorical one-hot encoding, and data checks.
    Guarantees strict separation of training statistics from test evaluation.
    """
    def __init__(self, scale_numerical: bool = True):
        self.scale_numerical = scale_numerical
        self.scaler: Optional[StandardScaler] = None
        self.encoder: Optional[OneHotEncoder] = None
        self.feature_names_: List[str] = []

    def check_data_quality(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Perform sanity checks, missing value audit, and duplicate checks."""
        missing = df.isnull().sum().to_dict()
        duplicates = df.duplicated(subset=["latitude", "longitude"]).sum()
        class_dist = df[TARGET_COLUMN].value_counts(normalize=True).to_dict()
        
        return {
            "total_records": len(df),
            "missing_values": missing,
            "has_missing": any(v > 0 for v in missing.values()),
            "spatial_duplicates": int(duplicates),
            "class_distribution": class_dist,
        }

    def fit(self, train_df: pd.DataFrame) -> "CorridorDataPreprocessor":
        """Fit preprocessors using training data exclusively."""
        # 1. Fit OneHotEncoder on categorical variables
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        self.encoder.fit(train_df[CATEGORICAL_FEATURES])
        encoded_cat_names = list(self.encoder.get_feature_names_out(CATEGORICAL_FEATURES))

        # 2. Fit StandardScaler on continuous variables
        if self.scale_numerical:
            self.scaler = StandardScaler()
            self.scaler.fit(train_df[NUMERICAL_FEATURES])

        self.feature_names_ = NUMERICAL_FEATURES + encoded_cat_names
        return self

    def transform(self, df: pd.DataFrame) -> Tuple[np.ndarray, Optional[np.ndarray]]:
        """Transform a dataframe using fitted encoders and scalers."""
        if self.encoder is None:
            raise RuntimeError("Preprocessor must be fitted before transforming data.")

        # Transform numerical features
        if self.scale_numerical and self.scaler is not None:
            num_data = self.scaler.transform(df[NUMERICAL_FEATURES])
        else:
            num_data = df[NUMERICAL_FEATURES].values

        # Transform categorical features
        cat_data = self.encoder.transform(df[CATEGORICAL_FEATURES])

        # Concatenate features
        X = np.hstack([num_data, cat_data])

        # Extract target if present
        y = df[TARGET_COLUMN].values if TARGET_COLUMN in df.columns else None

        return X, y

    def fit_transform(self, train_df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Fit on train_df and transform in one step."""
        self.fit(train_df)
        return self.transform(train_df)
