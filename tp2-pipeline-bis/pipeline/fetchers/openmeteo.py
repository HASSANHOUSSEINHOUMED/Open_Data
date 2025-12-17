# pipeline/fetchers/openmeteo.py
# Fetcher pour l'API OpenMeteo (météo)

from typing import Generator
from datetime import datetime
from tqdm import tqdm

from .base import BaseFetcher
from ..config import OPENMETEO_CONFIG, MAX_ITEMS
from ..models import WeatherData


class OpenMeteoFetcher(BaseFetcher):
    """Fetcher pour OpenMeteo."""
    
    def __init__(self):
        super().__init__(OPENMETEO_CONFIG)
    
    def fetch_batch(self, latitude: float, longitude: float) -> dict:
        """Récupère les données météo pour une localisation."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "timezone": "auto"
        }
        
        try:
            data = self._make_request("/forecast", params)
            self.stats["items_fetched"] += 1
            return data
        except Exception as e:
            self.stats["requests_failed"] += 1
            print(f"Erreur météo: {e}")
            return {}
    
    def fetch_all(
        self,
        cities_coords: list[dict],
        verbose: bool = True
    ) -> Generator[dict, None, None]:
        """Récupère les données météo pour plusieurs villes."""
        from datetime import datetime
        
        self.stats["start_time"] = datetime.now()
        
        pbar = tqdm(cities_coords, desc="OpenMeteo", disable=not verbose)
        
        for city_data in pbar:
            weather = self.fetch_batch(
                city_data["latitude"],
                city_data["longitude"]
            )
            
            if weather:
                weather["city"] = city_data.get("city", "Unknown")
                weather["latitude"] = city_data["latitude"]
                weather["longitude"] = city_data["longitude"]
                yield weather
            
            self._rate_limit()
        
        pbar.close()
        self.stats["end_time"] = datetime.now()
        
        if verbose:
            duration = (self.stats["end_time"] - self.stats["start_time"]).seconds
            print(f"✅ {self.stats['items_fetched']} données météo récupérées en {duration}s")