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



class Pivot:
	
	def __init__(self,symbol,count,tf):
		
		self.symbol=symbol
		self.count=count
		self.tf=tf


	def pivot_calculation(self):
		params={"count": 2,"granularity":self.tf}
		api = oandapyV20.API(access_token=access_token,environment='practice')
		r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
		rv1=api.request(r)


		low=float(rv1['candles'][-2]['mid']['l'])
		high=float(rv1['candles'][-2]['mid']['h'])
		op=float(rv1['candles'][-2]['mid']['o'])
		cl=float(rv1['candles'][-2]['mid']['c'])


		pp=(low+high+cl)/3
		ppx=list(range(self.count))
		ppy=[pp]*self.count



		s1=(pp*2)-high
		s1x=list(range(self.count))
		s1y=[s1]*self.count


		s2=pp-(high-low)
		s2x=list(range(self.count))
		s2y=[s2]*self.count
		
		s3=low-2*(high-pp)
		s3x=list(range(self.count))
		s3y=[s3]*self.count


		r1=(pp*2)-low
		r1x=list(range(self.count))
		r1y=[r1]*self.count

		r2=pp+(high-low)
		r2x=list(range(self.count))
		r2y=[r2]*self.count

		r3=high+2*(pp-low)
		r3=pp+(high-low)
		r3x=list(range(self.count))
		r3y=[r3]*self.count

		
		# return(ppx,ppy,s1x,s1y,s2x,s2y,s3x,s3y,r1x,r1y,r2x,r2y,r3x,r3y)

		return(ppy,s1y,s2y,s3y,r1y,r2y,r3y)
		




	