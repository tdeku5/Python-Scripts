# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:07:38 2023

@author: tdeku

Queries data from SQL database created in yfinance_scraper and creates return correlation heatmap.
"""

import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
con = sqlite3.connect("financial_data3.db")

stocks = ['SPY', 'XLI', 'XLE', 'XLK', 'XLU', 'XLF', 'XLY', 'XLP', 'XLB', 'XLC', 'XHB']
commodities = ['DBC', 'USO', 'UGA', 'UNG', 'CORN', 'SOYB', 'CANE', 'WEAT', 'CPER', 'SLV', 'GLD', 'PAL']
fixed_income = ['TLT', 'IEF', 'IEI', 'SHY', 'MBB', 'VCIT', 'USHY']
currencies = ['UUP', 'FXE', 'FXB', 'FXY', 'FXA', 'BIL']

all_assets = stocks + commodities + fixed_income + currencies

dataframes = {}

for symbol in all_assets:
    dataframes[symbol] = pd.read_sql_query(f"SELECT close from financial_data3 where symbol='{symbol}' and date>='2018-07-01'", con)

df_assets = pd.concat(dataframes, axis=1)
df_assets.columns = all_assets

for symbol in all_assets:
    df_assets[symbol] = np.log(df_assets[symbol]).diff()
    
df_assets = df_assets.drop([0])
df_assets.drop('PAL', axis=1, inplace=True)

plt.figure(figsize=(30,12))
mask = np.triu(np.ones_like(df_assets.corr(), dtype=np.bool))
sector_map = sns.heatmap(df_assets.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
sector_map.set_title("Asset Correlation Heatmap")