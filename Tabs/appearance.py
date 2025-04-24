import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Apparence'"""
    st.header("Analyse par Apparence")

    st.markdown("""
        ##### Apparence des résultats dans les pages de recherche et leur impact sur les performances SEO.        
        """)
    
    col1, col2 = st.columns([5, 6])  # Ratio 5/5
    
    with col1:
        st.markdown("""
        ### Aperçu des données brutes
                    
        Les valeurs maximales de Clics, Impressions et CTR sont surlignées en jaune, et les meilleures positions (les plus basses) sont surlignées en vert.

        Les données brutes indiquent des variations significatives de performance selon l'apparence des résultats.

        On observe notamment que certains types d'apparence génèrent un CTR plus élevé même avec moins d'impressions, suggérant une meilleure pertinence perçue par les utilisateurs.           
        """)
    
    with col2:
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
        
        La majorité des impressions se fait pour l'apparence de type **Rich results**, qui représente:
                    
        **X%** des impressions totales
        
        Suivie par:
        
        **Featured snippet**:
                    
        X% des impressions
        
        **Résultat standard**:
                    
        X% des impressions
        
        **Image**:
                    
        X% des impressions
        """)
    
    # Graphique des clics par apparence (texte à gauche, image à droite)
    st.subheader("Répartition des Clics par Type d'Apparence")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        La distribution des clics montre que **Rich results** génère également le plus de clics:
                    
        **X%** des clics totaux
        
        Cependant, **Featured snippet** présente une proportion plus importante de clics par rapport à ses impressions:
                    
        **X%** des clics
                            
        Cela suggère une meilleure efficacité des featured snippets pour attirer les utilisateurs.
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
                       
        L'analyse du CTR révèle que les **Featured snippets** offrent le meilleur taux de conversion, avec **X%**.
        
        Cela confirme leur efficacité supérieure à attirer les clics malgré un volume d'impressions plus faible.
        
        Les **Rich results** présentent un CTR de **X%**, ce qui est bon mais inférieur à celui des featured snippets.
        """)
    
    # Position et CTR par apparence (texte à gauche, image à droite)
    st.subheader("Position Moyenne et CTR par Type d'Apparence")
    col1, col2 = st.columns([3, 7])  # Ratio 30/70
    
    with col1:
        st.markdown("""
        
        On observe une corrélation claire entre la **position moyenne** et le **CTR**:
        
        Les types d'apparence positionnés en haut des résultats (position proche de 1) génèrent généralement un meilleur CTR.
        
        Les **Featured snippets** bénéficient d'une position moyenne de **X**, expliquant en partie leur excellent CTR.
        
        En revanche, les **Résultats standards** sont positionnés en moyenne à **X** et présentent un CTR plus faible de **X%**.
        """)
    
    with col2:
        try:
            st.image("Assets/appearance_position_ctr.png", use_column_width=True)
        except:
            st.warning("Image 'Assets/appearance_position_ctr.png' non trouvée. Veuillez générer ce graphique.")
    
    # Section de recommandations
    st.subheader("Résumé des observations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
                         
        - **Prioriser les featured snippets**: Ils génèrent le meilleur CTR et représentent une opportunité de visibilité même avec moins d'impressions
        
        - **Développer les rich results**: Ils combinent bon volume d'impressions et CTR satisfaisant
                    
        - **Éviter de se contenter des résultats standards**: Leur faible CTR et position moyenne moins favorable les rendent moins efficaces
        
        - **Intégrer des images**: Bien qu'ayant un volume limité, elles peuvent compléter efficacement la stratégie
        """)
    
    with col2:
        st.markdown("""
      
        - **La position influence fortement le CTR**: L'optimisation pour des positions plus hautes reste essentielle
        
        - **L'apparence visuelle des résultats compte autant que la position**: Diversifier les types d'apparence permet de maximiser l'engagement
        
        - **Adapter le contenu aux formats préférentiels**: Structurer le contenu pour favoriser les featured snippets et rich results
                    
        - **Analyser les tendances spécifiques par secteur**: Certains types d'apparence peuvent être plus efficaces pour les pneus électriques
        """)