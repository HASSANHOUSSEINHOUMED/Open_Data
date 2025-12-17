# Open Data - Travaux Pratiques et Projets

Dépôt central regroupant tous les travaux pratiques et projets réalisés pour le matière **Open Data** à l'IPSSI Paris.

## 📋 Structure du Projet
```
Open_Data/
├── tp1-exploration/              # TP1 - Exploration de données
│   ├── exploration.ipynb         # Notebook d'analyse
│   ├── FICHE_TECHNIQUE.md        # Documentation technique
│   └── README.md
│
├── tp2-pipeline-bis/             # TP2 - Pipeline d'acquisition et transformation
│   ├── pipeline/                 # Code modulaire (fetchers, enricher, etc.)
│   ├── tests/                    # Tests unitaires (9/9 PASSED)
│   ├── data/                     # Données (raw, processed, reports)
│   ├── exploration.ipynb         # Notebook de démonstration
│   ├── README.md                 # Documentation
│   └── pyproject.toml            # Configuration projet
│
├── tp3-app/                      # TP3 - Application Data Interactive avec Chatbot
│   ├── app_streamlit.py          # Application Streamlit principale
│   ├── utils/                    # Modules (data, charts, chatbot)
│   ├── data/processed/           # Données Parquet du TP2
│   ├── README.md                 # Documentation
│   ├── screen_page_*.jpg         # Screenshots de démonstration
│   └── pyproject.toml            # Configuration projet
│
└── README.md                     # Cette documentation
```

## 📚 Travaux Pratiques

### **TP1 - Exploration de Données Open Data** ✅
**Durée** : 1h30  
**Objectif** : Explorer et documenter un dataset Open Data avec assistance IA

**Dataset** : Accidents corporels de la circulation routière (data.gouv.fr)
- 439k lignes, 36 colonnes
- Données de 2005 à 2022

**Livrables** :
- `exploration.ipynb` : Notebook avec 8 questions explorées
- `FICHE_TECHNIQUE.md` : Documentation auto-générée

**Points clés** :
- ✅ Chargement de données (gestion encodage, séparateurs)
- ✅ Analyse exploratoire avec assistance IA
- ✅ Documentation professionnelle

**Accès** : [TP1 Folder](./tp1-exploration/)

---

### **TP2 - Pipeline d'Acquisition et Transformation de Données** ✅
**Durée** : 5h  
**Objectif** : Construire un pipeline de production pour l'acquisition, enrichissement et analyse de données

**APIs utilisées** :
- **OpenMeteo** : Données météo en temps réel
- **API Adresse** : Géocodage et enrichissement (Base Adresse Nationale)

**Résultats** :
- ✅ 3 villes analysées (Paris, Lyon, Marseille)
- ✅ Qualité globale : **A** (100% complétude)
- ✅ Score géocodage moyen : **0.967**
- ✅ Tests : **9/9 PASSED**

**Architecture** :
```
Données météo (OpenMeteo)
        ↓
Enrichissement (Géocodage API Adresse)
        ↓
Transformation et nettoyage
        ↓
Analyse de qualité
        ↓
Stockage Parquet + Rapports
```

**Modules implémentés** :
- `pipeline/config.py` - Configuration centralisée
- `pipeline/fetchers/` - Acquisition multi-sources
- `pipeline/enricher.py` - Enrichissement croisé
- `pipeline/transformer.py` - Transformation fluide
- `pipeline/quality.py` - Scoring automatique
- `pipeline/storage.py` - Stockage Parquet
- `tests/` - Tests unitaires (pytest)

**Accès** : [TP2 Folder](./tp2-pipeline-bis/)

---

### **TP3 - Application Data Interactive avec Chatbot** ✅
**Durée** : 2h25  
**Objectif** : Créer une application interactive pour explorer les données avec visualisations et chatbot IA

**Fonctionnalités** :
- ✅ Chargement des données Parquet du TP2
- ✅ Filtres dynamiques par colonne
- ✅ Visualisations interactives (Plotly)
- ✅ Chatbot IA (Claude Sonnet 4.5) intégré
- ✅ Affichage des données brutes

**Architecture** :
```
Streamlit Application
    ├── Data Module (chargement Parquet)
    ├── Charts Module (visualisations Plotly)
    ├── Chatbot Module (Claude Sonnet 4.5)
    └── Utils (filtrage, agrégation)
```

**Technologies** :
- **Streamlit** : Framework pour applications data
- **Plotly** : Visualisations interactives
- **Claude Sonnet 4.5** : Chatbot IA
- **DuckDB** : Requêtes SQL optimisées

**Résultats** :
- ✅ Application fonctionnelle et intuitive
- ✅ Chatbot répond à des questions complexes
- ✅ Visualisations interactives et informatives
- ✅ Score de géocodage moyen : 0.967

**Accès** : [TP3 Folder](./tp3-app/)

---

## 🚀 Démarrage Rapide

### Installation Globale
```bash
# Cloner le repo
git clone https://github.com/HASSANHOUSSEINHOUMED/Open_Data.git
cd Open_Data
```

### Exécuter TP1
```bash
cd tp1-exploration
jupyter notebook exploration.ipynb
```

### Exécuter TP2
```bash
cd tp2-pipeline-bis
uv sync
uv run python -m pipeline.main
# ou tests :
uv run pytest tests/ -v
```

### Exécuter TP3
```bash
cd tp3-app
uv sync
uv run streamlit run app_streamlit.py
# Ouvre http://localhost:8501
```

---

## 📊 Technologies Utilisées Globalement

### Python Ecosystem
- **Python 3.14**
- **pandas** : Manipulation de données
- **numpy** : Calculs numériques
- **duckdb** : Requêtes SQL

### Data Engineering
- **httpx** : Requêtes HTTP robustes
- **tenacity** : Retry automatique
- **pyarrow** : Stockage Parquet
- **pydantic** : Validation de modèles

### Data Visualization
- **Plotly** : Visualisations interactives
- **Streamlit** : Applications data

### DevOps & Tests
- **pytest** : Tests unitaires
- **uv** : Gestionnaire de dépendances ultra-rapide
- **jupyter** : Notebooks interactifs

### APIs Open Data
- **OpenMeteo** : Météo mondiale
- **API Adresse** : Géocodage français
- **data.gouv.fr** : Portail Open Data français

---

## 👤 Auteur

**Hassan HOUSSEIN HOUMED**  
Mastère 2 IA, Big Data & Dev - IPSSI Paris

## 📄 Licence

- **Données** : Licence Ouverte (ODbL)
- **Code** : Libre d'utilisation pour fins éducatives

---

## 📞 Contact & Support

Pour toute question ou amélioration :

- 📧 Email : hassan.houssein.houmed@gmail.com

- 🐙 GitHub : https://github.com/HASSANHOUSSEINHOUMED

---

**Dernière mise à jour** : Décembre 2025