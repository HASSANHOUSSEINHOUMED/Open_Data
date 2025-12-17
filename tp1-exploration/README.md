# TP1 - Exploration augmentée d'un dataset Open Data

## Dataset choisi
Accidents corporels de la circulation routière (data.gouv.fr)
- Source : https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024/
- Nombre de lignes : 439 332
- Nombre de colonnes : 36

## Description
Ce TP explore un dataset Open Data contenant les informations sur les accidents corporels survenus sur les routes françaises. L'exploration est assistée par Claude Sonnet 4.5 pour identifier les caractéristiques, problèmes de qualité et analyses potentielles.

## Installation
```bash
cd tp1-exploration
uv sync
```

## Configuration
1. Créer un fichier `.env` à la racine du projet
2. Ajouter la clé API Anthropic :
```env
ANTHROPIC_API_KEY=clé_ici
```

## Utilisation
```bash
uv run jupyter notebook
```
Ouvrez le fichier `exploration.ipynb`

## Fichiers du projet
- `exploration.ipynb` : Notebook principal avec l'exploration du dataset
- `FICHE_TECHNIQUE.md` : Documentation détaillée du dataset
- `accidents.csv` : Fichier de données (à télécharger depuis data.gouv.fr)

## Contenu du TP
- Partie 0 : Setup de l'environnement
- Partie 1 : Chargement du dataset
- Partie 2 : Exploration assistée par IA (8 questions)
- Partie 3 : Génération de la fiche technique

## Outils utilisés
- Python 3.14
- pandas : manipulation de données
- duckdb : requêtes SQL
- plotly : visualisations
- litellm : accès à Claude API
- Claude Sonnet 4.5 : analyse assistée par IA

## Auteur
Hassan HOUSSEIN HOUMED

## Licence
Data : CC-BY
Notebook : Libre d'utilisation
