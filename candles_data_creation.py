
import pandas as pd

import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.orders as orders 
import oandapyV20.endpoints.pricing as pricing

from mpl_finance import candlestick_ohlc


from dotenv import load_dotenv
import os

load_dotenv()
access_token=os.getenv("access_token")
accountID=os.getenv("accountID")


class Candles_data_crea:
	def __init__(self,symbol,granularity,count):
		
		self.symbol=symbol
		self.granularity=granularity
		self.count=count

	def request(self):
			
			params={"count": self.count,"granularity": self.granularity}
			api = oandapyV20.API(access_token=access_token,environment='practice')
			r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
			self.rv1=api.request(r)
			print( "\n")
			print('make a request for '+self.symbol+' on '+self.granularity+' / number of candles: '+str(self.count))
			
	def data_crea(self):
			
			candlestick_ohlc=[]
			candle_status=['o','h','l','c']
			for n in range(self.count):
				candles_add=[]
				for s in candle_status:
					candles_add.append(self.rv1['candles'][n]['mid'][s])
				candlestick_ohlc.append(candles_add)

			self.data=pd.DataFrame(candlestick_ohlc,columns=['o','h','l','c']) 
			self.data=self.data.apply(pd.to_numeric)
			print('\ncreation of data frame for'+' '+ self.symbol+' '+self.granularity)
			
			return(self.data)
	

	def ohlc_crea(self,ax):

			candlestick_ohlc=[]
			candle_status=['o','h','l','c']
			for n in range(self.count):
				candles_add=[]
				candles_add.append(n)
				
				for s in candle_status:
					candles_add.append(float(self.rv1['candles'][n]['mid'][s]))
				candlestick_ohlc.append(candles_add)
				# print(candlestick_ohlc)
				#candlestick_ohlc(ax,candlestick_ohlc,width=0.75,colorup='#999999',colordown='black')


			
			return(candlestick_ohlc)
	

