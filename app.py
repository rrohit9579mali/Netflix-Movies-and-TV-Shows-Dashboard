# main_app.py

import streamlit as st
import pandas as pd
import overview_analysis as oa
import Genre_and_Filtered_Search as gfs
import Word_Clouds as wc
import director_cast_analysis as dca
import Search_Recommendation as sr

# Load dataset
df = pd.read_csv('Data_Set/cleand_data.csv')

# Title with HTML styling
st.markdown("<h1 style='color: green;'>Netflix Movies and TV Shows</h1>", unsafe_allow_html=True)

# Sidebar section
st.sidebar.markdown("<h2 style='color: red;'>Navigation</h2>", unsafe_allow_html=True)

# Dropdown for selecting view
option = st.sidebar.selectbox(
    'Select View',
    ['Overview Dashboard', 'Genre & Filtered Search', 'Director / Cast Analysis', 'Search + Recommendation', 'Word Clouds']
)

# Button
btn = st.sidebar.button('Submit')

# Conditional rendering
if btn:
    if option == 'Overview Dashboard':
        oa.show_movie_vs_tv_chart(df, option)

    elif option == 'Genre & Filtered Search':
        gfs.Genre__Filtered_Search(df, option)

    elif option == 'Search + Recommendation':
        sr.search_recomadation(df, option)

    elif option == 'Word Clouds':
        wc.word_clouds(df, option)

    elif option == 'Director / Cast Analysis':
        dca.director_cast_analysis(df, option)
