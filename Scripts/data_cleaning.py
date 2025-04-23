import pandas as pd
import os
import re


# Chemin vers le dossier contenant les données brutes
chemin_donnees_brutes = "raw_data"

# Liste des dossiers exacts
dossiers = [
    "manufacturer URL",
    "Tesla KWD",
    "Electric KWD",
    "Electric URL",
    "Global"
]

# Liste des fichiers exacts
fichiers = [
    "Appareils.csv",
    "Apparence dans les résultats de recherche.csv",
    "Dates.csv",
    "Filtres.csv",
    "Pages.csv",
    "Pays.csv",
    "Requêtes.csv"
]

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists("Clean_data"):
    os.makedirs("Clean_data")

# Fonction pour nettoyer et préparer les données
# Fonction pour nettoyer et préparer les données
def nettoyer_donnees(df, nom_fichier):
    # Copie du dataframe pour éviter de modifier l'original
    df_clean = df.copy()
    
    # 1. Convertir les colonnes de pourcentage (comme CTR)
    if 'CTR' in df_clean.columns:
        # Enlever le symbole % et convertir en float avec 4 décimales
        df_clean['CTR'] = df_clean['CTR'].astype(str).str.replace('%', '').astype(float) / 100
        # Arrondir à 4 décimales
        df_clean['CTR'] = df_clean['CTR'].round(4)
    
    # Reste de la fonction inchangé...
    # 2. Standardiser les formats de date si nécessaire
    if 'Date' in df_clean.columns:
        try:
            # Convertir en datetime
            df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')
        except:
            print(f"Impossible de convertir les dates dans {nom_fichier}")
    
    # 3. Standardiser les noms de colonnes (supprimer les espaces, accents, etc.)
    df_clean.columns = df_clean.columns.str.strip().str.replace(' ', '_')
    
    # 4. Gérer les valeurs manquantes
    for col in df_clean.columns:
        # Pour les colonnes numériques
        if df_clean[col].dtype in ['int64', 'float64']:
            df_clean[col] = df_clean[col].fillna(0)
        # Pour les colonnes textuelles
        else:
            df_clean[col] = df_clean[col].fillna('')
    
    return df_clean

# Traiter chaque type de fichier
for fichier in fichiers:
    # Créer un DataFrame vide pour stocker les données consolidées
    df_consolide = pd.DataFrame()
    
    # Parcourir chaque dossier
    for dossier in dossiers:
        chemin_dossier = os.path.join(chemin_donnees_brutes, dossier)
        
        # Vérifier si le dossier existe
        if not os.path.exists(chemin_dossier):
            print(f"Dossier '{chemin_dossier}' non trouvé, passage au suivant")
            continue
            
        chemin_fichier = os.path.join(chemin_dossier, fichier)
        
        # Vérifier si le fichier existe
        if os.path.exists(chemin_fichier):
            try:
                # Lire le fichier CSV avec différents encodages possibles
                try:
                    df = pd.read_csv(chemin_fichier, encoding='utf-8')
                except UnicodeDecodeError:
                    try:
                        df = pd.read_csv(chemin_fichier, encoding='latin1')
                    except UnicodeDecodeError:
                        df = pd.read_csv(chemin_fichier, encoding='ISO-8859-1')
                
                # Ajouter une colonne pour identifier la source
                df['Source'] = dossier
                
                # Ajouter au DataFrame consolidé
                df_consolide = pd.concat([df_consolide, df], ignore_index=True)
                
                print(f"Fichier {chemin_fichier} traité avec succès")
            except Exception as e:
                print(f"Erreur lors du traitement de {chemin_fichier}: {e}")
        else:
            print(f"Fichier '{fichier}' non trouvé dans le dossier '{chemin_dossier}'")
    
    # Nettoyer et préparer les données consolidées
    if not df_consolide.empty:
        df_consolide = nettoyer_donnees(df_consolide, fichier)
        
        # Créer un nom de fichier propre pour le fichier consolidé
        nom_base = os.path.splitext(fichier)[0]  # Nom sans extension
        nom_excel = re.sub(r'[^\w\-_\.]', '_', nom_base) + "_all.xlsx"
        
        # Sauvegarder en Excel avec format de date spécifié
        chemin_sortie = os.path.join("Clean_data", nom_excel)
        with pd.ExcelWriter(chemin_sortie, engine='openpyxl', datetime_format='YYYY-MM-DD') as writer:
            df_consolide.to_excel(writer, index=False)
        
        print(f"Fichier Excel consolidé et nettoyé créé: {chemin_sortie}")

print("Consolidation et nettoyage terminés!")