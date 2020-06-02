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

    def keyStatistics(self):
         print(self.df.describe() )


       
