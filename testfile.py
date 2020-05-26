##  Testfile for notes 

import pandas as pd
import numpy as np

# Testing with the OkCupid dataset.
# Found at: https://github.com/rudeboybert/JSE_OkCupid

# Read in the dataset
OkCupid = pd.read_csv(r"Data\profiles.csv")

# Check that the dataset looks fine
OkCupid.head(5)

OkCupid.info()

#Store the number of rows and cols:
row, col = OkCupid.shape

#Store the names of each column
col_Names = list(OkCupid.columns)

# Returns by default only numeric variables
OkCupid.describe()

# All the variables
OkCupid.describe(include='all')

# Only strings
OkCupid.describe(include=[np.object])

# All the information for one spesific individual
OkCupid.iloc[0] 

# Only male individuals
OkCupid[OkCupid.sex == "m"]

# List unique 
list( OkCupid["sex"].unique() )

OkCupid.head(5)

### Histogram:
import matplotlib.pyplot as plt


#To test hist use:
#   age
#   sex
#   status

#def histPlot():

#Numeric: age
x = OkCupid.age

num_bins = len( x.unique() )

n, bins, patches = plt.hist(x, bins=num_bins, range = [x.min(),x.max()], density=False, histtype='bar', color='b', edgecolor='k', alpha=0.5)
plt.xlim(x.min(), x.max())
plt.show()

#plt.setp(patches[0], 'facecolor', 'g')

#Missing: labels
#Frequency
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import matplotlib


n, bins, patches = plt.hist(x, bins=num_bins, range = [x.min(),x.max()], density=False, histtype='bar', color='b', edgecolor='k', alpha=0.5)


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

data = OkCupid.age

plt.hist(data, weights=np.ones(len(data)) / len(data) )

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()



formatter = FuncFormatter(to_percent)

# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)



plt.xlim(x.min(), x.max())
plt.show()



         
# Def
x = OkCupid.sex

len( OkCupid[OkCupid.sex == "m"] ) # 35829

len( OkCupid[OkCupid.sex == "f"] ) # 24117

len( OkCupid.sex ) # 59946




# Sex

x = OkCupid.sex
num_bins = len( x.unique() )

n, bins, patches = plt.hist(x, bins=num_bins, density=True, histtype='bar', color='b', edgecolor='k', alpha=0.5)
plt.show()



n, bins, rectangles = ax.hist(x, num_bins, density=True)

plt.hist(x, density=True, bins=num_bins)


plt.hist(x, bins=num_bins, )
plt.ylabel('Frequency')
plt.xlabel('Data')
plt.title("Histogram")
plt.show()


#Use some of this:

from matplotlib import pyplot as plt

gen x and y 

# Function to plot
plt.plot(x,y)

# Function to plot the bar
plt.bar(x,y)

# Function to plot histogram
plt.hist(x)

# plot circles?
plt.plot(x,t, 'ro')





