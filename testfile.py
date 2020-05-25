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




