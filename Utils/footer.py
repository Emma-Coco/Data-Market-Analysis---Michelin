import streamlit as st

def display_footer():
    """Affiche le pied de page personnalisé avec logos"""
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <p style="color: #002855; font-style: italic;">
            Dashboard développé dans le cadre du projet Data Market Analysis - 2025
        </p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Logo_HETIC.png" width="100">  
    </div>

    <div style="display: flex; justify-content: flex-end; align-items: center; margin-top: 0.5rem;">
        <p style="margin: 0 10px 0 0;">Et la participation de</p>  
        <img src="https://vtlogo.com/wp-content/uploads/2020/11/jellyfish-group-vector-logo.png" width="80">     
    </div>
    """, unsafe_allow_html=True)  # ⬅️ le paramètre important ici

