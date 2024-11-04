import candles_data_creation
import dataframe_calculation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from mpl_finance import candlestick_ohlc

import os
import sys





class Stochastic:
	
	def __init__(self,dataframe,count,period):
		
		self.dataframe=dataframe
		self.count=count
		self.period=period
	
	def sto_calculation(self):
	

		maxa=self.dataframe.h.rolling(self.period).max()
		mina=self.dataframe.l.rolling(self.period).min()
		
		denom=maxa-mina

		num=self.dataframe.c-mina
		self.dataframe['%k']=(num/denom)*100
		self.dataframe['%D'] = self.dataframe['%k'].rolling(3).mean()

		# self.dataframe['%k'].plot()
		# self.dataframe['%D'].plot()

		plt.legend()
		
		

		
		
		return(self.dataframe['%k'],self.dataframe['%D'])




class Rsi:

	def __init__(self,dataframe,count,period):

		self.dataframe=dataframe
		self.count=count
		self.period=period

	def rsi_calculation(self):
		
		o_s=[]
		for n in range(self.count):
			o_s.append(50)
		

		oversold=list(range(self.count))
	
	
		
		rsi=[]
		for i in range(self.count):
				
				if i-self.period<0:
					rsi.append(None)
				
				else:
					average=[]
					gain=[]
					loss=[]
					for i2 in range(self.period):	
						if self.dataframe.c[i-i2]>self.dataframe.o[i-i2]:
							add=abs(self.dataframe.c[i-i2]-self.dataframe.o[i-i2])
							gain.append(add)
						if self.dataframe.c[i-i2]<self.dataframe.o[i-i2]:
							add=abs(self.dataframe.c[i-i2]-self.dataframe.o[i-i2])
							loss.append(add)
					try:	
						average=(sum(gain)/self.period)/(sum(loss)/self.period)
					except ZeroDivisionError as e:
						average=1
					rsi.append(100-(100/(1+average)))
		
		rsi=pd.Series(rsi)
	
		
		return(rsi,oversold,o_s)



 
class Atr_global:

		def __init__(self,dataframe,count,period):

			self.dataframe=dataframe
			self.count=count
			self.period=period

		def atr_glo_calculation(self):

			atr_global=[]
			
			for n in range(self.count):
				add_atr=abs(self.dataframe['c'][n]-self.dataframe['o'][n])
				atr_global.append(add_atr)

			atr_global=statistics.mean(atr_global)

			return(atr_global)










		# for n in range(self.period,self.count):

			# loss_gain=[]
			# for n2 in range(self.period):
			# 	add=abs(self.dataframe.c[n-n2]-self.dataframe.o[n-n2])
			# 	loss_gain.append(add)
			# lg_average=sum(loss_gain)/(self.period)

			# seri=[]
			# a=100-(100/(1+lg_average))
			# seri.append(a)
			# seri=pd.Series(seri)

			# seri.plot()
			# plt.show()



