import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Recommandations'"""
    # Titre principal avec style
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Recommandations Stratégiques</h1>", unsafe_allow_html=True)
    
    # Ligne de séparation
    st.markdown("<hr style='border: 2px solid #1E88E5; margin-bottom: 30px;'>", unsafe_allow_html=True)
    
    # Section Ciblage avec carte colorée
    st.markdown("""
    <div style="background-color: #E3F2FD; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #1E88E5;">
        <h3 style="color: #1E88E5;">Ciblage utilisateurs</h3>
        <ul>
            <li><strong style="color: #1565C0;">Mieux cibler les utilisateurs et leurs besoins</strong> : Adapter le contenu pour répondre aux attentes spécifiques des utilisateurs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section KWD
    st.markdown("""
    <div style="background-color: #FFF8E1; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #FFA000;">
        <h3 style="color: #FFA000;">Optimisation des mots-clés</h3>
        <ul>
            <li><strong style="color: #FF8F00;">Améliorer les KWD pour mieux toucher la cible</strong> : Travailler sur les mots-clés pour faire remonter les positions dans les résultats</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section Référencement
    st.markdown("""
    <div style="background-color: #E8F5E9; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #43A047;">
        <h3 style="color: #43A047;">Référencement</h3>
        <ul>
            <li><strong style="color: #2E7D32;">Effectuer un travail approfondi de référencement</strong> : Restructurer les éléments techniques pour améliorer la visibilité</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section URL
    st.markdown("""
    <div style="background-color: #F3E5F5; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #8E24AA;">
        <h3 style="color: #8E24AA;">Recherche organique</h3>
        <ul>
            <li><strong style="color: #6A1B9A;">Optimiser les URL pour le bon public</strong> : S'assurer que les pages répondent précisément à la demande organique des utilisateurs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Section Forces existantes
    st.markdown("""
    <div style="background-color: #FFEBEE; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #E53935;">
        <h3 style="color: #E53935;">Exploitation des atouts</h3>
        <ul>
            <li><strong style="color: #C62828;">Tirer profit des forces identifiées</strong> : Capitaliser sur les appareils performants, types d'apparence efficaces et périodes clés</li>
            <li><strong style="color: #C62828;">Corriger les lacunes soulevées</strong> : Résoudre les problèmes identifiés dans l'analyse pour améliorer les performances</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Conclusion avec appel à l'action
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; padding: 20px; background-color: #F5F5F5; border-radius: 10px;">
        <p style="font-style: italic; color: #616161;">
        Ces recommandations sont basées sur l'analyse complète des données SEO collectées entre novembre 2024 et février 2025.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Exécution de la fonction si ce script est exécuté directement
if __name__ == "__main__":
    show()