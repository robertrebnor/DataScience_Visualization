#########################################################
###                                                   ###
###           Descriptive Visualization               ###
###                                                   ###                     
#########################################################
"""Overview of the program:

    Goal:
    -----
    *Visualization of data
    
    
    Functions:
    ----------
    .. :
 
"""
import matplotlib.pyplot as plt
import numpy as np

import DataProcessing as DataProc

class VisualizeDescriptive(DataProc.DataProcessing): 

    def __init__(self,DataPath, FileType, sheetName):
        super().__init__(DataPath, FileType, sheetName)
    
    def PieChart(self, column, choiceLimit = None, limit = None):
        Data_df = None
        if choiceLimit == None:
            Data_df = self.sortCol_byPercentage(column) #DataProc.DataProcessing.sortCol_byPercentage(self, column)
        elif choiceLimit == "Categories":
            Data_df = self.byNumbers_LimitNumberCategories(column, limit) # DataProc.DataProcessing.byNumbers_LimitNumberCategories(self, column, limit)
        elif choiceLimit == "Percentage":
            Data_df = self.byPercentage_LimitNumberCategories(column, limit) #DataProc.DataProcessing.byPercentage_LimitNumberCategories(self, column, limit)
        else:
            print("Choice not recognized")

        Data_df.reset_index(inplace=True)

        # Returns a list with the uniquq variable names
        listCategories = Data_df[column].unique()  #trouble here? is this col now called index from ".byNumbers_LimitNumberCategories"

        # Set the currency ISO as the row index
        Data_df.set_index(column, inplace=True)

        quantity = []
        for cat in listCategories:
            quantity.append( Data_df.loc[cat,"Values"])
        
        plt.pie(quantity, labels = listCategories, startangle=90, autopct='%.1f%%', shadow = False)
        plt.show()

    def Histogram(self, column, variableCategory):

        variable = self.df[column]
        num_bins = len( variable.unique() )

        if variableCategory == "quantitative":
            x_min = variable.min()
            x_max = variable.max()

            n, bins, patches = plt.hist(variable, bins=num_bins, range = [x_min, x_max], density=False, histtype='bar', color='b', edgecolor='k', alpha=0.5)
            plt.xlim(x_min, x_max)
        
        elif variableCategory == "qualitative":

            variable_dict = variable.value_counts().to_dict()

            bars = list() #name of the bars
            num_obs = list() #height of the bares
            for keys,values in variable_dict.items():
                bars.append(keys)
                num_obs.append(values)

            y_pos = np.arange(len(bars))
            
            # Create bars
            plt.bar(y_pos, num_obs)
            # Create names on the x-axis
            plt.xticks(y_pos, bars, rotation = 90)
            #plt.yticks()
            # Fix space below plot to type bar names
            plt.tight_layout()

        plt.show()


