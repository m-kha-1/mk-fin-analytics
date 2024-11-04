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





class High_low:
	def __init__(self,symbol,count,tf):
		self.symbol=symbol
		self.count=count
		self.tf=tf
		print('\ndaily high low :'+self.symbol)

	def high_low(self):
		
		params={"count": 2,"granularity":self.tf}
		api = oandapyV20.API(access_token=access_token,environment='practice')
		r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
		rv1=api.request(r)


		low=float(rv1['candles'][-2]['mid']['l'])
		high=float(rv1['candles'][-2]['mid']['h'])
		op=float(rv1['candles'][-2]['mid']['o'])
		cl=float(rv1['candles'][-2]['mid']['c'])


	

		ecart=high-low
		ecart_pourcentage=round(ecart/100,5)

		low_bande_h=low+(ecart_pourcentage*5)
		low_bande_l=low-(ecart_pourcentage*5)


		high_bande_h=high+(ecart_pourcentage*5)
		high_bande_l=high-(ecart_pourcentage*5)




		low_y=[low]*self.count
	
		high_y=[high]*self.count


		low_bande_h_y=[low_bande_h]*self.count

		low_bande_l_y=[low_bande_l]*self.count


		high_bande_h_y=[high_bande_h]*self.count

		high_bande_l_y=[high_bande_l]*self.count






		op_y=[op]*self.count
		
		cl_y=[cl]*self.count


		

		return(low_y,low_bande_l_y,low_bande_h_y,high_y,high_bande_l_y,high_bande_h_y)



