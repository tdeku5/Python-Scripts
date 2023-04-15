# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:17:29 2023

@author: tdeku
"""

import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
con = sqlite3.connect("financial_data3.db")

fixed_income = ['TLT', 'IEF', 'IEI', 'SHY', 'MBB', 'VCIT', 'USHY']
currencies = ['UUP', 'FXE', 'FXB', 'FXY', 'FXA', 'BIL']

all_assets = fixed_income + currencies

dataframes = {}

for symbol in all_assets:
    dataframes[symbol] = pd.read_sql_query(f"SELECT close from financial_data3 where symbol='{symbol}' and date>='2018-07-01'", con)

df_assets = pd.concat(dataframes, axis=1)
df_assets.columns = all_assets

for symbol in all_assets:
    df_assets[symbol] = np.log(df_assets[symbol]).diff()
    
df_assets = df_assets.drop([0])
#df_assets.drop('PAL', axis=1, inplace=True)

plt.figure(figsize=(20,10))
mask = np.triu(np.ones_like(df_assets.corr(), dtype=np.bool))
sector_map = sns.heatmap(df_assets.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
sector_map.set_title("Bonds & Currencies Correlation Heatmap")