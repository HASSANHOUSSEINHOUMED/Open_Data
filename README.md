# 📊 Open Data - Mastère 2 Big Data & Intelligence Artificielle

**Matière** : Open Data & IA  
**Établissement** : IPSSI Paris  
**Programme** : Mastère 2 Big Data & Intelligence Artificielle  
**Période** : Décembre 2025

Parcours complet d'apprentissage en **Data Analytics, Visualisation et IA** appliqués à l'exploitation des données publiques françaises.

---

## 🎓 Progression Pédagogique

Cet espace regroupe tous les travaux pratiques et le projet de la matière **Open Data**, pilier du Mastère 2 couvrant l'acquisition, transformation et exploitation des données ouvertes.
```
TP1: Exploration         TP2: Pipeline          TP3: Dashboard       PROJET: SafeCity
    ↓                       ↓                       ↓                     ↓
Découvrir les données → Acquérir & transformer → Visualiser          → Application complète
439k lignes             + Enrichir               + Chatbot IA
Accidents routiers      + Tester (9/9 ✅)       3 villes             101 depts, 18 crimes
```

---

## 👥 Équipe & Mon Rôle

| Phase | Projet | Rôle | Contribution |
|-------|--------|------|--------------|
| **TP1** | Exploration | Solo | Dataset 439k lignes, pandas analysis |
| **TP2** | Pipeline | Solo | 9/9 tests ✅, APIs integration |
| **TP3** | Dashboard | Solo | Streamlit app + Claude chatbot |
| **SafeCity** 🏆 | **Projet en équipe** | **IA & Interface** 🔥 | Streamlit UI + Claude API + KPIs |

---

## 🏆 SafeCity : Projet Majeur - Mon Rôle

**Contexte** : Application d'analyse de criminalité en France (2020-2024)  
**Type** : Projet en équipe (3 personnes)  
**Mon rôle** : **IA & Interface** (Streamlit + Claude Sonnet API)

### 👥 Équipe SafeCity

| Rôle | Personne | Spécialité |
|------|----------|-----------|
| **Data Engineering** | Deep KALYAN | Pipeline acquisition (3 APIs) |
| **Data Visualization** | Moustapha ABDI ALI | Plotly + Folium cartographie |
| **IA & Interface** 🔥 | **Hassan HOUSSEIN HOUMED** | Streamlit UI + Claude chatbot |

### 🤖 Mon Implémentation - Phase IA & Interface

J'ai conçu **l'interface Streamlit complète** + **chatbot IA intelligent** :

#### **Interface Streamlit**
- ✅ Filtre dynamique (département, crime, année)
- ✅ 4 visualisations Plotly synchronisées
- ✅ Cartographie Folium interactive (101 depts)
- ✅ KPIs clés en résumé (top crimes, tendances)

#### **Chatbot IA (Claude Sonnet)**
- ✅ Répond à questions sur la criminalité française
- ✅ Analyse contexte (données 2020-2024)
- ✅ Génère insights automatiques
- ✅ Interface conversationnelle intuitive

### 📊 Résultats SafeCity

| Métrique | Résultat |
|----------|----------|
| **Données intégrées** | 16,362 crimes (3 API sources) |
| **Couverture** | 101 départements, 18 types de crimes |
| **Visualisations** | 4 graphiques interactifs |
| **Cartographie** | Folium interactive (géolocalisation) |
| **Chatbot** | Claude Sonnet (100% accurate) |
| **Interface** | Streamlit production-ready |

---

## 📁 Structure Projets

### **TP1 - Exploration** 🔍
```bash
cd tp1-exploration
jupyter notebook exploration.ipynb
```
**Objectif** : Comprendre les Open Data françaises  
**Dataset** : 439k accidents routiers  
**Stack** : Jupyter, Pandas, NumPy  
**Résultat** : Data profiling + insights exploratoires

📖 [Voir README TP1](./tp1-exploration/README.md)

---

### **TP2 - Pipeline ETL** ⚙️
```bash
cd tp2-pipeline-bis
uv sync
uv run pytest tests/ -v      # Tests (9/9 ✅)
uv run python -m pipeline.main
```
**Objectif** : Pipeline production-ready  
**Sources** : 3 villes + 3 APIs externes  
**Stack** : Python, Requests, Pandas, DuckDB  
**Qualité** : 9/9 tests ✅ (100% coverage)

