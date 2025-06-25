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
    #orientation = "horizontal",
)

if selected == "Upload dados":
    uploadDados()
    rawDataDefalt()

if selected == "Viz BD":
    vizData()

if selected == "Historico":
    historyData()