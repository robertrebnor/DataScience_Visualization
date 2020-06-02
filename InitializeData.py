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
from scipy import stats
import numpy as np

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
        lineMark = "-"
        baselength = 30
        row, col = self.df.shape

        print(lineMark*baselength)
        print("***Some basic information:")
        print("")
        print("The number of rows: ", row)
        print("The number of cols: ", col)
        print("")
        print("***The first 5 observations:")
        print("")
        print( self.df.head(5) )
        print("")
        print("***The columns and their data type:")
        print("")
        self.print_Col_dtype()


# fix a better style for the print of "basicInfo"
# should here use "self.df.dtype" to show what types the cols are. 
# is it possible two put the col_name and dtype in a dict?
#       And give the user the possibility to answer "yes/no" if they want to changes some dtype.
#       Then let them change the different values in the dict which then is used to change the dtypes of the cols

    def print_Col_dtype(self):
        lineMark = "-"
        df_dict = self.df.dtypes.to_dict() 
        longestKey = None #The length of this is just to left-adjust the printing of the dict
        if len ( max(df_dict.keys(), key=len)) > len("Variable"): #tests if the "Variable" is shorter than the longes key
            longestKey = len ( max(df_dict.keys(), key=len))
        else: 
            longestKey = len("Variable")

        print("Variable".ljust(longestKey, " ") , "   dtype".ljust(12, ' '), "Unique obs.") 
        print(lineMark*( longestKey + 8 + 12 +  5)  )
        for keys,values in df_dict.items(): #prints the keys and values from the dict in a nice format
            print(keys.ljust(longestKey, ' '), ": ", str(values).ljust(10, ' '), " ", len( self.df[keys].unique())   ) #consider fix the number of unique obs by str().rjust
        
    def change_dTypes(self, new_dTypes):
        df_dict = self.df.dtypes.to_dict() 
        for keys,values in new_dTypes.items(): #the dict containing the changes
            if keys in df_dict: #if correct cols
                self.df[keys] =  self.df[keys].astype(values)
            else:
                print("The column ", keys ," was not found.")
        print("")
        print("Changes complete, the updated dTypes are:")
        print("")
        self.print_Col_dtype()

    def keyStatsNumerical(self, col_name):
        # should make it so it only reads in self.df[col_name] once?
        # Numerical variables:
        # Count
        count = len( self.df[col_name] )
        # Number of unique obs?
        numUnique = len( self.df[col_name].unique() )
        # Number of misings
        numNaN = self.df[col_name].isna().sum()
        # mean
        mean = self.df[col_name].mean() 
        # sted
        std = self.df[col_name].std() 
        # min
        min = self.df[col_name].min() 
        # 25%
        q25 = self.df[col_name].quantile(0.25)
        # 50 %
        q50 = self.df[col_name].quantile(0.50)
        # 75 %
        q75 = self.df[col_name].quantile(0.75)
        # max
        max = self.df[col_name].max() 

        # possible lower and upper extreme values
        # with Z-score  
        z_lower =  self.df[ stats.zscore(self.df[col_name].notna())  < -3 ]  ## Works?
        z_NumbLow = len( z_lower)

        z_higher =  self.df[ stats.zscore(self.df[col_name].notna())  > 3 ]
        z_NumbHigh = len( z_higher)

        # Using box-plot (IQR):
        IQR = q75 - q25 #IQR = Q3 - Q1,  interquartile range.

        IQR_lower =  self.df[ self.df[col_name] <= (q25 - 1.5 * IQR) ] #Find the lower extreme values
        IQR_higher = self.df[ self.df[col_name] >= (q75 + 1.5 * IQR) ]

        bp_NumbLow = len(IQR_lower)
        bp_NumbHigh = len(IQR_higher)

        return count, numUnique, numNaN, round(mean, 2), round(std, 2), round(min, 2), round(q25, 2),  round(q50, 2), round(q75, 2), round(max, 2), z_NumbLow, z_NumbHigh, bp_NumbLow, bp_NumbHigh

    def printKeyStatsNumerical(self, col_names):
        # col_names is a list
        # test using df
        KS_list = { "Key statistics": ["Count", "Number of Unique", "Number of NaN", "Mean", "Std.dev.", "Min", "Q25", "Q50", "Q75", "Max", "Number of Z less -3", "Number of Z above 3", "ExtremVal Box plot low", "ExtremVal Box plot high"]
                    }

        #Add a first column
        col_names.insert(0, "Key statistics") 

        # set ut the dataframe
        printKeyStatsNum = pd.DataFrame(KS_list, columns = col_names)

        #plot key stats for each column into the df
        for col in col_names:
            listValues = []
            listValues = self.keyStatsNumerical(col)

            for i in range( len(listValues)):
                printKeyStatsNum.loc[i,col] = listValues[i]
            
        print(printKeyStatsNum.head(13))


       


    def keyStatistics(self):
         print(self.df.describe() )


       
