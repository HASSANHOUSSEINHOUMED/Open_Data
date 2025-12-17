# tests/test_transformer.py
# Tests pour le transformer

import pytest
import pandas as pd
import numpy as np
from pipeline.transformer import DataTransformer


class TestDataTransformer:
    """Tests pour DataTransformer."""
    
    @pytest.fixture
    def sample_df(self):
        """DataFrame de test."""
        return pd.DataFrame({
            'city': ['Paris', 'Lyon', 'Paris', 'Marseille'],
            'temperature': [15.0, 12.0, 15.0, 20.0],
            'humidity': [65, None, 65, 75],
            'weather': ['  Nuageux  ', None, 'Nuageux', 'Ensoleille'],
        })
    
    def test_remove_duplicates(self, sample_df):
        """Test la suppression des doublons."""
        transformer = DataTransformer(sample_df)
        result = transformer.remove_duplicates(['city']).get_result()
        
        assert len(result) == 3
        assert result['city'].nunique() == 3
    
    def test_handle_missing_values_median(self, sample_df):
        """Test le remplacement par la mediane."""
        transformer = DataTransformer(sample_df)
        result = transformer.handle_missing_values(numeric_strategy='median').get_result()
        
        assert result['humidity'].isnull().sum() == 0
    
    def test_normalize_text(self, sample_df):
        """Test la normalisation du texte."""
        transformer = DataTransformer(sample_df)
        result = transformer.normalize_text_columns(['weather']).get_result()
        
        assert 'nuageux' in result['weather'].values
    
    def test_chaining(self, sample_df):
        """Test le chainpage des transformations."""
        transformer = DataTransformer(sample_df)
        result = (
            transformer
            .remove_duplicates()
            .handle_missing_values()
            .get_result()
        )
        
        assert len(transformer.transformations_applied) >= 2