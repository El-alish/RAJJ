import streamlit as st
import pandas as pd
import numpy as np
import translate
from deep_translator import GoogleTranslator

df = pd.DataFrame({
    "LAT": 46.174497199765426, 
    "LON": 1.8694600366983392,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

tab1, tab2, tab3 = st.tabs(["Accès", "Nos tarifs", "Nos horaires"])
with tab1:
    st.write("Comment accéder à notre cinéma ?")
    st.write("Notre adresse :")
    st.write('Au Grand RAJJ')
    st.write('Place de la Mairie')
    st.write('23000 Gueret')
    st.map(df, size=400, color='#0044ff')

with tab2:
    st.subheader("Nos tarifs")
    st.write("Tarif normal : 10€")
    st.write("Tarif réduit (France-Travail ou Handicapé) : 8€")
    st.write("Tarif - de 16 ans : 6€")
    st.write("Tarif enfant : 4€")

with tab3:
    st.subheader("Nos horaires")
    st.write("Lundi au Vendredi : 12h30 - Minuit")
    st.write("Week-end : 10h - Minuit")
