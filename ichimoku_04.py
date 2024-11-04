import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.orders as orders
import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc

from dotenv import load_dotenv
import os

load_dotenv()
access_token=os.getenv("access_token")
accountID=os.getenv("accountID")


dt=str(datetime.datetime.now().isoformat(' ', 'minutes'))

API=oandapyV20.API(access_token=access_token,environment='practice')



class Ichimoku():
	def __init__(self,timeframe,cat,data_ohlc):
		self.timeframe=timeframe
		self.cat=cat
		self.data_ohlc=data_ohlc

	# def directories_creation(self):
	# 	if os.path.isdir('ichimoku_'+self.timeframe)==False:
	# 		os.mkdir('ichimoku_'+self.timeframe)

	# 	if os.path.isdir('ichimoku_'+self.timeframe+'/GRAPHS')==False:
	# 		os.mkdir('ichimoku_'+self.timeframe+'/GRAPHS')

	# 	if os.path.isdir('ichimoku_'+self.timeframe+'/GRAPHS/'+self.cat)==False:
	# 		os.mkdir('ichimoku_'+self.timeframe+'/GRAPHS/'+self.cat)

	def ichimoku_lines(self):

		#request onada api
		

		# params={'granularity':self.timeframe,'count':len(self.data_ohlc)}
		# r=instruments.InstrumentsCandles(instrument=self.instrument,params=params)
		# rv=API.request(r)


		#dataset candles

		open_data=[]
		close_data=[]
		high_data=[]
		low_data=[]
		full_range=[]
		for n in range(0,26):

			open_data.append(None)
			
			high_data.append(None)

			low_data.append(None)

			close_data.append(None)

		for n in range(0,len(self.data_ohlc)):

			open_data.append(float(self.data_ohlc[n][0]))
			
			high_data.append(float(self.data_ohlc[n][1]))

			low_data.append(float(self.data_ohlc[n][2]))

			close_data.append(float(self.data_ohlc[n][3]))

		for n in range(0,26):

			open_data.append(None)
			
			high_data.append(None)

			low_data.append(None)

			close_data.append(None)
		for n in range(len(self.data_ohlc)+52):
			full_range.append(n)
		
		

		#creation series ohlc	


		self.open=pd.Series(open_data)
		self.high=pd.Series(high_data)
		self.low=pd.Series(low_data)
		self.close=pd.Series(close_data)
		self.s5=pd.Series(full_range)
		# print(close)
		
		
		# lows and highs over 9 26 52 periods
		#l low
		#h high

		self.l9=self.low.rolling(9).min()
		self.h9=self.high.rolling(9).max()
		
		self.l26=self.low.rolling(26).min()
		self.h26=self.high.rolling(26).max()

		self.l52=self.low.rolling(52).min()
		self.h52=self.high.rolling(52).max()


		#lists creation for Ichimoku lines

		self.CL=[]
		self.BL=[]
		self.SPANA=[]
		self.SPANB=[]
		self.laggingspan=[]
		c52=[]

		

		self.CL=(self.l9+self.h9)/2
		self.BL=(self.l26+self.h26)/2
		self.SPANA=(self.CL+self.BL)/2
		self.SPANB=(self.h52+self.l52)/2
		
		trans_a=[]
		for i in range(52):
			trans_a.append(None)
		for i in range(0,len(self.data_ohlc)+26):
			
			trans_a.append(self.SPANA[i+26])
		self.SPANA=pd.Series(trans_a)
		trans_b=[]
		for i in range(52):
			trans_b.append(None)
		for i in range(0,len(self.data_ohlc)+26):
			trans_b.append(self.SPANB[i+26])

		self.SPANB=pd.Series(trans_b)
		
		trans_lag=[]
		for i in range(26,len(self.data_ohlc)+26):
			trans_lag.append(self.close[i])
		for i in range(len(self.data_ohlc),len(self.data_ohlc)+51):
			trans_lag.append(None)

		self.laggingspan=pd.Series(trans_lag)
		
		# print(self.df['Close'][155:156])
		# print(self.df['Close'][155])
		a=self.close[155]
		b=self.SPANA[155]
		c=self.SPANB[155]
		d=self.close[129]
		e=self.laggingspan[129]
		txt1='[0]=SPANA\n[1]=SPANB\n[2]=Conversion Line\n[3]=Base Line\n[4]=Lagging Span\n[6]=number of candles + 78\n' 
		txt2='[7]=current CL value\n[8]=current BL value\n[9]=SPANA\n[10]=SPANB\n'  
		print(txt1)
		print(txt2)
		return (self.SPANA,self.SPANB,self.CL,self.BL,self.laggingspan,self.close,len(self.data_ohlc)+78,self.CL[len(self.data_ohlc)],self.BL[len(self.data_ohlc)],self.SPANA[len(self.data_ohlc)],self.SPANB[len(self.data_ohlc)])


	# def display(self):
	# 	# plt.figure(figsize=(20,14))
	# 	# #plt.style.use('fivethirtyeight')
	# 	# # ax1=plt.subplot2grid((1,1),(0,0))
	# 	# # ax1.plot(self.SPANA,c='black',lw=0.8)
	# 	# # ax1.plot(self.SPANB,c='g',lw=0.8)
	# 	# # ax1.plot(self.CL,c='pink',lw=0.8)
	# 	# # ax1.plot(self.BL,c='magenta',lw=0.8)
	# 	# # ax1.plot(self.laggingspan,c='r',lw=0.8)
	# 	# # ax1.plot(self.close,lw=1.8)

	# 	# # ax1.fill_between(range(len(self.data_ohlc)+78),self.SPANA,self.SPANB)
		
	# 	# plt.show()







