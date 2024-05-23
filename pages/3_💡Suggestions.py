import streamlit as st
import base64
from pathlib import Path
from deep_translator import GoogleTranslator

#st.sidebar.markdown("# Suggestions")
page_title="Suggestions"

with st.sidebar:
    st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWVmMXR6b2c2eXM5cjY2c2xuZGhqbzlhYzUwZGR5czM1bHY5dGtlcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/DwTYpuxQCF2xmhuoqs/giphy.gif')

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
df = pd.read_csv('df_merge_ratings.csv', sep=',')

#df.columns
# Set the display option to show all columns
pd.set_option('display.max_columns', None)

# Display the first few rows of the DataFrame
#display(df.head())
X = df.select_dtypes(include=[np.number])

#on selectionne seulement les colonnes numériques
primary_title_movies = X.groupby(df['primaryTitle']).mean().reset_index()  #Grouper les données par 'primaryTitle' et calculer la moyenne
numeric_cols = primary_title_movies.select_dtypes(include=[np.number]).columns # Sélectionner les noms des colonnes numériques après le groupby
from sklearn.preprocessing import StandardScaler
# Normalisation
scaler = StandardScaler()
scaled_features = scaler.fit_transform(primary_title_movies[numeric_cols])
# Créer un nouveau dataframe avec les caractéristiques normalisées
scaled_df = pd.DataFrame(scaled_features, columns=numeric_cols)
scaled_df['primaryTitle'] = primary_title_movies['primaryTitle']

modelNN = NearestNeighbors(n_neighbors=6)
modelNN.fit(scaled_features)
#on crée le modèle
#scaled_df.loc[scaled_df['primaryTitle'] == 'Toy Story']
#on cherche les films de Toy Story
#film_connus = ['Toy Story','The Dark Knight','The Avengers','The Lord of the Rings: The Return of the King','The Lord of the Rings: The Fellowship of the Ring','The Lord of the Rings: The Two Towers']
#on fait une liste de films connus
#modelNN
import warnings

# Ignorer tous les avertissements
warnings.filterwarnings("ignore")

from fuzzywuzzy import fuzz, process
def find_closest_title(title, scaled_df):
    closest_match = process.extractOne(title, scaled_df['primaryTitle'], scorer=fuzz.token_set_ratio)
    if closest_match[1] > 70:
        return closest_match[0]
    return None

# Fonction pour obtenir les recommandations pour un film donné
def recommander_films(film_title):
        # Trouver le titre le plus proche
    closest_title = find_closest_title(film_title, scaled_df)
    if closest_title is None:
        return f"Aucun titre proche trouvé pour '{film_title}'."

    
    # Obtenir les caractéristiques du film spécifié (sans la colonne 'primaryTitle')
    caracteristiques = scaled_df[scaled_df['primaryTitle'] == film_title].drop(columns=['primaryTitle'])
    
    # Trouver les films similaires
    distances, indices = modelNN.kneighbors(caracteristiques)
    
    recommended_indices = indices[0][distances[0] > 0]  # Exclure l'indice avec une distance de 0 (soi-même)
    recommended_movies = primary_title_movies.iloc[recommended_indices][:5]  # Limiter à 5 résultats
    # Afficher les films recommandés avec des informations supplémentaires
    #recommended_movies = primary_title_movies.iloc[indices[0]]
    recommended_movies['startYear'] = recommended_movies['startYear'].round().astype(int)
    recommended_movies['averageRating'] = recommended_movies['averageRating'].round(2).astype(float)
    recommended_movies['runtimeMinutes'] = recommended_movies['runtimeMinutes'].round().astype(int)

    # Créer un dictionnaire de mapping pour les noms des colonnes
    column_mapping = {
        'primaryTitle': 'Titre',
        'startYear': 'Année',
        'averageRating': 'Note',
        'runtimeMinutes': 'Durée en mns'
    }
    
    # Mapper les noms des colonnes
    recommended_movies.rename(columns=column_mapping, inplace=True)
    
    # Sélectionner les colonnes à afficher
    columns_to_display = ['Titre', 'Année', 'Note', 'Durée en mns']
    return recommended_movies[columns_to_display]

# Saisie de l'utilisateur
#user_input = input("Entrez le nom du film :")
#print(recommander_films(user_input))


# Interface utilisateur avec Streamlit
st.title("Recommandation de Films")
st.subheader("Parcourez notre base de données et entrez le nom d'un film pour obtenir des recommandations similaires.")

# SelectBox

data = pd.read_csv('tmdb_full.csv', sep=',')

#Exemple de DataFrame
#data = pd.DataFrame({
#    'poster_path': ['zzZCWxroewVrcKPtz6Xi1x9SinU.jpg', 'anotherImage.jpg', 'yetAnotherImage.jpg']
#})

#Préfixe de l'URL
url_prefix = "https://image.tmdb.org/t/p/w185/"

#Nouvelle Colonne

# Saisie de l'utilisateur
user_input = st.selectbox("Entrez le nom du film :", (scaled_df['primaryTitle']), index=None, placeholder="Choisissez un film parmi 176594 films",)


if user_input:
    with st.spinner('Votre recherche en cours, merci de patienter quelques instants'):
        time.sleep(4)

    recommendations = recommander_films(user_input)
    st.write("Votre recherche : " + user_input)
    st.write("Voici Des Films Recommandés :")
            # Ajout de la colonne URL pour les affiches de films
    recommendations = recommendations.merge(data[['original_title', 'poster_path', 'overview']], left_on='Titre', right_on='original_title')
    recommendations['URL'] = url_prefix + recommendations['poster_path']
    recommendations['Synopsis'] = recommendations['overview']
  # Traduction des synopsis
    recommendations['Synopsis FR'] = recommendations['Synopsis'].apply(lambda x: GoogleTranslator(source='auto', target='fr').translate(x))
    # Afficher les images dans Streamlit
    for idx, row in recommendations.iterrows():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(row['URL'], width=250)
        with col2:
            st.write(f"**Titre :** {row['Titre']}")
            st.write(f"**Année de production :** {row['Année']}")
            st.write(f"**Note :** {row['Note']}")
            st.write(f"**Durée en minutes :** {row['Durée en mns']}")
        with col3:
            st.write(f"**Synopsis :** {row['Synopsis']}")
            st.write(f"**Synopsis FR: ** {row['Synopsis FR']}")

    #st.dataframe(recommendations.style.format({
    #'startYear': lambda x: f"{x:.0f}"  # Remove commas from years (treated as float/int)
#}).format({
    #'Note': lambda x: f"{x:.2f}⭐"  # Remove commas from years (treated as float/int)
#}),hide_index=True
#)
