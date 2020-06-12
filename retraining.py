from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd
import itertools
import mysql.connector
import db_credentials
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import recall_score
import numpy as np
import argparse
from sklearn.preprocessing import LabelEncoder
import utils
from scipy import stats
from scipy.stats import chisquare
import matplotlib.pyplot as plt  # doctest: +SKIP
from sklearn import datasets, metrics, model_selection, svm

def main():
    pass


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='modelisation running')
	parser.add_argument('mode', type=str, help='')
	args = parser.parse_args()
	mode  = args.mode.lower()

	MYDB = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	FEATURES_COLS = ['volume', 'numberOfTrades','var_ema', 'var_bollinger', 'var_stoch', 'rsi_indicator','stoch_indicator', 'RSI', 'ema_indicator', 'bollinger_indicator', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE','CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH','CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK','CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER','CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING','CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI','CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD','CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK','CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH','CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU','CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR','CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS','CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE','CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI','CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS']
	NAME_DICT = {0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:'12ema',81:'26ema',82:'upper_band',83:'lower_band',84:'%K',85:'%D', 86:"label"}
	SQL = "SELECT * FROM master_record_staging"
	df_staging = utils.create_dataframe(MYDB, SQL, NAME_DICT, FEATURES_COLS)
	SQL = "SELECT * FROM master_record"
	df_master = utils.create_dataframe(MYDB, SQL, NAME_DICT, FEATURES_COLS)
	continuous_columns = ['volume', 'numberOfTrades','var_ema', 'var_bollinger', 'var_stoch','RSI']
	categorical_columns = ['rsi_indicator','stoch_indicator', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE','CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH','CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK','CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER','CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING','CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI','CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD','CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK','CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH','CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU','CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR','CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS','CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE','CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI','CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS']
	model = RandomForestClassifier(n_estimators = 60, max_depth = 7,min_samples_leaf = 5)

	SAMPLE_SIZE = utils.generate_sample(df_staging,df_master)
	utils.check_distribution(SAMPLE_SIZE, df_staging, df_master, mode, model, continuous_columns, categorical_columns)
	

