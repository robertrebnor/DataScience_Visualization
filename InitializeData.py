#########################################################
###                                                   ###
###           Initialize Data                         ###
###                                                   ###                     
#########################################################
"""Overview of the program:

    Goal:
    -----
    *Initialize data into a dataframe
    *Format the dataframe and set appropriate types to columns 
    
    Functions:
    ----------
    __init__: Creates a dataframe 
    returnDf: return the dataframe
 
"""

import pandas as pd


class ReadData(): 
      
    # init method or constructor 
    def __init__(self, DataPath, FileType, sheetName):
        if FileType == "excel" and sheetName == None:
            self.df = pd.read_excel(DataPath)
        elif FileType == "excel" and sheetName != None:
            self.df = pd.read_excel(DataPath, sheet_name = sheetName)
        elif FileType == "csv":
            self.df = pd.read_csv(DataPath)
        # Everytime a new dataframe is loaded, print some basic info: 
        self.basicInfo()

    def returnDf(self):
        return self.df

    def basicInfo(self):
        row, col = self.df.shape
        print("row", row)
        print("col", col)
        print("")
        
# fix a better style for the print of "basicInfo"
# should here use "self.df.dtype" to show what types the cols are. 
# is it possible two put the col_name and dtype in a dict?
#       And give the user the possibility to answer "yes/no" if they want to changes some dtype.
#       Then let them change the different values in the dict which then is used to change the dtypes of the cols


    def keyStatistics(self):
         print(self.df.describe() )


       
