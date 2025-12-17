# pipeline/enricher.py
# Module d'enrichissement des données

import pandas as pd
from tqdm import tqdm

from .fetchers.adresse import AdresseFetcher
from .models import GeocodingResult


class DataEnricher:
    """Enrichit les données météo avec le géocodage."""
    
    def __init__(self):
        self.geocoder = AdresseFetcher()
        self.enrichment_stats = {
            "total_processed": 0,
            "successfully_enriched": 0,
            "failed_enrichment": 0,
        }
    
    def build_geocoding_cache(self, addresses: list[str]) -> dict[str, GeocodingResult]:
        """Construit un cache de géocodage pour éviter les requêtes en double."""
        cache = {}
        
        print(f"🌍 Géocodage de {len(addresses)} adresses uniques...")
        
        for result in self.geocoder.fetch_all(addresses):
            cache[result.original_address] = result
        
        success_rate = sum(1 for r in cache.values() if r.is_valid) / len(cache) * 100 if cache else 0
        print(f"✅ Taux de succès: {success_rate:.1f}%")
        
        return cache
    
    def enrich_weather(
        self,
        weather_data: list[dict],
        geocoding_cache: dict[str, GeocodingResult]
    ) -> list[dict]:
        """Enrichit les données météo avec le géocodage."""
        enriched = []
        
        for weather in tqdm(weather_data, desc="Enrichissement"):
            self.enrichment_stats["total_processed"] += 1
            
            enriched_weather = weather.copy()
            
            # Chercher l'adresse dans le cache
            city = weather.get("city", "")
            if city and city in geocoding_cache:
                geo = geocoding_cache[city]
                
                enriched_weather["address_label"] = geo.label
                enriched_weather["postal_code"] = geo.postal_code
                enriched_weather["geocoding_score"] = geo.score
                
                if geo.is_valid:
                    self.enrichment_stats["successfully_enriched"] += 1
                else:
                    self.enrichment_stats["failed_enrichment"] += 1
            
            enriched.append(enriched_weather)
        
        return enriched
    
    def get_stats(self) -> dict:
        """Retourne les statistiques d'enrichissement."""
        stats = self.enrichment_stats.copy()
        stats["geocoder_stats"] = self.geocoder.get_stats()
        
        if stats["total_processed"] > 0:
            stats["success_rate"] = stats["successfully_enriched"] / stats["total_processed"] * 100
        else:
            stats["success_rate"] = 0
        
        return stats