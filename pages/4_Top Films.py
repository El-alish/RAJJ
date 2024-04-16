import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)


select_office = sorted(df['primaryTitle'].unique())
select_office_dropdown = st.sidebar.multiselect('Select one or multiple title to display data:', select_office)
select_year_range = reversed(sorted(df['startYear'].unique()))
yearmax = df['startYear'].max()
yearmin = df['startYear'].min()
select_year_slider = st.sidebar.select_slider('Use slider to display year range:', options=select_year_range, value=(yearmax, yearmin))
startyear, endyear = list(select_year_slider)[0], list(select_year_slider)[1]
    
selected_office_year = df[(df.Office.isin(select_office_dropdown)) & ((df.Year <= startyear) & (df.Year >= endyear))]
    
st.map(selected_office_year)
st.dataframe(selected_office_year.reset_index(drop=True))
