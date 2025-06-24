import pandas as pd


rawData = pd.read_csv()

"""
tratamento dos dados(patern)
column1 = panel_address
column2 = type_device
column3 = action
column4 = description

"""
rawData = pd.DataFrame(rawData)
rawData = rawData[['column1', 'column2', 'column3', 'column4']]

rawData.rename(columns={
    'column1' : 'panel_adress', 
    'column2' : 'type_device',
    'column3' : 'action',
    'column4' : 'description'
})