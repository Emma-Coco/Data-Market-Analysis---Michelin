import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

def show():
    st.title("📊 Dashboard SEO - Analyse des requêtes")

    # Chargement des données
    df = pd.read_excel("Clean_data/Requêtes_all.xlsx")
    df.columns = [col.strip() for col in df.columns]

    # Extraction des mots-clés
    keywords = [
        "michelin tires", "tesla tires", "michelin", "tesla", "tires", 
        "crossclimate", "discount tire", "town fair tire", "tire rotation"
    ]

    def extract_keyword(text):
        text_lower = str(text).lower()
        for kw in keywords:
            if kw in text_lower:
                return kw
        return "autres"

    df["keyword"] = df["Requêtes_les_plus_fréquentes"].apply(extract_keyword)

    # Score SEO
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df[["Clics", "Impressions", "Position"]]), columns=["Clics_s", "Impressions_s", "Position_s"])
    df["seo_score"] = (
        (df_scaled["Clics_s"] * 0.4) +
        (df_scaled["Impressions_s"] * 0.3) +
        ((1 - df_scaled["Position_s"]) * 0.3)
    )

    # 🔽 Filtres dans la page
    with st.container():
        with st.expander("Paramètres de visualisation", expanded=True):
            colf1, colf2 = st.columns(2)
            with colf1:
                metric = st.selectbox("Choisissez la métrique à visualiser :", ["Clics", "Impressions", "CTR", "seo_score"])
            with colf2:
                top_n = st.slider("Nombre d'éléments à afficher :", 5, 50, 10)

    # Graphiques en colonnes
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Top {top_n} Requêtes par {metric}")
        df_sorted = df.sort_values(by=metric, ascending=False).head(top_n)
        fig = px.bar(
            df_sorted,
            x="Requêtes_les_plus_fréquentes",
            y=metric,
            color="Source",
            labels={"Requêtes_les_plus_fréquentes": "Requêtes"},
            title=""
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader(f"Répartition des mots-clés par {metric}")
        df_keywords = df.groupby("keyword")[[metric]].sum().reset_index()
        df_keywords_sorted = df_keywords.sort_values(by=metric, ascending=False).head(top_n)
        fig_keyword = px.pie(
            df_keywords_sorted,
            names="keyword",
            values=metric,
            title=""
        )
        st.plotly_chart(fig_keyword, use_container_width=True)

    # Graphique SEO
    st.markdown("---")
    st.subheader("🚀 Top Requêtes par Score SEO")

    top_seo = df.sort_values(by="seo_score", ascending=False).head(10)
    fig_seo = px.bar(
        top_seo,
        x="Requêtes_les_plus_fréquentes",
        y="seo_score",
        color="Source",
        labels={"Requêtes_les_plus_fréquentes": "Requêtes", "seo_score": "Score SEO"},
        title=""
    )
    st.plotly_chart(fig_seo, use_container_width=True)
