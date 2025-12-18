# 📊 Open Data - Travaux Pratiques & Projet en Équipe

Parcours complet d'apprentissage en Data Engineering, Visualisation et IA appliqués à l'Open Data français.

---

## 🎓 Progression Pédagogique
```
TP1: Exploration         TP2: Pipeline          TP3: Dashboard       PROJET: SafeCity
    ↓                       ↓                       ↓                     ↓
Découvrir les données → Acquérir & transformer → Visualiser          → Application complète
439k lignes             + Enrichir               + Chatbot IA
Accidents routiers      + Tester (9/9 ✅)       3 villes             101 depts, 18 crimes
```

---

## 📁 Structure

| Dossier | Objectif | Stack |
|---------|----------|-------|
| **tp1-exploration/** | Comprendre les Open Data | Jupyter, Pandas |
| **tp2-pipeline-bis/** | Pipeline production-ready | Python, APIs, Pytest |
| **tp3-app/** | Dashboard interactif avec IA | Streamlit, Plotly, Claude |
| **safecity-app/** | Application en équipe (3 personnes) | Full stack |

---

## 🚀 Démarrage Rapide

### TP1 - Exploration
```bash
cd tp1-exploration
jupyter notebook exploration.ipynb
```
📖 [Voir README TP1](./tp1-exploration/README.md)

---

### TP2 - Pipeline
```bash
cd tp2-pipeline-bis
uv sync
uv run pytest tests/ -v      # Tests (9/9 ✅)
uv run python -m pipeline.main   # Run pipeline
```
📖 [Voir README TP2](./tp2-pipeline-bis/README.md)

---

### TP3 - Dashboard Interactif
```bash
cd tp3-app
uv sync
uv run streamlit run app_streamlit.py
```
🔗 http://localhost:8501

📖 [Voir README TP3](./tp3-app/README.md)

---

### 🏛️ SafeCity - Projet en Équipe
```bash
cd safecity-app
uv sync
uv run streamlit run app.py
```
🔗 http://localhost:8501

📖 [Voir README SafeCity](./safecity-app/README.md)

---

## 🎯 Projet SafeCity : La Synthèse

**Contexte** : Application d'analyse de criminalité en France (2020-2024)

**Équipe** (3 personnes) :
- **Deep** - Data Engineer (Pipeline acquisition)
- **Moustapha** - Data Visualizer (Plotly + Folium)
- **Hassan** - IA & Interface (Streamlit + Claude)

**Résultats** :
- ✅ 3 APIs intégrées → 16,362 crimes + population + géographie
- ✅ Dashboard complet : 4 visualisations + cartographie interactive
- ✅ Chatbot IA répondant à des questions sur la criminalité
- ✅ Interface Streamlit intuitive avec filtres dynamiques

**Valeur ajoutée** :
- Production-ready (Parquet, tests, documentation)
- Open Data réels (Ministère Intérieur + INSEE + IGN)
- IA intégrée de manière pertinente
- Code modulaire et réutilisable

---

## 📚 Technologies Maîtrisées

### Data
- **Pandas, NumPy, DuckDB** - Manipulation
- **Parquet, JSON, CSV** - Stockage

### APIs & Integration
- **OpenMeteo, API Adresse** - Données externes
- **Anthropic, LiteLLM** - IA

### Data Viz
- **Plotly** - Graphiques interactifs
- **Folium** - Cartographie
- **Streamlit** - Applications web

### Engineering
- **pytest** - Tests automatisés
- **uv** - Gestionnaire dépendances
- **Git** - Versioning

---

## 📊 Progression Compétences

| Compétence | TP1 | TP2 | TP3 | SafeCity |
|-----------|-----|-----|-----|----------|
| Open Data | ✅ | ✅ | ✅ | ✅ |
| ETL/Pipeline | - | ✅ | ✅ | ✅ |
| Visualisation | - | - | ✅ | ✅ |
| IA/LLM | - | - | ✅ | ✅ |
| Travail en équipe | - | - | - | ✅ |

---

## 📈 Résultats Clés

| Métrique | TP2 | TP3 | SafeCity |
|----------|-----|-----|----------|
| Données | 3 villes | 1 source | 3 sources |
| Tests | 9/9 ✅ | - | - |
| Visualisations | - | 4 types | 4 types |
| Chatbot | - | ✅ | ✅ |
| Qualité code | A | - | Production-ready |

---

## 👤 Auteur

**Hassan HOUSSEIN HOUMED**  
Mastère 2 Big Data & AI - IPSSI Paris

---

## 📞 Contact

📧 hassan.houssein.houmed@gmail.com  
🐙 https://github.com/HASSANHOUSSEINHOUMED

---

**Dernière mise à jour** : Décembre 2025