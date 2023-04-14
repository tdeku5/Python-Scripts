# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:48:02 2023

@author: tdeku

This is inspired and much of the code is taken from PyQuant News - a newsletter/learniing platform for quant finance.
"""

from sys import argv

import pandas as pd
import yfinance as yf
import sqlite3

conn = sqlite3.connect('financial_data2.db')
c = conn.cursor()

today1 = pd.Timestamp.today()

def get_data(symbol, start, end):
    data = yf.download(symbol, start=start, end=end)
    data.reset_index(inplace=True)
    data.rename(columns={
        "Date": "date",
        "Open": "open",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    }, inplace=True)
    data['symbol'] = symbol
    return data

def save_data_range(symbol, start, end, con):
    data = get_data(symbol, start, end)
    data.to_sql(
        "financial_data2", 
        con, 
        if_exists="append", 
        index=False
    )  

def save_last_trading_session(symbol, con):
    today = pd.Timestamp.today()
    ticker = yf.Ticker(symbol)
    hist_data = ticker.history(period='max')  # Get historical data
    last_trading_day = hist_data.index[-1]  # Get the last available trading day
    data = get_data(symbol, last_trading_day, last_trading_day)
    data.to_sql(
        "financial_data2",
        con,
        if_exists="append",
        index=False
    )

stocks = ['SPY', 'XLI', 'XLE', 'XLK', 'XLU', 'XLF', 'XLY', 'XLP', 'XLB', 'XLC', 'XHB']
commodities = ['DBC', 'USO', 'UGA', 'UNG', 'CORN', 'SOYB', 'CANE', 'WEAT', 'CPER', 'SLV', 'GLD', 'PAL']
fixed_income = ['TLT', 'IEF', 'IEI', 'SHY', 'MBB', 'VCIT', 'USHY']
currencies = ['UUP', 'FXE', 'FXB', 'FXY', 'FXA', 'BIL']


x = list(range(0,11))
for i in x:
    get_data(stocks[i], start='2000-01-01', end=today1)
    save_data_range(stocks[i], start='2000-01-01', end=today1, con=conn)
    save_last_trading_session(stocks[i], con=conn)
 
 
y = list(range(0,12))
for i in y:
    get_data(commodities[i], start='2000-01-01', end=today1)
    save_data_range(commodities[i], start='2000-01-01', end=today1, con=conn)
    save_last_trading_session(commodities[i], con=conn)

    
z = list(range(0,7))
for i in z:
    get_data(fixed_income[i], start='2000-01-01', end=today1)
    save_data_range(fixed_income[i], start='2000-01-01', end=today1, con=conn)
    save_last_trading_session(fixed_income[i], con=conn)
    
w = list(range(0,6))
for i in w:
    get_data(currencies[i], start='2000-01-01', end=today1)
    save_data_range(currencies[i], start='2000-01-01', end=today1, con=conn)
    save_last_trading_session(currencies[i], con=conn)
    
