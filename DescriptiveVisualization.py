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
import DataProcessing as DataProc
import matplotlib.pyplot as plt

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

