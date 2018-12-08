import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import random
#from scipy.stats import norm
import Common

## LocationCusine - Class for generation of Location Vs Food category matrix
#
# Computes location vs Food category matrix using input CSV file
#
class EthnicCusine:
    ## The constructor. Includes Helper object, Food Entry and FoodCount
    # @param self The object pointer
    def __init__(self):
        H = Common.Helper()
        self.ethnic_data = {0:"hispanic", 1:"white", 2:"black", 3:"asian"}
        self.rows = len(H.GetCusineType())
        self.columns = len(self.ethnic_data)
        self.EthnicCount = np.zeros((self.rows,self.columns))

    ## GetEthnicData
    # @return self.ethnic_data
    def GetEthnicData(self):
        return self.ethnic_data

    ## CreateEthnicSet - Create the Location vs Ethnicity matrix,     
    # @param self The Object pointer
    #
    def CreateEthnicset(self, EthnicData):
        H = Common.Helper()

        num_entries = H.GetTotalNumEntries()
        TableEntry = [[]] * num_entries
        for entry in range(0, num_entries):
            row = random.randint(0,self.rows - 1)
            column = random.randint(0, self.columns - 1)
            while(self.EthnicCount[row][column] >= EthnicData[row][column]):
                row = random.randint(0, self.rows - 1)
                column = random.randint(0, self.columns - 1)

            Cusine_type = H.GetCusineMap().get(row)
            Ethnic_type = self.GetEthnicData().get(column)
            TableEntry[entry] = [Cusine_type,Ethnic_type]
            self.EthnicCount[row][column] += 1

        #print("Location Set")
        #print(TableEntry)
        #print("\nSum ")
        #print(sum(self.EthnicCount))
        return TableEntry

    