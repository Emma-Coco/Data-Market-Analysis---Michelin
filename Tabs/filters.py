import streamlit as st
import pandas as pd

def show():
    """Contenu de l'onglet 'Filtres'"""
    st.header("Analyse des Filtres SEO")

    st.markdown("""
    ##### Comprendre comment les données ont été extraites à l’aide de filtres appliqués dans la Google Search Console.

    Ces filtres permettent de :
    - cibler des pages spécifiques (ex: /manufacturer),
    - se concentrer sur certaines requêtes (ex: +electric, +tesla),
    - limiter l’analyse aux 3 derniers mois ou au type de recherche “Web”.

    Ils influencent **directement les analyses des onglets Pages, Requêtes et Sources**.
    """)

    # Chargement des données
    try:
        df = pd.read_excel("Clean_data/Filtres_all.xlsx")
    except:
        st.error("Erreur lors du chargement du fichier Filtres_all.xlsx")
        return

    # Aperçu des données brutes
    st.subheader("📋 Données filtrées par source")
    st.dataframe(df)

    st.markdown("""
    ### 🧭 Structure des filtres utilisés

    On observe que chaque source (Manufacturer, Electric, Tesla...) applique des **filtres différents** :
    
    - Requêtes ciblées : permettent d'analyser des **intentions spécifiques** (véhicules électriques, marques, etc.)
    - Pages ciblées : orientent l'analyse sur certaines **sections du site**.
    - Temporalité : focus sur les **3 derniers mois**, donc données fraîches et exploitables.
    """)

    # Image du plot généré précédemment
    st.image("Assets/filtres_par_source_type.png", use_column_width=True)
    
    st.subheader(" Types de filtres appliqués par source")

    st.image("Assets/filtres_par_source.png", use_column_width=True)

    st.markdown("""
    Ce graphique montre quels types de **filtres ont été appliqués** à chaque source :

    -  **Tous les types de sources utilisent le filtre “Type de recherche”** : il s’agit donc uniquement de recherches Web.
    -  **Manufacturer URL** est la seule à utiliser le filtre **Page**, ce qui la rend plus ciblée.
    -  **Tesla KWD** et **Electric KWD** filtrent par **Requête**, ce qui permet d’isoler des expressions comme “tesla” ou “electric”.
    -  En revanche, **Electric URL** ne filtre pas par requête, ce qui peut expliquer une couverture plus large mais moins précise.

     Cela montre que **la qualité des données collectées dépend fortement de la granularité des filtres appliqués.**
    """)


    st.subheader("Résumé des observations selon les objectifs")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ####  Pour améliorer la **qualité des analyses SEO**
        - Poursuivre le filtrage ciblé des requêtes EV et des marques automobiles stratégiques.
        - Appliquer des **filtres cohérents entre sources** pour comparer plus facilement (ex : même période ou même marque).

        ####  Pour améliorer la **cohérence entre datasets**
        - Aligner les filtres entre Requêtes, Pages et Sources pour tracer précisément la performance par thématique.
        - Ajouter des libellés internes aux filtres pour en faciliter la lecture en équipe (Tesla, Electric, etc.).
        """)
    with col2:
        st.markdown("""
        ####  Vers une stratégie SEO efficace
        - Utiliser les filtres comme base pour segmenter vos campagnes (SEA & SEO).
        - Exploiter les données filtrées dans des dashboards thématiques (ex : cluster par marque EV).
        - **Prioriser les sources** où les filtres montrent déjà un bon CTR pour amplifier les résultats (ex: Electric URL + /auto).
        """)
