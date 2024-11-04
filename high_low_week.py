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





class High_low_week:
	def __init__(self,symbol,count):
		self.symbol=symbol
		self.count=count
		print('\nweekly high low :'+self.symbol)

	def high_low(self):
		
		params={"count": 2,"granularity":'W'}
		api = oandapyV20.API(access_token=access_token,environment='practice')
		r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
		rv1=api.request(r)


		low=float(rv1['candles'][-2]['mid']['l'])
		high=float(rv1['candles'][-2]['mid']['h'])
		op=float(rv1['candles'][-2]['mid']['o'])
		cl=float(rv1['candles'][-2]['mid']['c'])


		low_x=list(range(self.count))
		low_y=[]
		for n in range(self.count):
			low_y.append(low)

		high_x=list(range(self.count))
		high_y=[]
		for n in range(self.count):
			high_y.append(high)

		op_x=list(range(self.count))
		op_y=[]
		for n in range(self.count):
			op_y.append(op)
		
		cl_x=list(range(self.count))
		cl_y=[]
		for n in range(self.count):
			cl_y.append(cl)

		return(low_x,low_y,high_x,high_y,op_x,op_y,cl_x,cl_y)




# o=High_low_day('EUR_USD',4)
# val=o.high_low()
