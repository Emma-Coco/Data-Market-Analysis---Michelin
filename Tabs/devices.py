# Fichier: Tabs/devices.py
import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Appareils'"""
    st.header("Analyse par Appareils")

    st.markdown("""
        Appareils utilisés lors de la navigation pour la récolte des données SEO.        
        """)
    
    col1, col2 = st.columns([5, 5])  # Ratio 5/4
    
    with col1:
        st.markdown("""
        ### Aperçu des données brutes
                    
        Les valeurs maximales de Clics, Impressions et CTR sont surlignées en jaune, et les meilleures positions (les plus basses) sont surlignées en vert.

        Les données brutes mettent déjà en évidence que les clics et les impressions sont plus nombreux sur **mobile** pour *manufacturer url*.

        Cependant, le CTR et la position semblent bien meilleurs sur **Tablette** pour *Electric URL*, avec toute fois une fiabilité (basée sur le nombre d'impressions) moyenne.           
        """)
    
    with col2:
        try:
            # Charger les données
            df = pd.read_excel("Clean_data/Appareils_all.xlsx")
            
            # Filtrer pour exclure la catégorie "Global"
            df_filtered = df[df['Source'] != 'Global'].copy()
            
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
            st.warning("Veuillez vérifier que le fichier 'Clean_data/Appareils_all.xlsx' existe et est accessible.")
    
    # Graphique des impressions (image à gauche, texte à droite)
    st.subheader("Répartition des Impressions par Appareil et Source")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30 pour donner plus d'espace au graphique
    
    with col1:
        st.image("Assets/device_impressions_by_source.png", use_column_width=True)
        
    with col2:
        st.markdown("""
        
        C'est donc sur **mobile** que se réalisent le plus d'impressions, avec : 
                    
        **Manufacturer URL:**
                    
        81.50% des impressions
        
       **Tesla KWD:**
                    
        11.21% des impressions
        
        **Electric URL:**
                    
        5.16% des impressions
        
        **Electric KWD:**
                    
        2.13% des impressions
        """)
    
    # Graphique des clics (texte à gauche, image à droite)
    st.subheader("Répartition des Clics par Appareil et Source")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        C'est sur **mobile** également que s'effectuent le plus de clics, avec : 
                    
        **Manufacturer URL:**
                    
        76.19% des clics
                            
       **Tesla KWD:**
                    
        15.45% des clics
        
        **Electric URL:**
                    
        7.10% des clics
        
        **Electric KWD:**
                    
        1.26% des clics
        """)
    
    with col2:
        st.image("Assets/device_clicks_by_source.png", use_column_width=True)
    
    # Taux de conversion (image à gauche, texte à droite)
    st.subheader("Taux de Conversion (CTR) Moyen par Source et Appareil")
    col1, col2 = st.columns([7, 3])  # Ratio 70/30
    
    with col1:
        st.image("Assets/ctr_par_source_appareil.png", use_column_width=True)
    
    with col2:
        st.markdown("""
                    

        Contre toute attente, c'est *Electric URl* qui détient le meilleur taux CTR pour tous les appareils, mais principalement pour la **tablette**. Or, la tablette était en dernière position pour les impressions et les clics. 
                    
        """)
    
    # Position et CTR (texte à gauche, image à droite)
    st.subheader("Position Moyenne et CTR par Type d'Appareil")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        ### Analyse
        
        - Meilleure position = meilleur CTR
        - Mobile bien positionné
        - Corrélation position/conversion
        """)
    
    with col2:
        st.image("Assets/position_ctr_par_appareil.png", use_column_width=True)
    
    # Section de recommandations plus concise
    st.subheader("Recommandations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - **Prioritiser l'expérience mobile** (65% du trafic)
        - **Optimiser le contenu desktop** (35% du trafic)
        - **Limiter les investissements tablette** (2% seulement)
        """)
    
    with col2:
        st.markdown("""
        - **Stratégie différenciée par source**
        - **Focus sur les URLs fabricants**
        - **Améliorer les positions pour les requêtes électriques**
        """)