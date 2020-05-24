import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials


def main():
    pass
#connect to the database
#select the data
#rename the columns
#get min (-1) and max(1) or else (0) per company per day
#insert label and the other data in the master record


if __name__ == "__main__":

	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	sql = "SELECT * FROM unlabelled_record "
	name_dict={0:"index", 1:"date_of_day" , 2:"label" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"index2", 20:"CDL2CROWS" , 21:"CDL3BLACKCROWS" , 22:"CDL3INSIDE" , 23:"CDL3LINESTRIKE" , 24:"CDL3OUTSIDE" , 25:"CDL3STARSINSOUTH" , 26:"CDL3WHITESOLDIERS" , 27:"CDLABANDONEDBABY" , 28:"CDLADVANCEBLOCK" , 29:"CDLBELTHOLD" , 30:"CDLBREAKAWAY" , 31:"CDLCLOSINGMARUBOZU" , 32:"CDLCONCEALBABYSWALL" , 33:"CDLCOUNTERATTACK" , 34:"CDLDARKCLOUDCOVER" , 35:"CDLDOJI" , 36:"CDLDOJISTAR" , 37:"CDLDRAGONFLYDOJI" , 38:"CDLENGULFING" , 39:"CDLEVENINGDOJISTAR" , 40:"CDLEVENINGSTAR" , 41:"CDLGAPSIDESIDEWHITE" , 42:"CDLGRAVESTONEDOJI" , 43:"CDLHAMMER" , 44:"CDLHANGINGMAN" , 45:"CDLHARAMI" , 46:"CDLHARAMICROSS" , 47:"CDLHIGHWAVE" , 48:"CDLHIKKAKE" , 49:"CDLHIKKAKEMOD" , 50:"CDLHOMINGPIGEON" , 51:"CDLIDENTICAL3CROWS" , 52:"CDLINNECK" , 53:"CDLINVERTEDHAMMER" , 54:"CDLKICKING" , 55:"CDLKICKINGBYLENGTH" , 56:"CDLLADDERBOTTOM" , 57:"CDLLONGLEGGEDDOJI" , 58:"CDLLONGLINE" , 59:"CDLMARUBOZU" , 60:"CDLMATCHINGLOW" , 61:"CDLMATHOLD" , 62:"CDLMORNINGDOJISTAR" , 63:"CDLMORNINGSTAR" , 64:"CDLONNECK" , 65:"CDLPIERCING" , 66:"CDLRICKSHAWMAN" , 67:"CDLRISEFALL3METHODS" , 68:"CDLSEPARATINGLINES" , 69:"CDLSHOOTINGSTAR" , 70:"CDLSHORTLINE" , 71:"CDLSPINNINGTOP" , 72:"CDLSTALLEDPATTERN" , 73:"CDLSTICKSANDWICH" , 74:"CDLTAKURI" , 75:"CDLTASUKIGAP" , 76:"CDLTHRUSTING" , 77:"CDLTRISTAR" , 78:"CDLUNIQUE3RIVER" , 79:"CDLUPSIDEGAP2CROWS" , 80:"CDLXSIDEGAP3METHODS"}
	df = utils.get_data(mydb, sql, name_dict)
	print(df.head())

	select_min_from_db(mydb,sql_get_min_max,sql_get_id)

	def select_min_from_db(mydb,sql_get_min_max,sql_get_id):
		try:
			mycursor = mydb.cursor()
			mycursor.execute(sql_get_min_max)
			table_rows = mycursor.fetchall()[0][0]
			sql = sql_get_id + str(table_rows)
		except:
			pass
		try:
			mycursor.execute(sql)
			table_rows = mycursor.fetchall()[0][0]
		except:
			pass
		return table_rows