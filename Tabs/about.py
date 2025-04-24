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
             
    **Catégories:**
    - Général : Résultats sur une large quantité de données issues du site général, et pas pas spécifiquement des sources ciblées citées ci-dessus
    - Appareils : Types d'appareil utilisé (ordinateur, tablette, téléphonne)
    - Apparence dans les résultats de recherche : Différentes façons dont les pages peuvent être présentées aux utilisateurs (extraits de produits, extraits d'avis, résultats de traduction, vidéo)
    - Dates : Tendances en fonction des jours/semaines/mois sur une période d'étalant du 06/11/2024 au 05/02/2025
    - Filtres : 
    - Pages : 
    - Pays : 
    - Requêtes : 
    
    **Naviguez entre les différents onglets d'analyse et explorez les tendances et insights pour chaque catégories.**
    """)