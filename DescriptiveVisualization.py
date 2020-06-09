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
import DataProcessing as dataproc
import matplotlib.pyplot as plt

class VisualizeDescriptive(): 

    def __init__(self, dataframe):
        self.df = dataframe
    
    def PieChart(self, column, choiceLimit = None, limit = None):
        Data_df = None
        if choiceLimit == None:
            Data_df = dataproc.DataProcessing.sortCol_byPercentage(self, column)
            print(Data_df)
        elif choiceLimit == "Categories":
            Data_df = dataproc.DataProcessing.byNumbers_LimitNumberCategories(self, column, limit)
        elif choiceLimit == "Percentage":
            Data_df = dataproc.DataProcessing.byPercentage_LimitNumberCategories(self, column, limit)
        else:
            print("Choice not recognized")

        # Returns a list with the uniquq variable names
        listCategories = Data_df[column].unique() 

        # Set the currency ISO as the row index
        Data_df.set_index(column, inplace=True)

        quantity = []
        for cat in listCategories:
            quantity.append( Data_df.loc[cat,"Values"])
        
        plt.pie(quantity, labels = listCategories, startangle=90, autopct='%.1f%%', shadow = False)
        plt.show()

