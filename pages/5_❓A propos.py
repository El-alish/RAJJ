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

tab1, tab2, tab3, tab4 = st.tabs(["Accès", "Nos tarifs", "Nos horaires", "Contact"])
with tab1:
    st.write("Comment accéder à notre cinéma ?")
    st.write("Notre adresse :")
    st.write('Au Grand RAJJ')
    st.write('Place de la Mairie')
    st.write('23000 Gueret')
    st.map(df, size=400, color='#0044ff')

with tab2:
    st.subheader("Nos tarifs")
    col0, col1, col2, col3 = st.columns(4)
    with col0:
        container = st.container(border=False)
        container.image("RAJJ-master\Images\Capture d'écran 2024-05-23 160027.png")
    with col1:
        container = st.container(border=False)
        container.image("RAJJ-master\Images\Capture d'écran 2024-05-23 160040.png")
    with col2:
        container = st.container(border=False)
        container.image("RAJJ-master\Images\Capture d'écran 2024-05-23 160050.png")
    with col3:
        container = st.container(border=False)
        container.image("RAJJ-master\Images\Capture d'écran 2024-05-23 160110.png")

with tab3:
        container = st.container(border=False)
        container.image("RAJJ-master\Images\Horaire.png")

with tab4:
    st.subheader("Comment nous contacter ?")
    st.write("Téléphone : 08 35 65 65 65")
    st.write("Mail : augrandrajj@gueret.fr")
    st.write("Nos Réseaux Sociaux :")
    st.write("[Facebook](https://www.facebook.com/)")
    st.write("[Twitter](https://twitter.com/)")
    st.write("[Instagram](https://www.instagram.com/)")
