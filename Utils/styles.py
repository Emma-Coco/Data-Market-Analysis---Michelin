import streamlit as st

def set_page_style():
    """Définit un style CSS avancé pour transformer les onglets en écran distinct"""
    st.markdown("""
    <style>
        /* Couleurs principales Michelin */
        :root {
            --michelin-blue: #002855;
            --michelin-yellow: #FFD100;
            --michelin-light-blue: #b3c7e6;
            --michelin-gray: #f7f7f7;
            --michelin-dark-gray: #e0e0e0;
        }
        
        /* Réduire l'espace entre le header et le contenu */
        .block-container {
            padding-top: 1rem !important;
            margin-top: 0 !important;
        }
        
        /* Ajuster les marges du titre principal */
        h1:first-of-type {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Réduire les marges des sous-titres */
        h3 {
            margin-top: 0.5rem !important;
            margin-bottom: 1.5rem !important;
        }
        
        /* Container principal pour les onglets */
        .stTabs {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 40, 85, 0.12);
            margin: 1rem 0 2rem 0; /* Réduit la marge du haut */
            overflow: hidden;
            border: 1px solid #e0e0e0;
        }
        
        /* Barre d'onglets */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            background-color: var(--michelin-blue);
            padding: 5px 5px 0 5px;
            border-bottom: none;
        }
        
        /* Style des onglets */
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 8px 8px 0 0;
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
            padding: 12px 24px;
            margin-right: 2px;
            transition: all 0.3s ease;
            border: none;
        }
        
        /* Animation au survol */
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            transform: translateY(-2px);
        }
        
        /* Onglet actif */
        .stTabs [aria-selected="true"] {
            background-color: white !important;
            color: var(--michelin-blue) !important;
            font-weight: 600 !important;
            transform: translateY(-4px);
            box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.1);
        }
        
        /* Contenu des onglets */
        .stTabs [data-baseweb="tab-panel"] {
            padding: 25px 20px;
            background-color: white;
            border-radius: 0 0 10px 10px;
            min-height: 400px; /* Hauteur minimale pour l'effet écran */
        }
        
        /* Changer la ligne de navigation rouge en jaune */
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: var(--michelin-yellow) !important;
            height: 3px !important;
        }
        
        /* Effet "écran" en arrière-plan */
        .stTabs:before {
            content: "";
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            background-color: var(--michelin-dark-gray);
            z-index: -1;
            border-radius: 12px;
        }
        
        /* Effet de bordure lumineuse */
        .stTabs:after {
            content: "";
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(135deg, var(--michelin-yellow) 0%, transparent 50%, var(--michelin-blue) 100%);
            z-index: -2;
            border-radius: 12px;
            opacity: 0.3;
            filter: blur(3px);
        }
        
        /* Personnalisation des titres pour l'écran */
        .stTabs h1, .stTabs h2, .stTabs h3 {
            color: var(--michelin-blue) !important;
        }
        
        /* Animation subtile des onglets */
        @keyframes tabFadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .stTabs [data-baseweb="tab-panel"] {
            animation: tabFadeIn 0.3s ease-out;
        }
    </style>
    """, unsafe_allow_html=True)