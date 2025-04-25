import streamlit as st

def about_tab():
    """Contenu de l'onglet 'À propos'"""
    st.header("À propos de ce dashboard")
    
    # Description du projet avec style amélioré
    st.markdown("""
    <div class="section">
        <p style="font-size: 1.1rem; color: #444; margin-bottom: 1.5rem;">
        Cette application vous permet d'explorer et d'analyser les performances SEO de Michelin sur le marché mexicain.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enjeu principal avec mise en valeur
    st.markdown("""
    <div class="section">
        <div class="metric-card" style="border-left: 5px solid #FFD100; padding-left: 1.5rem;">
            <h3 style="color: #002855; margin-bottom: 0.8rem;">Enjeu principal</h3>
            <p>La catégorisation des requêtes liées aux pneus pour véhicules électriques, permettant d'identifier les tendances et opportunités spécifiques à ce segment.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sources de données
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="subheader">', unsafe_allow_html=True)
    st.subheader("Sources de données")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Liste des sources avec style amélioré
    sources = [
        "Manufacturer URLs",
        "Electric URLs",
        "Electric KWD (Keywords)",
        "Tesla KWD (Keywords)",
        "Global"
    ]
    
    # Création d'une disposition en colonnes pour les sources
    cols = st.columns(len(sources))
    for i, (col, source) in enumerate(zip(cols, sources)):
        with col:
            st.markdown(f"""
            <div class="metric-card" style="text-align: center; min-height: 100px; display: flex; align-items: center; justify-content: center;">
                <div style="font-weight: 500;">{source}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Guide d'utilisation
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="subheader">', unsafe_allow_html=True)
    st.subheader("Comment utiliser ce dashboard")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="recommendation-card">
        <strong>1.</strong> Naviguez entre les différents onglets d'analyse
    </div>
    <div class="recommendation-card">
        <strong>2.</strong> Explorez les tendances et insights pour chaque segment
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Période d'analyse
    st.markdown("""
    <div class="section">
        <div class="metric-card" style="background-color: #002855; color: white; text-align: center;">
            <div style="font-size: 1.1rem; margin-bottom: 0.5rem;">Période d'analyse</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #FFD100;">06/11/2024 - 05/02/2025</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def recommendations_tab():
    """Contenu de l'onglet 'Recommandations'"""
    st.header("Recommandations Stratégiques")
    
    # Section pour les recommandations basées sur les analyses
    st.subheader("Opportunités SEO identifiées")
    
    # Exemple de recommandations
    recommandations = [
        "Optimiser le contenu pour les requêtes liées aux véhicules électriques",
        "Développer des pages spécifiques pour le marché mexicain sur les pneus tout-terrain",
        "Créer des contenus techniques sur la durabilité des pneus pour véhicules électriques"
    ]
    
    for i, rec in enumerate(recommandations):
        st.markdown(f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #002855; margin-bottom: 10px;">
        <strong>{i+1}.</strong> {rec}
        </div>
        """, unsafe_allow_html=True)
    
    # Visualisation des opportunités
    st.subheader("Impact potentiel des optimisations")
    # Graphique d'impact...

def devices_tab():
    """Contenu de l'onglet 'Appareils'"""
    st.header("Analyse par Appareils")
    
    # Exemple
    st.subheader("Répartition des recherches par type d'appareil")
    # Intégration du code de visualisation...

def dates_tab():
    """Contenu de l'onglet 'Dates'"""
    st.header("Analyse Temporelle")
    
    st.subheader("Évolution des recherches dans le temps")
    # Visualisations temporelles...

def appearance_tab():
    """Contenu de l'onglet 'Apparence'"""
    st.header("Analyse de l'Apparence")
    
    st.subheader("Éléments visuels et leur impact")
    # Visualisations...

def global_analysis_tab():
    """Contenu de l'onglet 'Analyse Globale'"""
    st.header("Analyse Globale des données SEO")
    
    # Exemple de métriques clés avec style amélioré
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total des requêtes</div>
            <div class="metric-value">XXXXX</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Mots-clés prioritaires</div>
            <div class="metric-value">XXX</div>
            <div class="metric-change-positive">+12%</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Opportunités identifiées</div>
            <div class="metric-value">XX</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="subheader">', unsafe_allow_html=True)
    st.subheader("Distribution des types de requêtes")
    st.markdown('</div>', unsafe_allow_html=True)
    # Code de visualisation...
    st.markdown('</div>', unsafe_allow_html=True)

def queries_tab():
    """Contenu de l'onglet 'Appareils'"""
    st.header("Analyse par Appareils")
    
    # Exemple
    st.subheader("Répartition des recherches par type d'appareil")
    # Intégration du code de visualisation...