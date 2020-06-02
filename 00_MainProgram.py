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

#From this, I want to change some of the dTypes:
#Different types of dtypes:
#object
#int64
#float64
#bool
#category
#datetime64
#timedelta[ns]


#to changes in df
new_dTypes = { 
                "sex": "category",
                "status": "category",
                "body_type": "category",
                "diet": "category",
                "drinks": "category",
                "drugs": "category",
                "smokes": "category",
                "job": "category",
                "location": "category",
                "orientation": "category",
                "education": "category",
                #"last_online": "datetime64", #must look more into this
                }
#ethnicity - fix this in some way?
#offspring - category, but must be fixed
#pets - category, but must be fixed
#religion category and string,  but must be fixed
#sign  category and string,  but must be fixed
#speaks category and string,  but must be fixed

# OkCupid.df["last_online"] #look at this

OkCupid.change_dTypes(new_dTypes)









