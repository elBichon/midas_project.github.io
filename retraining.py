from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
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
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelEncoder


def main():
    pass


if __name__ == "__main__":

	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	feature_cols = ['volume', 'numberOfTrades','var_ema', 'var_bollinger', 'var_stoch', 'rsi_indicator','stoch_indicator', 'RSI', 'ema_indicator', 'bollinger_indicator', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE','CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH','CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK','CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER','CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING','CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI','CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD','CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK','CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH','CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU','CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR','CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS','CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE','CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI','CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS']

	sql = "SELECT * FROM master_record_staging"
	table_rows = utils.execute_query(sql,mydb)
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:"label", 81:'12ema',82:'26ema',83:'upper_band',84:'lower_band',85:'%K',86:'%D'}
	df_staging = utils.get_data(mydb, sql, name_dict)
	df_staging = df_staging[feature_cols]
	utils.preprocess(df_staging)

	sql = "SELECT * FROM master_record"
	table_rows = utils.execute_query(sql,mydb)
	name_dict={0:"index", 1:"date_of_day" , 2:"hour" , 3:"name" , 4:"volume" , 5:"numberOfTrades" , 6:"var_ema" , 7:"var_bollinger" , 8:"var_stoch" , 9:"rsi_indicator" , 10:"stoch_indicator" , 11:"RSI" , 12:"ema_indicator" , 13:"bollinger_indicator" , 14:"fft_20_close" , 15:"fft_100_close" , 16:"fft_100_open" , 17:"fft_100_low" , 18:"fft_100_high", 19:"CDL2CROWS" , 20:"CDL3BLACKCROWS" , 21:"CDL3INSIDE" , 22:"CDL3LINESTRIKE" , 23:"CDL3OUTSIDE" , 24:"CDL3STARSINSOUTH" , 25:"CDL3WHITESOLDIERS" , 26:"CDLABANDONEDBABY" , 27:"CDLADVANCEBLOCK" , 28:"CDLBELTHOLD" , 29:"CDLBREAKAWAY" , 30:"CDLCLOSINGMARUBOZU" , 31:"CDLCONCEALBABYSWALL" , 32:"CDLCOUNTERATTACK" , 33:"CDLDARKCLOUDCOVER" , 34:"CDLDOJI" , 35:"CDLDOJISTAR" , 36:"CDLDRAGONFLYDOJI" , 37:"CDLENGULFING" , 38:"CDLEVENINGDOJISTAR" , 39:"CDLEVENINGSTAR" , 40:"CDLGAPSIDESIDEWHITE" , 41:"CDLGRAVESTONEDOJI" , 42:"CDLHAMMER" , 43:"CDLHANGINGMAN" , 44:"CDLHARAMI" , 45:"CDLHARAMICROSS" , 46:"CDLHIGHWAVE" , 47:"CDLHIKKAKE" , 48:"CDLHIKKAKEMOD" , 49:"CDLHOMINGPIGEON" , 50:"CDLIDENTICAL3CROWS" , 51:"CDLINNECK" , 52:"CDLINVERTEDHAMMER" , 53:"CDLKICKING" , 54:"CDLKICKINGBYLENGTH" , 55:"CDLLADDERBOTTOM" , 56:"CDLLONGLEGGEDDOJI" , 57:"CDLLONGLINE" , 58:"CDLMARUBOZU" , 59:"CDLMATCHINGLOW" , 60:"CDLMATHOLD" , 61:"CDLMORNINGDOJISTAR" , 62:"CDLMORNINGSTAR" , 63:"CDLONNECK" , 64:"CDLPIERCING" , 65:"CDLRICKSHAWMAN" , 66:"CDLRISEFALL3METHODS" , 67:"CDLSEPARATINGLINES" , 68:"CDLSHOOTINGSTAR" , 69:"CDLSHORTLINE" , 70:"CDLSPINNINGTOP" , 71:"CDLSTALLEDPATTERN" , 72:"CDLSTICKSANDWICH" , 73:"CDLTAKURI" , 74:"CDLTASUKIGAP" , 75:"CDLTHRUSTING" , 76:"CDLTRISTAR" , 77:"CDLUNIQUE3RIVER" , 78:"CDLUPSIDEGAP2CROWS" , 79:"CDLXSIDEGAP3METHODS", 80:"label", 81:'12ema',82:'26ema',83:'upper_band',84:'lower_band',85:'%K',86:'%D'}
	df_master = utils.get_data(mydb, sql, name_dict)
	df_master = df_master[feature_cols]
	utils.preprocess(df_master)

	for col in df_master.columns:
		ks = stats.ks_2samp(df_staging[col], df_master[col])
		if ks.pvalue < 0.05 and ks.statistic>0.1:
			print(f'{col}: {ks}')

	SAMPLE_SIZE = min(len(df_staging),len(df_master))
	SAMPLE_SIZE = min(SAMPLE_SIZE,10000)
	print(SAMPLE_SIZE)

	training_sample = df_staging.sample(SAMPLE_SIZE, random_state=49)
	testing_sample = df_master.sample(SAMPLE_SIZE, random_state=48)

	# Is the data from the training set?
	training_sample['source_training'] = 1
	testing_sample['source_training'] = 0

	# Build combined training set
	combined = testing_sample.append(training_sample)
	combined.reset_index(inplace=True, drop=True)

	# Now randomize
	combined = combined.reindex(np.random.permutation(combined.index))
	combined.reset_index(inplace=True, drop=True)

	# Get ready to train
	y = combined['source_training'].values
	combined.drop('source_training',axis=1,inplace=True)
	x = combined.values

	model = RandomForestClassifier(n_estimators = 60, max_depth = 7,min_samples_leaf = 5)
	lst = []

	for i in combined.columns:
	    score = cross_val_score(model,pd.DataFrame(combined[i]),y,cv=2,scoring='roc_auc')
	    if (np.mean(score) > 0.75):
	        lst.append(i)
	        print(i,np.mean(score))
	print(lst)