# tf_simi(['EUR_USD','EUR_CAD','EUR_CHF','EUR_JPY','EUR_AUD','EUR_GBP',\
# 	 'USD_CAD','USD_CHF','USD_JPY','AUD_USD','AUD_CAD','AUD_JPY','AUD_CHF','AUD_NZD','GBP_NZD',\
# 	 'GBP_CHF','GBP_CAD','GBP_USD','GBP_JPY','GBP_AUD',\
# 	 'NZD_JPY','NZD_CHF','CHF_JPY','CAD_JPY','CAD_CHF'],'FOREX_MAIN')




# # tf_simi(['EUR_DKK','EUR_HKD','EUR_CZK','EUR_HKD','EUR_NOK','EUR_PLN','EUR_HUF','EUR_SEK','EUR_SGD',\
# # 	'EUR_TRY','USD_DKK','USD_HKD','USD_CZK','USD_HKD','USD_NOK','USD_PLN','USD_HUF','USD_SEK','USD_SGD','USD_TRY','GBP_HKD','GBP_SGD','USD_CNH'],'FOREX_SEC1')
# # tf_simi(['GBP_HKD','GBP_SGD'],'FOREX_SEC2')

# tf_simi(['FR40_EUR','DE30_EUR','NL25_EUR','UK100_GBP','EU50_EUR','US30_USD','NAS100_USD','SPX500_USD','US2000_USD',\
# 	'HK33_HKD','SG30_SGD','JP225_USD','AU200_AUD','IN50_USD','TWIX_USD','CN50_USD'],'INDICES_MAIN')

# tf_simi(['EUR_USD','USD_JPY','GBP_USD','US30_USD','NAS100_USD','SPX500_USD','XAU_USD'],'SELECTION1')

# tf_simi(['BCO_USD','WTICO_USD','NATGAS_USD','CORN_USD','SOYBN_USD','WHEAT_USD','SUGAR_USD','XCU_USD'],'COMMODITIES_MAIN')

# tf_simi(['XAU_USD','XAG_USD'],'METALS_MAIN')



# tf_simi(['BCO_USD','WTICO_USD','NATGAS_USD','CORN_USD','SOYBN_USD','WHEAT_USD','SUGAR_USD','XCU_USD'],'COMMODITIES_MAIN')
# tf_simi(['XPT_USD','XPD_USD'],'METALS_SEC')
# tf_simi(['UK10YB_GBP','DE10YB_EUR','USB30Y_USD','USB10Y_USD','USB05Y_USD','USB02Y_USD'],'BUND')

# a=Ichimoku('EUR_USD','D','INDICES_MAIN')
# a.directories_creation()
# y=a.ichimoku_lines()
# a.display()
# print(y)
# print(y[0])