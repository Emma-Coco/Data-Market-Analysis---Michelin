import pandas as pd
import os
import re

# Chemin vers le dossier contenant les données brutes
chemin_donnees_brutes = "C:/Users/HP/Downloads/DIA3_HETIC/Data_marketing/project/Data-Market-Analysis---Michelin/raw_data"

# Liste des dossiers exacts
dossiers = [
    "manufacturer URL",
    "Tesla KWD",
    "Electric KWD",
    "Electric URL",
    "Global",
]

# Liste des fichiers exacts
fichiers = [
    "Appareils.csv",
    "Apparence dans les résultats de recherche.csv",
    "Dates.csv",
    "Filtres.csv",
    "Pages.csv",
    "Pays.csv",
    "Requêtes.csv",
]

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists("Clean_data"):
    os.makedirs("Clean_data")


# Fonction pour nettoyer et préparer les données
def nettoyer_donnees(df, nom_fichier):
    df_clean = df.copy()

    # 1. Convertir les colonnes de pourcentage (comme CTR)
    if 'CTR' in df_clean.columns:
        df_clean['CTR'] = (
            df_clean['CTR']
            .astype(str)
            .str.replace('%', '')
            .str.replace(',', '.')
            .astype(float)
            / 100
        )
        df_clean['CTR'] = df_clean['CTR'].round(4)

    # 2. Standardiser les formats de date si nécessaire
    if 'Date' in df_clean.columns:
        if not pd.api.types.is_datetime64_any_dtype(df_clean['Date']):
            df_clean['Date'] = pd.to_datetime(
                df_clean['Date'], errors='coerce'
            )
            n_dates_na = df_clean['Date'].isna().sum()
            print(f"{n_dates_na} dates non reconnues dans {nom_fichier}")

    # 3. Standardiser les noms de colonnes
    df_clean.columns = df_clean.columns.str.strip().str.replace(' ', '_')

    # 4. Gérer les valeurs manquantes
    for col in df_clean.columns:
        if df_clean[col].dtype in ['int64', 'float64']:
            df_clean[col] = df_clean[col].fillna(0)
        else:
            df_clean[col] = df_clean[col].fillna('')

    return df_clean


# Traiter chaque type de fichier
for fichier in fichiers:
    df_consolide = pd.DataFrame()

    for dossier in dossiers:
        chemin_dossier = os.path.join(chemin_donnees_brutes, dossier)

        if not os.path.exists(chemin_dossier):
            print(f"Dossier '{chemin_dossier}' non trouvé, passage au suivant")
            continue

        chemin_fichier = os.path.join(chemin_dossier, fichier)

        if os.path.exists(chemin_fichier):
            try:
                try:
                    df = pd.read_csv(
                        chemin_fichier, encoding='utf-8', thousands=','
                    )
                except UnicodeDecodeError:
                    try:
                        df = pd.read_csv(
                            chemin_fichier, encoding='latin1', thousands=','
                        )
                    except UnicodeDecodeError:
                        df = pd.read_csv(
                            chemin_fichier,
                            encoding='ISO-8859-1',
                            thousands=',',
                        )

                df['Source'] = dossier
                df_consolide = pd.concat([df_consolide, df], ignore_index=True)
                print(f"Fichier {chemin_fichier} traité avec succès")
            except Exception as e:
                print(f"Erreur lors du traitement de {chemin_fichier}: {e}")
        else:
            print(
                f"Fichier '{fichier}' non trouvé dans le dossier '{chemin_dossier}'"
            )

    if not df_consolide.empty:
        df_consolide = nettoyer_donnees(df_consolide, fichier)
        nom_base = os.path.splitext(fichier)[0]
        nom_excel = re.sub(r'[^\w\-_\.]', '_', nom_base) + "_all.xlsx"
        chemin_sortie = os.path.join("./Data-Market-Analysis---Michelin/Clean_data", nom_excel)
        df_consolide.to_excel(chemin_sortie, index=False, engine='openpyxl')
        print(f"Fichier Excel consolidé et nettoyé créé: {chemin_sortie}")
    else:
        print(f"Aucune donnée trouvée pour {fichier}")

print("Consolidation et nettoyage terminés!")
