import streamlit as st

def show():
    """Affiche le contenu de l'onglet 'À propos'"""
    st.header("À propos de ce dashboard")
    
    st.write("""
    Cette application vous permet d'explorer et d'analyser les performances SEO de Michelin sur le marché mexicain.
    
    **Enjeu principal:** La catégorisation des requêtes liées aux pneus pour véhicules électriques, permettant d'identifier les tendances et opportunités spécifiques à ce segment.
    
    **Sources de données:**
    - Manufacturer URLs
    - Electric URLs
    - Electric KWD (Keywords)
    - Tesla KWD (Keywords)
    - Global
    
    **Comment utiliser ce dashboard:**
    1. Naviguez entre les différents onglets d'analyse
    2. Explorez les tendances et insights pour chaque segment
    """)