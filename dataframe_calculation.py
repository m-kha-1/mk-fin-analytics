import pandas as pd



class Dataframe_calc:
	def __init__(self,data):
		self.data=data

		 	
	def bollinger_band(self,period):
		
		try:
	 		std=self.data['c'].rolling(period).std()
	 		print('\n'+str(period)+' creation of bollinger band ')
	 		
	 		ema=self.data['c'].rolling(period).mean()
	 		b1=ema+std*2
	 		b2=ema-std*2
	 		#ema.plot()
	 		

	 		return(ema,b1,b2)
		
		except NameError as e :
			print('no data')

	

	def sma(self,period):
		
		try:
			sma=self.data['c'].rolling(period).mean()
			print('\ncreation of ' +str(period)+' sma  ')
			
			return(sma)
	
		except NameError as e :
			print('no data')



	def ema(self,period):
		
		try:
			sma=self.data['c'].ewm(period).mean()
			print('\ncreation of ' +str(period)+' ema  ')
			
			return(sma)
	
		except NameError as e :
			print('no data')