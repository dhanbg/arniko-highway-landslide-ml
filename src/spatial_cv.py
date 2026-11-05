"""
spatial_cv.py
Spatial Validation and Spatial Block Cross-Validation module.
Prevents spatial autocorrelation data leakage by holding out entire geographic sectors
or spatial blocks along Nepal's Arniko Highway rather than random row-level splitting.
"""

from typing import List, Tuple, Generator
import numpy as np
import pandas as pd
from sklearn.model_selection import BaseCrossValidator

class SpatialSectorKFold(BaseCrossValidator):
    """
    Spatial Cross-Validator that splits dataset based on spatial sectors / geographic zones.
    Each fold completely holds out one spatial sector to simulate model generalization to
    unseen road corridors or geographically distinct sectors.
    """
    def __init__(self, sector_column: str = "spatial_sector"):
        self.sector_column = sector_column

    def get_n_splits(self, X: pd.DataFrame = None, y=None, groups=None) -> int:
        if groups is not None:
            return len(np.unique(groups))
        if X is not None and self.sector_column in X.columns:
            return X[self.sector_column].nunique()
        return 3

    def split(self, X: pd.DataFrame, y=None, groups=None) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        if groups is None:
            if self.sector_column not in X.columns:
                raise ValueError(f"Column '{self.sector_column}' not found in X.")
            groups = X[self.sector_column].values

        unique_sectors = np.unique(groups)
        indices = np.arange(len(X))

        for test_sector in unique_sectors:
            test_mask = (groups == test_sector)
            train_mask = ~test_mask
            yield indices[train_mask], indices[test_mask]


def spatial_corridor_train_test_split(
    df: pd.DataFrame,
    test_sector: str = "Sector_3_Upper_Barhabise_Kodari"
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Splits the dataset into spatial training sectors and a held-out test sector.
    Default held-out test sector is Sector 3 (Upper Arniko: Barhabise to Kodari),
    which is the most rugged, high-relief, and seismically vulnerable section.
    
    Parameters:
        df (pd.DataFrame): Input Arniko highway dataset.
        test_sector (str): Sector designated as held-out test corridor.
        
    Returns:
        train_df, test_df (Tuple[pd.DataFrame, pd.DataFrame])
    """
    test_df = df[df["spatial_sector"] == test_sector].copy().reset_index(drop=True)
    train_df = df[df["spatial_sector"] != test_sector].copy().reset_index(drop=True)
    
    return train_df, test_df
