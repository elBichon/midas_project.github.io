#! /usr/bin/env python3
# coding: utf-8
import mysql.connector
import db_credentials
import pandas as pd
import talib, re  
import numpy as np
import utils


def main():
    pass

if __name__ == "__main__":
	
	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM fourier_processed_stock")
	table_rows = mycursor.fetchall()
	df = pd.DataFrame(table_rows)
	df = df.rename(columns={0:'index', 1:'fft_20_close', 2:'fft_20_open', 3:'fft_20_low', 4:'fft_20_high', 5:'fft_100_close', 6:'fft_100_open', 7:'fft_100_low', 8:'fft_100_high'})
	ohlc = df[['fft_100_open', 'fft_100_high', 'fft_100_low', 'fft_100_close']]

	O  = np.array(ohlc.fft_100_open,dtype='f8')
	H  = np.array(ohlc.fft_100_high,dtype='f8')
	L   = np.array(ohlc.fft_100_low,dtype='f8')
	C = np.array(ohlc.fft_100_close,dtype='f8')
	  
	cdls = re.findall('(CDL\w*)', ' '.join(dir(talib)))
	for cdl in cdls:  
		toExec = getattr(talib, cdl)  
		out = toExec(np.array(O), np.array(H), np.array(L), np.array(C))  
		df[str(cdl)] = out
		df[str(cdl)] = df[str(cdl)].apply(utils.labelCorrection)

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

	sql = "INSERT INTO candlestick_indicator (CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE, CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, CDL3WHITESOLDIERS, CDLABANDONEDBABY, CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER, CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI, CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, CDLINNECK, CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS, CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI, CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(O):
		try:
			mycursor = mydb.cursor()
			val = (CDL2CROWS[i], CDL3BLACKCROWS[i], CDL3INSIDE[i], CDL3LINESTRIKE[i], CDL3OUTSIDE[i], CDL3STARSINSOUTH[i], CDL3WHITESOLDIERS[i], CDLABANDONEDBABY[i], CDLADVANCEBLOCK[i], CDLBELTHOLD[i], CDLBREAKAWAY[i], CDLCLOSINGMARUBOZU[i], CDLCONCEALBABYSWALL[i], CDLCOUNTERATTACK[i], CDLDARKCLOUDCOVER[i], CDLDOJI[i], CDLDOJISTAR[i], CDLDRAGONFLYDOJI[i], CDLENGULFING[i], CDLEVENINGDOJISTAR[i], CDLEVENINGSTAR[i], CDLGAPSIDESIDEWHITE[i], CDLGRAVESTONEDOJI[i], CDLHAMMER[i], CDLHANGINGMAN[i], CDLHARAMI[i], CDLHARAMICROSS[i], CDLHIGHWAVE[i], CDLHIKKAKE[i], CDLHIKKAKEMOD[i], CDLHOMINGPIGEON[i], CDLIDENTICAL3CROWS[i], CDLINNECK[i], CDLINVERTEDHAMMER[i], CDLKICKING[i], CDLKICKINGBYLENGTH[i], CDLLADDERBOTTOM[i], CDLLONGLEGGEDDOJI[i], CDLLONGLINE[i], CDLMARUBOZU[i], CDLMATCHINGLOW[i], CDLMATHOLD[i], CDLMORNINGDOJISTAR[i], CDLMORNINGSTAR[i], CDLONNECK[i], CDLPIERCING[i], CDLRICKSHAWMAN[i], CDLRISEFALL3METHODS[i], CDLSEPARATINGLINES[i], CDLSHOOTINGSTAR[i], CDLSHORTLINE[i], CDLSPINNINGTOP[i], CDLSTALLEDPATTERN[i], CDLSTICKSANDWICH[i], CDLTAKURI[i], CDLTASUKIGAP[i], CDLTHRUSTING[i], CDLTRISTAR[i], CDLUNIQUE3RIVER[i], CDLUPSIDEGAP2CROWS[i], CDLXSIDEGAP3METHODS[i])
			mycursor.execute(sql, val)
			print(mycursor.rowcount, "record inserted.")
		except:
			pass
		i += 1
	mydb.commit()


