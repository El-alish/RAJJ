import streamlit as st
import pandas as pd

df = pd.read_csv('https://drive.google.com/file/d/1W60klEPbdt3JV7up4L6_B5YCEFrHcFAb/view?usp=drive_link', sep=','"
                 
st.dataframe(df)
