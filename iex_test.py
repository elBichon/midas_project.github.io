from datetime import datetime
from iexfinance.stocks import get_historical_intraday
from iexfinance.stocks import Stock
import plotly.graph_objects as go
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
#import numpy as np
import itertools
# to not display the warnings of tensorflow
import credentials
import os
import utils
import time
from mpl_finance import candlestick_ohlc
from alpha_vantage.timeseries import TimeSeries
plt.style.use('ggplot')


x = []
y = []
x2 = []
y2 = []

if __name__ == "__main__":
	while True:
		df = get_historical_intraday("CSCO", output_format='pandas',token=credentials.token)
		df = df.fillna(method='ffill')
		df = df.reset_index()
		min_refresh = df.index

		fft_100_high = []
		fft_100_low = []
		fft_100_close = []
		fft_100_open = []
		fft_20_high = []
		fft_20_low = []
		fft_20_close = []
		fft_20_open = []
		df_close = df['close'].values.tolist()
		df_fft_close = utils.fourier_transform(df,'close',fft_20_close,fft_100_close)
		df_fft_low = utils.fourier_transform(df,'low',fft_20_low,fft_100_low)
		df_fft_open = utils.fourier_transform(df,'open',fft_20_open,fft_100_open)
		df_fft_open = utils.fourier_transform(df,'high',fft_20_high,fft_100_high)
		volume = df['volume'].values.tolist()

		fft_20_close = list(itertools.chain.from_iterable(fft_20_close))
		fft_20_high = list(itertools.chain.from_iterable(fft_20_high))
		fft_20_low = list(itertools.chain.from_iterable(fft_20_low))
		fft_20_open = list(itertools.chain.from_iterable(fft_20_open))
		fft_100_close = list(itertools.chain.from_iterable(fft_100_close))
		fft_100_high = list(itertools.chain.from_iterable(fft_100_high))
		fft_100_low = list(itertools.chain.from_iterable(fft_100_low))
		fft_100_open = list(itertools.chain.from_iterable(fft_100_open))
		df_dict = {'index': len(list(range(0,len(df)))), 'date':df.date.values.tolist(),'close':df_close,'fft_20_close':fft_20_close,'fft_20_low':fft_20_low,'fft_20_high':fft_20_high,'fft_20_open':fft_20_open,'fft_100_close':fft_100_close,'fft_100_high':fft_100_high,'fft_100_low':fft_100_low,'fft_100_open':fft_100_open,'volume':volume}
		df = pd.DataFrame(df_dict)
		df = df[['date','close','fft_20_close','fft_20_low','fft_20_high','fft_20_open','fft_100_close','fft_100_low','fft_100_high','fft_100_open','volume']]

		df['ma20'] = df['fft_20_close'].rolling(window=20).mean()
		df['ma50'] = df['fft_20_close'].rolling(window=50).mean()
		df['12ema'] = pd.ewma(df['fft_20_close'], span=12)
		df['26ema'] = pd.ewma(df['fft_20_close'], span=26)
		df['20sd'] = pd.stats.moments.rolling_std(df['fft_20_close'],20)
		df['ma21'] = df['fft_20_close'].rolling(window=21).mean()
		df['upper_band'] = df['ma21'] + (df['20sd']*2)
		df['lower_band'] = df['ma21'] - (df['20sd']*2)
		df['%K'] = utils.STOK(df['fft_20_close'], df['fft_20_low'], df['fft_20_high'], 14)
		df['%D'] = utils.STOD(df['fft_20_close'], df['fft_20_low'], df['fft_20_high'], 14)
		
		k_list = df['%K'].values.tolist()
		d_list = df['%D'].values.tolist()
		stoch_indicator = utils.stoch_indicator(k_list,d_list)

		upper_band = df['upper_band'].values.tolist()
		lower_band = df['lower_band'].values.tolist()
		fft_20_close = df.fft_20_close.values.tolist()
		bollinger_indicator = utils.bollinger_indicator(upper_band,lower_band,fft_20_close)
		
		df['RSI'] = utils.computeRSI(df['fft_20_close'], 14)
		rsi_list = df['RSI'].values.tolist()
		rsi_indicator = utils.rsi_indicator(rsi_list)
		
		ema_indicator = [0]
		ema_12 = df['12ema'].values.tolist()
		ema_26 = df['26ema'].values.tolist()
		index = df.index.values.tolist()
		ema_indicator = utils.ema_indicator(ema_12,ema_26,index,fft_20_close)


		df_dict = {'index':df.index.values.tolist(),'date_of_day':df.date.values.tolist(),'volume':volume,'close':df.close.values.tolist(),'fft_20_close': df.fft_20_close.values.tolist(),'fft_20_open': df.fft_20_open.values.tolist(),'fft_20_low': df.fft_20_low.values.tolist(),'fft_20_high': df.fft_20_high.values.tolist(),'fft_100_close': df.fft_100_close.values.tolist(),'fft_100_low': df.fft_100_low.values.tolist(),'fft_100_high': df.fft_100_high.values.tolist(),'fft_100_open': df.fft_100_open.values.tolist(),'fft_100_close': df.fft_100_close.values.tolist(),'fft_100_low': df.fft_100_low.values.tolist(),'fft_100_high': df.fft_100_high.values.tolist(),'fft_100_open': df.fft_100_open.values.tolist(),'rsi_indicator':rsi_indicator,'stoch_indicator':stoch_indicator,'%K':df['%K'].values.tolist(),'%D':df['%D'].values.tolist(),'RSI':rsi_list,
	'ma20':df['ma20'].values.tolist(),'ma50':df['ma50'].values.tolist(),'26ema':df['26ema'].values.tolist(),'12ema':df['12ema'].values.tolist(),'upper_band':df['upper_band'].values.tolist(),'lower_band':df['lower_band'].values.tolist(),'ema_indicator':ema_indicator,'bollinger_indicator':bollinger_indicator}
		df = pd.DataFrame(df_dict)
		df['var_ema'] = df['26ema'] - df['12ema']
		df['var_bollinger'] = df['upper_band'] - df['lower_band']
		print(df.head())

		rsi = df.rsi_indicator.values.tolist()
		stoch = df.stoch_indicator.values.tolist()
		index = df.index.values.tolist()
		fft_100_close = df.fft_100_close.values.tolist()


		fig = plt.figure(figsize = (20, 5))
		plt.title('stochastich chart')
		df.plot(y=['fft_100_close'])
		df.plot(y=['%K', '%D'], figsize = (20, 5))
		plt.axhline(0, linestyle='--', alpha=0.1)
		plt.axhline(20, linestyle='--', alpha=0.5)
		plt.axhline(30, linestyle='--')
		plt.axhline(70, linestyle='--')
		plt.axhline(80, linestyle='--', alpha=0.5)
		plt.axhline(100, linestyle='--', alpha=0.1)
		plt.savefig('stoch.png')

		fig = plt.figure(figsize = (20, 5))
		plt.figure(figsize=(20,5))
		plt.title('RSI chart')
		plt.plot(df['index'], df['RSI'])
		plt.axhline(0, linestyle='--', alpha=0.1)
		plt.axhline(20, linestyle='--', alpha=0.5)
		plt.axhline(30, linestyle='--')
		plt.axhline(70, linestyle='--')
		plt.axhline(80, linestyle='--', alpha=0.5)
		plt.axhline(100, linestyle='--', alpha=0.1)
		plt.savefig('rsi.png')
				
		fig = plt.figure(figsize = (20, 5))
		plt.figure(figsize=(20,5))
		plt.scatter(x,y, label='event', color='k', s=25, marker="o")
		plt.scatter(x2,y2, label='event', color='r', s=25, marker="o")
		plt.plot(df['index'],df['fft_100_close'],label='fft_100_close')
		plt.plot(df['index'],df['26ema'],label='moving average 26')
		plt.plot(df['index'],df['12ema'],label='moving average 12')
		plt.plot(df['index'],df['lower_band'],label='lower')
		plt.plot(df['index'],df['upper_band'],label='upper')
		plt.legend()
		plt.savefig('stock.png', dpi=fig.dpi)

		fig = plt.figure(figsize = (20, 5))
		plt.figure(figsize=(20,5))
		plt.scatter(x,y, label='event', color='k', s=25, marker="o")
		plt.plot(df['index'],df['fft_100_close'],label='fft_100_close')
		plt.plot(df['index'],df['fft_20_close'],label='fft_20_close')
		plt.plot(df['index'],df['ma20'],label='moving average 20')
		plt.plot(df['index'],df['ma50'],label='moving average 50')
		plt.legend()
		plt.savefig('stock20.png', dpi=fig.dpi)

		ohlc = df[['index', 'fft_100_open', 'fft_100_high', 'fft_100_low', 'fft_100_close']]
		fig = plt.figure(figsize=(20,5))
		fig, ax = plt.subplots()
		candlestick_ohlc(ax, ohlc.values, width=0.4,colorup='g', colordown='r');
		ax.set_xlabel('Date')
		ax.set_ylabel('Price')
		plt.savefig("ohlcnn.png")

		plt.close('all')
		time.sleep(60)
