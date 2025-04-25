import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def show():
    """Contenu de l'onglet 'Pages'"""
    st.header("Analyse par Pages")

    st.markdown(
        """
    ##### Analyse des performances SEO des pages de destination les plus populaires.
    On se concentre ici sur les pages traitant des véhicules, et en particulier sur les pages `/auto` (cibles électriques).
    """
    )

    # Chargement des données
    try:
        df = pd.read_excel("Clean_data/Pages_all.xlsx")
        df = df[df['Source'] != 'Global']
        df.rename(columns={"Pages_les_plus_populaires": "Page"}, inplace=True)
    except Exception as e:
        st.error("Erreur lors du chargement du fichier Pages_all.xlsx")
        return

    # Création de la colonne type de page
    df['Type'] = df['Page'].apply(
        lambda x: (
            "Pages électriques (/auto)"
            if "/auto" in str(x)
            else "Autres pages"
        )
    )


    # Chargement des données

    df = pd.read_excel("Clean_data/Pages_all.xlsx")
    df = df[df['Source'] != 'Global']
    df.rename(columns={"Pages_les_plus_populaires": "Page"}, inplace=True)

    # Création de la colonne type de page
    df['Type'] = df['Page'].apply(
        lambda x: (
            "Pages électriques (/auto)" if "/auto" in str(x) else "Autres pages"
        )
    )

    # Création d'une version cliquable de l'URL
    df['Page_cliquable'] = df['Page'].apply(
        lambda x: f'<a href="{x}" target="_blank">{x}</a>'
    )

    # Aperçu du top des pages
    st.subheader("📄 Aperçu des Pages")
    col1, col2 = st.columns([5, 5])

    with col1:
        st.markdown(
            """
            ### Données brutes stylisées avec liens

            Cet aperçu montre les pages les plus performantes en termes de clics, d’impressions et de CTR.

            Les URLs sont maintenant **cliquables** pour un accès direct aux pages.
        """
        )

    with col2:
        st.markdown(
            df[['Page_cliquable', 'Clics', 'Impressions', 'CTR', 'Position']]
            .sort_values("Clics", ascending=False)
            .head(10)
            .to_html(escape=False, index=False),
            unsafe_allow_html=True,
        )

    # Agrégation des performances par type de page
    agg_df = (
        df.groupby("Type")
        .apply(
            lambda g: pd.Series(
                {
                    "Clics totaux": g["Clics"].sum(),
                    "Impressions totales": g["Impressions"].sum(),
                    "CTR pondéré": (
                        g["Clics"].sum() / g["Impressions"].sum()
                        if g["Impressions"].sum() > 0
                        else 0
                    ),
                    "Position pondérée": (
                        (g["Position"] * g["Impressions"]).sum()
                        / g["Impressions"].sum()
                        if g["Impressions"].sum() > 0
                        else 0
                    ),
                }
            )
        )
        .reset_index()
    )

    # Visualisations comparatives
    st.subheader(" Performance des Pages de véhicules électriques vs autres")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        sns.barplot(
            data=agg_df, x="Type", y="CTR pondéré", palette="Greens", ax=ax1
        )
        ax1.set_ylabel("CTR moyen pondéré")
        ax1.set_title("CTR moyen - vehicules électriques vs autres")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        sns.barplot(
            data=agg_df,
            x="Type",
            y="Position pondérée",
            palette="Oranges_d",
            ax=ax2,
        )
        ax2.set_ylabel("Position moyenne pondérée")
        ax2.set_title("Position moyenne - Pages électriques vs autres")
        st.pyplot(fig2)
    # Marques les plus cliquées sur les pages électriques
    st.subheader("Marques les plus recherchées (Pages électriques)")

    col1, col2 = st.columns([7, 3])

    with col1:
        st.image("Assets/clics_par_marque_page.png", use_column_width=True)

    with col2:
        st.markdown(
            """
    Ce graphique présente les **10 marques de véhicules** les plus cliquées via les pages `/auto`.

     **Ce qu'on en tire :**
    - Certaines pages concernant les marques notamment **Tesla** dominent nettement en volume de clics, révélant un intérêt utilisateur fort.
    - Cela oriente directement les efforts de contenu et d’optimisation vers ces marques.
    - Les marques les moins visibles peuvent être retravaillées via du contenu dédié ou des campagnes SEO/SEA ciblées.
    """
        )

    # Résumé stratégique
    st.subheader(" Résumé des observations selon les objectifs")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        ####  Objectif : Augmenter la **visibilité**
        - Les pages électriques ont un bon volume d’impressions mais sont moins bien positionnées.
        - Optimiser le SEO on-page (balises, maillage interne, chargement).
        -  Revoir l’organisation du site pour donner plus de poids aux pages stratégiques.

        ####  Objectif : Améliorer le **taux de conversion (CTR)**
        - Les pages électriques ont un CTR plus faible.
        -  Travailler les titres/metas + mettre des CTA visibles.
        -  Ajouter du contenu engageant (avis, photos, comparateurs).
        """
        )

    with col2:
        st.markdown(
            """
        ####  Objectif : Optimiser le **référencement naturel (Position)**
        - Position moyenne élevée = manque d’optimisation ou de notoriété.
        -  Ajouter du contenu sémantique sur les pneus pour véhicules électriques.
        -  Obtenir des backlinks thématiques sur ces pages.

        ####  Objectif : Renforcer la stratégie SEO autour de l’électrique
        - Créer un **cluster éditorial** “véhicules électriques”.
        - Segmenter les pages par marque/modèle (Tesla, Hyundai…).
        - Intégrer ces pages aux campagnes SEA & contenus organiques.
        """
        )
