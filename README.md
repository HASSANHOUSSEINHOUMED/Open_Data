# Open Data - Travaux Pratiques et Projets

Dépôt central regroupant tous les travaux pratiques et projets réalisés pour le module **Open Data** à l'IPSSI Paris.

## 📋 Structure du Projet
```
Open_Data/
├── tp1-exploration/          # TP1 - Exploration de données
│   ├── exploration.ipynb     # Notebook d'analyse
│   ├── FICHE_TECHNIQUE.md    # Documentation technique
│   └── README.md
│
├── tp2-pipeline-bis/         # TP2 - Pipeline d'acquisition et transformation
│   ├── pipeline/             # Code modulaire
│   ├── tests/                # Tests unitaires (9/9 PASSED)
│   ├── data/                 # Données (raw, processed, reports)
│   ├── exploration.ipynb     # Notebook de démonstration
│   ├── README.md             # Documentation
│   └── pyproject.toml        # Configuration projet
│
└── README.md                 # Cette documentation
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
**Durée** : 5h (J2 après-midi + J3 matin)  
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

**Livrables** :
- Code modulaire et testé
- Rapport de qualité automatique
- Données transformées (Parquet)
- Documentation complète

**Accès** : [TP2 Folder](./tp2-pipeline-bis/)

---

## 🚀 Démarrage Rapide

### Installation
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
uv run jupyter notebook
# Ou lancer le pipeline :
uv run python -m pipeline.main
# Ou exécuter les tests :
uv run pytest tests/ -v
```

---

## 📊 Technologies Utilisées

### Python Ecosystem
- **Python 3.14**
- **pandas** : Manipulation de données
- **numpy** : Calculs numériques
- **duckdb** : Requêtes SQL sur données

### Data Engineering
- **httpx** : Requêtes HTTP robustes
- **tenacity** : Retry automatique
- **pyarrow** : Stockage Parquet compressé
- **pydantic** : Validation de modèles

### DevOps & Tests
- **pytest** : Tests unitaires
- **uv** : Gestionnaire de dépendances ultra-rapide
- **jupyter** : Notebooks interactifs

### APIs Open Data
- **OpenMeteo** : Météo mondiale
- **API Adresse** : Géocodage français
- **data.gouv.fr** : Portail Open Data français

---



## 📖 Documentation Détaillée

- [TP1 - README](./tp1-exploration/README.md)
- [TP2 - README](./tp2-pipeline-bis/README.md)

---

## 👤 Auteur

**Hassan HOUSSEIN HOUMED**  
Mastère 2  IA, Big Data & Dev - IPSSI Paris

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