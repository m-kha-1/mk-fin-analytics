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
		
		line=pd.Series()
		line['%k']=(num/denom)*100
		line['%D'] = line['%k'].ewm(3).mean()

		
		return(line['%k'],line['%D'])




class Rsi:

	def __init__(self,dataframe,count,period):

		self.dataframe=dataframe
		self.count=count
		self.period=period

	def rsi_calculation(self):
		
		

		#gain loss

		data_gain=self.dataframe.c.diff()
		data_gain=data_gain.clip(lower=0)

		data_loss=self.dataframe.c.diff()
		data_loss=abs(data_loss.clip(upper=0))

		gain=data_gain.ewm(self.period).mean()

		loss=data_loss.ewm(self.period).mean()

		ratio=gain/loss


		#rsi

		rsi=100-(100/(1+ratio))
		rsi[0:self.period]=None


		#levels

		ob=[]
		overboughtx=list(range(0,self.count))
		overboughty=[70]*self.count
		ob.append(overboughtx)
		ob.append(overboughty)

		
		os=[]
		oversoldx=list(range(0,self.count))
		oversoldy=[30]*self.count
		os.append(oversoldx)
		os.append(oversoldy)


		ne=[]
		neutralx=list(range(0,self.count))
		neutraly=[50]*self.count
		ne.append(neutralx)
		ne.append(neutraly)


		return(rsi,os,ne,ob)


















		# o_s=[]
		# for n in range(self.count):
		# 	o_s.append(50)
		

		# oversold=list(range(self.count))
	
	
		
		# rsi=[]
		# for i in range(self.count):
				
		# 		if i-self.period<0:
		# 			rsi.append(None)
				
		# 		else:
		# 			average=[]
		# 			gain=[]
		# 			loss=[]
		# 			for i2 in range(self.period):	
		# 				if self.dataframe.c[i-i2]>self.dataframe.o[i-i2]:
		# 					add=abs(self.dataframe.c[i-i2]-self.dataframe.o[i-i2])
		# 					gain.append(add)
		# 				if self.dataframe.c[i-i2]<self.dataframe.o[i-i2]:
		# 					add=abs(self.dataframe.c[i-i2]-self.dataframe.o[i-i2])
		# 					loss.append(add)
		# 			try:	
		# 				average=(sum(gain)/self.period)/(sum(loss)/self.period)
		# 			except ZeroDivisionError as e:
		# 				average=1
		# 			rsi.append(100-(100/(1+average)))
		
		# rsi=pd.Series(rsi)
	
		
		#return(rsi,oversold,o_s)



class Candles_size:

	def __init__(self,dataframe,count,period):

			self.dataframe=dataframe
			self.count=count
			self.period=period
			print('\ncreation of Candles_size:')
			print('[0]:candles size mean \n'+'[1]: candles size data\n'+'[2]: candles size mean level\n' )


	def candles_size_calc(self):
			candles_size_global=[]
			
			for n in range(self.count):
				add_candles_size=abs(self.dataframe['c'][n]-self.dataframe['o'][n])
				candles_size_global.append(add_candles_size)

			candles_size_mean_value=statistics.mean(candles_size_global)

			candles_size_data=pd.Series(candles_size_global)

			candles_size=candles_size_data.rolling(self.period).mean()

			candles_size_max=max(candles_size_global)
			candles_size_min=min(candles_size_global)
			candles_size_20_thr=candles_size_min+((candles_size_max-candles_size_min)/5)

			candles_size_last_values=candles_size_data.tail(6)

			candles_size_mean=[]
			candles_size_mean1=list(range(self.count))
			candles_size_mean2=[candles_size_mean_value]*self.count
			candles_size_mean.append(candles_size_mean1)
			candles_size_mean.append(candles_size_mean2)

			return(candles_size_mean_value,candles_size,candles_size_mean)





class Atr_global:

		def __init__(self,dataframe,count,period):

			self.dataframe=dataframe
			self.count=count
			self.period=period
			print('\ncreation of ATR data:')
			print('[0]:atr data \n'+'[1]:last values(period)\n'+'[2]:atr minimun '+'[3]:atr maximum \n'+'[3]:atr 20% threshold \n' )

		

		def atr_calc(self):

			

			tr1=self.dataframe['h']-self.dataframe['l']
			tr2=abs(self.dataframe['h']-self.dataframe['c'].shift(1))
			tr3=abs(self.dataframe['l']-self.dataframe['c'].shift(1))

			tr=pd.concat([tr1,tr2,tr3],axis=1)
			tr=np.max(tr,axis=1)
			atr=tr.rolling(self.period).mean()
			atr_min=atr.min()
			atr_max=atr.max()
			threshold=atr_min+((atr_max-atr_min)/3)
			last_values=atr.tail(self.period)




			return(atr,last_values,atr_min,atr_max,threshold)










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



