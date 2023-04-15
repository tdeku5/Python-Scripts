# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:22:03 2023

@author: tdeku
"""
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
con = sqlite3.connect("financial_data3.db")

commodities = ['DBC', 'USO', 'UGA', 'UNG', 'CORN', 'SOYB', 'CANE', 'WEAT', 'CPER', 'SLV', 'GLD']

dataframes = {}

for symbol in commodities:
    dataframes[symbol] = pd.read_sql_query(f"SELECT close from financial_data3 where symbol='{symbol}' and date>='2018-07-01'", con)

df_commodities = pd.concat(dataframes, axis=1)
df_commodities.columns = commodities

for symbol in commodities:
    df_commodities[symbol] = np.log(df_commodities[symbol]).diff()
    
df_commodities = df_commodities.drop([0])

plt.figure(figsize=(16,6))
mask = np.triu(np.ones_like(df_commodities.corr(), dtype=np.bool))
sector_map = sns.heatmap(df_commodities.corr(), mask=mask, vmin=-0.25, vmax=1, annot=True, cmap='BrBG')
sector_map.set_title("Commodities Correlation Heatmap")
