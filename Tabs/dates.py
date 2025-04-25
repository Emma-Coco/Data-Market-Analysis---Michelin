import streamlit as st
import pandas as pd
import os

def show():
    """Contenu de l'onglet 'Calendrier'"""
    st.header("Analyse Temporelle")

    st.markdown("""
        ##### Évolution des performances SEO dans le temps
        """)
    
    # Affichage du graphique principal avec une taille réduite
    st.subheader("Évolution Temporelle des Performances")
    
    try:
        # Utiliser une largeur fixe au lieu de toute la largeur
        col1, col2, col3 = st.columns([1, 8, 1])  # Colonnes avec ratio pour centrer l'image
        with col2:
            st.image("Assets/evolution_temporelle.png", use_column_width=True)
    except:
        st.warning("Image 'Assets/evolution_temporelle.png' non trouvée. Veuillez générer ce graphique.")
    
    # Espace pour commentaires sous le graphique
    st.markdown("""
    Comme dans les précédentes analyses, *Manufacturer URL* domine largement en volume (10x plus de clics/impressions que les autres sources) malgré une légère ***baisse à partir de décembre***. Cette tendance est clairement visible sur les deux premiers graphiques où la ligne verte de Manufacturer URL évolue très au-dessus des autres sources.

    Toutefois, lorsqu'on observe les données sur une base longitudinale (dispersées dans le temmps), c'est *Tesla KWD* qui maintient les meilleures positions (souvent entre 5-15) et un CTR stable relativement élevé (2-4%). Electric KWD présente quant à lui une forte volatilité avec des pics exceptionnels de CTR (jusqu'à 9% comme on peut le voir vers mi-novembre et fin novembre) mais des performances très instables d'un jour à l'autre.

    L'analyse des graphiques confirme une corrélation positive entre position et CTR - les sources apparaissant plus haut dans les résultats (comme *Tesla KWD*) obtiennent généralement un meilleur taux de conversion. Comme constaté au cours des autres analyses, la stratégie actuelle semble reposer sur Manufacturer URL pour générer du volume tandis que les sources KWD offrent une meilleure efficacité de conversion sur un trafic plus ciblé. 
                
    *Electric KW*D, avec ses pics de performance occasionnels remarquables, semble présenter un potentiel d'optimisation significatif si sa stabilité pouvait être améliorée.

    """)
    
    # Focus sur les pics de CTR
    st.subheader("Focus sur les pics observés pour Electric KWD le 22/11/24")
    
    # Espace texte avant première image
    st.markdown("""
    Il est possible, par exemple, de mettre l'accent sur des pics particuliers observés pour les variations du CTR d'*Electric KWD*, notamment le pic le plus important survenu le **22 novembre 2024**.
    """)
    
    # Première image - Anomalies CTR
    try:
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.image("Assets/anomalies_CTR.png", use_column_width=True)
    except:
        st.warning("Image 'Assets/anomalies_CTR.png' non trouvée. Veuillez générer ce graphique.")
    
    # Espace texte entre les images
    st.markdown("""
    Dans ce graphique, sont observées quatre anomalies majeures du CTR pour *Electric KWD* (points rouges) :

    Trois pics à 5% (08-11, 25-11 et 09-12)
    Un pic exceptionnel à 9% le 22-11, le plus élevé de toute la période

    On note une tendance générale à la baisse sur la période (ligne bleue foncée), une forte volatilité quotidienne, et l'absence d'anomalies après mi-décembre, suggérant une stabilisation à des niveaux plus bas.
    Le pic du 22 novembre se distingue clairement comme l'événement le plus remarquable, méritant une analyse approfondie.
    """)
    
    # Seconde image - Anomalies Position
    try:
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.image("Assets/anomalies_position.png", use_column_width=True)
    except:
        st.warning("Image 'Assets/anomalies_position.png' non trouvée. Veuillez générer ce graphique.")
    
    # Espace texte final
    st.markdown("""
    Trois anomalies négatives sont à observer, indiquant des positions particulièrement basses dans les résultats :

    04-12 : position 23.81
    16-01 : position 27.23
    26-01 : position 30.31 (la pire)


    Une forte instabilité des positions quotidiennes (ligne bleue claire) oscillant entre 8 et 30
    Une tendance générale (ligne bleue foncée) montrant des performances variables avec une détérioration en janvier 2025
    Aucune anomalie positive détectée (positions exceptionnellement bonnes)

    Dans ce cadre, ***il est difficile de voir un quelconque lien entre l'impact de la position sur le CTR***. Elles suggèrent une relation ***complexe et peut-être inverse*** entre les pics de performance CTR et l'évolution ultérieure des positions. Il serait donc imprudent de formuler des observations et de créer des loiens concrets en utilisant la **position** afin de prédire les **variations** d'autres KPI.
    """)

    # Analyse hebdomadaire
    st.subheader("Analyse des performances par jour de la semaine")

    # Image des performances hebdomadaires  
    try:
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.image("Assets/tendances_jour_semaine.png", use_column_width=True)
    except:
        st.warning("Image 'Assets/tendances_jour_semaine.png' non trouvée. Veuillez générer ce graphique.")

    # Espace texte sous l'image
    st.markdown("""
    Cette analyse des performances par jour de la semaine révèle plusieurs tendances intéressantes :

    - Les **clics** semblent relativement stables tout au long de la semaine, avec une légère tendance à la baisse le week-end
    - Les **impressions** montrent une légère augmentation en fin de semaine (vendredi et samedi)
    - Le **CTR** est généralement plus élevé en début de semaine (lundi et mardi) et plus faible le dimanche
    - Les **positions** restent relativement constantes, avec une légère amélioration le lundi

    Ces données suggèrent que les ***jours ouvrables***, particulièrement le début de semaine, pourraient être plus propices à l'engagement des utilisateurs, tandis que le week-end génère potentiellement plus d'impressions mais avec un taux de conversion plus faible.
    """)
    
    # Analyse détaillée par période
    st.subheader("Analyse par Période")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Période à fort trafic
        
        Analyse des périodes où le trafic a été particulièrement élevé :
        
        - Quels mois/semaines ont généré le plus d'impressions et de clics
        - Facteurs potentiellement contributifs
        - Performances relatives (CTR) pendant ces périodes
        """)
    
    with col2:
        st.markdown("""
        ### Tendances de positionnement
        
        Analyse de l'évolution des positions moyennes :
        
        - Tendance générale (amélioration ou détérioration)
        - Corrélation entre position et autres métriques
        - Périodes de changements significatifs
        """)
    
    # Comparaison saisonnière
    st.subheader("Comparaison Saisonnière")
    
    try:
        st.image("Assets/comparaison_saisonniere.png", use_column_width=True)  # Image hypothétique
    except:
        st.markdown("Graphique de comparaison saisonnière non disponible")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Performances hebdomadaires
        
        - Analyse des performances selon les jours de la semaine
        - Identification des jours les plus performants
        - Recommandations basées sur ces tendances
        """)
    
    with col2:
        st.markdown("""
        ### Impact des mises à jour
        
        - Identification des changements suite aux mises à jour majeures
        - Analyse des impacts positifs ou négatifs
        - Recommandations d'ajustements stratégiques
        """)
    
    # Résumé et recommandations
    st.subheader("Résumé des observations")
    
    st.markdown("""
    Synthèse des principales observations temporelles et recommandations :
    
    - Points clés identifiés dans l'analyse temporelle
    - Opportunités de croissance basées sur les tendances historiques
    - Recommandations stratégiques pour optimiser les performances futures
    """)

show()