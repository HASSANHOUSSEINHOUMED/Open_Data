# pipeline/transformer.py
# Module de transformation et nettoyage

import pandas as pd
import numpy as np
from typing import Callable


class DataTransformer:
    """Transforme et nettoie les données."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.transformations_applied = []
    
    def remove_duplicates(self, subset: list[str] = None) -> 'DataTransformer':
        """Supprime les doublons."""
        initial = len(self.df)
        
        if subset is None:
            subset = [self.df.columns[0]]
        
        self.df = self.df.drop_duplicates(subset=subset, keep='first')
        removed = initial - len(self.df)
        
        self.transformations_applied.append(f"Doublons supprimes: {removed}")
        return self
    
    def handle_missing_values(
        self,
        numeric_strategy: str = 'median',
        text_strategy: str = 'unknown'
    ) -> 'DataTransformer':
        """Gere les valeurs manquantes."""
        
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if numeric_strategy == 'median':
                fill_value = self.df[col].median()
            elif numeric_strategy == 'mean':
                fill_value = self.df[col].mean()
            else:
                fill_value = 0
            
            if fill_value is not None:
                null_count = self.df[col].isnull().sum()
                if null_count > 0:
                    self.df[col] = self.df[col].fillna(fill_value)
                    self.transformations_applied.append(f"{col}: {null_count} nulls remplis")
        
        text_cols = self.df.select_dtypes(include=['object']).columns
        for col in text_cols:
            null_count = self.df[col].isnull().sum()
            if null_count > 0:
                self.df[col] = self.df[col].fillna(text_strategy)
                self.transformations_applied.append(f"{col}: {null_count} nulls → '{text_strategy}'")
        
        return self
    
    def normalize_text_columns(self, columns: list[str] = None) -> 'DataTransformer':
        """Normalise les colonnes texte."""
        if columns is None:
            columns = self.df.select_dtypes(include=['object']).columns.tolist()
        
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip().str.lower()
        
        self.transformations_applied.append(f"Normalisation texte appliquee")
        return self
    
    def get_result(self) -> pd.DataFrame:
        """Retourne le DataFrame transforme."""
        return self.df
    
    def get_summary(self) -> str:
        """Retourne un resume des transformations."""
        return "\n".join([f"• {t}" for t in self.transformations_applied])