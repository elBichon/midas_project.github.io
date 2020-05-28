import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import recall_score
import pickle

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
	table_rows = utils.extract_data(sql,mydb)
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:"label"}
	df = utils.get_data(mydb, sql, name_dict)
	df = df[['volume', 'numberOfTrades','var_ema', 'var_bollinger', 'var_stoch', 'rsi_indicator','stoch_indicator', 'RSI', 'ema_indicator', 'bollinger_indicator','CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE','CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH','CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK','CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER','CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING','CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI','CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD','CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK','CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH','CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU','CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR','CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS','CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE','CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI','CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'label']]
	print(df.head())

	#drop column label
	#standardize the data
	#train a random forest/decision tree
	#cross validation
	#save model as a pickle
	#report on performances of the model 
	#report of the structure of the model

	param_grid = { 
    'n_estimators': [100, 200, 300, 400, 500, 700, 800, 1000],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8, 10, 15, 20, 50, 100],
    'criterion' :['gini', 'entropy']}
	sql = "SELECT * FROM master_record_staging"
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:"label"}
	scoring = ['precision_macro', 'recall_macro']
	feature_cols = ['volume', 'numberOfTrades','var_ema', 'var_bollinger', 'var_stoch', 'rsi_indicator','stoch_indicator', 'RSI', 'ema_indicator', 'bollinger_indicator', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE','CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH','CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK','CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER','CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING','CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI','CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD','CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK','CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH','CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU','CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR','CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS','CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE','CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI','CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS']
	filename = 'model.sav'

	df = utils.get_data(mydb, sql, name_dict)
	train_data_features = df[feature_cols] 
	y = df.label 
    
	forest = RandomForestClassifier(random_state=42)
	forest = GridSearchCV(estimator=forest, param_grid=param_grid, cv= 5)
	forest = forest.fit(train_data_features, y)
	print(forest.best_params_)
	params = forest.best_params_
	forest = RandomForestClassifier(random_state=42, max_features=str(params.get('max_features')), n_estimators= int(params.get('n_estimators')), max_depth=int(params.get('max_depth')), criterion=str(params.get('criterion')))
	forest.fit(train_data_features, y)

	pickle.dump(forest, open(filename, 'wb'))
	print('saving model as: '+filename)
	scores = cross_val_score(forest, train_data_features, y, cv=5)
	print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
	scores = cross_validate(forest, train_data_features, y, scoring=scoring)
	scores_list = (sorted(scores.keys()))
	for score in scores_list:
		print(score)
		print(scores[score])
