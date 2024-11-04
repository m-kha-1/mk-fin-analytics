# import datetime 
# import os
# import shutil as sh


# class Directory_crea:
# 	def __init__(self,symbols,template):
		
# 		self.symbols=symbols
# 		self.template=template
		

		

# 	def crea(self):
		
# 		d=str(datetime.date.today())
		

# 		if self.template==1:

# 			if os.path.isdir(d+'/'+self.symbols[0])==True:
				
# 				sh.rmtree(d+'/'+self.symbols[0])


# 			if os.path.isdir(d)==False:
				
# 				os.mkdir(d)
			
# 			if os.path.isdir(d+'/'+self.symbols[0])==False:
				
# 				os.mkdir(d+'/'+self.symbols[0])
# 			return(d+'/'+self.symbols[0])

# 		if self.template==2:
			
# 			directory_lst=[]
			

# 			if os.path.isdir(d+'/'+self.symbols[0])==True:
				
# 				sh.rmtree(d+'/'+self.symbols[0])


# 			if os.path.isdir(d)==False:
				
# 				os.mkdir(d)
			
# 			if os.path.isdir(d+'/'+self.symbols[0])==False:
				
# 				os.mkdir(d+'/'+self.symbols[0])
			
# 			directory_lst=[]
# 			for s in self.symbols[1]:

# 				os.mkdir(d+'/'+self.symbols[0]+'/'+s)
# 				directory_lst.append(d+'/'+self.symbols[0]+'/'+s)
# 			return(directory_lst)
			




import datetime 
import time
import os
import shutil as sh


class Directory_crea:
	def __init__(self,symbols,template):
		
		self.symbols=symbols
		self.template=template
		

		

	def crea(self):
		
		# d=str(datetime.date.today())
		d=str(datetime.date.today())
		dtnow=datetime.datetime.now()
		h=str(dtnow.hour)
		t=time.time()
		d=d+"_"+str(h)+"h"
		

		if self.template==1:

			if os.path.isdir(d+'/'+self.symbols[0])==True:
				
				sh.rmtree(d+'/'+self.symbols[0])


			if os.path.isdir(d)==False:
				
				os.mkdir(d)
				print(d)
			
			if os.path.isdir(d+'/'+self.symbols[0])==False:
				
				os.mkdir(d+'/'+self.symbols[0])
			return(d+'/'+self.symbols[0])

		if self.template==2:
			
			directory_lst=[]
			

			if os.path.isdir(d+'/'+self.symbols[0])==True:
				
				sh.rmtree(d+'/'+self.symbols[0])


			if os.path.isdir(d)==False:
				
				os.mkdir(d)
				print(d)
			
			if os.path.isdir(d+'/'+self.symbols[0])==False:
				
				os.mkdir(d+'/'+self.symbols[0])
			
			directory_lst=[]
			for s in self.symbols[1]:

				os.mkdir(d+'/'+self.symbols[0]+'/'+s)
				directory_lst.append(d+'/'+self.symbols[0]+'/'+s)
			return(directory_lst)
		