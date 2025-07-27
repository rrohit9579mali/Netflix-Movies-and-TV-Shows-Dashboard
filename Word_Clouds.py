import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
def word_clouds(df,option):
    st.markdown(f"<h3 style='color: yellow'>{option} </h3>",unsafe_allow_html=True)
