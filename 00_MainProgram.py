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
import DataProcessing as dataproc

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

# Change dTypes in the dataframe
OkCupid.change_dTypes(new_dTypes)

### Get descriptive statistics for the different types of variables:
# The choices:
#   *quantitative
#   *qualitative
#   *string (not fixed)
#   *time   (not fixed)

# Testing quantitative:
variableCategory = "quantitative"
OkCupid.printDescriptiveStats_byVariableType(variableCategory)

# Testing qualitative:
variableCategory = "qualitative"

# Category variables:
# Count
# Missing
# Number of unique categories
# Frequency within each category?

# test DataProcessing:
column = "body_type"

# Need to fix this
OkCupid2 = OkCupid.returnDf().copy()
OkCupid_datproc = dataproc.DataProcessing(OkCupid2)

# Strange sort?
OkCupid_datproc.byNumbers_LimitNumberCategories(column)

OkCupid_datproc.byPercentage_LimitNumberCategories(column)



##################Plots, move these into DescriptiveVisualization 

#make a copy here for simplicity when testing
OkCupid2 = OkCupid.returnDf().copy()

column = "sex"

listCategories = OkCupid2[column].unique() #returns a list with the uniquq variable names, so this is the lables

CountsByName = OkCupid2[column].value_counts().to_frame()

quantity = []
for cat in listCategories:
    quantity.append( CountsByName.loc[cat,column])
print("done")


plt.pie(quantity, labels = listCategories, autopct = '% 1.1f %%', shadow = True, startangle = 140 )
plt.show()

plt.pie(quantity, labels = listCategories, startangle=90, autopct='%.1f%%', shadow = False)
plt.show()


import numpy as np
#Bar plot:
height = quantity
bars = listCategories
y_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(y_pos, height)
 
# Add title and axis names
plt.title('My title')
plt.xlabel('categories')
plt.ylabel('values')
 
# Limits for the Y axis
#plt.ylim(0,60)
 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()


###################### Some notes
#listCategories = OkCupid2[column].unique() #returns a list with the uniquq variable names, so this is the lables for plots

# Could be useful:
#CountsByName = CountsByName.to_dict()
#CountsByName = OkCupid2[column].value_counts().to_dict()


# Test gets descriptive statistics for numerical variables:
#col_names = ["height", "income", "age"]

#wanted_dType = "float64"
#OkCupid.getSpesific_dTypes(wanted_dType)

#col_names = ["height", "income", "age"]
#OkCupid.printKeyStatsNumerical(col_names)



## Visualziering: 
#   Numerical:
# Histogram?
# Graph plot 
# Boxplots

#   Categorical:
# Histograms/bar plots
# pie charts







