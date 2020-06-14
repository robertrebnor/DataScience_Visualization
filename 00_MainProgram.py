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
from time import time

import SetUpFile as SetUpFile

start_time = time()
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

## Testing multiple inheritance, using the "SetUpFile" to initialize 
OkCupid = SetUpFile.StartProg(DataPath, FileType, sheetName) 

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


#########################################################
###                                                   ###
###                 2. Descriptive Statistics         ###
###                                                   ###                     
#########################################################

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
OkCupid.printDescriptiveStats_byVariableType(variableCategory)

# Category variables:
# Frequency within each category?

end_time  = time()
time_used = end_time - start_time
print(f"Time elapsed: {time_used:.2f} seconds.") #9.92 sec, slow


######### Testing visualization #############################

### Test PieChart
column = "body_type"

# Test PieChart with out any limit
OkCupid.PieChart(column)

# Test PieChart with limited number of categories 
OkCupid.PieChart(column, choiceLimit = "Categories", limit = 5)

# Test PieChart with a lower limit on percentage.
OkCupid.PieChart(column, choiceLimit = "Percentage", limit = 5)


### Testing histogram
# Test histogram with a quantitative variable 
column = "age"
variableCategory = "quantitative"

OkCupid.Histogram(column, variableCategory)

# Test histogram with a qualitative variable
column = "body_type"
variableCategory = "qualitative"

OkCupid.Histogram(column, variableCategory)

### Testing scatter plots

# Simple scatter plot

# Scatter plot with multiple categories and colors


#test using: height, income and age
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')



test_df = OkCupid.returnDf()

#change height from inches to cm
test_df["height"] = test_df["height"]*2.54

x = test_df["age"]
y = test_df["height"]

x = test_df["age"]
y = test_df["height"]

plt.scatter(x, y, marker='o')
plt.show()


# test using seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# On boxes: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot

test_df = OkCupid.returnDf()
sns.set()
sns.relplot(x='age' y='height', col="time", hue="smoker", style="smoker", size="size", data=tips);

# darkgrid, whitegrid, dark, white, and ticks
#sns.set_style("whitegrid")
sns.relplot(x='age', y='height', hue='sex', data=test_df,legend=False)
#plt.legend(,loc='lower right')
plt.legend(["m", "f"], bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.tight_layout()
plt.show()


sns.lmplot(x='age', y= 'height', data=test_df, fit_reg=False, legend=False, kind ="scatter")
plt.show()


g = sns.relplot(x='age', y='height', hue='sex', data=test_df)

# resize figure box to -> put the legend out of the figure
box = g.ax.get_position() # get position of figure
g.ax.set_position([box.x0, box.y0, box.width * 0.85, box.height]) # resize position

# Put a legend to the right side
#g.ax.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)

plt.show(g)







#change height from inches to cm
test_df["height"] = test_df["height"]*2.54

# Use the 'hue' argument to provide a factor variable
g=sns.lmplot(x='age', y= 'height', data=test_df, hue='sex', fit_reg=False, legend=False)


# Move the legend to an empty part of the plot
plt.legend(["m","f"],loc='lower right')

plt.show(g)





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







