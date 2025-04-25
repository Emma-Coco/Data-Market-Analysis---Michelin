import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Apparence'"""
    st.header("Analyse par Apparence")

    st.markdown("""
        ##### Apparence des résultats dans les pages de recherche et leur impact sur les performances SEO.        
        """)
    
    col1, col2 = st.columns([6, 5])  # Ratio 5/6
    
    with col1:

        try:
            # Charger les données
            df = pd.read_excel("Clean_data/Apparence_dans_les_résultats_de_recherche_all.xlsx")
            
            # Filtrer pour exclure la catégorie "Global" si nécessaire
            if 'Source' in df.columns:
                df_filtered = df[df['Source'] != 'Global'].copy()
            else:
                df_filtered = df.copy()
            
            # Renommer la colonne Apparence_dans_les_résultats_de_recherche en Apparence
            if 'Apparence_dans_les_résultats_de_recherche' in df_filtered.columns:
                df_filtered = df_filtered.rename(columns={'Apparence_dans_les_résultats_de_recherche': 'Apparence'})
            
            # Ajouter une colonne de fiabilité basée sur le volume d'impressions
            df_filtered['Fiabilité'] = pd.cut(
                df_filtered['Impressions'], 
                bins=[0, 10, 100, 1000, 10000, float('inf')],
                labels=['Très faible', 'Faible', 'Moyenne', 'Bonne', 'Excellente']
            )
            
            # Utiliser une div avec style CSS pour coller le tableau à droite
            st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
            st.dataframe(df_filtered.style.highlight_max(subset=['Clics', 'Impressions', 'CTR'], axis=0, color='#FFD100')
                              .highlight_min(subset=['Position'], axis=0, color='#90EE90')
                              .format({'CTR': '{:.4f}', 'Position': '{:.2f}'}))
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erreur lors du chargement des données: {str(e)}")
            st.warning("Veuillez vérifier que le fichier 'Clean_data/Apparence_dans_les_résultats_de_recherche_all.xlsx' existe et est accessible.")
    
       
    with col2:
        st.markdown("""
        ### Aperçu des données brutes
                    
        Les valeurs maximales de Clics, Impressions et CTR sont surlignées en jaune, et les meilleures positions (les plus basses) sont surlignées en vert.

        Les données brutes mettent en évidence que les clics et les impressions sont plus nombreux sur les **Extraits de produits** pour *Manufacturer URL*.

        Cependant, le CTR et la position semblent bien meilleurs sur les **Extraits de produits** pour *Electric URL*, bien que la ***fiabilité*** (basée sur le nombre d'impressions) soit cette fois ***très faible***. En effet, pour une impression nous obtenons un clique, ce qui donne un CTR de 1 mais récolté sur un seul utilisateur.       
        """)
    
       
    # NOUVELLE SECTION: Distribution de l'apparence par source (texte à droite, image à gauche)
    st.subheader("Distribution des Types d'Apparence par Source")
    col1, col2 = st.columns([4, 5])  # Ratio 70/30
    
    with col1:
         st.markdown("""
        
        Toutes les sources n'apparaissent pas à chaque fois avec tous les types d'apparences. 
            
        Pour que cela soit plus clair, le tableau ci-contre présente le type d'apparence disponible pour chaque source dans le jeu de données analysé.
        
        Nous voyons par exemple que toutes les sources apparaissent selon des **Extraits de produits**, les deux sources KWD se présentent également sous forme d'**Extraits d'avis**, et Electric URL est le seul a être trouvé selon des **Résultats traduits**.
        
        """)
      
    with col2:
        try:
            st.image("Assets/appearance_by_source.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/appearance_by_source.png' non trouvée. Veuillez générer ce graphique.")
    
    
    # Graphique des impressions par apparence (image à gauche, texte à droite)
    st.subheader("Répartition des Impressions par Type d'Apparence")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30 pour donner plus d'espace au graphique
    
    with col1:
        try:
            st.image("Assets/appearance_impressions.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/appearance_impressions.png' non trouvée. Veuillez générer ce graphique.")
        
    with col2:
         st.markdown("""
        
        C'est avec les **Extraits de produits** que se réalisent le plus d'impressions, avec : 
                    
        **Manufacturer URL:**
                    
        75.69% des impressions
        
        **Tesla KWD:**
                    
        23.16% des impressions
        
        **Electric URL:**
                    
        0.04% des impressions
                     
        **Electric KWD:**
                     
        1.11% des impressions
                     
        Suivis d'assez loin par les **Extraits d'avis**, et en dernier lieu, les **Résultats traduits** qui n'apparaissent que peu.
        """)
    
    # Graphique des clics par apparence (texte à gauche, image à droite)
    st.subheader("Répartition des Clics par Type d'Apparence")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        C'est également sur les **Extraits de produits** que s'effectuent le plus de clics, avec : 
                    
        **Manufacturer URL:**
                    
        89.40% des clics
                            
       **Tesla KWD:**
                    
        9.60% des clics
        
        **Electric URL:**
                    
        0.80% des clics
        
        **Electric KWD:**
                    
        0.20% des clics
        """)
    
    with col2:
        try:
            st.image("Assets/appearance_clicks.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/appearance_clicks.png' non trouvée. Veuillez générer ce graphique.")
    
    # Taux de conversion par apparence (image à gauche, texte à droite)
    st.subheader("Taux de Conversion (CTR) Moyen par Type d'Apparence")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30
    
    with col1:
        try:
            st.image("Assets/appearance_ctr.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/appearance_ctr.png' non trouvée. Veuillez générer ce graphique.")
    
    with col2:
        st.markdown("""
                       
        Ici, nous obtenons on score incroyable de CTR à 100% pour les Extraits de produits d'*Electric URL*, mais rappelons que ces résultats ne sont pas fiables puisque obtenus sur une seule personne.
                    
        Idem pour le CTR issu des **Résultats traduits**, toujours pour *Electric URL*, de 8,82% obtenu sur de très petits scores (3 clics pour 34 impressions)

        Le CTR le plus probants (le plus "haut" et fiable - 0,72%) est toutefois quand même obtenu avec les **Extraits de produits**, mais pour *manufacturer URL*. Il s'agit des meilleurs résultats utilisables (fiables), avec le plus haut taux d'impressions (61981) et de clics (447). 
        """)
    
    # Position et CTR par apparence (texte à gauche, image à droite)
    st.subheader("Position Moyenne et CTR par Type d'Apparence")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        Ici aussi, nous constations que le meilleur CTR (.0882) est obtenu avec la meilleure positions (10.62) pour les **Résultats traduits**, mais toujours avec une maigre fiabilité sur ces résultats.
        
        Ces observation laissent encore à penser qu'une meilleure ***position*** impliquerait un meilleur ***CTR***

        Résultats les moins probants en terme de CTR et de position sont les **extraits d'avis**, avec globalement un taux d'impressions et de clics moyen.
        """)
    
    with col2:
        try:
            st.image("Assets/position_ctr_par_type_avec_fiabilite.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/position_ctr_par_type_avec_fiabilite.png' non trouvée. Veuillez générer ce graphique.")
    
    # Section de recommandations
    st.subheader("Résumé des observations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        st.markdown("""
                    
        - À nouveau, **Si l'objectif est de créer de l'engagement**, il semble qu'*Electric URL* touche un public plus restreint mais ciblé, à travers les **Résultats Traduits** et Extraits de produits**, mais il serait utile de pouvoir observer cette tendance sur des données plus vastes et fiables.
                         
        - **Si l'objectif est de donner de la visibilité** : favoriser les sources telles que  pour *Manufacturer URL* en misant sur les *Extraits de produits*.
                    
        - Les sources/apparences avec le plus grand **CTR** sont encore une fois celles avec la **fiabilité** la plus basse (nombre de sujets touchés très restreint)
                    
        - À nouveau, unee meilleure performance CTR sur ces résultats moins représentés amènent à penser qu'ils touchent **LA BONNE CIBLE** : stratégie à développer

        
        """)
    
    with col2:
        st.markdown("""
      
        - Continuer à privilégier les "Extraits de produits" sur "Manufacturer URL" pour le volume
                    
        - Explorer le potentiel des "Résultats traduits" sur "Electric URL" mais aussi d'autres sources pour améliorer l'engagement (tout en reconnaissant les limites de fiabilité)
                    
        - Travailler à améliorer les performances des sources KWD qui sont significativement en-dessous des benchmarks standards
                    
        - Tenter d'améliorer les positions, où les mots-clés (KWD) peuvent jouer un rôle crucial
                    
        - Analyser les raisons de la faible performance des "Extraits d'avis" malgré leur bonne visibilité
                    
        """)