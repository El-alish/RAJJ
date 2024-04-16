import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI

st.set_page_config(
    page_title="RAJJ - Cinema",
    page_icon="⭐",
)
       
st.title("Bienvenue au cinéma RAJJ - Élu meilleur cinéma de la Creuse")

st.image('https://t4.ftcdn.net/jpg/04/46/93/93/360_F_446939375_83iP0UYTg5F9vHl6icZwgrEBHXeXMVaU.jpg', caption='Vous ne savez pas quoi regarder ?')



st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["open_ai_key"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
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

st.write("Merci d'utiliser notre menu de gauche pour accéder aux diverses pages de notre site.")
st.sidebar.success("Faites votre choix pour naviguer sur le site. ☝️ ")
