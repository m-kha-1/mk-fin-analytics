import numpy as np
import pandas as pd

import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.orders as orders 
import oandapyV20.endpoints.pricing as pricing

from dotenv import load_dotenv
import os

load_dotenv()
access_token=os.getenv("access_token")
accountID=os.getenv("accountID")




class SR:
	def __init__(self,symbol,count,tf):
		self.symbol=symbol
		self.tf=tf
		self.count=count
		print('')

	def sr(self):
		
		self.request()
		self.dataframe_creation(self.rv1)
		

		c=self.data.shape[0]-4
		swing_low=np.array([])
		swing_low_x=np.array([])
		swing_low1=[]

		for i in range(0,c):
			
			if self.data.l[i+1]<self.data.l[i] and self.data.l[i+2]<self.data.l[i+1]:
			
				if self.data.l[i+2]<self.data.l[i+3] and self.data.l[i+3]<self.data.l[i+4]:
					# swing_low=np.append(swing_low,self.data.l[i+2])
					# swing_low_x=np.append(swing_low_x,[i+2])
					swing_low1.append(self.data.l[i+2])

		

	
		swing_high1=[]

		for i in range(0,c):
			
			if self.data.l[i+1]>self.data.l[i] and self.data.l[i+2]>self.data.l[i+1]:
			
				if self.data.l[i+2]>self.data.l[i+3] and self.data.l[i+3]>self.data.l[i+4]:
					# swing_high=np.append(swing_high,self.data.l[i+2])
					# swing_high_x=np.append(swing_high_x,[i+2])
					swing_high1.append(self.data.h[i+2])

	

	


	

		return(swing_low1,swing_high1)


	def request(self):
		params={"count": self.count,"granularity": self.tf}
		api = oandapyV20.API(access_token=access_token,environment='practice')
		r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
		self.rv1=api.request(r)
		return(self.rv1)


	def dataframe_creation(self,rq):
		candlestick_ohlc=[]
		candle_status=['o','h','l','c']
		for n in range(self.count):
			candles_add=[]
			for s in candle_status:
				candles_add.append(rq['candles'][n]['mid'][s])
			candlestick_ohlc.append(candles_add)

		self.data=pd.DataFrame(candlestick_ohlc,columns=['o','h','l','c']) 
		self.data=self.data.apply(pd.to_numeric)
		print('\ncreation of data frame for'+' '+ self.symbol+' '+self.tf)
		
		return(self.data)




