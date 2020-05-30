import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials


def main():
    pass

if __name__ == "__main__":

	mydb = mysql.connector.connect(
	  host = db_credentials.host,
	  user = db_credentials.user,
	  passwd = db_credentials.passwd,
	  database = db_credentials.database
	) 

	sql = "SELECT * FROM raw_stock"
	name_dict = {0:"index", 1:"date_of_day", 2: "hour", 3: "name", 4: "high", 5: "low", 6: "open", 7: "close", 8: "volume", 9: "numberOfTrades"}
	df = utils.get_data(mydb, sql, name_dict)

	fft_100_high = []
	fft_100_low = []
	fft_100_close = []
	fft_100_open = []
	fft_20_high = []
	fft_20_low = []
	fft_20_close = []
	fft_20_open = []

	index = df.index.values.tolist()
	df_close = df['close'].values.tolist()
	df_fft_close = utils.fourier_transform(df,'close',fft_20_close,fft_100_close)
	df_fft_low = utils.fourier_transform(df,'low',fft_20_low,fft_100_low)
	df_fft_open = utils.fourier_transform(df,'open',fft_20_open,fft_100_open)
	df_fft_open = utils.fourier_transform(df,'high',fft_20_high,fft_100_high)

	fft_20_close = list(itertools.chain.from_iterable(fft_20_close))
	fft_20_high = list(itertools.chain.from_iterable(fft_20_high))
	fft_20_low = list(itertools.chain.from_iterable(fft_20_low))
	fft_20_open = list(itertools.chain.from_iterable(fft_20_open))
	fft_100_close = list(itertools.chain.from_iterable(fft_100_close))
	fft_100_high = list(itertools.chain.from_iterable(fft_100_high))
	fft_100_low = list(itertools.chain.from_iterable(fft_100_low))
	fft_100_open = list(itertools.chain.from_iterable(fft_100_open))


	df['fft_20_close'] = fft_20_close
	df['fft_20_high'] = fft_20_high
	df['fft_20_low'] = fft_20_low
	df['fft_20_open'] = fft_20_open
	df['fft_100_close'] = fft_100_close
	df['fft_100_high'] = fft_100_high
	df['fft_100_low'] = fft_100_low
	df['fft_100_open'] = fft_100_open

	
	df = df[['date_of_day', 'hour', 'numberOfTrades', 'name', 'volume', 'fft_20_close', 'fft_20_open', 'fft_20_low', 'fft_20_high', 'fft_100_close', 'fft_100_open', 'fft_100_low', 'fft_100_high']]
	val = [tuple(x) for x in df.values]
	sql = "INSERT INTO fourier_processed_stock (date_of_day, hour, numberOfTrades, name, volume, fft_20_close, fft_20_open, fft_20_low, fft_20_high, fft_100_close, fft_100_open, fft_100_low, fft_100_high) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	mycursor = mydb.cursor()
	mycursor.executemany(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "was inserted.") 
