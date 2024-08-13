import pandas as pd
import numpy as np


df = pd.read_excel('purchase_data_1.xlsx')
matrixA = []
dataframe1 = pd.read_excel('purchase_data_1.xlsx')
l = dataframe1.values
dataframe1['R/P'] = 'RICH'
dataframe1.loc[dataframe1['Payment (Rs)'] < 200,'R/P' ] = 'POOR'
print(dataframe1)
'''
print(l[0][4])
for i in range (0, len(l)):
    if l[i][4] > 200:
        
    else:
        dataframe1['R/P'] = 'POOR'

print(dataframe1)
'''

