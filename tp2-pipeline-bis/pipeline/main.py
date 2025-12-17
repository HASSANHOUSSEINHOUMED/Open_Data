# pipeline/main.py
# Script principal du pipeline

import argparse
from datetime import datetime
import pandas as pd

from .fetchers.openmeteo import OpenMeteoFetcher
from .enricher import DataEnricher
from .transformer import DataTransformer
from .quality import QualityAnalyzer
from .storage import save_raw_json, save_parquet
from .config import MAX_ITEMS


def run_pipeline(
    cities: list[dict],
    max_items: int = MAX_ITEMS,
    skip_enrichment: bool = False,
    verbose: bool = True
) -> dict:
    """
    Execute le pipeline complet.
    
    Args:
        cities: Liste des villes avec lat/lon
        max_items: Nombre max d'items
        skip_enrichment: Passer l'enrichissement
        verbose: Afficher la progression
    
    Returns:
        Statistiques du pipeline
    """
    stats = {"start_time": datetime.now()}
    
    print("=" * 60)
    print("PIPELINE OPEN DATA - METEO + GEOCODAGE")
    print("=" * 60)
    
    # ETAPE 1 : Acquisition
    print("\nETAPE 1 : Acquisition des donnees meteo")
    fetcher = OpenMeteoFetcher()
    weather_data = list(fetcher.fetch_all(cities, verbose))
    
    if not weather_data:
        print("Aucune donnee recuperee. Arret.")
        return {"error": "No data fetched"}
    
    save_raw_json(weather_data, "weather_raw")
    stats["fetcher"] = fetcher.get_stats()
    
    # ETAPE 2 : Enrichissement
    if not skip_enrichment:
        print("\nETAPE 2 : Enrichissement (geocodage)")
        enricher = DataEnricher()
        
        city_names = [city["city"] for city in cities]
        geo_cache = enricher.build_geocoding_cache(city_names[:50])
        
        weather_data = enricher.enrich_weather(weather_data, geo_cache)
        stats["enricher"] = enricher.get_stats()
    else:
        print("\nETAPE 2 : Enrichissement (ignore)")
    
    # ETAPE 3 : Transformation
    print("\nETAPE 3 : Transformation et nettoyage")
    df = pd.DataFrame(weather_data)
    
    transformer = DataTransformer(df)
    df_clean = (
        transformer
        .remove_duplicates()
        .handle_missing_values(numeric_strategy='median')
        .get_result()
    )
    
    print(f"Transformations appliquees:\n{transformer.get_summary()}")
    stats["transformer"] = {"transformations": transformer.transformations_applied}
    
    # ETAPE 4 : Qualite
    print("\nETAPE 4 : Analyse de qualite")
    analyzer = QualityAnalyzer(df_clean)
    metrics = analyzer.analyze()
    
    print(f"Note: {metrics.quality_grade}")
    print(f"Completude: {metrics.completeness_score * 100:.1f}%")
    print(f"Doublons: {metrics.duplicates_pct:.1f}%")
    
    analyzer.generate_report("weather_quality")
    stats["quality"] = metrics.dict()
    
    # ETAPE 5 : Stockage
    print("\nETAPE 5 : Stockage final")
    output_path = save_parquet(df_clean, "weather")
    stats["output_path"] = str(output_path)
    
    # RESUME
    stats["end_time"] = datetime.now()
    stats["duration_seconds"] = (stats["end_time"] - stats["start_time"]).seconds
    
    print("\n" + "=" * 60)
    print("PIPELINE TERMINE")
    print("=" * 60)
    print(f"Duree: {stats['duration_seconds']}s")
    print(f"Donnees: {len(df_clean)}")
    print(f"Qualite: {metrics.quality_grade}")
    print(f"Fichier: {output_path}")
    
    return stats


def main():
    parser = argparse.ArgumentParser(description="Pipeline Open Data")
    parser.add_argument("--skip-enrichment", "-s", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true", default=True)
    
    args = parser.parse_args()
    
    cities = [
        {"city": "Paris", "latitude": 48.8566, "longitude": 2.3522},
        {"city": "Lyon", "latitude": 45.7640, "longitude": 4.8357},
        {"city": "Marseille", "latitude": 43.2965, "longitude": 5.3698},
    ]
    
    run_pipeline(cities, skip_enrichment=args.skip_enrichment, verbose=args.verbose)


if __name__ == "__main__":
    main()