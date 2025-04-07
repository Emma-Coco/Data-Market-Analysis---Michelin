import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Michelin SEO Dashboard - Mexico",
    page_icon="🔍",
    layout="wide"
)

# Titre et introduction
st.title("Michelin SEO Dashboard - Marché Mexicain")
st.markdown("### Analyse des données search pour le marché sud-américain")

# Description du projet
st.write("""
Cette application vous permet d'explorer et d'analyser les performances SEO de Michelin sur le marché mexicain.
Utilisez le menu de navigation pour accéder aux différentes analyses.
""")

# Information sur les données
st.subheader("Sources de données")
st.write("""
Les données analysées proviennent de 5 sources principales:
- Manufacturer URLs
- Electric URLs
- Electric KWD (Keywords)
- Tesla KWD (Keywords)
- Global
""")

# Ajouter une section "Comment utiliser"
st.subheader("Comment utiliser ce dashboard")
st.write("""
1. Naviguez entre les différentes pages d'analyse via le menu latéral
2. Utilisez les filtres disponibles pour affiner les visualisations
3. Explorez les tendances et insights pour chaque segment
""")

# Pied de page
st.markdown("---")
st.markdown("*Dashboard développé dans le cadre du projet Data Market Analysis - 2025*")