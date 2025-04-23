import streamlit as st
from Utils.styles import set_page_style
from Utils.header import display_header
from Utils.footer import display_footer
from Tabs import about, recommendations, devices, dates, appearance, global_analysis

# Configuration de la page
st.set_page_config(page_title="Michelin SEO Dashboard - Mexico", page_icon="🔍", layout="wide")

# Application du style personnalisé
set_page_style()

# Affichage du logo en haut
display_header()

# Titre et sous-titre sous le logo
st.title("SEO Dashboard - Marché Mexicain")
st.markdown("### Analyse des données search pour le marché sud-américain du 06/11/2024 au 05/02/2025")

# Création des onglets
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "À propos", "Recommandations", "Appareils", "Dates", "Apparence", "Analyse Globale"
])

# Affichage du contenu dans chaque onglet
with tab1:
    about.show()
# with tab2:
#     recommendations.show()
# with tab3:
#     devices.show()
# with tab4:
#     dates.show()
# with tab5:
#     appearance.show()
# with tab6:
#     global_analysis.show()

# Affichage du pied de page
display_footer()