#########################################################
###                                                   ###
###           Descriptive Statistics                  ###
###                                                   ###                     
#########################################################
"""Overview of the program:

    Goal:
    -----
    *Preforming descriptive statistics
    
    
    Functions:
    ----------
    .. :
 
"""
import InitializeData as InitData
import numpy as np
import pandas as pd

## Testing inheritance 
# The class inherits the properties from the class "ReadData" in InitializeData
class DescriptiveStatistics(InitData.ReadData):

    # The initi gives the same dataframe as initlized 
    def __init__(self,DataPath, FileType, sheetName):
        super().__init__(DataPath, FileType, sheetName)

    
    def basicInfo(self):
        """ Prints basic info about a dataframe.

        Output
        ------
        Prints the number of rows and cols, the 5 first observations 
        in the dataframe and the column names and variable types.
        """
        
        lineMark = "-"
        baselength = 30
        row, col = self.df.shape

        print(lineMark*baselength)
        print("***Some basic information:")
        print("")
        print("The number of rows: ", row)
        print("The number of cols: ", col)
        print("")
        print("***The first 5 observations:")
        print("")
        print( self.df.head(5) )
        print("")
        print("***The columns and their data type:")
        print("")
        self.print_Col_dtype()
    
# fix a better style for the print of "basicInfo"
# should here use "self.df.dtype" to show what types the cols are. 
# is it possible two put the col_name and dtype in a dict?
#       And give the user the possibility to answer "yes/no" if they want to changes some dtype.
#       Then let them change the different values in the dict which then is used to change the dtypes of the cols


    def print_Col_dtype(self):
        """For each column in a dataframe it prints the variable type and the number of unique observations.
        """
        lineMark = "-"
        df_dict = self.df.dtypes.to_dict() #Want the col names and dypes togehter in a dict
        longestKey = None #The length of this is just to left-adjust the printing of the dict
        if len ( max(df_dict.keys(), key=len)) > len("Variable"): #Tests if "Variable" is shorter than the longes key
            longestKey = len ( max(df_dict.keys(), key=len))
        else: 
            longestKey = len("Variable")

        print("Variable".ljust(longestKey, " ") , "   dtype".ljust(12, ' '), "Unique obs.") #Prints the header of the table
        print(lineMark*( longestKey + 8 + 12 +  5)  ) 
        for keys,values in df_dict.items(): #Prints the keys and values from the dict in a nice format, and the number of unique observations 
            print(keys.ljust(longestKey, ' '), ": ", str(values).ljust(10, ' '), " ", len( self.df[keys].unique())   ) #consider fix the number of unique obs by str().rjust
        
    def change_dTypes(self, new_dTypes):
        """Changes variable types for columns.

        Parameters
        ----------
        new_dTypes:  dict
            the keys is the name of the columns that we want to change the dType of
            the values is the dType we want to change to
        
        Output
        ------
        Changes the dType for the wanted variables in the dataframe and prints the result.
        """
        df_dict = self.df.dtypes.to_dict() 
        for keys,values in new_dTypes.items(): #The dict containing the changes
            if keys in df_dict: #If a col names in the given dict is in the dataframe, then change the dType in the dataframe.
                self.df[keys] =  self.df[keys].astype(values)
            else:
                print("The column ", keys ," was not found.")
        print("")
        print("Changes complete, the updated dTypes are:")
        print("")
        self.print_Col_dtype() #Prints the update version of col names, dType and number of unique obs.

    def getSpesific_dTypes(self, dType_of_cols):
        """ Gets the col names for a given dType.

        Parameters
        ----------
        dType_of_cols:  list
            A list of the dType we are searching for.
        
        Output
        ------        
        Returns a list of a given dType variable, find all the cols with this dType.
        """
        
        list_of_cols = self.df.select_dtypes(include= dType_of_cols).columns
        list(list_of_cols)

        return list_of_cols

    #This is a static method:
    #@staticmethod
    def get_dTypesInGroup(self, variableCategory): #Remove this out from this class, can be used for the different types of Visualization
        """ Get the dTypes for a spesific variable category.

        Parameters
        ----------
        variableCategory:  string
            The name of the variable category.
            Grouping dtypes by:
                Quantitative variable:
                    *int64
                    *float64
                Qualitative variables:
                    *bool
                    *category
                String:   (not addressed yet)
                    *object 
                Time:    (not addressed yet)
                    *datetime64
                    *timedelta[ns]
        Output
        ------        
        Returns a list with the dTypes within a variable category.       
        """
        listOf_dType = list()
        if variableCategory == "quantitative":
            listOf_dType = [ "int64", "float64" ]
        elif variableCategory == "qualitative":
            listOf_dType = [ "bool", "category" ]
        elif variableCategory == "string": 
            listOf_dType = [ "object" ]
        elif variableCategory == "time": 
            print("Not fixed yet")
            #listOf_dType = [ "datetime64", "timedelta[ns]" ]
        else:
            print("Chosen variable category not recognized")
        return listOf_dType
    
    def printDescriptiveStats_byVariableType(self, variableCategory):
        """Prints descriptive statistics for a spesific variable category 
        """
        # Get the different dTypes within a spesific variable category
        listOf_dTypes = self.get_dTypesInGroup(variableCategory)
        
        # For each of the dTypes, get the variable names 
        listOfVariableNames = list( self.getSpesific_dTypes(listOf_dTypes) )
        
        # Get and print the key statistics for the choicen variables
        self.printKeyStatsNumerical(listOfVariableNames ,variableCategory)

         
    def printKeyStatsNumerical(self, col_names, variableCategory):
        """Prints the key descriptive statistics for numerical variables.
        Presents the results using a dataframe.
        
        # Col_names: list with the name of the columns with numerical values
        """
        if variableCategory == "quantitative":
            # A dict, containing all the key statistics that is to be presented
            KS_list = { "Key statistics": ["Count", "Number of Unique", "Number of NaN", "Mean", "Std.dev.", "Min", "Q25", "Q50", "Q75", "Max", "Number of Z less -3", "Number of Z above 3", "ExtremVal Box plot low", "ExtremVal Box plot high"]
                        }
        elif variableCategory == "qualitative":
            KS_list = { "Key statistics": ["Count", "Unique categories", "Number of NaN"]
                        }
                      # Add: Frequency within each category? or the top three larges and lowest?

        # Copy a list for cols i df.
        df_colList = col_names.copy()
        #Add a first column
        df_colList.insert(0, "Key statistics") 

        # Set up the dataframe
        printKeyStats = pd.DataFrame(KS_list, columns = df_colList)

        ## THIS IF AND THE keyStatsNumerical and the keyStatsQualitative must be fixed, contains much of the same code
        if variableCategory == "quantitative":
            #plot key stats for each column into the df
            for col in col_names:
                listValues = []
                listValues = self.keyStatsNumerical(col)

                for i in range( len(listValues)):
                    printKeyStats.loc[i,col] = listValues[i]
        elif variableCategory == "qualitative":
            for col in col_names:
                listValues = []
                listValues = self.keyStatsQualitative(col)

                for i in range( len(listValues)):
                    printKeyStats.loc[i,col] = listValues[i]

        print(printKeyStats.head(len(printKeyStats.index)  ))


    def keyStatsQualitative(self, col_name):
        #["Count", "Number of Unique", "Number of NaN"]
        # Count
        count = len( self.df[col_name] )
        # Number of unique obs?
        numUnique = len( self.df[col_name].unique() )
        # Number of misings
        numNaN = self.df[col_name].isna().sum()

        return count, numUnique, numNaN


    def keyStatsNumerical(self, col_name):
        """Caculates key descriptive statistics for numerical variables
        """
        # should make it so it only reads in self.df[col_name] once?
        
        # Count
        count = len( self.df[col_name] )
        # Number of unique obs?
        numUnique = len( self.df[col_name].unique() )
        # Number of misings
        numNaN = self.df[col_name].isna().sum()
        # mean
        mean = self.df[col_name].mean() 
        # sted
        std = self.df[col_name].std() 
        # min
        min = self.df[col_name].min() 
        # 25%
        q25 = self.df[col_name].quantile(0.25)
        # 50 %
        q50 = self.df[col_name].quantile(0.50)
        # 75 %
        q75 = self.df[col_name].quantile(0.75)
        # max
        max = self.df[col_name].max() 

        # possible lower and upper extreme values
        # with Z-score  

        # Manually calc z score
        df_zscore = (self.df[col_name] - mean )/ std

        z_NumbLow = np.count_nonzero(df_zscore < -3)
        z_NumbHigh = np.count_nonzero(df_zscore > 3) 

        # Using "stats" - Does not work?
        #z_lower =  self.df[ stats.zscore(self.df[col_name].notna())  < -3 ] 
        #z_NumbLow = len( z_lower)
        #z_higher =  self.df[ stats.zscore(self.df[col_name].notna())  > 3 ]
        #z_NumbHigh = len( z_higher)

        # Using box-plot (IQR):
        IQR = q75 - q25 #IQR = Q3 - Q1,  interquartile range.

        IQR_lower =  self.df[ self.df[col_name] <= (q25 - 1.5 * IQR) ] #Find the lower extreme values
        IQR_higher = self.df[ self.df[col_name] >= (q75 + 1.5 * IQR) ]

        bp_NumbLow = len(IQR_lower)
        bp_NumbHigh = len(IQR_higher)

        return count, numUnique, numNaN, round(mean, 2), round(std, 2), round(min, 2), round(q25, 2),  round(q50, 2), round(q75, 2), round(max, 2), z_NumbLow, z_NumbHigh, bp_NumbLow, bp_NumbHigh



       


    def keyStatistics(self):
         print(self.df.describe() )
