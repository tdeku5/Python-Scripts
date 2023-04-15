# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:14:00 2023

@author: tdeku

This script queries equity sector ETF data from the SQL database created in yfinance and creates a 
return correlation heatmap.
"""
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
con = sqlite3.connect("financial_data2.db")

stocks = ['SPY', 'XLI', 'XLE', 'XLK', 'XLU', 'XLF', 'XLY', 'XLP', 'XLB', 'XLC', 'XHB']

dataframes = {}

# Construct dataframe
# 2018-07-01 is most recent date that data is available for ALL ETFs - XLC originated mid 2018
for symbol in stocks:
    dataframes[symbol] = pd.read_sql_query(f"SELECT close from financial_data2 where symbol='{symbol}' and date>='2018-07-01'", con)

df_stocks = pd.concat(dataframes, axis=1)
df_stocks.columns = stocks

for symbol in stocks:
    df_stocks[symbol] = np.log(df_stocks[symbol]).diff()
    
df_stocks = df_stocks.drop([0])

# Create heatmap
plt.figure(figsize=(16,6))
mask = np.triu(np.ones_like(df_stocks.corr(), dtype=np.bool))
sector_map = sns.heatmap(df_stocks.corr(), mask=mask, vmin=-0.25, vmax=1, annot=True, cmap='BrBG')
sector_map.set_title("Equity Sectors Correlation Heatmap")
