# utils/data.py
# Module de chargement des donnees depuis Parquet

import duckdb
import pandas as pd
from pathlib import Path


def load_data(filepath: str | Path) -> pd.DataFrame:
    """
    Charge les donnees depuis un fichier Parquet.
    
    DuckDB offre de meilleures performances que pandas pour les gros fichiers.
    
    Args:
        filepath: Chemin vers le fichier Parquet
    
    Returns:
        DataFrame pandas avec les donnees chargees
    """
    con = duckdb.connect()
    df = con.execute(f"SELECT * FROM read_parquet('{filepath}')").df()
    con.close()
    return df


def get_data_summary(df: pd.DataFrame) -> dict:
    """
    Retourne un resume des donnees pour le contexte du chatbot.
    
    Args:
        df: DataFrame source
    
    Returns:
        Dict avec rows, columns, types, sample
    """
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "sample": df.head(5).to_dict()
    }


def filter_data(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Applique des filtres au DataFrame.
    
    Permet de filtrer par colonne et valeur(s).
    
    Args:
        df: DataFrame source
        filters: Dict de {colonne: valeur ou liste}
    
    Returns:
        DataFrame filtre
    """
    df_filtered = df.copy()
    
    for col, value in filters.items():
        if col not in df_filtered.columns:
            continue
        if isinstance(value, list):
            df_filtered = df_filtered[df_filtered[col].isin(value)]
        else:
            df_filtered = df_filtered[df_filtered[col] == value]
    
    return df_filtered