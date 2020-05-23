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

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM raw_stock")
	table_rows = mycursor.fetchall()
	print(table_rows)
	df = pd.DataFrame(table_rows)
	print(df.head())
	df = df.rename(columns={0:"index", 1:"date_of_day", 2: "hour_min", 3: "name", 4: "high", 5: "low", 6: "open", 7: "close", 8: "volume", 9: "numberOfTrades"})

	print(df.head())
	fft_100_high = []
	fft_100_low = []
	fft_100_close = []
	fft_100_open = []
	fft_20_high = []
	fft_20_low = []
	fft_20_close = []
	fft_20_open = []

	df_close = df['close'].values.tolist()
	df_fft_close = utils.fourier_transform(df,'close',fft_20_close,fft_100_close)
	df_fft_low = utils.fourier_transform(df,'low',fft_20_low,fft_100_low)
	df_fft_open = utils.fourier_transform(df,'open',fft_20_open,fft_100_open)
	df_fft_open = utils.fourier_transform(df,'high',fft_20_high,fft_100_high)
	volume = df['volume'].values.tolist()

	fft_20_close = list(itertools.chain.from_iterable(fft_20_close))
	fft_20_high = list(itertools.chain.from_iterable(fft_20_high))
	fft_20_low = list(itertools.chain.from_iterable(fft_20_low))
	fft_20_open = list(itertools.chain.from_iterable(fft_20_open))
	fft_100_close = list(itertools.chain.from_iterable(fft_100_close))
	fft_100_high = list(itertools.chain.from_iterable(fft_100_high))
	fft_100_low = list(itertools.chain.from_iterable(fft_100_low))
	fft_100_open = list(itertools.chain.from_iterable(fft_100_open))
	date_of_day = df.date_of_day.values.tolist() 
	hour_min = df.hour_min.values.tolist()
	name = df.name.values.tolist()
	volume = df.volume.values.tolist()
	numberOfTrades = df.numberOfTrades.values.tolist()

	sql = "INSERT INTO fourier_processed_stock (date_of_day, label, numberOfTrades, name, volume, fft_20_close, fft_20_open, fft_20_low, fft_20_high, fft_100_close, fft_100_open, fft_100_low, fft_100_high) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(date_of_day):
		try:
			mycursor = mydb.cursor()
			val = (str(date_of_day[i]), str(hour_min[i]), numberOfTrades[i], str(name[i]), volume[i], fft_20_close[i], fft_20_open[i], fft_20_low[i], fft_20_high[i], fft_100_close[i], fft_100_open[i], fft_100_low[i], fft_100_high[i])
			mycursor.execute(sql, val)
			print(mycursor.rowcount, "record inserted.")
		except:
			pass
		i += 1
	mydb.commit()