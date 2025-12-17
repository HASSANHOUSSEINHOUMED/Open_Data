# pipeline/models.py
# Modèles de données avec Pydantic

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WeatherData(BaseModel):
    """Modèle pour les données météo."""
    city: str
    latitude: float
    longitude: float
    temperature: Optional[float] = None
    humidity: Optional[int] = None
    weather_code: Optional[int] = None
    wind_speed: Optional[float] = None
    
    # Enrichissement
    address_label: Optional[str] = None
    postal_code: Optional[str] = None
    geocoding_score: Optional[float] = None
    
    # Métadonnées
    fetched_at: datetime = None
    quality_score: Optional[float] = None


class GeocodingResult(BaseModel):
    """Résultat de géocodage."""
    original_address: str
    label: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    score: float = 0.0
    postal_code: Optional[str] = None
    city_code: Optional[str] = None
    city: Optional[str] = None
    
    @property
    def is_valid(self) -> bool:
        return self.score >= 0.5 and self.latitude is not None


class QualityMetrics(BaseModel):
    """Métriques de qualité."""
    total_records: int
    valid_records: int
    completeness_score: float
    duplicates_count: int
    duplicates_pct: float
    geocoding_success_rate: float
    quality_grade: str
    null_counts: dict = {}
    
    @property
    def is_acceptable(self) -> bool:
        return self.quality_grade in ['A', 'B', 'C']