import pandas as pd
import itertools
import utils
import credentials 
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


	sql = "SELECT * FROM fourier_processed_stock"
	name_dict = {0:'index', 1:'date_of_day', 2:'hour', 3:'numberOfTrades', 4:'name', 5:'volume', 6:'fft_20_close', 7:'fft_20_open', 8:'fft_20_low', 9:'fft_20_high', 10:'fft_100_close', 11:'fft_100_open', 12:'fft_100_low', 13:'fft_100_high'}
	df = utils.get_data(mydb, sql, name_dict)
	
	index = df.index.values.tolist()
	date_of_day = df.date_of_day.values.tolist()
	volume = df.volume.values.tolist()
	name = df.name.values.tolist()
	hour = df.hour.values.tolist()
	numberOfTrades = df.numberOfTrades.values.tolist()

	df = utils.get_technical_indicators(df)
	fft_20_close = df.fft_20_close.values.tolist()
	fft_100_close = df.fft_100_close.values.tolist()
	fft_100_low = df.fft_100_low.values.tolist()
	fft_100_open = df.fft_100_open.values.tolist()
	fft_100_high = df.fft_100_high.values.tolist()

	stoch_indicator = utils.stoch_indicator(df['%K'].values.tolist(),df['%D'].values.tolist())
	bollinger_indicator = utils.bollinger_indicator(df['upper_band'].values.tolist(),df['lower_band'].values.tolist(),fft_20_close)
	df['RSI'] = utils.computeRSI(df['fft_20_close'], 14)
	rsi_list = df['RSI'].values.tolist()
	rsi_indicator = utils.rsi_indicator(df['RSI'].values.tolist())
	ema_indicator = utils.ema_indicator(df['12ema'].values.tolist(),df['26ema'].values.tolist(),df.index.values.tolist(),fft_20_close)
	df_dict = {'var_stoch':df.var_stoch.values.tolist(), 'rsi_indicator':rsi_indicator,'stoch_indicator':stoch_indicator,'rsi':df['RSI'].values.tolist(),'ma20':df['ma20'].values.tolist(),'ma50':df['ma50'].values.tolist(),'26ema':df['26ema'].values.tolist(),'12ema':df['12ema'].values.tolist(),'upper_band':df['upper_band'].values.tolist(),'lower_band':df['lower_band'].values.tolist(),'ema_indicator':ema_indicator,'bollinger_indicator':bollinger_indicator,'var_ema':df.var_ema.values.tolist(),'var_bollinger':df.var_bollinger.values.tolist(),'%K':df['%K'].values.tolist(),'%D':df['%D'].values.tolist()}
	df = pd.DataFrame(df_dict)
	rsi = df.rsi_indicator.values.tolist()
	stoch = df.stoch_indicator.values.tolist()
	bollinger = df.bollinger_indicator.values.tolist()
	ema_12 = df['12ema'].values.tolist()
	ema_26 = df['26ema'].values.tolist()
	upper_list = df['upper_band'].values.tolist()
	lower_list = df['lower_band'].values.tolist()
	K_value = df['%K'].values.tolist()
	D_value = df['%D'].values.tolist()

	index = df.index.values.tolist()
	df_dict = {'var_ema':df['var_ema'].values.tolist(), 'var_bollinger':df.var_bollinger.values.tolist(), 'rsi_indicator':rsi_indicator, 'stoch_indicator':stoch_indicator, 'var_stoch': df['var_stoch'].values.tolist(), 'RSI':rsi_list,'ema_indicator':ema_indicator,'bollinger_indicator':bollinger_indicator,'fft_20_close': fft_20_close,'fft_100_close': fft_100_close,'fft_100_open': fft_100_open,'fft_100_low': fft_100_low,'fft_100_high':fft_100_high , 'ema_12': ema_12,'ema_26': ema_26,'upper_list': upper_list,'lower_list':lower_list , 'K_value': K_value, 'D_value':D_value}
	df = pd.DataFrame(df_dict)
	df = df.fillna(-100)
	var_ema = df.var_ema.values.tolist() 
	var_bollinger = df.var_bollinger.values.tolist()
	var_stoch = df.var_stoch.values.tolist() 
	rsi_indicator = df.rsi_indicator.values.tolist() 
	stoch_indicator = df.stoch_indicator.values.tolist() 
	RSI = df.RSI.values.tolist()
	ema_indicator = df.ema_indicator.values.tolist() 
	bollinger_indicator = df.bollinger_indicator.values.tolist()
	ema_12 = df['ema_12'].values.tolist()
	ema_26 = df['ema_26'].values.tolist()
	upper_list = df['upper_list'].values.tolist()
	lower_list = df['lower_list'].values.tolist()
	K_value = df['K_value'].values.tolist()
	D_value = df['D_value'].values.tolist()

	sql = "INSERT INTO processed_stock (date_of_day, hour, name, volume, numberOfTrades, var_ema, var_bollinger, var_stoch, rsi_indicator, stoch_indicator, RSI, ema_indicator, bollinger_indicator,fft_20_close,fft_100_close,fft_100_open,fft_100_low,fft_100_high, ema_12, ema_26, upper_list, lower_list, K_value, D_value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	i = 0
	while i < len(index):
		print(str(i)+'/'+str(len(index)))
		val = (date_of_day[i], hour[i], name[i], volume[i], numberOfTrades[i], var_ema[i], var_bollinger[i], var_stoch[i], rsi_indicator[i], stoch_indicator[i], RSI[i], ema_indicator[i], bollinger_indicator[i],fft_20_close[i],fft_100_close[i],fft_100_open[i],fft_100_low[i],fft_100_high[i], ema_12[i], ema_26[i], upper_list[i], lower_list[i], K_value[i], D_value[i])
		utils.insert_multiple_into_db(mydb, sql,val)
		i += 1