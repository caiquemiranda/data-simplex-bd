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
from upload_dados.upload import upload_dados
from viz.viz import viz_data
from history.history import history_data
from data_base.data_modeling.raw_data import raw_data_defalt
from upload_dados.upload import tratamento_upload


with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Upload dados","Viz BD","Historico"],
    icons = ["house","gear","activity"],
    menu_icon = "cast",
    default_index = 0,
)

if selected == "Upload dados":
    upload_dados()
    tratamento_upload()

if selected == "Viz BD":
    viz_data()
    file = 'src/dataBase/dataModeling/dataTests/rawData2.csv'
    raw_data_defalt(file)

if selected == "Historico":
    history_data()