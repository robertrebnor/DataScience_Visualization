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
    __init__: Creates a dataframe, prints basic info
    returnDf: Return the dataframe
    basicInfo: 
 
"""
import numpy as np
import pandas as pd


import DescriptiveStatistics as DescStats 

class ReadData(): 
      
    # init method or constructor 
    def __init__(self, DataPath, FileType, sheetName):
        """
        Creates a dataframe from a datafile. Prints basic info,
        such as rows, cols, head, col names and variable types.

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
        if FileType == "excel" and sheetName == None:
            self.df = pd.read_excel(DataPath)
        elif FileType == "excel" and sheetName != None:
            self.df = pd.read_excel(DataPath, sheet_name = sheetName)
        elif FileType == "csv":
            self.df = pd.read_csv(DataPath)
        print("")
        print("Dataframe created.")

        # Everytime a new dataframe is loaded, print some basic info: 
        DescStats.DescriptiveStatistics.basicInfo(self)

    # Use __call__ instead of "returnDf"
    #def __call__(self): 
    #   return self.df

    def returnDf(self):
        """Returns the dataframe
        """
        return self.df

    def UpdateDf(self, dataframe):
        self.df = dataframe

    def Df_toFile(self, DataPath, FileType, sheetName):
        if FileType == "excel" and sheetName == None:
            self.df = pd.to_excel(DataPath)
        elif FileType == "excel" and sheetName != None:
            self.df = pd.to_excel(DataPath, sheet_name = sheetName)
        elif FileType == "csv":
            self.df = pd.to_csv(DataPath)
        print("Dataframe save at: ", DataPath)
    

 