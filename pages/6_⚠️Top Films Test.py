import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Au Grand RAJJ - TOP",
    page_icon="🎬",
    layout="wide"
)

st.warning("Cette page est en cours d'amélioration", icon="⚠️")


# Chargement des données
df = pd.read_csv('top5moviebyyear.csv', sep=",", names=['Titre du film', 'Année', 'Genres', 'Note', 'Votes'])
df['Genres'] = df['Genres'].str.replace('[', '').str.replace(']', '').str.replace(" ' ", " ")

# Chargement des données supplémentaires pour les URL et synopsis
data = pd.read_csv('tmdb_full.csv', sep=',')
url_prefix = "https://image.tmdb.org/t/p/w185/"

# Titre de la page
st.title('Découvrez le TOP des films par année et/ou par genre')

# Barre latérale pour les filtres
st.sidebar.header("Filtrez ici 👇")

annee = st.sidebar.multiselect(
    "Quelle année souhaitez-vous ?",
    options=df.sort_values(by="Année", ascending=False).Année.unique(),
    default=None,
    placeholder="Choisissez une année",
)

genre = st.sidebar.multiselect(
    "Quel genre de film souhaitez-vous ?",
    options=df.sort_values(by="Genres", ascending=True).Genres.unique(),
    default=None,
    placeholder="Choisissez un genre",
)

# Filtrage des données
df_selection = df.query("Année == @annee | Genres == @genre")

if df_selection.empty:
    st.error(" :warning: En l'absence de résultat, merci de choisir une autre année ou un autre genre.")
    st.stop()

# Ajout de la colonne URL pour les affiches de films et de la colonne Synopsis
df_selection = df_selection.merge(data[['original_title', 'poster_path', 'overview']],
                                  left_on='Titre du film', right_on='original_title', how='left')
df_selection['URL'] = url_prefix + df_selection['poster_path']
df_selection['Synopsis'] = df_selection['overview']
#df_selection['Synopsis FR'] = df_selection['Synopsis'].apply(lambda x: GoogleTranslator(source='auto', target='fr').translate(x))

# Affichage des sous-titres
st.subheader(f"Année(s) : {', '.join(map(str, annee))}")
st.subheader(f"Genre(s) : {', '.join(genre)}")

# Affichage des films
for idx, row in df_selection.iterrows():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(row['URL'], width=250)
    with col2:
        st.write(f"**Titre :** {row['Titre du film']}")
        st.write(f"**Année de production :** {row['Année']}")
        st.write(f"**Note :** {row['Note']}")
        st.write(f"**Votes :** {row['Votes']}")
    with col3:
        st.write(f"**Synopsis :** {row['Synopsis']}")
        #st.write(f"**Synopsis FR :** {row['Synopsis FR']}")
