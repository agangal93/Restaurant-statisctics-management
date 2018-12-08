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
# Computes location vs Food category matrix using the input CSV file
#
class LocationCusine:
    ## The constructor. Includes Helper object, Cusine map and Zone map
    # @param self The object pointer
    def __init__(self):
        H = Common.Helper()
        self.rows = len(H.GetCusineMap())
        self.columns = len(H.GetZoneMap())
        self.CusineCount = np.zeros((self.rows,self.columns))

    ## CreateLocationDataset - Create the Location vs FoodEntry matrix,     
    # @param self - The Object pointer  
    #        LocationData - Table of entries for Cusine vs Zone
    def CreateLocationDataset(self, LocationData):
        H = Common.Helper()

        num_entries = H.GetTotalNumEntries()
        TableEntry = [[]] * num_entries
        for entry in range(0, num_entries):
            row = random.randint(0,self.rows - 1)
            column = random.randint(0, self.columns - 1)
            while(self.CusineCount[row][column] >= LocationData[row][column]):
                row = random.randint(0, self.rows - 1)
                column = random.randint(0, self.columns - 1)

            Cusine_type = H.GetCusineMap().get(row)
            Zone_type = H.GetZoneMap().get(column)
            TableEntry[entry] = [Cusine_type,Zone_type]
            self.CusineCount[row][column] += 1

        #print("Location Set")
        #print(TableEntry)
        #print("\nSum ")
        #print(sum(self.CusineCount))
        return TableEntry
