import pandas as pd
import streamlit as st

def rawDataDefalt(file):
    rawData = pd.read_csv(
        filepath_or_buffer = file,
        #'dataTests/rawData2.csv', 
        encoding='latin-1',
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

if __name__ == "__main__":
    file = 'dataTests/rawData2.csv'
    rawDataDefalt(file)