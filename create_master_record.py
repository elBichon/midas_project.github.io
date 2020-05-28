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

	sql = "SELECT name, MIN(fft_100_close) FROM unlabelled_record GROUP BY name"
	table_rows = utils.extract_data(sql,mydb)
	min_index_list = []
	i = 0
	while i < len(table_rows):
		sql = "SELECT id FROM unlabelled_record WHERE name = '"+str(table_rows[i][0])+"' AND fft_100_close LIKE "+str(table_rows[i][1]).replace('.0','')
		utils.get_index(sql,min_index_list,mydb)
		i += 1

	sql = "SELECT name, MAX(fft_100_close) FROM unlabelled_record GROUP BY name"
	table_rows = utils.extract_data(sql,mydb)
	max_index_list = []
	i = 0
	while i < len(table_rows):
		sql = "SELECT id FROM unlabelled_record WHERE name = '"+str(table_rows[i][0])+"' AND fft_100_close LIKE "+str(table_rows[i][1]).replace('.0','')
		utils.get_index(sql,max_index_list,mydb)
		i += 1

	sql = "SELECT * FROM unlabelled_record"
	table_rows = utils.extract_data(sql,mydb)
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS"}
	df = utils.get_data(mydb, sql, name_dict)

	index = df.index.values.tolist()
	date_of_day = df.date_of_day.values.tolist()
	hour = df.hour.values.tolist() 
	name = df.name.values.tolist()
	volume = df.volume.values.tolist()
	numberOfTrades = df.numberOfTrades.values.tolist()
	var_ema = df.var_ema.values.tolist()
	var_bollinger = df.var_bollinger.values.tolist()
	var_stoch = df.var_stoch.values.tolist()
	rsi_indicator = df.rsi_indicator.values.tolist()
	stoch_indicator = df.stoch_indicator.values.tolist()
	RSI = df.RSI.values.tolist() 
	ema_indicator = df.ema_indicator.values.tolist() 
	bollinger_indicator = df.bollinger_indicator.values.tolist()
	fft_20_close = df.fft_20_close.values.tolist()
	fft_100_close = df.fft_100_close.values.tolist()
	fft_100_open = df.fft_100_open.values.tolist()
	fft_100_low = df.fft_100_low.values.tolist()
	fft_100_high = df.fft_100_high.values.tolist()

	CDL2CROWS = df.CDL2CROWS.values.tolist()
	CDL3BLACKCROWS = df.CDL3BLACKCROWS.values.tolist()
	CDL3INSIDE = df.CDL3INSIDE.values.tolist()
	CDL3LINESTRIKE = df.CDL3LINESTRIKE.values.tolist()
	CDL3OUTSIDE = df.CDL3OUTSIDE.values.tolist()
	CDL3STARSINSOUTH = df.CDL3STARSINSOUTH.values.tolist()
	CDL3WHITESOLDIERS = df.CDL3WHITESOLDIERS.values.tolist()
	CDLABANDONEDBABY = df.CDLABANDONEDBABY.values.tolist()
	CDLADVANCEBLOCK = df.CDLADVANCEBLOCK.values.tolist()
	CDLBELTHOLD = df.CDLBELTHOLD.values.tolist()
	CDLBREAKAWAY = df.CDLBREAKAWAY.values.tolist()
	CDLCLOSINGMARUBOZU = df.CDLCLOSINGMARUBOZU.values.tolist()
	CDLCONCEALBABYSWALL = df.CDLCONCEALBABYSWALL.values.tolist()
	CDLCOUNTERATTACK = df.CDLCOUNTERATTACK.values.tolist()
	CDLDARKCLOUDCOVER = df.CDLDARKCLOUDCOVER.values.tolist()
	CDLDOJI = df.CDLDOJI.values.tolist()
	CDLDOJISTAR = df.CDLDOJISTAR.values.tolist()
	CDLDRAGONFLYDOJI = df.CDLDRAGONFLYDOJI.values.tolist()
	CDLENGULFING = df.CDLENGULFING.values.tolist()
	CDLEVENINGDOJISTAR = df.CDLEVENINGDOJISTAR.values.tolist()
	CDLEVENINGSTAR = df.CDLEVENINGSTAR.values.tolist()
	CDLGAPSIDESIDEWHITE = df.CDLGAPSIDESIDEWHITE.values.tolist()
	CDLGRAVESTONEDOJI = df.CDLGRAVESTONEDOJI.values.tolist()
	CDLHAMMER = df.CDLHAMMER.values.tolist()
	CDLHANGINGMAN = df.CDLHANGINGMAN.values.tolist()
	CDLHARAMI = df.CDLHARAMI.values.tolist()
	CDLHARAMICROSS = df.CDLHARAMICROSS.values.tolist()
	CDLHIGHWAVE = df.CDLHIGHWAVE.values.tolist()
	CDLHIKKAKE = df.CDLHIKKAKE.values.tolist()
	CDLHIKKAKEMOD = df.CDLHIKKAKEMOD.values.tolist()
	CDLHOMINGPIGEON = df.CDLHOMINGPIGEON.values.tolist()
	CDLIDENTICAL3CROWS = df.CDLIDENTICAL3CROWS.values.tolist()
	CDLINNECK = df.CDLINNECK.values.tolist()
	CDLINVERTEDHAMMER = df.CDLINVERTEDHAMMER.values.tolist()
	CDLKICKING = df.CDLKICKING.values.tolist()
	CDLKICKINGBYLENGTH = df.CDLKICKINGBYLENGTH.values.tolist()
	CDLLADDERBOTTOM = df.CDLLADDERBOTTOM.values.tolist()
	CDLLONGLEGGEDDOJI = df.CDLLONGLEGGEDDOJI.values.tolist()
	CDLLONGLINE = df.CDLLONGLINE.values.tolist()
	CDLMARUBOZU = df.CDLMARUBOZU.values.tolist()
	CDLMATCHINGLOW = df.CDLMATCHINGLOW.values.tolist()
	CDLMATHOLD = df.CDLMATHOLD.values.tolist()
	CDLMORNINGDOJISTAR = df.CDLMORNINGDOJISTAR.values.tolist()
	CDLMORNINGSTAR = df.CDLMORNINGSTAR.values.tolist()
	CDLONNECK = df.CDLONNECK.values.tolist()
	CDLPIERCING = df.CDLPIERCING.values.tolist()
	CDLRICKSHAWMAN = df.CDLRICKSHAWMAN.values.tolist()
	CDLRISEFALL3METHODS = df.CDLRISEFALL3METHODS.values.tolist()
	CDLSEPARATINGLINES = df.CDLSEPARATINGLINES.values.tolist()
	CDLSHOOTINGSTAR = df.CDLSHOOTINGSTAR.values.tolist()
	CDLSHORTLINE = df.CDLSHORTLINE.values.tolist()
	CDLSPINNINGTOP = df.CDLSPINNINGTOP.values.tolist()
	CDLSTALLEDPATTERN = df.CDLSTALLEDPATTERN.values.tolist()
	CDLSTICKSANDWICH = df.CDLSTICKSANDWICH.values.tolist()
	CDLTAKURI = df.CDLTAKURI.values.tolist()
	CDLTASUKIGAP = df.CDLTASUKIGAP.values.tolist()
	CDLTHRUSTING = df.CDLTHRUSTING.values.tolist()
	CDLTRISTAR = df.CDLTRISTAR.values.tolist()
	CDLUNIQUE3RIVER = df.CDLUNIQUE3RIVER.values.tolist()
	CDLUPSIDEGAP2CROWS = df.CDLUPSIDEGAP2CROWS.values.tolist()
	CDLXSIDEGAP3METHODS = df.CDLXSIDEGAP3METHODS.values.tolist()

	label = [0]*len(table_rows)
	utils.labelling_data(label,min_index_list,max_index_list)

	sql = "INSERT INTO master_record_staging (date_of_day, hour, name, volume, numberOfTrades,var_ema, var_bollinger, var_stoch, rsi_indicator,stoch_indicator, RSI, ema_indicator, bollinger_indicator,fft_20_close, fft_100_close, fft_100_open, fft_100_low,fft_100_high, CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE,CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH,CDL3WHITESOLDIERS, CDLABANDONEDBABY, CDLADVANCEBLOCK,CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU,CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING,CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE,CDLGRAVESTONEDOJI, CDLHAMMER, CDLHANGINGMAN, CDLHARAMI,CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD,CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, CDLINNECK,CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH,CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU,CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR,CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE,CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER,CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS, label) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(index):
		print(str(i)+'/'+str(len(index)))
		val = (date_of_day[i], hour[i], name[i], volume[i], numberOfTrades[i], var_ema[i], var_bollinger[i], var_stoch[i], rsi_indicator[i], stoch_indicator[i], RSI[i], ema_indicator[i], bollinger_indicator[i],fft_20_close[i],fft_100_close[i],fft_100_open[i],fft_100_low[i],fft_100_high[i] ,CDL2CROWS[i], CDL3BLACKCROWS[i], CDL3INSIDE[i], CDL3LINESTRIKE[i], CDL3OUTSIDE[i], CDL3STARSINSOUTH[i], CDL3WHITESOLDIERS[i], CDLABANDONEDBABY[i], CDLADVANCEBLOCK[i], CDLBELTHOLD[i], CDLBREAKAWAY[i], CDLCLOSINGMARUBOZU[i], CDLCONCEALBABYSWALL[i], CDLCOUNTERATTACK[i], CDLDARKCLOUDCOVER[i], CDLDOJI[i], CDLDOJISTAR[i], CDLDRAGONFLYDOJI[i], CDLENGULFING[i], CDLEVENINGDOJISTAR[i], CDLEVENINGSTAR[i], CDLGAPSIDESIDEWHITE[i], CDLGRAVESTONEDOJI[i], CDLHAMMER[i], CDLHANGINGMAN[i], CDLHARAMI[i], CDLHARAMICROSS[i], CDLHIGHWAVE[i], CDLHIKKAKE[i], CDLHIKKAKEMOD[i], CDLHOMINGPIGEON[i], CDLIDENTICAL3CROWS[i], CDLINNECK[i], CDLINVERTEDHAMMER[i], CDLKICKING[i], CDLKICKINGBYLENGTH[i], CDLLADDERBOTTOM[i], CDLLONGLEGGEDDOJI[i], CDLLONGLINE[i], CDLMARUBOZU[i], CDLMATCHINGLOW[i], CDLMATHOLD[i], CDLMORNINGDOJISTAR[i], CDLMORNINGSTAR[i], CDLONNECK[i], CDLPIERCING[i], CDLRICKSHAWMAN[i], CDLRISEFALL3METHODS[i], CDLSEPARATINGLINES[i], CDLSHOOTINGSTAR[i], CDLSHORTLINE[i], CDLSPINNINGTOP[i], CDLSTALLEDPATTERN[i], CDLSTICKSANDWICH[i], CDLTAKURI[i], CDLTASUKIGAP[i], CDLTHRUSTING[i], CDLTRISTAR[i], CDLUNIQUE3RIVER[i], CDLUPSIDEGAP2CROWS[i], CDLXSIDEGAP3METHODS[i], label[i])
		utils.insert_multiple_into_db(mydb, sql,val)
		i += 1