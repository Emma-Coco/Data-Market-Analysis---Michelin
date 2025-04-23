import streamlit as st

def display_footer():
    """Affiche le pied de page personnalisé avec logo Michelin"""
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <p style="color: #002855; font-style: italic;">Dashboard développé dans le cadre du projet Data Market Analysis - 2025</p>
        <img src="Assets/Michelin-Logo.png" width="100">
    </div>
    """, unsafe_allow_html=True)