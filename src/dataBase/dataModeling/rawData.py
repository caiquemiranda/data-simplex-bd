import pandas as pd
import streamlit as st


def rawDataDefalt():
    rawData = pd.read_csv(
        'dataTests/rawData2.csv', 
        encoding='latin-1',
        #sep=',',
        header=None,
        )

    rawData = pd.DataFrame(rawData)
    rawData.columns = [f"Column{i+1}" for i in range(rawData.shape[1])]
    rawData = rawData[['Column1', 'Column2', 'Column3', 'Column4']]
    rawData.rename(columns={
        'Column1' : 'panel_adress', 
        'Column2' : 'type_device',
        'Column3' : 'action',
        'Column4' : 'description'
    }, inplace=True)

    rawData.set_index('panel_adress', inplace=True)

    return st.dataframe(rawData)