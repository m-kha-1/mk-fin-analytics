import numpy as np
import pandas as pd




class Swing_low_high:
	def __init__(self,data):
		self.data=data
		
		print('\n creation swing low high: \n swing[0] : position candle swing low \n swing [1]: value swing low  \n swing[2] : position candle swing high \n swing [3]: value swing high'
			   )
	def swing_low_high_calc(self):
		
		
		c=self.data.shape[0]-4
		swing_low=np.array([])
		swing_low_x=np.array([])
		for i in range(0,c):
			
			if self.data.l[i+1]<self.data.l[i] and self.data.l[i+2]<self.data.l[i+1]:
			
				if self.data.l[i+2]<self.data.l[i+3] and self.data.l[i+3]<self.data.l[i+4]:
					swing_low=np.append(swing_low,self.data.l[i+2])
					swing_low_x=np.append(swing_low_x,[i+2])

		swing_low_x=swing_low_x.astype(int)

		swing_low=[]

		# for i in swing_low_x:
		# 	swing_low.append([self.data[i]]*5)




		swing_high=np.array([])
		swing_high_x=np.array([])
		for i in range(0,c):
			
			if self.data.l[i+1]>self.data.l[i] and self.data.l[i+2]>self.data.l[i+1]:
			
				if self.data.l[i+2]>self.data.l[i+3] and self.data.l[i+3]>self.data.l[i+4]:
					swing_high=np.append(swing_high,self.data.l[i+2])
					swing_high_x=np.append(swing_high_x,[i+2])

		swing_high_x=swing_high_x.astype(int)

		swing_high=[]

		# for i in swing_high_x:
		# 	swing_high.append([self.data[i]]*5)



		#return(swing_low,self.data[swing_low_x],swing_high,self.data[swing_high_x])

		return(swing_low_x,self.data.l[swing_low_x],swing_high_x,self.data.h[swing_high_x])