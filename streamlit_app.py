import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI # type: ignore

st.set_page_config(
    page_title="Au Grand RAJJ - Cinema",
    page_icon="⭐",
    layout = "wide"
)
st.title('Au Grand RAJJ - Cinéma au coeur de la Creuse')

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

st.subheader("Bienvenue ! Merci d'utiliser les onglets de notre menu de gauche pour naviguer.")       
tab1, tab2 = st.tabs(["Accueil", "L'équipe derrière le projet"])
with tab1:
    #st.image('https://www.jolie-bobine.fr/wp-content/uploads/2022/03/Animated-Films-Letterboxd-Featured.jpeg')
    st.image('https://www.purevpn.com/wp-content/uploads/2021/09/Binge-watch-movies-banner.jpg')
    st.write('')


with tab2:
    st.title("Projet Recommandations De Films")
    st.write("Projet réalisé dans le cadre de la formation BootCamp Data Analyst, au sein de l'école de formation Wild Code School, en full remote.")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("[Alain Recuze](https://www.linkedin.com/in/arecuze/)")
        st.image("RAJJ-master\Images\Alain.png")
        
    with col2:
        st.subheader("[Joseph Gouttin](https://www.linkedin.com/in/josephgouttin/)")
        st.image("RAJJ-master\Images\Joseph.png")
    
    with col3:
        st.subheader("[Julian Rudeau](https://www.linkedin.com/in/julian-rudeau-7163a8a9/)")
        st.image("RAJJ-master\Images\Julian.png")
    
    with col4:
        st.subheader("[Roberto Kwadjanie](https://www.linkedin.com/in/roberto-kwadjanie-8b6719127/)")
        st.image("RAJJ-master\Images\Roberto.png")
        st.write("[Source création d'Avatar](https://stan-leigh-avatar-maker-app-avatar-app-4f6sov.streamlit.app/)")


with st.sidebar:
    st.image('RAJJ-master\Images\chatbot.png')
    #st.sidebar.success("Cliquez sur les onglets pour naviguer☝️ ")
    st.write("Notre assistant GPT est là pour vous aider dans vos recherches. Posez vos questions à notre ChatGPT maison.")
    st.write("Exemple : Quels sont les meilleurs films Français? 👇")
    
    # Set OpenAI API key from Streamlit secrets
    client = OpenAI(api_key=st.secrets["open_ai_key"])
    
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Votre recherche ici"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
