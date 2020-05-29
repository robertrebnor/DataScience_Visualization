#########################################################
###                                                   ###
###           Initialize Data                         ###
###                                                   ###                     
#########################################################
"""Overview of the program:

    Goal:
    -----
    *Initialize data into a dataframe
    *Format the dataframe and set appropriate types to columns 
    
    Functions:
    ----------
    get_df: Creates a dataframe 
    GraphicalInspectionGeneral: Plotting in 2D
    GraphicalInspectionGeneral_3D: Plotting in 3D
 
"""

import pandas as pd

def get_df(DataPath, FileType, sheetName=None):
    """ Create a dataframe using Pandas

       Parameters
    ----------
    DataPath:  string
        the path to the file.
    FileType: string
        Says which filetype to read in.
        Options are: "excel" and "csv"
    sheetName: string
        If filetype is Excel and there are multiple sheets within the Excel file,
        sheetName specifies which sheet to read in.
        By default sheetName is sat to empty.
    Output
    ------
    A dataframe from Pandas

    """
    df = None
    if FileType == "excel" and sheetName == None:
        df = pd.read_excel(DataPath)
    elif FileType == "excel" and sheetName != None:
        df = pd.read_excel(DataPath, sheet_name = sheetName)
    elif FileType == "csv":
        df = pd.read_csv(DataPath)
    return df


