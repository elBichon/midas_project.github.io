import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Master
import sqlalchemy.dialects.sqlite
from flask import Flask, jsonify
import mysql.connector
import db_credentials
import utils
from flask import Flask, render_template, request
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

MYDB = mysql.connector.connect(
  host=db_credentials.host,
  user=db_credentials.user,
  passwd=db_credentials.passwd,
  database=db_credentials.database
)

@app.route('/')
@app.route('/query-stock')
def query():
	NAME_DICT={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"CDL2CROWS", 15:"CDL3BLACKCROWS", 16:"CDL3INSIDE" , 17:"CDL3LINESTRIKE" , 18:"CDL3OUTSIDE" , 19:"CDL3STARSINSOUTH" , 20:"CDL3WHITESOLDIERS" , 21:"CDLABANDONEDBABY" , 22:"CDLADVANCEBLOCK" , 23:"CDLBELTHOLD" , 24:"CDLBREAKAWAY" , 25:"CDLCLOSINGMARUBOZU" , 26:"CDLCONCEALBABYSWALL" , 27:"CDLCOUNTERATTACK" , 28:"CDLDARKCLOUDCOVER" , 29:"CDLDOJI" , 30:"CDLDOJISTAR" , 31:"CDLDRAGONFLYDOJI" , 32:"CDLENGULFING" , 33:"CDLEVENINGDOJISTAR" , 34:"CDLEVENINGSTAR" , 35:"CDLGAPSIDESIDEWHITE" , 36:"CDLGRAVESTONEDOJI" , 37:"CDLHAMMER" , 38:"CDLHANGINGMAN" , 39:"CDLHARAMI" , 40:"CDLHARAMICROSS" , 41:"CDLHIGHWAVE" , 42:"CDLHIKKAKE" , 43:"CDLHIKKAKEMOD" , 44:"CDLHOMINGPIGEON" , 45:"CDLIDENTICAL3CROWS" , 46:"CDLINNECK" , 47:"CDLINVERTEDHAMMER" , 48:"CDLKICKING" , 49:"CDLKICKINGBYLENGTH" , 50:"CDLLADDERBOTTOM" , 51:"CDLLONGLEGGEDDOJI" , 52:"CDLLONGLINE" , 53:"CDLMARUBOZU" , 54:"CDLMATCHINGLOW" , 55:"CDLMATHOLD" , 56:"CDLMORNINGDOJISTAR" , 57:"CDLMORNINGSTAR" , 58:"CDLONNECK" , 59:"CDLPIERCING" , 60:"CDLRICKSHAWMAN" , 61:"CDLRISEFALL3METHODS" , 62:"CDLSEPARATINGLINES" , 63:"CDLSHOOTINGSTAR" , 64:"CDLSHORTLINE" , 65:"CDLSPINNINGTOP" , 66:"CDLSTALLEDPATTERN" , 67:"CDLSTICKSANDWICH" , 68:"CDLTAKURI" , 69:"CDLTASUKIGAP" , 70:"CDLTHRUSTING" , 71:"CDLTRISTAR" , 72:"CDLUNIQUE3RIVER" , 73:"CDLUPSIDEGAP2CROWS" , 74:"CDLXSIDEGAP3METHODS", 
75: "fft_20_close", 76:"fft_100_close", 77:"fft_100_open", 78:"fft_100_low", 79:"fft_100_high",80:'ema_12',81:'ema_26',82:'upper_list',83:'lower_list',84:'K_value',85:'D_value',86:'label'}
	stock_symbol = request.args.get('stock_symbol').upper()
	SQL = "SELECT * FROM master_record WHERE name = '"
	SQL = utils.generate_query(SQL,stock_symbol)+"'"
	df = utils.get_data(MYDB, SQL, NAME_DICT)
	print(df.columns)
	df = df[df.D_value != -100]
	df = df[df.K_value != -100]
	df = df[df.RSI != -100]
	df = df[df.lower_list != -100]
	df = df[df.upper_list != -100]

	if isinstance(df, int) == False and len(df) != 0:
		stock_data = {"id":df.index.values.tolist(),"date":df.date_of_day.values.tolist(),"hour":df.hour.values.tolist(),"name":df.name.values.tolist(),"RSI":df.RSI.values.tolist(),"fft_20_close":df.fft_20_close.values.tolist(),"fft_100_close":df.fft_100_close.values.tolist(),"ema_12":df.ema_12.values.tolist(),"ema_26":df.ema_26.values.tolist(),"upper_list":df.upper_list.values.tolist(),"lower_list":df.lower_list.values.tolist(),"K_value":df.K_value.values.tolist(),"D_value":df.D_value.values.tolist(),"volume":df.volume.values.tolist(),"numberOfTrades":df.numberOfTrades.values.tolist()}
		return jsonify(stock_data)
	else:
		return '''<h1>Empty value</h1>'''

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)

#http://127.0.0.1:5000/query-stock?stock_symbol=CSCO

