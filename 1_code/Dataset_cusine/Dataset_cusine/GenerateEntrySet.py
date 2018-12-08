import numpy as np
import pandas as pd
import math
import Common

class EntrySet:
    ## The constructor.
    # @param self The object pointer
    def __init__(self):
        self.ZoneEntry = [];
        self.EthnicEntry = [];

    ## Validate rounding correction result.
    # @param self The object pointer
    #        arr1 Array to validate the sum of
    #        arr2 Expected value array
    def ValidateCorrection(self, arr1, total_arr):
        for row in range(0,len(arr1)):
            assert (sum(arr1[row]) == total_arr[row]),"Rounding correction failed!!!"

    ## Read and compute Zone and Ethnicity entry count Tables
    # @param self The object pointer
    def CreateEntrySet(self):
        H = Common.Helper()

        ## @var df - Pandas Data frame to get Ethnicity entries csv file
        #
        df = pd.read_csv('Food_Ethnic.csv')

        num_rows_ethnic = df.shape[0]
        num_columns_ethnic = df.shape[1]

        ## @var EthnicEntry - numpy array: Food category vs Ethnicity list
        #
        EthnicEntry = np.zeros((num_rows_ethnic, num_columns_ethnic - 1))
        for row in range(0,num_rows_ethnic):
            for column in range(1,num_columns_ethnic):
                EthnicEntry[row][column-1] = df.iloc[row][column]

        ## @var df - Pandas Data frame to get Zone entries from csv file
        #
        df = pd.read_csv('Food_Location.csv')

        num_rows_zone = df.shape[0]
        num_columns_zone = df.shape[1]

        ## @var ZoneEntry - numpy array: Food category vs Zone list
        #
        #ZoneEntry = [[0 for x in range(num_columns_zone - 1)] for x in range(num_rows_zone)]
        ZoneEntry = np.zeros((num_rows_zone, num_columns_zone - 1))
        for row in range(0,num_rows_zone):
            for column in range(1,num_columns_zone):
                ZoneEntry[row][column-1] = df.iloc[row][column]

        num_entries = H.GetTotalNumEntries()

        #Cusine_div_map = H.GetCusineDivision()
        #Total = 0
        #for val in range(0, len(H.GetCusineDivision())):
        #    Total += Cusine_div_map[H.GetCusineMap().get(val)]

        # Calculate normalized weights for each cusine category
        # and get the scaled number of entries of each type
        Cusine_val = [0] * len(H.GetCusineMap())
        for val in range(0, len(H.GetCusineMap())):
            #Cusine_val[val] = float(Cusine_div_map[H.GetCusineMap().get(val)])/Total
            #Cusine_val[val] = math.floor(Cusine_val[val] * num_entries)
            Cusine_val[val] = math.floor(float(num_entries)/len(H.GetCusineMap()))

        # Correct the error generated due to rounding
        H.RoundingCorrection(Cusine_val,num_entries)

        for row in range(0,len(ZoneEntry)):
            for column in range(0,len(ZoneEntry[0])):
                ZoneEntry[row][column] = math.floor(ZoneEntry[row][column] * Cusine_val[row])

        for row in range(0,len(ZoneEntry)):
            H.RoundingCorrection(ZoneEntry[row],Cusine_val[row])

        self.ValidateCorrection(ZoneEntry,Cusine_val)
        #print("\nError corrected Zone distribution\n")
        #print(ZoneEntry)

        return ZoneEntry, EthnicEntry, Cusine_val
