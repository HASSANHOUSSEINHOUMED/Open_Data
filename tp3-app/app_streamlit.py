# app_streamlit.py
# Application Streamlit - Dashboard Open Data interactif

import streamlit as st
import pandas as pd
from pathlib import Path

# Import des modules locaux
from utils.data import load_data, filter_data, get_data_summary
from utils.charts import (
    create_bar_chart, create_pie_chart, 
    create_scatter_plot, create_histogram,
    create_line_chart, create_heatmap
)
from utils.chatbot import DataChatbot

# Configuration de la page
st.set_page_config(
    page_title="Open Data Explorer",
    page_icon="📊",
    layout="wide"
)

# --- Chargement des donnees ---
@st.cache_data
def get_data():
    """Charge les donnees avec cache pour performance."""
    data_path = Path("data/processed")
    parquet_files = list(data_path.glob("*.parquet"))
    
    if not parquet_files:
        st.error("Aucun fichier Parquet trouve dans data/processed/")
        st.stop()
    
    return load_data(parquet_files[0])

df = get_data()

# --- Header ---
st.title("📊 Open Data Explorer")
st.markdown("*Explorez vos donnees Open Data de maniere interactive*")

# --- Sidebar : Filtres ---
st.sidebar.header("🔍 Filtres")

# Filtre dynamique base sur les colonnes categoriques
# Filtrer les colonnes object qui ne contiennent PAS de dicts
categorical_cols = []
for col in df.select_dtypes(include=['object']).columns:
    try:
        df[col].dropna().unique()
        categorical_cols.append(col)
    except (TypeError, KeyError):
        pass

filters = {}

for col in categorical_cols[:3]:  # Limiter a 3 filtres
    unique_values = df[col].dropna().unique().tolist()
    if len(unique_values) <= 50:
        selected = st.sidebar.multiselect(
            f"Filtrer par {col}",
            options=unique_values,
            default=[]
        )
        if selected:
            filters[col] = selected

# Appliquer les filtres
df_filtered = filter_data(df, filters) if filters else df

# --- Metriques ---
st.header("📈 Vue d'ensemble")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total lignes", f"{len(df_filtered):,}")
with col2:
    st.metric("Colonnes", len(df_filtered.columns))
with col3:
    numeric_cols = df_filtered.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        st.metric(f"Moyenne {numeric_cols[0]}", f"{df_filtered[numeric_cols[0]].mean():.2f}")
with col4:
    st.metric("Filtres actifs", len(filters))

# --- Visualisations ---
st.header("📊 Visualisations")

tab1, tab2, tab3, tab4 = st.tabs(["Distribution", "Comparaison", "Correlation", "Scatter"])

with tab1:
    st.subheader("Distribution des valeurs")
    
    numeric_cols = df_filtered.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Choisir une colonne", numeric_cols)
        fig = create_histogram(df_filtered, x=selected_col, title=f"Distribution de {selected_col}")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Comparaison par categorie")
    
    if categorical_cols and numeric_cols:
        cat_col = st.selectbox("Categorie", categorical_cols, key="cat")
        num_col = st.selectbox("Valeur", numeric_cols, key="num")
        
        agg_df = df_filtered.groupby(cat_col)[num_col].mean().reset_index()
        agg_df = agg_df.nlargest(15, num_col)
        
        fig = create_bar_chart(agg_df, x=cat_col, y=num_col, 
                               title=f"Moyenne de {num_col} par {cat_col}")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Matrice de correlation")
    
    if len(numeric_cols) >= 2:
        fig = create_heatmap(df_filtered)
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Scatter plot")
    
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("Axe X", numeric_cols, key="x_scatter")
        y_col = st.selectbox("Axe Y", numeric_cols, key="y_scatter")
        
        fig = create_scatter_plot(df_filtered, x=x_col, y=y_col,
                                  title=f"{x_col} vs {y_col}")
        st.plotly_chart(fig, use_container_width=True)

# --- Donnees brutes ---
st.header("🗃️ Donnees")

with st.expander("Voir les donnees brutes"):
    st.dataframe(df_filtered.head(100), use_container_width=True)

# --- Chatbot ---
st.header("🤖 Assistant Data")

# Initialiser le chatbot (cache de session)
if "chatbot" not in st.session_state:
    st.session_state.chatbot = DataChatbot(df)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
if prompt := st.chat_input("Posez une question sur les donnees..."):
    # Afficher le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtenir la reponse
    with st.chat_message("assistant"):
        with st.spinner("Reflexion..."):
            response = st.session_state.chatbot.chat(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Bouton pour reinitialiser
if st.button("🔄 Nouvelle conversation"):
    st.session_state.chatbot.reset()
    st.session_state.messages = []
    st.rerun()

# --- Footer ---
st.markdown("---")
st.markdown("*Application creee dans le cadre du module Open Data & IA - IPSSI*")