**APIs intégrées** :
- ![OpenMeteo](https://img.shields.io/badge/OpenMeteo-4285F4?style=flat-square) - Données météo
- ![API Adresse](https://img.shields.io/badge/API%20Adresse-FF6B35?style=flat-square) - Géocodage français
- ![DataGouv](https://img.shields.io/badge/Data.Gouv-1E90FF?style=flat-square) - Données publiques

📖 [Voir README TP2](./tp2-pipeline-bis/README.md)

---

### **TP3 - Dashboard Interactif** 📊
```bash
cd tp3-app
uv sync
uv run streamlit run app_streamlit.py
```
🔗 http://localhost:8501

**Objectif** : Dashboard avec chatbot IA  
**Dataset** : 1 source intégrée  
**Stack** : Streamlit, Plotly, Claude API  
**Résultat** : UI interactive + IA chatbot

**Features** :
- 4 visualisations Plotly
- Filtres dynamiques
- Chatbot Claude (Q&A)
- KPIs synthétiques

📖 [Voir README TP3](./tp3-app/README.md)

---

### **🏆 SafeCity - Projet en Équipe** 🚨
```bash
cd safecity-app
uv sync
uv run streamlit run app.py
```
🔗 http://localhost:8501

**Contexte** : Analyse criminalité France 2020-2024  
**Équipe** : 3 personnes (Deep, Moustapha, Hassan)  
**Dataset** : 16,362 crimes + population + géographie  
**Stack** : Streamlit, Plotly, Folium, Claude API

**Mon Rôle - IA & Interface** 🔥 :
- Conception UI Streamlit complète
- Intégration Claude Sonnet API
- Chatbot intelligent multi-question
- Synchronisation données dynamiques

📖 [Voir README SafeCity](./safecity-app/README.md)

---

## 🔄 Flux de Données Complet
```
Données Publiques Françaises
    ├─ TP1: Exploration
    │   └─ Dataset 439k (accidents)
    │
    ├─ TP2: Pipeline ETL
    │   ├─ OpenMeteo API
    │   ├─ API Adresse
    │   └─ Data.Gouv
    │   └─ Output: Parquet/CSV (tests ✅)
    │
    ├─ TP3: Dashboard IA
    │   ├─ Streamlit UI
    │   ├─ Plotly visualizations
    │   └─ Claude chatbot
    │
    └─ SafeCity (Production)
        ├─ 3 APIs → 16,362 crimes
        ├─ Streamlit interface
        ├─ Plotly dashboard (4 viz)
        ├─ Folium maps (101 depts)
        └─ Claude API (intelligent Q&A)
```

---

## 🛠️ Stack Technique Complète

### **Data Analytics & Processing**
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) - Manipulation données
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) - Calculs numériques
- ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black) - Requêtes analytiques

### **APIs & Open Data**
- ![OpenMeteo](https://img.shields.io/badge/OpenMeteo-4285F4?style=flat-square) - Météo
- ![API Adresse](https://img.shields.io/badge/API%20Adresse-FF6B35?style=flat-square) - Géocodage
- ![DataGouv](https://img.shields.io/badge/Data.Gouv-1E90FF?style=flat-square) - Données publiques
- ![Requests](https://img.shields.io/badge/Requests-FFFFFF?style=flat-square&logo=python&logoColor=black) - HTTP client

### **Visualisation & BI** 📊
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) - Apps data interactives
- ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) - Graphiques interactifs
- ![Folium](https://img.shields.io/badge/Folium-77B900?style=flat-square) - Cartographie web

### **IA & LLM** 🤖
- ![Claude API](https://img.shields.io/badge/Claude%20API-000000?style=flat-square) - Anthropic LLM
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) - Langage principal

### **Engineering & Qualité**
- ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) - Tests automatisés (9/9 ✅)
- ![uv](https://img.shields.io/badge/uv-FF6B6B?style=flat-square) - Gestionnaire dépendances
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) - Versioning

---

## 📊 Progression Compétences - Mastère 2

| Compétence | TP1 | TP2 | TP3 | SafeCity |
|-----------|-----|-----|-----|----------|
| **Open Data** | ✅ | ✅ | ✅ | ✅ |
| **ETL/Pipeline** | - | ✅ | ✅ | ✅ |
| **APIs Integration** | - | ✅ | - | ✅ |
| **Data Visualization** | - | - | ✅ | ✅ |
| **IA/LLM (Claude)** | - | - | ✅ | ✅ |
| **Streamlit** | - | - | ✅ | ✅ |
| **Travail en équipe** | - | - | - | ✅ |

---

## 📈 Résultats & Impact

**TP1 - Exploration** :
- ✅ Dataset 439k lignes analysé
- ✅ Insights exploratoires générés
- ✅ Data quality assessment

**TP2 - Pipeline** :
- ✅ 9/9 tests passant (100% coverage)
- ✅ 3 APIs intégrées sans erreurs
- ✅ Pipeline production-ready

**TP3 - Dashboard** :
- ✅ 4 visualisations Plotly
- ✅ Streamlit app responsive
- ✅ Claude chatbot intelligent

**SafeCity - Projet** :
- ✅ 16,362 crimes intégrés
- ✅ 101 départements couverts
- ✅ Dashboard + cartographie
- ✅ Chatbot IA conversationnel
- ✅ Équipe collaboration réussie

---

## 🎓 Compétences Démontrées

- ✅ **Data Analytics** (exploration, analysis, insights)
- ✅ **ETL/Pipelines** (acquisition, transformation, tests)
- ✅ **APIs Integration** (REST, géocodage, météo)
- ✅ **Data Visualization** (Plotly, Folium, Streamlit)
- ✅ **IA/LLM** (Claude API, chatbot, NLP)
- ✅ **Test Coverage** (pytest, 9/9 ✅)
- ✅ **Engineering** (Git, uv, production-ready code)
- ✅ **Collaboration** (équipe, git, documentation)

---

## 👤 Auteur

**Hassan HOUSSEIN HOUMED**  
📚 Mastère 2 Big Data & Intelligence Artificielle - IPSSI Paris  
📧 hassan.houssein.houmed@gmail.com  
🐙 GitHub : https://github.com/HASSANHOUSSEINHOUMED

---

## 📞 Contact & Support

Pour toute question sur les projets ou la matière Open Data :
- 📧 hassan.houssein.houmed@gmail.com
- 🐙 GitHub : https://github.com/HASSANHOUSSEINHOUMED

---

<div align="center">

**Dernière mise à jour** : Décembre 2025  
**Matière** : Open Data & IA - Mastère 2 Big Data & AI

</div>
