import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from streamlit_option_menu import option_menu

data_source = "data/rawData2.csv"

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Upload dados","Viz BD","Historico"],
    icons = ["house","gear","activity"],
    menu_icon = "cast",
    default_index = 0,
)

if selected == "Upload dados":
    st.subheader("Upload de arquivos")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV")
    if uploaded_file is not None:
        rawData = pd.read_csv(uploaded_file)
        st.write(rawData)

if selected == "Viz BD":
    st.header('Viz BD')

    rawData = pd.read_csv(
    filepath_or_buffer = data_source,
    encoding='latin-1',
    header=None,)
    st.write(rawData)
    
if selected == "Historico":
    st.header('Historico')
