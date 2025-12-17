# Accidents corporels de la circulation routière en France

## Informations générales
- **Source** : data.gouv.fr
- **Licence** : Licence Ouverte (à vérifier sur le portail)
- **Nombre de lignes** : 439 332
- **Nombre de colonnes** : 36
- **Période couverte** : Plusieurs années (à déterminer selon les données `org`)

## Description

Ce dataset recense les **accidents corporels de la circulation routière** survenus en France métropolitaine et dans les départements d'outre-mer. Chaque ligne correspond à un accident ayant fait au moins une victime (décédé, blessé hospitalisé ou blessé léger). Les données sont collectées par les forces de l'ordre à partir des procès-verbaux d'accidents.

Le fichier contient des informations détaillées sur les **circonstances des accidents** (conditions météorologiques, luminosité, type de collision), la **localisation géographique** (département, commune, adresse, coordonnées GPS) et les **conséquences humaines** (nombre de tués, blessés graves, blessés légers). Ces données sont issues du fichier caractéristiques des accidents du Fichier National des Accidents Corporels (BAAC).

Les informations permettent d'analyser les facteurs de risque routier, d'identifier les zones accidentogènes et d'évaluer l'impact des politiques de sécurité routière. La richesse des variables offre des possibilités d'analyse croisée entre conditions météorologiques, infrastructure routière et gravité des accidents.

## Structure des données

| Colonne | Type | Description | Valeurs manquantes |
|---------|------|-------------|-------------------|
| **org** | int64 | Organisme ayant saisi l'accident (1-5) | 0 |
| **lum** | int64 | Conditions d'éclairage (1:jour, 2:crépuscule, 3:nuit éclairée, 4:nuit non éclairée, 5:inconnu) | 0 |
| **agg** | int64 | Localisation (1:hors agglo, 2:en agglo) | 0 |
| **int** | int64 | Type d'intersection (0:hors intersection, 1-9:types variés) | 0 |
| **atm** | float64 | Conditions atmosphériques (1:normale, 2-9:pluie, neige, brouillard...) | 23 |
| **col** | float64 | Type de collision (1-7:frontale, arrière, latérale...) | 9 |
| **com** | int64 | Code commune INSEE | 0 |
| **dep** | int64 | Code département | 0 |
| **catr** | float64 | Catégorie de route (1:autoroute, 2:nationale, 3:départementale...) | 13 673 |
| **infra** | float64 | Infrastructure spéciale (0:normale, 1-7:pont, tunnel...) | 14 014 |
| **voie** | float64 | Numéro de route | 32 254 |
| **v1** | float64 | Indice numérique de route | 211 832 |
| **v2** | object | Lettre indice de route | 418 106 |
| **circ** | float64 | Régime de circulation (1:sens unique, 2:bidirectionnel...) | 13 885 |
| **nbv** | float64 | Nombre de voies | 14 540 |
| **pr** | object | Point repère (PR) | 219 717 |
| **pr1** | float64 | Distance au PR | 220 106 |
| **vosp** | float64 | Voie réservée (0:non, 1-3:piste cyclable, couloir bus...) | 14 205 |
| **prof** | float64 | Profil en long (1:plat, 2:pente, 3:sommet...) | 13 910 |
| **plan** | float64 | Tracé en plan (1:rectiligne, 2:courbe...) | 13 909 |
| **situ** | float64 | Situation de l'accident (1:chaussée, 2:accotement...) | 13 857 |
| **ttue** | int64 | **Nombre de tués** | 0 |
| **tbg** | int64 | **Nombre de blessés graves** | 0 |
| **tbl** | int64 | **Nombre de blessés légers** | 0 |
| **tindm** | int64 | **Nombre d'indemnes** | 0 |
| **typenumero** | float64 | Type de numéro de voie | 124 888 |
| **numero** | float64 | Numéro dans la voie | 239 579 |
| **distancemetre** | float64 | Distance en mètres | 127 124 |
| **libellevoie** | object | Nom de la voie | 124 590 |
| **coderivoli** | object | Code RIVOLI de la voie | 439 190 |
| **grav** | float64 | Gravité maximale de l'accident (0.43-444188) | 0 |
| **gps** | object | Coordonnées GPS combinées | 434 814 |
| **lat** | float64 | Latitude | 279 783 |
| **long** | object | Longitude | 279 856 |
| **adr** | object | Adresse complète | 428 287 |
| **numac** | float64 | Numéro d'accident unique | 1 |

