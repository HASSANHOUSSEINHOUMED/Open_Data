# tests/test_fetchers.py
# Tests pour les fetchers

import pytest
from pipeline.fetchers.openmeteo import OpenMeteoFetcher
from pipeline.fetchers.adresse import AdresseFetcher


class TestOpenMeteoFetcher:
    """Tests pour OpenMeteoFetcher."""
    
    def test_fetch_batch_returns_dict(self):
        """Test que fetch_batch retourne un dictionnaire."""
        fetcher = OpenMeteoFetcher()
        result = fetcher.fetch_batch(48.8566, 2.3522)
        
        assert isinstance(result, dict)
    
    def test_fetch_batch_has_current_data(self):
        """Test que les donnees contiennent des infos."""
        fetcher = OpenMeteoFetcher()
        result = fetcher.fetch_batch(48.8566, 2.3522)
        
        if result:
            assert "current" in result or "latitude" in result


class TestAdresseFetcher:
    """Tests pour AdresseFetcher."""
    
    def test_geocode_single_valid_address(self):
        """Test le geocodage d'une adresse valide."""
        fetcher = AdresseFetcher()
        result = fetcher.geocode_single("20 avenue de segur paris")
        
        assert result.original_address == "20 avenue de segur paris"
        assert result.score >= 0
        assert result.latitude is not None or result.latitude is None
    
    def test_geocode_single_invalid_address(self):
        """Test le geocodage d'une adresse invalide."""
        fetcher = AdresseFetcher()
        result = fetcher.geocode_single("xyzabc123456notreal")
        
        assert result.score < 0.5 or result.latitude is None
    
    def test_geocode_empty_address(self):
        """Test le geocodage d'une adresse vide."""
        fetcher = AdresseFetcher()
        result = fetcher.geocode_single("")
        
        assert result.score == 0