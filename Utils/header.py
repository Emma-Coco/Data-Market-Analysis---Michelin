import streamlit as st

def display_header():
    """Header avec logo ajusté, ombre, décalage, et icône menu"""

    st.markdown("""
    <style>
        header {display: none !important;}
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #FFFFFF;
            color: white;
            padding: 10px;
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: space-between; /* Sépare logo et menu */
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        }
        .fixed-header img {
            height: 32px;
            margin-left: 70px;
        }
        .menu-icon {
            font-size: 24px;
            margin-right: 70px;
            color: #333;
            user-select: none;
        }
        .header-padding {
            height: 60px;
        }
    </style>

    <div class="fixed-header">
        <img src="https://upload.wikimedia.org/wikipedia/fr/f/fe/Logo_Michelin.svg">
        <div class="menu-icon">☰</div>
    </div>

    <div class="header-padding"></div>
    """, unsafe_allow_html=True)
