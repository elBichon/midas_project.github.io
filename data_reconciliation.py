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
	  database = db_credentials.database)

	sql = "SELECT * FROM processed_stock LEFT JOIN candlestick_indicator ON processed_stock.id = candlestick_indicator.id UNION SELECT * FROM processed_stock RIGHT JOIN candlestick_indicator ON processed_stock.id = candlestick_indicator.id"
	name_dict={0:"index", 1:"date_of_day" , 2:"label" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"index2", 20:"CDL2CROWS" , 21:"CDL3BLACKCROWS" , 22:"CDL3INSIDE" , 23:"CDL3LINESTRIKE" , 24:"CDL3OUTSIDE" , 25:"CDL3STARSINSOUTH" , 26:"CDL3WHITESOLDIERS" , 27:"CDLABANDONEDBABY" , 28:"CDLADVANCEBLOCK" , 29:"CDLBELTHOLD" , 30:"CDLBREAKAWAY" , 31:"CDLCLOSINGMARUBOZU" , 32:"CDLCONCEALBABYSWALL" , 33:"CDLCOUNTERATTACK" , 34:"CDLDARKCLOUDCOVER" , 35:"CDLDOJI" , 36:"CDLDOJISTAR" , 37:"CDLDRAGONFLYDOJI" , 38:"CDLENGULFING" , 39:"CDLEVENINGDOJISTAR" , 40:"CDLEVENINGSTAR" , 41:"CDLGAPSIDESIDEWHITE" , 42:"CDLGRAVESTONEDOJI" , 43:"CDLHAMMER" , 44:"CDLHANGINGMAN" , 45:"CDLHARAMI" , 46:"CDLHARAMICROSS" , 47:"CDLHIGHWAVE" , 48:"CDLHIKKAKE" , 49:"CDLHIKKAKEMOD" , 50:"CDLHOMINGPIGEON" , 51:"CDLIDENTICAL3CROWS" , 52:"CDLINNECK" , 53:"CDLINVERTEDHAMMER" , 54:"CDLKICKING" , 55:"CDLKICKINGBYLENGTH" , 56:"CDLLADDERBOTTOM" , 57:"CDLLONGLEGGEDDOJI" , 58:"CDLLONGLINE" , 59:"CDLMARUBOZU" , 60:"CDLMATCHINGLOW" , 61:"CDLMATHOLD" , 62:"CDLMORNINGDOJISTAR" , 63:"CDLMORNINGSTAR" , 64:"CDLONNECK" , 65:"CDLPIERCING" , 66:"CDLRICKSHAWMAN" , 67:"CDLRISEFALL3METHODS" , 68:"CDLSEPARATINGLINES" , 69:"CDLSHOOTINGSTAR" , 70:"CDLSHORTLINE" , 71:"CDLSPINNINGTOP" , 72:"CDLSTALLEDPATTERN" , 73:"CDLSTICKSANDWICH" , 74:"CDLTAKURI" , 75:"CDLTASUKIGAP" , 76:"CDLTHRUSTING" , 77:"CDLTRISTAR" , 78:"CDLUNIQUE3RIVER" , 79:"CDLUPSIDEGAP2CROWS" , 80:"CDLXSIDEGAP3METHODS"}
	df = utils.get_data(mydb, sql, name_dict)
	df = df.drop('index2', 1)

	date_of_day = df.date_of_day.values.tolist()
	label = df.label.values.tolist() 
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

	sql = "INSERT INTO unlabelled_record (date_of_day, label, name, volume, numberOfTrades,var_ema, var_bollinger, var_stoch, rsi_indicator,stoch_indicator, RSI, ema_indicator, bollinger_indicator,fft_20_close, fft_100_close, fft_100_open, fft_100_low,fft_100_high, CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE,CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH,CDL3WHITESOLDIERS, CDLABANDONEDBABY, CDLADVANCEBLOCK,CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU,CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING,CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE,CDLGRAVESTONEDOJI, CDLHAMMER, CDLHANGINGMAN, CDLHARAMI,CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD,CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, CDLINNECK,CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH,CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU,CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR,CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE,CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER,CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(date_of_day):
		print(str(i)+'/'+str(len(date_of_day)))
		val = (date_of_day[i], label[i], name[i], volume[i], numberOfTrades[i], var_ema[i], var_bollinger[i], var_stoch[i], rsi_indicator[i], stoch_indicator[i], RSI[i], ema_indicator[i], bollinger_indicator[i],fft_20_close[i],fft_100_close[i],fft_100_open[i],fft_100_low[i],fft_100_high[i] ,CDL2CROWS[i], CDL3BLACKCROWS[i], CDL3INSIDE[i], CDL3LINESTRIKE[i], CDL3OUTSIDE[i], CDL3STARSINSOUTH[i], CDL3WHITESOLDIERS[i], CDLABANDONEDBABY[i], CDLADVANCEBLOCK[i], CDLBELTHOLD[i], CDLBREAKAWAY[i], CDLCLOSINGMARUBOZU[i], CDLCONCEALBABYSWALL[i], CDLCOUNTERATTACK[i], CDLDARKCLOUDCOVER[i], CDLDOJI[i], CDLDOJISTAR[i], CDLDRAGONFLYDOJI[i], CDLENGULFING[i], CDLEVENINGDOJISTAR[i], CDLEVENINGSTAR[i], CDLGAPSIDESIDEWHITE[i], CDLGRAVESTONEDOJI[i], CDLHAMMER[i], CDLHANGINGMAN[i], CDLHARAMI[i], CDLHARAMICROSS[i], CDLHIGHWAVE[i], CDLHIKKAKE[i], CDLHIKKAKEMOD[i], CDLHOMINGPIGEON[i], CDLIDENTICAL3CROWS[i], CDLINNECK[i], CDLINVERTEDHAMMER[i], CDLKICKING[i], CDLKICKINGBYLENGTH[i], CDLLADDERBOTTOM[i], CDLLONGLEGGEDDOJI[i], CDLLONGLINE[i], CDLMARUBOZU[i], CDLMATCHINGLOW[i], CDLMATHOLD[i], CDLMORNINGDOJISTAR[i], CDLMORNINGSTAR[i], CDLONNECK[i], CDLPIERCING[i], CDLRICKSHAWMAN[i], CDLRISEFALL3METHODS[i], CDLSEPARATINGLINES[i], CDLSHOOTINGSTAR[i], CDLSHORTLINE[i], CDLSPINNINGTOP[i], CDLSTALLEDPATTERN[i], CDLSTICKSANDWICH[i], CDLTAKURI[i], CDLTASUKIGAP[i], CDLTHRUSTING[i], CDLTRISTAR[i], CDLUNIQUE3RIVER[i], CDLUPSIDEGAP2CROWS[i], CDLXSIDEGAP3METHODS[i])
		utils.insert_multiple_into_db(mydb, sql,val)
		i += 1