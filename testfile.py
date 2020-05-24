##testfile for notes 


import pandas


# A dataset: OkCupid
#https://github.com/rudeboybert/JSE_OkCupid


# Some other notes for Pandas:
df.info()

row, col = df.shape


#Use the date as index instead of numbers?
df.set_index('date', inplace=True)	#Note: date could be "year" or multiple hirarqy
df["Year"] = df.index.year
fd["Month"] = df.index.month
df["Day"] = fd.index.day

# go back to the original index
df.reset_index()


#check more into this:
df.index[0].date() 	#datetime.date
vs	
df.index[0]		#Timestamp
