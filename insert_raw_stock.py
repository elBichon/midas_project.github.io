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
	df = get_historical_intraday(trade_symbol, output_format='pandas',token= credentials.token)
	df = df.fillna(method='ffill')
	print(df.columns)
	print(df.tail())

	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	date_list = df.date.values.tolist()
	label_list = df.label.values.tolist()
	high_list = df.high.values.tolist()
	low_list = df.low.values.tolist()
	open_list = df.open.values.tolist()
	close_list = df.close.values.tolist()
	volume_list = df.volume.values.tolist()
	numberOfTrades_list = df.numberOfTrades.values.tolist()

	print('inserting data for: ', trade_symbol)

	sql = "INSERT INTO raw_stock (date, label, name, high, low, open, close, volume, numberOfTrades) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (date_list[i], label_list[i], trade_symbol,  high_list[i], low_list[i], open_list[i], close_list[i], volume_list[i], numberOfTrades_list[i])
	utils.insert_multiple_into_db(sql,val,date_list)