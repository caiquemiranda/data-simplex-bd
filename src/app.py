import streamlit as st
#import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
#import snowflake.connector
#import streamlit_option_menu
from streamlit_option_menu import option_menu

#internals
from uploadDados.upload import uploadDados
from viz.viz import vizData
from history.history import historyData
from dataBase.dataModeling.rawData import rawDataDefalt

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Upload dados","Viz BD","Historico"],
    icons = ["house","gear","activity"],
    menu_icon = "cast",
    default_index = 0,
)

def tratamento():
    file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    pd.DataFrame(file)

    return st.dataframe(file)

if selected == "Upload dados":
    uploadDados()
    tratamento()

if selected == "Viz BD":
    vizData()
    file = 'src/dataBase/dataModeling/dataTests/rawData2.csv'
    rawDataDefalt(file)

if selected == "Historico":
    historyData()