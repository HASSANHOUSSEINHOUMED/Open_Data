# utils/charts.py
# Module de visualisations avec Plotly

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_bar_chart(df: pd.DataFrame, x: str, y: str, title: str = "") -> go.Figure:
    """
    Cree un bar chart interactif.
    
    Args:
        df: DataFrame source
        x: Colonne pour l'axe X
        y: Colonne pour l'axe Y
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    fig = px.bar(
        df, x=x, y=y, 
        title=title,
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        hovermode="x unified"
    )
    return fig


def create_pie_chart(df: pd.DataFrame, names: str, values: str, title: str = "") -> go.Figure:
    """
    Cree un pie chart (donut) interactif.
    
    Args:
        df: DataFrame source
        names: Colonne pour les labels
        values: Colonne pour les valeurs
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    fig = px.pie(
        df, names=names, values=values,
        title=title,
        hole=0.3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


def create_scatter_plot(df: pd.DataFrame, x: str, y: str, 
                        color: str = None, title: str = "") -> go.Figure:
    """
    Cree un scatter plot interactif.
    
    Args:
        df: DataFrame source
        x: Colonne pour l'axe X
        y: Colonne pour l'axe Y
        color: Colonne pour la couleur (optionnel)
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    fig = px.scatter(
        df, x=x, y=y, color=color,
        title=title,
        template="plotly_white"
    )
    fig.update_traces(marker=dict(size=8, opacity=0.7))
    return fig


def create_histogram(df: pd.DataFrame, x: str, nbins: int = 30, 
                     title: str = "") -> go.Figure:
    """
    Cree un histogramme interactif.
    
    Args:
        df: DataFrame source
        x: Colonne pour l'histogramme
        nbins: Nombre de bins
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    fig = px.histogram(
        df, x=x, nbins=nbins,
        title=title,
        template="plotly_white"
    )
    return fig


def create_line_chart(df: pd.DataFrame, x: str, y: str, 
                      title: str = "") -> go.Figure:
    """
    Cree un line chart interactif.
    
    Args:
        df: DataFrame source
        x: Colonne pour l'axe X
        y: Colonne pour l'axe Y
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    fig = px.line(
        df, x=x, y=y,
        title=title,
        template="plotly_white",
        markers=True
    )
    return fig


def create_heatmap(df: pd.DataFrame, title: str = "") -> go.Figure:
    """
    Cree une heatmap de correlation.
    
    Selectionne uniquement les colonnes numeriques.
    
    Args:
        df: DataFrame source
        title: Titre du graphique
    
    Returns:
        Figure Plotly
    """
    numeric_df = df.select_dtypes(include=['number'])
    corr = numeric_df.corr()
    
    fig = px.imshow(
        corr,
        title=title or "Matrice de correlation",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )
    return fig