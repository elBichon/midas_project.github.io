import mysql.connector
import db_credentials

#create database
mydb = mysql.connector.connect(
  host=db_credentials.host,
  user=db_credentials.user,
  passwd=db_credentials.passwd,
) 
mycursor = mydb.cursor()

print('creating database for Midas Hand')
try:
	mycursor.execute("CREATE DATABASE Midas_Hand")
	mycursor.execute("SHOW DATABASES")
except:
	mycursor.execute("SHOW DATABASES")
	pass

#for x in mycursor:
#  print(x) 
#connect to database
mydb = mysql.connector.connect(
  host=db_credentials.host,
  user=db_credentials.user,
  passwd=db_credentials.passwd,
  database=db_credentials.database
) 


print('creating tables for midas hand')
mycursor = mydb.cursor()
try:
	mycursor.execute("CREATE TABLE raw_stock (id INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(255), hour VARCHAR(255), name VARCHAR(255), high FLOAT, low FLOAT, open FLOAT, close FLOAT, volume INT, numberOfTrades INT)") 
except:
	pass
try:
	mycursor.execute("CREATE TABLE fourier_processed_stock (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, numberOfTrades INT , name TEXT, volume INT, fft_20_close FLOAT, fft_20_open FLOAT, fft_20_low FLOAT, fft_20_high FLOAT, fft_100_close FLOAT, fft_100_open FLOAT, fft_100_low FLOAT, fft_100_high FLOAT)") 
except:
	pass
try:
	mycursor.execute("CREATE TABLE processed_stock (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255), volume FLOAT, numberOfTrades INT, var_ema FLOAT, var_bollinger FLOAT, var_stoch FLOAT,rsi_indicator INT, stoch_indicator INT, RSI FLOAT, ema_indicator FLOAT, bollinger_indicator FLOAT, fft_20_close FLOAT, fft_100_close FLOAT, fft_100_open FLOAT, fft_100_low FLOAT, fft_100_high FLOAT)") 
except:
	pass
try:
	mycursor.execute("CREATE TABLE candlestick_indicator (id INT AUTO_INCREMENT PRIMARY KEY, CDL2CROWS INT, CDL3BLACKCROWS INT, CDL3INSIDE INT, CDL3LINESTRIKE INT, CDL3OUTSIDE INT, CDL3STARSINSOUTH INT, CDL3WHITESOLDIERS INT, CDLABANDONEDBABY INT, CDLADVANCEBLOCK INT, CDLBELTHOLD INT, CDLBREAKAWAY INT, CDLCLOSINGMARUBOZU INT, CDLCONCEALBABYSWALL INT, CDLCOUNTERATTACK INT, CDLDARKCLOUDCOVER INT, CDLDOJI INT, CDLDOJISTAR INT, CDLDRAGONFLYDOJI INT, CDLENGULFING INT, CDLEVENINGDOJISTAR INT, CDLEVENINGSTAR INT, CDLGAPSIDESIDEWHITE INT, CDLGRAVESTONEDOJI INT, CDLHAMMER INT, CDLHANGINGMAN INT, CDLHARAMI INT, CDLHARAMICROSS INT, CDLHIGHWAVE INT, CDLHIKKAKE INT, CDLHIKKAKEMOD INT, CDLHOMINGPIGEON INT, CDLIDENTICAL3CROWS INT, CDLINNECK INT, CDLINVERTEDHAMMER INT, CDLKICKING INT, CDLKICKINGBYLENGTH INT, CDLLADDERBOTTOM INT, CDLLONGLEGGEDDOJI INT, CDLLONGLINE INT, CDLMARUBOZU INT, CDLMATCHINGLOW INT, CDLMATHOLD INT, CDLMORNINGDOJISTAR INT, CDLMORNINGSTAR INT, CDLONNECK INT, CDLPIERCING INT, CDLRICKSHAWMAN INT, CDLRISEFALL3METHODS INT, CDLSEPARATINGLINES INT, CDLSHOOTINGSTAR INT, CDLSHORTLINE INT, CDLSPINNINGTOP INT, CDLSTALLEDPATTERN INT, CDLSTICKSANDWICH INT, CDLTAKURI INT, CDLTASUKIGAP INT, CDLTHRUSTING INT, CDLTRISTAR INT, CDLUNIQUE3RIVER INT, CDLUPSIDEGAP2CROWS INT, CDLXSIDEGAP3METHODS INT)")
