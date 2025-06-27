import streamlit as st
import pandas as pd

def uploadDados():
    return st.header('Faça o Upload dos dados aqui:')

def tratamentoUpload():
    file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    #df = pd.read_csv(file)
    return st.dataframe(file)
