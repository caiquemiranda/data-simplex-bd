import streamlit as st
import pandas as pd

def uploadDados():
    return st.header('Faça o Upload dos dados aqui:')

def tratamentoUpload():
    st.subheader("Upload de arquivos")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV")
    if uploaded_file is not None:
        rawData = pd.read_csv(uploaded_file)
        return st.write(rawData)
