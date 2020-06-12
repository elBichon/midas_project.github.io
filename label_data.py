#! /usr/bin/env python3
# coding: utf-8
import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials

def main():
    pass

if __name__ == "__main__":

	MYDB = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	SQL = "SELECT id, name, fft_100_close FROM unlabelled_record a WHERE fft_100_close = (SELECT MIN(fft_100_close) FROM unlabelled_record b WHERE b.name = a.name)"
	table_rows = utils.execute_query(MYDB,SQL)
	min_index_list = []
	min_index_list = utils.exctract_label(table_rows,min_index_list)

	SQL = "SELECT id, name, fft_100_close FROM unlabelled_record a WHERE fft_100_close = (SELECT MAX(fft_100_close) FROM unlabelled_record b WHERE b.name = a.name)"
	table_rows = utils.execute_query(MYDB,SQL)
	max_index_list = []
	max_index_list = utils.exctract_label(table_rows,max_index_list)

	SQL = "SELECT * FROM unlabelled_record"
	NAME_DICT={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"CDL2CROWS", 15:"CDL3BLACKCROWS", 16:"CDL3INSIDE" , 17:"CDL3LINESTRIKE" , 18:"CDL3OUTSIDE" , 19:"CDL3STARSINSOUTH" , 20:"CDL3WHITESOLDIERS" , 21:"CDLABANDONEDBABY" , 22:"CDLADVANCEBLOCK" , 23:"CDLBELTHOLD" , 24:"CDLBREAKAWAY" , 25:"CDLCLOSINGMARUBOZU" , 26:"CDLCONCEALBABYSWALL" , 27:"CDLCOUNTERATTACK" , 28:"CDLDARKCLOUDCOVER" , 29:"CDLDOJI" , 30:"CDLDOJISTAR" , 31:"CDLDRAGONFLYDOJI" , 32:"CDLENGULFING" , 33:"CDLEVENINGDOJISTAR" , 34:"CDLEVENINGSTAR" , 35:"CDLGAPSIDESIDEWHITE" , 36:"CDLGRAVESTONEDOJI" , 37:"CDLHAMMER" , 38:"CDLHANGINGMAN" , 39:"CDLHARAMI" , 40:"CDLHARAMICROSS" , 41:"CDLHIGHWAVE" , 42:"CDLHIKKAKE" , 43:"CDLHIKKAKEMOD" , 44:"CDLHOMINGPIGEON" , 45:"CDLIDENTICAL3CROWS" , 46:"CDLINNECK" , 47:"CDLINVERTEDHAMMER" , 48:"CDLKICKING" , 49:"CDLKICKINGBYLENGTH" , 50:"CDLLADDERBOTTOM" , 51:"CDLLONGLEGGEDDOJI" , 52:"CDLLONGLINE" , 53:"CDLMARUBOZU" , 54:"CDLMATCHINGLOW" , 55:"CDLMATHOLD" , 56:"CDLMORNINGDOJISTAR" , 57:"CDLMORNINGSTAR" , 58:"CDLONNECK" , 59:"CDLPIERCING" , 60:"CDLRICKSHAWMAN" , 61:"CDLRISEFALL3METHODS" , 62:"CDLSEPARATINGLINES" , 63:"CDLSHOOTINGSTAR" , 64:"CDLSHORTLINE" , 65:"CDLSPINNINGTOP" , 66:"CDLSTALLEDPATTERN" , 67:"CDLSTICKSANDWICH" , 68:"CDLTAKURI" , 69:"CDLTASUKIGAP" , 70:"CDLTHRUSTING" , 71:"CDLTRISTAR" , 72:"CDLUNIQUE3RIVER" , 73:"CDLUPSIDEGAP2CROWS" , 74:"CDLXSIDEGAP3METHODS", 
75: "fft_20_close", 76:"fft_100_close", 77:"fft_100_open", 78:"fft_100_low", 79:"fft_100_high",80:'ema_12',81:'ema_26',82:'upper_list',83:'lower_list',84:'K_value',85:'D_value'}
	df = utils.get_data(MYDB, SQL, NAME_DICT)
	if isinstance(df, int) == False and len(df) != 0:
		label = [0]*len(df)
		df['label'] = label
		utils.labelling_data(label,min_index_list,max_index_list)
		df = df[['date_of_day', 'hour', 'name', 'volume', 'numberOfTrades',
       'var_ema', 'var_bollinger', 'var_stoch', 'rsi_indicator',
       'stoch_indicator', 'RSI', 'ema_indicator', 'bollinger_indicator',
       'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE',
       'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS',
       'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY',
       'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK',
       'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI',
       'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR',
       'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER',
       'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE',
       'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS',
       'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH',
       'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU',
       'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR',
       'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS',
       'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE',
       'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI',
       'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER',
       'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'fft_20_close',
       'fft_100_close', 'fft_100_open', 'fft_100_low', 'fft_100_high',
       'ema_12', 'ema_26', 'upper_list', 'lower_list', 'K_value', 'D_value',
       'label']]
		SQL = "INSERT INTO master_record_staging (date_of_day,hour,name,volume,numberOfTrades,var_ema,var_bollinger,var_stoch,rsi_indicator,stoch_indicator,RSI,ema_indicator,bollinger_indicator,CDL2CROWS,CDL3BLACKCROWS,CDL3INSIDE,CDL3LINESTRIKE,CDL3OUTSIDE,CDL3STARSINSOUTH,CDL3WHITESOLDIERS,CDLABANDONEDBABY,CDLADVANCEBLOCK,CDLBELTHOLD,CDLBREAKAWAY,CDLCLOSINGMARUBOZU,CDLCONCEALBABYSWALL,CDLCOUNTERATTACK,CDLDARKCLOUDCOVER,CDLDOJI,CDLDOJISTAR,CDLDRAGONFLYDOJI,CDLENGULFING,CDLEVENINGDOJISTAR,CDLEVENINGSTAR,CDLGAPSIDESIDEWHITE,CDLGRAVESTONEDOJI,CDLHAMMER,CDLHANGINGMAN,CDLHARAMI,CDLHARAMICROSS,CDLHIGHWAVE,CDLHIKKAKE,CDLHIKKAKEMOD,CDLHOMINGPIGEON,CDLIDENTICAL3CROWS,CDLINNECK,CDLINVERTEDHAMMER,CDLKICKING,CDLKICKINGBYLENGTH,CDLLADDERBOTTOM,CDLLONGLEGGEDDOJI,CDLLONGLINE,CDLMARUBOZU,CDLMATCHINGLOW,CDLMATHOLD,CDLMORNINGDOJISTAR,CDLMORNINGSTAR,CDLONNECK,CDLPIERCING,CDLRICKSHAWMAN,CDLRISEFALL3METHODS,CDLSEPARATINGLINES,CDLSHOOTINGSTAR,CDLSHORTLINE,CDLSPINNINGTOP,CDLSTALLEDPATTERN,CDLSTICKSANDWICH,CDLTAKURI,CDLTASUKIGAP,CDLTHRUSTING,CDLTRISTAR,CDLUNIQUE3RIVER,CDLUPSIDEGAP2CROWS,CDLXSIDEGAP3METHODS,fft_20_close,fft_100_close,fft_100_open,fft_100_low,fft_100_high,ema_12,ema_26,upper_list,lower_list,K_value,D_value,label) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		VAL = [tuple(x) for x in df.values.tolist()]
		if len(VAL) > 0:
			utils.insert_data(MYDB,SQL,VAL)
		else:
			print('no data to insert')
	else:
		print('empty dataframe')
