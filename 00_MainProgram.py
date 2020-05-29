#########################################################
###                                                   ###
###                  The Main Program                 ###
###                                                   ###                     
#########################################################
"""Overview of the program:
    1. Initialize dataset: Set up the data file as a dataframe and make it ready for analysis
    2.
    3.
    4.
""" 

#import pandas as pd 
#import numpy as np

import InitializeData as initdt


#########################################################
###                                                   ###
###                 1. Initialize dataset             ###
###                                                   ###                     
#########################################################

# Enter the filepath to the dataset
DataPath = r"Data\profiles.csv"
# Enter the file type of the dataset
FileType = "csv"
# Enter if there is a specific sheet in Execl to read in
sheetName = None

OkCupid = initdt.ReadData(DataPath, FileType, sheetName)

#make a copy here for simplicity when testing
#OkCupid2 = OkCupid.returnDf().copy()

OkCupid.basicInfo()