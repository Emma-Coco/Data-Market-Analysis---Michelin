# Fichier: Utils/lexicon.py
import streamlit as st

def display_lexicon():
    """Affiche un lexique des termes SEO dans un expander"""
    # Style personnalisé pour les classes d'expander communes dans Streamlit
    st.markdown("""
        <style>
        /* Cibler les classes d'expander communes */
        div[data-testid="stExpander"] > div:first-child {
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            color: #002855 !important;
            background-color: #f0f2f6 !important;
            border-left: 4px solid #FFD100 !important;
            padding: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.expander("Lexique des termes SEO", expanded=False):
        st.markdown(
            """
            <style>
            .lexique-table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            }
            .lexique-table th {
                background-color: #002855;
                color: white;
                padding: 10px;
                text-align: left;
                font-weight: bold;
            }
            .lexique-table td {
                padding: 8px 10px;
                border-bottom: 1px solid #e0e0e0;
            }
            .lexique-table tr:nth-child(even) {
                background-color: #f5f5f5;
            }
            /* Suppression de l'effet de survol */
            </style>
            
            <table class="lexique-table">
                <tr>
                    <th>Terme</th>
                    <th>Définition</th>
                </tr>
                <tr>
                     <td><strong>CTR</strong></td>
                     <td>
                        Click-Through Rate (Taux de Clics) – Pourcentage de personnes qui cliquent sur un résultat après l'avoir vu dans les résultats de recherche. Formule : Clics ÷ Impressions.
                        <ul>
                        <li>La moyenne globale se situe généralement entre 1% et 2%</li>
                        <li>Pour les positions en première page : 2-5% est considéré comme bon</li>
                        <li>Pour les premières positions (1-3) : 5-10% est considéré comme bon à excellent</li>
                        </ul>
                    </td>
                </tr>
                <tr>
                    <td><strong>Position</strong></td>
                    <td>Position moyenne dans les résultats de recherche. Plus la valeur est basse (proche de 1), meilleur est le classement</td>
                </tr>
                <tr>
                    <td><strong>Impressions</strong></td>
                    <td>Nombre de fois où une page a été affichée dans les résultats de recherche</td>
                </tr>
                <tr>
                    <td><strong>Clics</strong></td>
                    <td>Nombre de fois où les utilisateurs ont cliqué sur un résultat de recherche</td>
                </tr>
                <tr>
                    <td><strong>Fiabilité</strong></td>
                    <td>Indice de confiance statistique basé sur le volume d'impressions : Très faible (&lt;10), Faible (10-100), Moyenne (100-1000), Bonne (1000-10000), Excellente (&gt;10000)</td>
                </tr>
                <tr>
                    <td><strong>Source</strong></td>
                    <td>Origine des données de recherche (Manufacturer URLs, Electric URLs, Electric KWD, Tesla KWD)</td>
                </tr>
                <tr>
                    <td><strong>KWD</strong></td>
                    <td>Keyword Data - Données de mots-clés spécifiques</td>
                </tr>
                <tr>
                    <td><strong>URL</strong></td>
                    <td>Uniform Resource Locator - Adresse web des pages analysées</td>
                </tr>
            </table>
            """,
            unsafe_allow_html=True
        )