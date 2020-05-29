
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




## Test using date as the row index:
from datetime import datetime

#Use the date as index instead of numbers?
logSpot.set_index('date', inplace=True)
logSpot["Year"] = logSpot.index.year
logSpot["Month"] = logSpot.index.month
logSpot["Day"] = logSpot.index.day

logForward1m.set_index('date', inplace=True)
logForward1m["Year"] = logForward1m.index.year
logForward1m["Month"] = logForward1m.index.month
logForward1m["Day"] = logForward1m.index.day


# To use index numbers when date is set as index
logSpot.index[0] # Timestamp('1976-01-01 00:00:00')
logSpot.index[0].date() #datetime.date(1976, 1, 1)

logSpot.datetime.date(1999,1,1)

logSpot.index.date(1999,1,1) #do not work

logSpot.iloc[0] #gives the observations of all the variables at index 0

testdato2 = "1999-01" #gives all observations for the month
testdato3 = "1999-01-01" # gives all observations for the day

logSpot.loc["1999-01-01"] #gives the observations of all the variables at date 1999-01-01

logSpot.loc[testdato2]
logSpot.loc[testdato3]

testData[testData.Year > 1998]

#Recall this loop:
# Kill all currencies with Euro after Dec98
for column in euro_aptList:
    for i in range( len(testData[column]) - 1):
        i +=1 
        if testData.loc[i,"Year"] > 1998:
            testData.loc[i,column] = "NaN"
print("End")
testData

# Only want this for obs after 1998, how to make this more efficient
# Could I use this command? (at least this gives me the index starting 1999)
testData[testData.Year > 1998] 

########################3

def get_df(DataPath, FileType, sheetName=None):
    """ Create a dataframe using Pandas

       Parameters
    ----------
    DataPath:  string
        the path to the file.
    FileType: string
        Says which filetype to read in.
        Options are: "excel" and "csv"
    sheetName: string
        If filetype is Excel and there are multiple sheets within the Excel file,
        sheetName specifies which sheet to read in.
        By default sheetName is sat to empty.
    Output
    ------
    A dataframe from Pandas

    """
    df = None
    if FileType == "excel" and sheetName == None:
        df = pd.read_excel(DataPath)
    elif FileType == "excel" and sheetName != None:
        df = pd.read_excel(DataPath, sheet_name = sheetName)
    elif FileType == "csv":
        df = pd.read_csv(DataPath)
    return df

class ReadData(): 
      
    # init method or constructor 
    def __init__(self, DataPath, FileType, sheetName): 
        if FileType == "excel" and sheetName == "":
            self = pd.read_excel(DataPath)
        elif FileType == "excel" and sheetName != "":
            self = pd.read_excel(DataPath, sheet_name = sheetName)
        elif FileType == "csv":
            self = pd.read_csv(DataPath)




# add option of only looking at key variables?
# add option if data set needs to be cleaned (remove rows or cols) and set indexes



 def __init__(self, DataPath): 
        self = pd.read_excel(DataPath)

#self.model = model
#self.color = color 
          
 #   def show(self): 
 #       print("Model is", self.model ) 
  #      print("color is", self.color ) 
