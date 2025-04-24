import streamlit as st
from Utils.styles import set_page_style
from Utils.header import display_header
from Utils.footer import display_footer
from Utils.lexicon import display_lexicon
from Tabs import about, recommendations, devices, dates, appearance, global_analysis, filters, pages, countries, queries

# Configuration de la page
st.set_page_config(page_title="Michelin SEO Dashboard - Mexico", page_icon="🔍", layout="wide")

# Application du style personnalisé
set_page_style()

# Affichage du logo en haut
display_header()

# Titre et sous-titre sous le logo
st.title("SEO Dashboard - Marché Mexicain")
st.markdown("### Analyse des données search pour le marché sud-américain pour la plage du 06/11/2024 au 05/02/2025")

# Affichage du lexique
display_lexicon()

# Création des onglets dans le nouvel ordre
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "À propos", "Général", "Appareils", "Apparence", "Dates", "Filtres", "Pages", "Pays", "Requêtes", "Recommendations"
])

# Affichage du contenu dans chaque onglet
with tab1:
    about.show()
with tab2:
    global_analysis.show()
with tab3:
    devices.show()
with tab4:
    appearance.show()
with tab5:
    dates.show()
with tab6:
    filters.show() 
with tab7:
    pages.show()  
with tab8:
    countries.show() 
with tab9:
    queries.show() 
with tab10:
    recommendations.show() 

# Affichage du pied de page
display_footer()