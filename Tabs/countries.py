import streamlit as st
import pandas as pd


def show():
    """Contenu de l'onglet 'Pays'"""
    st.header("Analyse par Pays")

    st.markdown(
        """
        ##### Analyse des performances SEO par pays d’origine des utilisateurs.
        Données collectées à partir des différentes sources (Manufacturer, Tesla, Electric...).
    """
    )

    # Chargement des données
    try:
        df = pd.read_excel("Clean_data/Pays_all.xlsx")
        df = df[df['Source'] != 'Global']
    except Exception as e:
        st.error("Erreur lors du chargement du fichier Pays_all.xlsx")
        return
    # Intro visuelle : Top 10 des pays par clics
    st.subheader("📊 Top 10 des pays par nombre de clics")

    col1, col2 = st.columns([6, 4])

    with col1:
        st.image("Assets/top10_clics_pays.png", use_column_width=True)

    with col2:
        st.markdown(
            """
            Ce graphique présente les **10 pays qui ont généré le plus de clics** vers les pages Michelin, **toutes sources confondues** (manufacturer, Tesla, Electric...).
            - Les **États-Unis** dominent très largement en volume de clics, ce qui reflète leur **fort engagement SEO** sur l’ensemble des sources.
            - Les autres pays du classement (Canada, Philippines, etc.) sont **loin derrière en volume**, ce qui montre une **forte concentration du trafic sur un seul marché**.
            - Ce déséquilibre suggère des **opportunités d’expansion SEO** à explorer, notamment sur des marchés comme le Mexique ou l’Amérique Latine, actuellement **moins visibles ou moins engagés**.
            """
        )

    with col1:
        st.markdown(
            """
        ### Aperçu des données brutes

        Les clics les plus élevés (engagement), les impressions (visibilité), et le CTR sont comparés entre pays.

        Cela permet d’identifier les marchés prioritaires, en volume ou en qualité (ex: CTR élevé).

        Les pays avec des positions faibles (meilleures) sont mis en évidence pour orienter les efforts SEO.
        """
        )

    with col2:
        st.dataframe(
            df.style.highlight_max(
                subset=['Clics', 'CTR'], axis=0, color='#FFD100'
            )
            .highlight_min(subset=['Position'], axis=0, color='#90EE90')
            .format({'CTR': '{:.2%}', 'Position': '{:.2f}'})
        )

    # Comparaison Mexique vs autres LatAm
    st.subheader("Focus sur le Mexique")

    st.markdown(
        "**CTR moyen pondéré et Position moyenne - Mexique vs autres pays d'Amérique Latine**"
    )
    st.image("Assets/pos_ctr_pondere_mexique.png", use_column_width=True)

    # Comparaison LatAm vs Autres (globale)
    st.subheader(" Performance par Continent")

    st.markdown(
        "**CTR moyen pondéré et Position moyenne - Amérique Latine vs Autres**"
    )
    st.image("Assets/pos_ctr_pondere_continents.png", use_column_width=True)

    # Résumé des observations selon les objectifs stratégiques
    st.subheader(" Résumé des observations selon les objectifs")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        ####  Objectif : Augmenter la **visibilité**
        - **Focus sur les pays à fort volume d'impressions** (ex : USA) mais CTR faible.
        - **Améliorer le positionnement** de ces pages avec un meilleur SEO on-page (balises, chargement, liens internes).
        - Adapter les contenus aux attentes locales pour mieux apparaître dans les résultats Google locaux.
        """
        )

        st.markdown(
            """
        ####  Objectif : Améliorer le **taux de conversion (CTR)**
        - **Le Mexique est un excellent levier** : CTR très élevé malgré une mauvaise position.
        - Prioriser les optimisations d’apparence (titles, metas, featured snippets).
        - Créer des pages ciblées sur les **intérêts locaux** (ex : pneus pour routes mexicaines, saisons…).
        """
        )

    with col2:
        st.markdown(
            """
        ####  Objectif : Optimiser le **référencement naturel (Position)**
        - Cibler les marchés où la position moyenne est basse mais avec un bon CTR → gros potentiel.
        - Renforcer la **présence technique SEO** : backlinks locaux, structures Hn, performance mobile.
        - Utiliser les requêtes EV performantes comme base pour étendre la couverture sémantique.
        """
        )

        st.markdown(
            """
        ####  Objectif : Déployer une stratégie **par région**
        - L’Amérique Latine performe globalement moins bien en visibilité → zone d’opportunité.
        - Segmenter par pays pour identifier les spécificités (ex : contenu Brésil ≠ Mexique).
        - Travailler des clusters éditoriaux régionaux (pneus pour EV, promos locales, guides d’achat…).
        """
        )