except:
	pass
try:
	mycursor.execute("CREATE TABLE twitter_content (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255), tweet_text TEXT)")
except:
	pass
try:
	mycursor.execute("CREATE TABLE processed_tweet (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255), processed_tweet_text TEXT,stock_variation float)")
except:
	pass
try:
	mycursor.execute("CREATE TABLE unlabelled_record (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255),volume FLOAT, numberOfTrades INT, var_ema FLOAT, var_bollinger FLOAT, var_stoch FLOAT,rsi_indicator INT, stoch_indicator INT, RSI FLOAT, ema_indicator FLOAT, bollinger_indicator FLOAT, CDL2CROWS INT, CDL3BLACKCROWS INT, CDL3INSIDE INT, CDL3LINESTRIKE INT, CDL3OUTSIDE INT, CDL3STARSINSOUTH INT, CDL3WHITESOLDIERS INT, CDLABANDONEDBABY INT, CDLADVANCEBLOCK INT, CDLBELTHOLD INT, CDLBREAKAWAY INT, CDLCLOSINGMARUBOZU INT, CDLCONCEALBABYSWALL INT, CDLCOUNTERATTACK INT, CDLDARKCLOUDCOVER INT, CDLDOJI INT, CDLDOJISTAR INT, CDLDRAGONFLYDOJI INT, CDLENGULFING INT, CDLEVENINGDOJISTAR INT, CDLEVENINGSTAR INT, CDLGAPSIDESIDEWHITE INT, CDLGRAVESTONEDOJI INT, CDLHAMMER INT, CDLHANGINGMAN INT, CDLHARAMI INT, CDLHARAMICROSS INT, CDLHIGHWAVE INT, CDLHIKKAKE INT, CDLHIKKAKEMOD INT, CDLHOMINGPIGEON INT, CDLIDENTICAL3CROWS INT, CDLINNECK INT, CDLINVERTEDHAMMER INT, CDLKICKING INT, CDLKICKINGBYLENGTH INT, CDLLADDERBOTTOM INT, CDLLONGLEGGEDDOJI INT, CDLLONGLINE INT, CDLMARUBOZU INT, CDLMATCHINGLOW INT, CDLMATHOLD INT, CDLMORNINGDOJISTAR INT, CDLMORNINGSTAR INT, CDLONNECK INT, CDLPIERCING INT, CDLRICKSHAWMAN INT, CDLRISEFALL3METHODS INT, CDLSEPARATINGLINES INT, CDLSHOOTINGSTAR INT, CDLSHORTLINE INT, CDLSPINNINGTOP INT, CDLSTALLEDPATTERN INT, CDLSTICKSANDWICH INT, CDLTAKURI INT, CDLTASUKIGAP INT, CDLTHRUSTING INT, CDLTRISTAR INT, CDLUNIQUE3RIVER INT, CDLUPSIDEGAP2CROWS INT, CDLXSIDEGAP3METHODS INT, fft_20_close FLOAT, fft_100_close FLOAT, fft_100_open FLOAT, fft_100_low FLOAT, fft_100_high FLOAT)") 
except:
	pass
