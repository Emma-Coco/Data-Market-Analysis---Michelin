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

    # Analyse hebdomadaire - Réduire la taille de l'image
    st.subheader("Analyse des performances par jour de la semaine")

    # Image des performances hebdomadaires avec taille réduite 
    try:
        col1, col2, col3 = st.columns([2, 7, 2])  # Ratio modifié pour une image plus petite
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

    Ces données suggèrent que les jours ouvrables, particulièrement **le début de semaine**, pourraient être plus propices à l'***engagement des utilisateurs***, tandis que le **week-end** génère potentiellement plus d'***impressions*** mais avec un taux de conversion plus faible. Le comportement d'exposition (impressions) reste constant, mais l'engagement (clics et CTR) varie davantage.
    """)
    
   # Comparaison saisonnière mensuelle
    st.subheader("Comparaison Mensuelle par Source")

    # Image de la comparaison mensuelle
    try:
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.image("Assets/comparaison_mensuelle.png", use_column_width=True)
    except:
        st.warning("Image 'Assets/comparaison_mensuelle.png' non trouvée. Veuillez générer ce graphique.")

    # Espace texte sous l'image
    st.markdown("""
    La répartition mensuelle des performances révèle des tendances saisonnières marquées :

    - **Clics** : *Manufacturer URL* montre une forte baisse en février, suivie d'une remontée significative en novembre et décembre
    - **CTR** : *Tesla KWD* présente une amélioration constante depuis février, atteignant son pic en décembre (2.7%)
    - **Positions** : Détérioration générale des positions en novembre pour toutes les sources sauf *Tesla KWD* qui s'améliore remarquablement
    - **Impressions** : Tendance similaire aux clics avec un creux en février et une reprise en fin d'année

    Ces variations mensuelles indiquent une ***saisonnalité claire*** avec un ***creux en février*** et une ***performance optimale en fin d'année***. La dynamique de *Tesla KWD* est particulièrement notable, montrant une amélioration progressive du CTR associée à des positions plus favorables en novembre et décembre.
    """)
    
    # Résumé et recommandations
    st.subheader("Résumé des observations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Points clés à retenir :")
        st.markdown("""
        1. **Domination de Manufacturer URL** en volume (×10) avec un CTR modéré, tandis que **Tesla KWD** offre le meilleur CTR et les meilleures positions

        2. **Electric KWD** montre un potentiel inexploité avec des pics exceptionnels de CTR (jusqu'à 9%) mais une grande instabilité

        3. **Saisonnalité marquée** : performance optimale en fin d'année (nov-déc) et creux en février

        4. **Engagement plus fort en début de semaine**, impressions plus élevées le week-end

        5. **Relation complexe entre position et CTR**, suggérant l'influence d'autres facteurs dans la performance
        """)

    with col2:
        st.markdown("#### Recommandations principales :")
        st.markdown("""
        1. **Stratégie différenciée** : optimiser Manufacturer URL pour le volume, Tesla KWD pour la conversion, et stabiliser Electric KWD

        2. **Planification saisonnière** : concentrer les efforts sur nov-déc et utiliser février pour tester de nouvelles approches

        3. **Programmation hebdomadaire optimisée** : contenus importants en début de semaine et adaptation du contenu weekend

        4. **Approche équilibrée** : ne pas se focaliser uniquement sur les positions mais travailler aussi sur la pertinence du contenu

        5. **Analyse des pics de performance** pour reproduire les conditions des meilleurs résultats observés
        """)

show()