## Qualité des données

### Points forts
- **Exhaustivité des accidents corporels** : base nationale complète avec 439 332 enregistrements
- **Variables de gravité complètes** : ttue, tbg, tbl sans valeurs manquantes
- **Identification unique** : colonne `numac` quasi-complète (1 seule valeur manquante)
- **Couverture géographique** : codes département et commune complets
- **Variables temporelles et contextuelles** : luminosité, météo bien renseignées

### Points d'attention
- **Géolocalisation incomplète** : 63,7% de valeurs manquantes pour lat/long, 99% pour gps
- **Adresses partielles** : 97,5% de valeurs manquantes pour `adr`
- **Code RIVOLI quasi-absent** : 99,96% de valeurs manquantes
- **Variables de route incomplètes** : v1 (48%), v2 (95%), pr (50%)
- **Valeurs aberrantes** : 
  - `numero` avec valeurs extrêmes (8e+280)
  - `voie` jusqu'à 90 000
  - `grav` avec des valeurs incohérentes (jusqu'à 444 188)
- **Types incohérents** : `long` en object au lieu de float64

## Cas d'usage potentiels

1. **Analyse de la sécurité routière**
   - Identification des zones à risque (black-spots)
   - Corrélation météo/luminosité et gravité des accidents
   - Évolution temporelle de l'accidentalité

2. **Cartographie des accidents**
   - Heatmaps des accidents par département/commune
   - Visualisation des axes routiers dangereux
   - Zonage pour priorisation des aménagements

3. **Études prédictives**
   - Modélisation de la gravité selon les conditions
   - Facteurs de risque (intersection, type de route)
   - Prévision saisonnière des accidents

4. **Politique publique**
   - Évaluation de l'impact des radars automatiques
   - Ciblage des campagnes de prévention
   - Allocation des ressources de secours

5. **Recherche académique**
   - Impact des infrastructures sur la sécurité
   - Comportements à risque selon contexte
   - Analyses socio-démographiques (à croiser avec d'autres datasets)

## Analyse recommandée

### Nettoyage prioritaire
```python
import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv('accidents.csv')

# Corriger le type de 'long'
df['long'] = pd.to_numeric(df['long'], errors='coerce')

# Filtrer valeurs aberrantes de 'grav'
df = df[df['grav'] < 100]  # Valeur à ajuster selon documentation

# Créer variable gravité simplifiée
df['avec_tue'] = (df['ttue'] > 0).astype(int)
df['total_victimes'] = df['ttue'] + df['tbg'] + df['tbl']
```

### Analyses essentielles

**1. Vue d'ensemble de l'accidentalité**
```python
# Distribution de la gravité
print(f"Accidents avec tué(s) : {df['ttue'].gt(0).sum()}")
print(f"Total de tués : {df['ttue'].sum()}")
print(f"Total de blessés : {(df['tbg'] + df['tbl']).sum()}")

# Top départements
top_dept = df.groupby('dep')['numac'].count().sort_values(ascending=False).head(10)
```

**2. Facteurs de risque**
```python
# Luminosité et gravité
df.groupby('lum')['ttue'].agg(['sum', 'mean'])

# Météo et accidents mortels
df[df['ttue'] > 0].groupby('atm').size()
```

**3. Cartographie (pour données géolocalisées)**
```python
import plotly.express as px

# Filtrer données avec coordonnées
df_geo = df.dropna(subset=['lat', 'long'])
df_geo = df_geo[(df_geo['lat'] > 41) & (df_geo['lat'] < 52)]

# Carte des accidents mortels
fig = px.scatter_mapbox(
    df_geo[df_geo['ttue'] > 0],
    lat='lat', lon='long',
    hover_name='dep',
    zoom=5
)
```

### Recommandations méthodologiques
- **Privilégier les analyses agrégées** (par département/commune) plutôt que ponctuelles vu les données GPS partielles
- **Vérifier la documentation officielle** pour décoder les variables catégorielles (lum, atm, col, etc.)
- **Croiser avec d'autres datasets** : données de trafic, météo détaillée, caractéristiques démographiques
- **Attention à la temporalité** : identifier les années couvertes via des métadonnées ou patterns dans les données