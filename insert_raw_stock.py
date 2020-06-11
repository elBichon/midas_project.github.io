#! /usr/bin/env python3
# coding: utf-8
from datetime import datetime
from iexfinance.stocks import get_historical_intraday
from iexfinance.stocks import Stock
import plotly.graph_objects as go
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import itertools
import os
import utils
import time
from mpl_finance import candlestick_ohlc
import credentials 
import argparse
import mysql.connector
import db_credentials
plt.style.use('ggplot')



def main():
    pass

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='modelisation running')
	parser.add_argument('symbol', type=str, help='')
	args = parser.parse_args()
	trade_symbol  = args.symbol
	if len(trade_symbol) != 0 and isinstance(trade_symbol, str) == True:
		try:
			df = get_historical_intraday(trade_symbol.upper(), output_format='pandas',token= credentials.token)
			df = df.fillna(method='ffill')
		except:
			pass

		MYDB = mysql.connector.connect(
		  host=db_credentials.host,
		  user=db_credentials.user,
		  passwd=db_credentials.passwd,
		  database=db_credentials.database
		) 

		name = [str(trade_symbol) for i in range(len(df.date.values.tolist()))]
		df['name'] = name
		df = df[['date', 'label', 'name', 'high', 'low', 'open', 'close', 'volume', 'numberOfTrades']]
		VAL = [tuple(x) for x in df.values]
		SQL = "INSERT INTO raw_stock (date, hour, name, high, low, open, close, volume, numberOfTrades) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		utils.insert_data(MYDB,SQL,VAL)

	else:
		pass

