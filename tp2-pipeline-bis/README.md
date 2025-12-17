# TP2 - Pipeline d'Acquisition et Transformation de Données

## Description

Pipeline complet de data engineering pour récupérer, enrichir, transformer et analyser les données météo avec géocodage.

**Combinaison d'APIs choisie :** OpenMeteo (météo) + API Adresse (géocodage)

## Architecture
```
Données météo (OpenMeteo API)
        ↓
Enrichissement (Géocodage via API Adresse)
        ↓
Transformation et nettoyage des données
        ↓
Analyse automatique de qualité
        ↓
Stockage en format Parquet
        ↓
Génération de rapports Markdown
```

## Résultats Obtenus

### Métriques Globales
- **Note de qualité** : A (excellent)
- **Complétude** : 100.0%
- **Doublons** : 0.0%
- **Villes analysées** : 3 (Paris, Lyon, Marseille)
- **Score géocodage moyen** : 0.967

### Données Générées
| Ville | Température | Humidité | Vitesse Vent | Code Postal |
|-------|-------------|----------|-------------|-------------|
| Paris | 13.9°C | 73% | 2.2 km/h | 75001 |
| Lyon | 10.2°C | 79% | 3.9 km/h | 69001 |
| Marseille | 14.8°C | 72% | 12.6 km/h | 13001 |

## Installation
```bash
cd tp2-pipeline-bis
uv sync
```

## Utilisation

### Lancer le pipeline complet
```bash
uv run python -m pipeline.main
```

### Exécuter les tests unitaires
```bash
uv run pytest tests/ -v
```

Résultat : **9/9 tests PASSED ✅**

## Structure du projet
```
tp2-pipeline-bis/
├── pipeline/
│   ├── __init__.py
│   ├── config.py           # Configuration centralisée (APIs, chemins, seuils)
│   ├── models.py           # Modèles Pydantic pour validation
│   ├── fetchers/           # Acquisition des données
│   │   ├── base.py         # Classe abstraite avec retry et rate limiting
│   │   ├── openmeteo.py    # Fetcher pour API OpenMeteo
│   │   └── adresse.py      # Fetcher pour API Adresse (géocodage)
│   ├── enricher.py         # Enrichissement croisé des données
│   ├── transformer.py      # Transformation et nettoyage
│   ├── quality.py          # Analyse et scoring de qualité
│   ├── storage.py          # Stockage JSON et Parquet
│   └── main.py             # Orchestration du pipeline
├── tests/
│   ├── test_fetchers.py    # Tests pour les fetchers
│   └── test_transformer.py # Tests pour la transformation
├── data/
│   ├── raw/                # Données brutes JSON
│   ├── processed/          # Données transformées Parquet
│   └── reports/            # Rapports de qualité Markdown
├── exploration.ipynb       # Notebook d'exploration et tests
├── .env                    # Variables d'environnement
├── .gitignore              # Fichiers à ignorer
├── pyproject.toml          # Configuration du projet
└── README.md               # Cette documentation
```

## Fonctionnalités Implémentées

### Acquisition Multi-Sources
- ✅ Requêtes HTTP robustes avec retry automatique (tenacity)
- ✅ Gestion des timeouts et des erreurs
- ✅ Rate limiting respecté
- ✅ Barre de progression (tqdm)

### Enrichissement Croisé
- ✅ Extraction d'adresses depuis les données météo
- ✅ Géocodage via API Adresse
- ✅ Cache de géocodage pour éviter les doublons
- ✅ Score de confiance du géocodage (0-1)

### Transformation et Nettoyage
- ✅ Suppression des doublons
- ✅ Gestion des valeurs manquantes (médiane)
- ✅ Normalisation du texte
- ✅ Chaînage des transformations (pattern fluide)

### Analyse de Qualité
- ✅ Scoring automatique (A, B, C, D, F)
- ✅ Calcul de complétude
- ✅ Détection des doublons
- ✅ Rapport Markdown générés automatiquement

### Stockage
- ✅ Sauvegarde des données brutes en JSON
- ✅ Sauvegarde des données transformées en Parquet
- ✅ Compression Snappy
- ✅ Horodatage des fichiers

### Tests Unitaires
```
tests/test_fetchers.py::TestOpenMeteoFetcher::test_fetch_batch_returns_dict PASSED
tests/test_fetchers.py::TestOpenMeteoFetcher::test_fetch_batch_has_current_data PASSED
tests/test_fetchers.py::TestAdresseFetcher::test_geocode_single_valid_address PASSED
tests/test_fetchers.py::TestAdresseFetcher::test_geocode_single_invalid_address PASSED
tests/test_fetchers.py::TestAdresseFetcher::test_geocode_empty_address PASSED
tests/test_transformer.py::TestDataTransformer::test_remove_duplicates PASSED
tests/test_transformer.py::TestDataTransformer::test_handle_missing_values_median PASSED
tests/test_transformer.py::TestDataTransformer::test_normalize_text PASSED
tests/test_transformer.py::TestDataTransformer::test_chaining PASSED

====== 9 passed in 3.48s ======
```

## APIs Utilisées

### OpenMeteo
- **URL** : https://api.open-meteo.com/v1
- **Avantages** : Aucune authentification, ultra-rapide, données météo complètes
- **Données récupérées** : Température, humidité, vitesse du vent, code météo

### API Adresse (Base Adresse Nationale)
- **URL** : https://api-adresse.data.gouv.fr
- **Avantages** : Service gouvernemental français, très fiable, pas de rate limit strict
- **Données récupérées** : Adresse complète, coordonnées GPS, code INSEE, code postal

## Technologies Utilisées

- **Python 3.14**
- **pandas** : Manipulation de données
- **httpx** : Requêtes HTTP asynchrones
- **pydantic** : Validation des modèles de données
- **tenacity** : Retry automatique avec backoff exponentiel
- **tqdm** : Barres de progression
- **pyarrow** : Stockage Parquet compressé
- **pytest** : Tests unitaires
- **uv** : Gestionnaire de dépendances ultra-rapide

## Auteur

Hassan HOUSSEIN HOUMED

## Licence

Données : Licence Ouverte (ODbL)
Code : Libre d'utilisation pour fins éducatives