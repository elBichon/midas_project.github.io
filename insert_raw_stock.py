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


	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	date_list = df.date.values.tolist()
	hour = df.label.values.tolist()
	high_list = df.high.values.tolist()
	low_list = df.low.values.tolist()
	open_list = df.open.values.tolist()
	close_list = df.close.values.tolist()
	volume_list = df.volume.values.tolist()
	numberOfTrades_list = df.numberOfTrades.values.tolist()

	print('inserting data for: ', trade_symbol)
	sql = "INSERT INTO raw_stock (date, hour, name, high, low, open, close, volume, numberOfTrades) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(date_list):
		print(str(i)+'/'+str(len(date_list)))
		val = (date_list[i], hour[i], trade_symbol,  high_list[i], low_list[i], open_list[i], close_list[i], volume_list[i], numberOfTrades_list[i])
		utils.insert_multiple_into_db(mydb, sql,val)
		i += 1 