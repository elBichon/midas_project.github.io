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
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:'ema_12', 20:'ema_26', 21:'upper_list', 22:'lower_list',23:'K_value',24:'D_value', 25:"index2", 26:"CDL2CROWS" , 27:"CDL3BLACKCROWS" , 28:"CDL3INSIDE" , 29:"CDL3LINESTRIKE" , 30:"CDL3OUTSIDE" , 31:"CDL3STARSINSOUTH" , 32:"CDL3WHITESOLDIERS" , 33:"CDLABANDONEDBABY" , 34:"CDLADVANCEBLOCK" , 35:"CDLBELTHOLD" , 36:"CDLBREAKAWAY" , 37:"CDLCLOSINGMARUBOZU" , 38:"CDLCONCEALBABYSWALL" , 39:"CDLCOUNTERATTACK" , 40:"CDLDARKCLOUDCOVER" , 41:"CDLDOJI" , 42:"CDLDOJISTAR" , 43:"CDLDRAGONFLYDOJI" , 44:"CDLENGULFING" , 45:"CDLEVENINGDOJISTAR" , 46:"CDLEVENINGSTAR" , 47:"CDLGAPSIDESIDEWHITE" , 48:"CDLGRAVESTONEDOJI" , 49:"CDLHAMMER" , 50:"CDLHANGINGMAN" , 51:"CDLHARAMI" , 52:"CDLHARAMICROSS" , 53:"CDLHIGHWAVE" , 54:"CDLHIKKAKE" , 55:"CDLHIKKAKEMOD" , 56:"CDLHOMINGPIGEON" , 57:"CDLIDENTICAL3CROWS" , 58:"CDLINNECK" , 59:"CDLINVERTEDHAMMER" , 60:"CDLKICKING" , 61:"CDLKICKINGBYLENGTH" , 62:"CDLLADDERBOTTOM" , 63:"CDLLONGLEGGEDDOJI" , 64:"CDLLONGLINE" , 65:"CDLMARUBOZU" , 66:"CDLMATCHINGLOW" , 67:"CDLMATHOLD" , 68:"CDLMORNINGDOJISTAR" , 69:"CDLMORNINGSTAR" , 70:"CDLONNECK" , 71:"CDLPIERCING" , 72:"CDLRICKSHAWMAN" , 73:"CDLRISEFALL3METHODS" , 74:"CDLSEPARATINGLINES" , 75:"CDLSHOOTINGSTAR" , 76:"CDLSHORTLINE" , 77:"CDLSPINNINGTOP" , 78:"CDLSTALLEDPATTERN" , 79:"CDLSTICKSANDWICH" , 80:"CDLTAKURI" , 81:"CDLTASUKIGAP" , 82:"CDLTHRUSTING" , 83:"CDLTRISTAR" , 84:"CDLUNIQUE3RIVER" , 85:"CDLUPSIDEGAP2CROWS" , 86:"CDLXSIDEGAP3METHODS"}
	df = utils.get_data(mydb, sql, name_dict)
	df = df.drop('index2', 1)
	index = df.index.values.tolist()
	ema_12 = df['ema_12'].values.tolist()
	ema_26 = df['ema_26'].values.tolist()
	upper_list = df['upper_list'].values.tolist()
	lower_list = df['lower_list'].values.tolist()
	K_value = df['K_value'].values.tolist()
	D_value = df['D_value'].values.tolist()
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

	sql = "INSERT INTO unlabelled_record (date_of_day, hour, name, volume, numberOfTrades,var_ema, var_bollinger, var_stoch, rsi_indicator,stoch_indicator, RSI, ema_indicator, bollinger_indicator, CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE,CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH,CDL3WHITESOLDIERS, CDLABANDONEDBABY, CDLADVANCEBLOCK,CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU,CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING,CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE,CDLGRAVESTONEDOJI, CDLHAMMER, CDLHANGINGMAN, CDLHARAMI,CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD,CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, CDLINNECK,CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH,CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU,CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR,CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE,CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER,CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS,fft_20_close, fft_100_close, fft_100_open, fft_100_low,fft_100_high, ema_12, ema_26, upper_list, lower_list, K_value, D_value ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(index):
		print(str(i)+'/'+str(len(index)))
		val = (date_of_day[i], hour[i], name[i], volume[i], numberOfTrades[i], var_ema[i], var_bollinger[i], var_stoch[i], rsi_indicator[i], stoch_indicator[i], RSI[i], ema_indicator[i], bollinger_indicator[i],CDL2CROWS[i], CDL3BLACKCROWS[i], CDL3INSIDE[i], CDL3LINESTRIKE[i], CDL3OUTSIDE[i], CDL3STARSINSOUTH[i], CDL3WHITESOLDIERS[i], CDLABANDONEDBABY[i], CDLADVANCEBLOCK[i], CDLBELTHOLD[i], CDLBREAKAWAY[i], CDLCLOSINGMARUBOZU[i], CDLCONCEALBABYSWALL[i], CDLCOUNTERATTACK[i], CDLDARKCLOUDCOVER[i], CDLDOJI[i], CDLDOJISTAR[i], CDLDRAGONFLYDOJI[i], CDLENGULFING[i], CDLEVENINGDOJISTAR[i], CDLEVENINGSTAR[i], CDLGAPSIDESIDEWHITE[i], CDLGRAVESTONEDOJI[i], CDLHAMMER[i], CDLHANGINGMAN[i], CDLHARAMI[i], CDLHARAMICROSS[i], CDLHIGHWAVE[i], CDLHIKKAKE[i], CDLHIKKAKEMOD[i], CDLHOMINGPIGEON[i], CDLIDENTICAL3CROWS[i], CDLINNECK[i], CDLINVERTEDHAMMER[i], CDLKICKING[i], CDLKICKINGBYLENGTH[i], CDLLADDERBOTTOM[i], CDLLONGLEGGEDDOJI[i], CDLLONGLINE[i], CDLMARUBOZU[i], CDLMATCHINGLOW[i], CDLMATHOLD[i], CDLMORNINGDOJISTAR[i], CDLMORNINGSTAR[i], CDLONNECK[i], CDLPIERCING[i], CDLRICKSHAWMAN[i], CDLRISEFALL3METHODS[i], CDLSEPARATINGLINES[i], CDLSHOOTINGSTAR[i], CDLSHORTLINE[i], CDLSPINNINGTOP[i], CDLSTALLEDPATTERN[i], CDLSTICKSANDWICH[i], CDLTAKURI[i], CDLTASUKIGAP[i], CDLTHRUSTING[i], CDLTRISTAR[i], CDLUNIQUE3RIVER[i], CDLUPSIDEGAP2CROWS[i], CDLXSIDEGAP3METHODS[i], fft_20_close[i],fft_100_close[i],fft_100_open[i],fft_100_low[i],fft_100_high[i], ema_12[i], ema_26[i], upper_list[i], lower_list[i], K_value[i], D_value[i])
		utils.insert_multiple_into_db(mydb, sql,val)
		i += 1