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


col_name = "height"
OkCupid.keyStatsNumerical(col_name)






















#make a copy here for simplicity when testing
OkCupid2 = OkCupid.returnDf().copy()

#Store the number of rows and cols:
row, col = OkCupid2.shape

# Returns by default only numeric variables
OkCupid2.describe()

# Numerical variables:
# Count
len( OkCupid2["height"] )
# Number of unique obs?
len( OkCupid2["height"].unique() )
# Number of misings
OkCupid2["height"].isna().sum()
# mean
OkCupid2["height"].mean() 
# sted
OkCupid2["height"].std() 
# min
OkCupid2["height"].min() 
# 25%
OkCupid2["height"].quantile(0.25)
# 50 %
OkCupid2["height"].quantile(0.50)
# 75 %
OkCupid2["height"].quantile(0.75)
# max
OkCupid2["height"].max() 
# possible lower and upper extreme values
# with Z-score
from scipy import stats
import numpy as np

## Works?
z_lower =  OkCupid2[ stats.zscore(OkCupid2["height"].notna())  < -3 ]
len( z_lower)

z_higher =  OkCupid2[ stats.zscore(OkCupid2["height"].notna())  > 3 ]
len( z_higher)


# Using box-plot (IQR):
Q1 = OkCupid2["height"].quantile(0.25)
Q3 = OkCupid2["height"].quantile(0.75)
IQR = Q3 - Q1 #IQR = Q3 - Q1,  interquartile range.


IQR_lower =  OkCupid2[ OkCupid2["height"] <= (Q1 - 1.5 * IQR) ] #Find the lower extreme values
IQR_higher = OkCupid2[ OkCupid2["height"] >= (Q3 + 1.5 * IQR) ]

len(IQR_lower)
len(IQR_higher)




# Category variables:
# Count
# Missing
# Number of unique categories
# Frequency within each category?



## Visualziering: 
#   Numerical:
# Histogram?
# Graph plot 
# Boxplots

#   Categorical:
# Histograms/bar plots
# pie charts



# All the variables
OkCupid2.describe(include='all')

# Only strings
OkCupid2.describe(include=[np.object])




