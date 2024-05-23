import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


st.set_page_config(
    page_title="Au Grand RAJJ - TOP",
    page_icon="🎬",
    layout = "wide"
)

df = pd.read_csv('top5moviebyyear.csv', sep=",", names=['Titre du film', 'Année', 'Genres', 'Note', 'Votes'])
df['Genres'] = df['Genres'].str.replace('[' , '')
df['Genres'] = df['Genres'].str.replace(']' , '')
df['Genres'] = df['Genres'].str.replace(" ' " , " ")
st.title('Découvrez le TOP des films par année et/ou par genre')
row1 = st.columns(1)

#st.image("https://as1.ftcdn.net/v2/jpg/02/16/28/24/1000_F_216282456_RfRu0YMjE5weIKefNdDckZdZqDZCHZAZ.jpg")


st.sidebar.header("Filtrez ici 👇")

annee = st.sidebar.multiselect(
    "Quelle année souhaitez vous? ",
    options=df.sort_values(by="Année",ascending=False).Année.unique(),
    #default=df["startYear"].unique(),
    default=None,
    placeholder="Choisissez une année",

)

genre = st.sidebar.multiselect(
    "Quel genre de film souhaitez vous? ",
    options=df.sort_values(by="Genres",ascending=True).Genres.unique(),
    #default=df["genres"].unique(),
    default=None,
    placeholder="Choisissez un genre",

)


df_selection = df.query(
    "Année == @annee | Genres == @genre"
)
if df_selection.empty:
    st.error(" :warning: En l'absence de résultat, merci de choisir une autre année ou un autre genre.")
    st.stop() # This will halt the app from further execution.

st.subheader(f"Année(s) : {str(annee)[1:-1]}")
st.subheader(f"Genre(s) : {str(genre)[2:-2]}")

styled_df = df_selection.style.format({
    'startYear': lambda x: f"{x:.0f}"  # Remove commas from years (treated as float/int)
}).format({
    'averageRating': lambda x: f"{x:.2f}"  # Remove commas from years (treated as float/int)
})

st.dataframe(styled_df)