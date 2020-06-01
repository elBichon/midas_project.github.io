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
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	sql = "SELECT * FROM master_record_staging"
	table_rows = utils.execute_query(sql,mydb)
	
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:'ema_12',81:'ema_26',82:'upper_list',83:'lower_list',84:'K_value',85:'D_value', 86:'label'}
	df = utils.get_data(mydb, sql, name_dict)

	df = df[["date_of_day","hour","name","volume","numberOfTrades","var_ema","var_bollinger","var_stoch","rsi_indicator","stoch_indicator","RSI","ema_indicator","bollinger_indicator","CDL2CROWS","CDL3BLACKCROWS","CDL3INSIDE","CDL3LINESTRIKE","CDL3OUTSIDE","CDL3STARSINSOUTH","CDL3WHITESOLDIERS","CDLABANDONEDBABY","CDLADVANCEBLOCK","CDLBELTHOLD","CDLBREAKAWAY","CDLCLOSINGMARUBOZU","CDLCONCEALBABYSWALL","CDLCOUNTERATTACK","CDLDARKCLOUDCOVER","CDLDOJI","CDLDOJISTAR","CDLDRAGONFLYDOJI","CDLENGULFING","CDLEVENINGDOJISTAR","CDLEVENINGSTAR","CDLGAPSIDESIDEWHITE","CDLGRAVESTONEDOJI","CDLHAMMER","CDLHANGINGMAN","CDLHARAMI","CDLHARAMICROSS","CDLHIGHWAVE","CDLHIKKAKE","CDLHIKKAKEMOD","CDLHOMINGPIGEON","CDLIDENTICAL3CROWS","CDLINNECK","CDLINVERTEDHAMMER","CDLKICKING","CDLKICKINGBYLENGTH","CDLLADDERBOTTOM","CDLLONGLEGGEDDOJI","CDLLONGLINE","CDLMARUBOZU","CDLMATCHINGLOW","CDLMATHOLD","CDLMORNINGDOJISTAR","CDLMORNINGSTAR","CDLONNECK","CDLPIERCING","CDLRICKSHAWMAN","CDLRISEFALL3METHODS","CDLSEPARATINGLINES","CDLSHOOTINGSTAR","CDLSHORTLINE","CDLSPINNINGTOP","CDLSTALLEDPATTERN","CDLSTICKSANDWICH","CDLTAKURI","CDLTASUKIGAP","CDLTHRUSTING","CDLTRISTAR","CDLUNIQUE3RIVER","CDLUPSIDEGAP2CROWS","CDLXSIDEGAP3METHODS","fft_20_close","fft_100_close","fft_100_open","fft_100_low","fft_100_high","ema_12","ema_26","upper_list","lower_list","K_value","D_value","label"]]
	sql = "INSERT INTO master_record (date_of_day,hour,name,volume,numberOfTrades,var_ema,var_bollinger,var_stoch,rsi_indicator,stoch_indicator,RSI,ema_indicator,bollinger_indicator,CDL2CROWS,CDL3BLACKCROWS,CDL3INSIDE,CDL3LINESTRIKE,CDL3OUTSIDE,CDL3STARSINSOUTH,CDL3WHITESOLDIERS,CDLABANDONEDBABY,CDLADVANCEBLOCK,CDLBELTHOLD,CDLBREAKAWAY,CDLCLOSINGMARUBOZU,CDLCONCEALBABYSWALL,CDLCOUNTERATTACK,CDLDARKCLOUDCOVER,CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLENGULFING,CDLEVENINGDOJISTAR,CDLEVENINGSTAR,CDLGAPSIDESIDEWHITE,CDLGRAVESTONEDOJI,CDLHAMMER,CDLHANGINGMAN,CDLHARAMI,CDLHARAMICROSS,CDLHIGHWAVE,CDLHIKKAKE,CDLHIKKAKEMOD,CDLHOMINGPIGEON,CDLIDENTICAL3CROWS,CDLINNECK,CDLINVERTEDHAMMER,CDLKICKING,CDLKICKINGBYLENGTH,CDLLADDERBOTTOM,CDLLONGLEGGEDDOJI,CDLLONGLINE,CDLMARUBOZU,CDLMATCHINGLOW,CDLMATHOLD,CDLMORNINGDOJISTAR,CDLMORNINGSTAR,CDLONNECK,CDLPIERCING,CDLRICKSHAWMAN,CDLRISEFALL3METHODS,CDLSEPARATINGLINES,CDLSHOOTINGSTAR,CDLSHORTLINE,CDLSPINNINGTOP,CDLSTALLEDPATTERN,CDLSTICKSANDWICH,CDLTAKURI,CDLTASUKIGAP,CDLTHRUSTING,CDLTRISTAR,CDLUNIQUE3RIVER,CDLUPSIDEGAP2CROWS,CDLXSIDEGAP3METHODS,fft_20_close,fft_100_close,fft_100_open,fft_100_low,fft_100_high,ema_12,ema_26,upper_list,lower_list,K_value,D_value,label) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = [tuple(x) for x in df.values.tolist()]
	mycursor = mydb.cursor()
	mycursor.executemany(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "was inserted.") 

	print(df.head())
	staging_table = ['raw_stock','fourier_processed_stock','processed_stock','candlestick_indicator','unlabelled_record','master_record_staging']
	for table in staging_table:
		print('deleting from table: '+table)
		sql = "truncate table " +table
		utils.delete_query(sql,mydb)