try:
	mycursor.execute("CREATE TABLE master_record_staging (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255),volume FLOAT, numberOfTrades INT, var_ema FLOAT, var_bollinger FLOAT, var_stoch FLOAT,rsi_indicator INT, stoch_indicator INT, RSI FLOAT, ema_indicator FLOAT, bollinger_indicator FLOAT, CDL2CROWS INT, CDL3BLACKCROWS INT, CDL3INSIDE INT, CDL3LINESTRIKE INT, CDL3OUTSIDE INT, CDL3STARSINSOUTH INT, CDL3WHITESOLDIERS INT, CDLABANDONEDBABY INT, CDLADVANCEBLOCK INT, CDLBELTHOLD INT, CDLBREAKAWAY INT, CDLCLOSINGMARUBOZU INT, CDLCONCEALBABYSWALL INT, CDLCOUNTERATTACK INT, CDLDARKCLOUDCOVER INT, CDLDOJI INT, CDLDOJISTAR INT, CDLDRAGONFLYDOJI INT, CDLENGULFING INT, CDLEVENINGDOJISTAR INT, CDLEVENINGSTAR INT, CDLGAPSIDESIDEWHITE INT, CDLGRAVESTONEDOJI INT, CDLHAMMER INT, CDLHANGINGMAN INT, CDLHARAMI INT, CDLHARAMICROSS INT, CDLHIGHWAVE INT, CDLHIKKAKE INT, CDLHIKKAKEMOD INT, CDLHOMINGPIGEON INT, CDLIDENTICAL3CROWS INT, CDLINNECK INT, CDLINVERTEDHAMMER INT, CDLKICKING INT, CDLKICKINGBYLENGTH INT, CDLLADDERBOTTOM INT, CDLLONGLEGGEDDOJI INT, CDLLONGLINE INT, CDLMARUBOZU INT, CDLMATCHINGLOW INT, CDLMATHOLD INT, CDLMORNINGDOJISTAR INT, CDLMORNINGSTAR INT, CDLONNECK INT, CDLPIERCING INT, CDLRICKSHAWMAN INT, CDLRISEFALL3METHODS INT, CDLSEPARATINGLINES INT, CDLSHOOTINGSTAR INT, CDLSHORTLINE INT, CDLSPINNINGTOP INT, CDLSTALLEDPATTERN INT, CDLSTICKSANDWICH INT, CDLTAKURI INT, CDLTASUKIGAP INT, CDLTHRUSTING INT, CDLTRISTAR INT, CDLUNIQUE3RIVER INT, CDLUPSIDEGAP2CROWS INT, CDLXSIDEGAP3METHODS INT, fft_20_close FLOAT, fft_100_close FLOAT, fft_100_open FLOAT, fft_100_low FLOAT, fft_100_high FLOAT, label INT)") 
except:
	pass
try:
	mycursor.execute("CREATE TABLE master_record (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day TEXT, hour TEXT, name VARCHAR(255),volume FLOAT, numberOfTrades INT, var_ema FLOAT, var_bollinger FLOAT, var_stoch FLOAT,rsi_indicator INT, stoch_indicator INT, RSI FLOAT, ema_indicator FLOAT, bollinger_indicator FLOAT, CDL2CROWS INT, CDL3BLACKCROWS INT, CDL3INSIDE INT, CDL3LINESTRIKE INT, CDL3OUTSIDE INT, CDL3STARSINSOUTH INT, CDL3WHITESOLDIERS INT, CDLABANDONEDBABY INT, CDLADVANCEBLOCK INT, CDLBELTHOLD INT, CDLBREAKAWAY INT, CDLCLOSINGMARUBOZU INT, CDLCONCEALBABYSWALL INT, CDLCOUNTERATTACK INT, CDLDARKCLOUDCOVER INT, CDLDOJI INT, CDLDOJISTAR INT, CDLDRAGONFLYDOJI INT, CDLENGULFING INT, CDLEVENINGDOJISTAR INT, CDLEVENINGSTAR INT, CDLGAPSIDESIDEWHITE INT, CDLGRAVESTONEDOJI INT, CDLHAMMER INT, CDLHANGINGMAN INT, CDLHARAMI INT, CDLHARAMICROSS INT, CDLHIGHWAVE INT, CDLHIKKAKE INT, CDLHIKKAKEMOD INT, CDLHOMINGPIGEON INT, CDLIDENTICAL3CROWS INT, CDLINNECK INT, CDLINVERTEDHAMMER INT, CDLKICKING INT, CDLKICKINGBYLENGTH INT, CDLLADDERBOTTOM INT, CDLLONGLEGGEDDOJI INT, CDLLONGLINE INT, CDLMARUBOZU INT, CDLMATCHINGLOW INT, CDLMATHOLD INT, CDLMORNINGDOJISTAR INT, CDLMORNINGSTAR INT, CDLONNECK INT, CDLPIERCING INT, CDLRICKSHAWMAN INT, CDLRISEFALL3METHODS INT, CDLSEPARATINGLINES INT, CDLSHOOTINGSTAR INT, CDLSHORTLINE INT, CDLSPINNINGTOP INT, CDLSTALLEDPATTERN INT, CDLSTICKSANDWICH INT, CDLTAKURI INT, CDLTASUKIGAP INT, CDLTHRUSTING INT, CDLTRISTAR INT, CDLUNIQUE3RIVER INT, CDLUPSIDEGAP2CROWS INT, CDLXSIDEGAP3METHODS INT, fft_20_close FLOAT, fft_100_close FLOAT, fft_100_open FLOAT, fft_100_low FLOAT, fft_100_high FLOAT, label INT)") 
except:
	pass

