import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Apparence'"""
    st.header("Analyse générale")

    
    col1, col2 = st.columns([6, 5])  # Ratio 5/6
    
    with col1:
        st.image("./Assets/Comparaison du ranking.png", use_column_width=True)
       
    with col2:
        st.markdown("""
        ### Comparaison du ranking
                    
        Le graphique intitulé « Comparaison du ranking moyen : Michelin vs concurrents » met en regard la position moyenne occupée par chacun des trois sites dans les résultats de recherche. Sur l’axe horizontal figurent les noms des domaines : Michelin, Cars.com et Motortrend. L’axe vertical, inversé pour refléter qu’une position plus basse correspond à un meilleur classement, va de 0 (en haut) à environ 40 (en bas).

        On observe que Michelin se distingue avec une position moyenne autour de 23, tandis que Cars.com et Motortrend se situent nettement plus bas, aux alentours de 36 et 37 respectivement. Autrement dit, les pages de Michelin apparaissent en moyenne bien plus haut dans les SERP que celles de ses deux concurrents, ce qui traduit un net avantage SEO pour Michelin.     
       
        """)
    
       
    # NOUVELLE SECTION: Distribution de l'apparence par source (texte à droite, image à gauche)
    st.subheader("Difficulté du mot-clé par rapport au classement Michelin.")
    col1, col2 = st.columns([4, 5])  # Ratio 70/30
    
    with col1:
         st.markdown("""
        
        Le nuage de points montre que pour les mots-clés de difficulté faible à moyenne (0–30), Michelin se classe majoritairement dans le top 20, tandis qu’au-delà de 30 la position se dégrade et se disperse jusqu’au rang 80. On note toutefois quelques mots-clés très difficiles bien placés et quelques mots-clés faciles mal classés, signalant que d’autres facteurs SEO influencent aussi le ranking.
                     
        """)
      
    with col2:
        st.image("./Assets/Keyword Difficulty vs Michelin Ranking.png", use_column_width=True)
    
    
    # Graphique des impressions par apparence (image à gauche, texte à droite)
    st.subheader("Répartition des types de résultat Michelin")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30 pour donner plus d'espace au graphique
    
    with col1:
        st.image("./Assets/Répartition des types de résultat Michelin.png", use_column_width=True)
        
    with col2:
         st.markdown("""
        
        Le graphique intitulé "Répartition des types de résultat Michelin" présente la distribution des différents formats de résultats Michelin dans les recherches SEO, où l'axe vertical indique le nombre de mots-clés et l'axe horizontal montre quatre types de résultats distincts. On observe une prédominance marquée des résultats "organic" avec environ 160 mots-clés, suivis par les "reviews" qui atteignent près de 40 mots-clés, tandis que les catégories "ai overview" et "site links" sont nettement moins représentées avec à peine quelques mots-clés chacune, probablement moins de 5. Cette visualisation suggère que la stratégie SEO pour le contenu Michelin devrait prioritairement cibler les résultats organiques traditionnels, qui constituent manifestement la plus grande opportunité de visibilité dans les moteurs de recherche.
                     
                     
        """)
    
    # Graphique des clics par apparence (texte à gauche, image à droite)
    st.subheader("Top 10 des pages de destination Michelin")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        Ce graphique horizontal intitulé "Top 10 des pages de destination Michelin" illustre les URLs de landing pages Michelin les plus fréquemment consultées, classées selon leur nombre d'apparitions. La page "michelin-crossclimate2" domine largement avec plus de 40 apparitions, soit presque le double de sa plus proche concurrente. La page "understanding-ev-tires" arrive en deuxième position avec environ 25 apparitions, suivie par "model-3" avec 20 apparitions. Les pages concernant les véhicules électriques sont bien représentées dans ce classement, avec notamment "electric-vehicle-tires", ainsi que plusieurs références à des modèles Tesla ("model-s", "model-y", "model-x"). On remarque également la présence de pages éducatives comme "how-to-reduce-tire-wear" et commerciales comme "shop-ev-tires", qui complètent ce top 10. Cette répartition met en évidence l'importance stratégique des pneus CrossClimate2 dans l'offre Michelin et l'intérêt croissant des consommateurs pour les solutions pneumatiques adaptées aux véhicules électriques.
                    
        """)
    
    with col2:

        st.image("./Assets/Top 10 des pages de destination Michelin.png", use_column_width=True)

    
    # Taux de conversion par apparence (image à gauche, texte à droite)
    st.subheader("Top 10 mots-clés à fort volume (Michelin Rang 1)")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30
    
    with col1:
        st.image("./Assets/Top 10 mots-clés à fort volume (Michelin Rang 1).png", use_column_width=True)

    
    with col2:
        st.markdown("""
                       
        Le graphique "Top 10 mots-clés à fort volume (Michelin Rang 1)" révèle que "michelin ev tire" et "michelin ev tires" dominent largement avec plus de 550 recherches mensuelles chacun. "Michelin tesla tires" suit avec environ 150 recherches, puis "ev tires wear faster" et "ev winter tires" entre 50-100 recherches. Les cinq derniers mots-clés du classement génèrent moins de 20 recherches mensuelles chacun. Cette distribution montre l'intérêt prédominant des internautes pour les pneumatiques Michelin spécifiquement conçus pour véhicules électriques.
                    
         """)
    