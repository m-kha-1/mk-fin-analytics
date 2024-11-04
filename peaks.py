import pandas as pd
import numpy as np

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


class Peaks:

	def __init__(self,dataframe,instrument):
		self.dataframe=dataframe
		self.instrument=instrument
		print('\n####\ncreation of peaks-high and valleys-low:')
		print('\nhigh[0][0] : [peaks candles indexes] \nhigh[0][1] : [peaks candles values]\n')
		print('\nlow[1][0] : [valleys candles indexes] \nlow[1][1] : [valleys candles values]\n')
		
		#current price 
		params={"count": 1,"granularity": 'S10'}
		api = oandapyV20.API(access_token=access_token,environment='practice')
		r = instruments.InstrumentsCandles(instrument=self.instrument, params=params)
		rv1=api.request(r)
		self.cp=float(rv1['candles'][0]['mid']['c'])
		

	def peaks_calculation(self):

		#print(self.cp)
		data=np.array(self.dataframe)
		



		data_dif=np.diff(data)

		
		data_dif_sign=np.sign(data_dif)


		data_dif_sign=np.diff(data_dif_sign)
		
		

		#high
		data_dif_HIGH=np.nonzero(data_dif_sign<0)[0]+1


		data_dif_HIGH_list=np.array([]).astype(int)

		for e in data_dif_HIGH:
		 	
		 	data_dif_HIGH_list=np.append(data_dif_HIGH,e)
		
		self.high=[data_dif_HIGH_list,data[data_dif_HIGH_list]]

		#low
		data_dif_LOW=np.nonzero(data_dif_sign>0)[0]+1


		data_dif_LOW_list=np.array([]).astype(int)


		for e in data_dif_LOW:
		 	
		 	data_dif_LOW_list=np.append(data_dif_LOW,e)
	

		self.low=[data_dif_LOW_list,data[data_dif_LOW_list]]
		
		
		

		self.last_points()
		return(self.high,self.low,self.fib,self.last_swing)


	def last_points(self):
		print('ouh')
		self.h3=self.high[1][-2]
		self.h2=self.high[1][-3]

		self.l3=self.low[1][-2]
		self.l2=self.low[1][-3]
		
		# if self.h3-self.h2 >0 and self.l3-self.l2>0:
		# 	print('yes')
		self.last_swing=''
		if self.low[0][-2] > self.high[0][-2]:
			self.last_swing='low'
		if self.high[0][-2] > self.low[0][-2]:
			self.last_swing='high'
	
	
		#operations

		if self.last_swing=='low':
			a=self.high[1][-2]
			b=self.low[1][-2]
			d=a-b
			ecart=self.cp-b
			self.fib=(ecart/d)*100
			# print(a)
			# print(b)
			# print(self.cp)
			# print(d)
			# print(ecart)

		
		if self.last_swing=='high':

			a=self.high[1][-2]
			b=self.low[1][-2]
			d=a-b
			ecart=a-self.cp
			self.fib=(ecart/d)*100
			# print(a)
			# print(b)
			# print(self.cp)
			# print(d)
			# print(ecart)

			# return(self.fib)


		# if last_swing=='high':
		# 	self.high[1][-2]-self.low[1][-2]



		


		

