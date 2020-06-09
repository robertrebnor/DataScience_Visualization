### Set up file

import DescriptiveStatistics as DescStats 
import DescriptiveVisualization  as VisDesc


# A class for set up the hole program
class StartProg(DescStats.DescriptiveStatistics, VisDesc.VisualizeDescriptive):

    # The initi gives the same dataframe as initlized 
    def __init__(self,DataPath, FileType, sheetName):
        super().__init__(DataPath, FileType, sheetName)