#########################################################
###                                                   ###
###           Data processing                         ###
###                                                   ###                     
#########################################################
"""Overview of the program:

    Goal:
    -----
    *Help class for data processing
    
    
    Functions:
    ----------
    .. :
 
"""

import InitializeData as InitData

class DataProcessing(InitData.ReadData):

    def __init__(self,DataPath, FileType, sheetName):
        super().__init__(DataPath, FileType, sheetName)

    def sortCol_byPercentage(self, column):

        # Create a df with the column, values and percentage
        Col_sortPercentage = self.df[column].value_counts().to_frame()
        Col_sortPercentage.reset_index(inplace=True)
        Col_sortPercentage['Percentage'] =  round( Col_sortPercentage[column] / Col_sortPercentage[column].sum()*100, 2 )

        #Change the col names so it looks nice
        Col_sortPercentage.rename(columns={"index": column, column: "Values"}, inplace=True)

        # Control that the df is sort correctly
        Col_sortPercentage.sort_values(by=["Values"],ascending=False, inplace=True)

        return Col_sortPercentage
    
    def byNumbers_LimitNumberCategories(self, column, maxCategories = 10):

        # Get a sorted df with col name, values and percentage
        Col_df = self.sortCol_byPercentage(column)

        # limit the number by number of categories
        NumberOfOthers = len(Col_df.index) - maxCategories
        if NumberOfOthers > 0:
            # Find the names of row to be grouped into "others"
            nameOthersList = Col_df[column].iloc[-NumberOfOthers:].to_list()

            # Create new df, with "others"
            df_fixed  = Col_df.replace(nameOthersList, 'All other categories')

            # Sum the new df
            df_fixed = df_fixed.groupby(column).sum()

        return df_fixed

    def byPercentage_LimitNumberCategories(self, column, minPercentage = 5):
        # limit the number by percentage of observations in a category
        
        # Get a sorted df with col name, values and percentage
        Col_df = self.sortCol_byPercentage(column)

        # Find the indexes for the rows with percent less than "minPercentage"
        indexes = Col_df[Col_df["Percentage"]  < minPercentage].index.to_list()

        # Find the names of these rows
        nameOthersList = Col_df[column].iloc[indexes].to_list()

        # Create new df, with "others"
        df_fixed  = Col_df.replace(nameOthersList, 'All other categories')

        # Sum the new df
        df_fixed = df_fixed.groupby(column).sum()
        
        return df_fixed


