# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:14:00 2023

@author: tdeku
"""
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# connect to the database
con = sqlite3.connect("financial_data2.db")

# Create pandas dataframes with the data
# Stocks
df_SPY = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='SPY' and date>='2018-07-01'", con)
df_XLI = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLI' and date>='2018-07-01'", con)
df_XLE = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLE' and date>='2018-07-01'", con)
df_XLK = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLK' and date>='2018-07-01'", con)
df_XLU = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLU' and date>='2018-07-01'", con)
df_XLF = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLF' and date>='2018-07-01'", con)
df_XLY = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLY' and date>='2018-07-01'", con)
df_XLP = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLP' and date>='2018-07-01'", con)
df_XLB = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLB' and date>='2018-07-01'", con)
df_XLC = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XLC' and date>='2018-07-01'", con)
df_XHB = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='XHB' and date>='2018-07-01'", con)

# Commodities
df_DBC = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='DBC' and date>='2018-07-01'", con)
df_USO = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='USO' and date>='2018-07-01'", con)
df_UGA = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='UGA' and date>='2018-07-01'", con)
df_UNG = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='UNG' and date>='2018-07-01'", con)
df_CORN = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='CORN' and date>='2018-07-01'", con)
df_SOYB = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='SOYB' and date>='2018-07-01'", con)
df_CANE = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='CANE' and date>='2018-07-01'", con)
df_WEAT = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='WEAT' and date>='2018-07-01'", con)
df_CPER = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='CPER' and date>='2018-07-01'", con)
df_SLV = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='SLV' and date>='2018-07-01'", con)
df_GLD = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='GLD' and date>='2018-07-01'", con)
df_PAL = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='PAL' and date>='2018-07-01'", con)

# Fixed Income
df_TLT = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='TLT' and date>='2018-07-01'", con)
df_IEF = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='IEF' and date>='2018-07-01'", con)
df_IEI = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='IEI' and date>='2018-07-01'", con)
df_SHY = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='SHY' and date>='2018-07-01'", con)
df_MBB = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='MBB' and date>='2018-07-01'", con)
df_VCIT = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='VCIT' and date>='2018-07-01'", con)
df_USHY = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='USHY' and date>='2018-07-01'", con)

# Currences
df_UUP = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='UUP' and date>='2018-07-01'", con)
df_FXE = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='FXE' and date>='2018-07-01'", con)
df_FXB = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='FXB' and date>='2018-07-01'", con)
df_FXY = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='FXY' and date>='2018-07-01'", con)
df_FXA = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='FXA' and date>='2018-07-01'", con)
df_BIL = pd.read_sql_query("SELECT date, close from financial_data2 where symbol='BIL' and date>='2018-07-01'", con)


# Get returns
spy_returns = np.log(df_SPY['close']).diff()
spy_returns = spy_returns.drop([0])

xli_returns = np.log(df_XLI['close']).diff()
xli_returns = xli_returns.drop([0])

xle_returns = np.log(df_XLE['close']).diff()
xle_returns = xle_returns.drop([0])

xlk_returns = np.log(df_XLK['close']).diff()
xlk_returns = xlk_returns.drop([0])

xlu_returns = np.log(df_XLU['close']).diff()
xlu_returns = xlu_returns.drop([0])

xlf_returns = np.log(df_XLF['close']).diff()
xlf_returns = xlf_returns.drop([0])

xly_returns = np.log(df_XLY['close']).diff()
xly_returns = xly_returns.drop([0])

xlp_returns = np.log(df_XLP['close']).diff()
xlp_returns = xlp_returns.drop([0])

xlb_returns = np.log(df_XLB['close']).diff()
xlb_returns = xlb_returns.drop([0])

xlc_returns = np.log(df_XLC['close']).diff()
xlc_returns = xlc_returns.drop([0])

xhb_returns = np.log(df_XHB['close']).diff()
xhb_returns = xhb_returns.drop([0])

stock_list = [spy_returns, xli_returns, xle_returns, xlk_returns, xlu_returns, xlf_returns, xly_returns, xlp_returns, xlb_returns, xlc_returns, xhb_returns]

df_sectors = pd.concat(stock_list, axis=1)
df_sectors.columns = ['SPY', 'XLI', 'XLE', 'XLK', 'XLU', 'XLF', 'XLY', 'XLP', 'XLB', 'XLC', 'XHB']


plt.figure(figsize=(16,6))
mask = np.triu(np.ones_like(df_sectors.corr(), dtype=np.bool))
sector_map = sns.heatmap(df_sectors.corr(), mask=mask, vmin=-0.25, vmax=1, annot=True, cmap='BrBG')
sector_map.set_title("Equity Sectors Correlation Heatmap")





