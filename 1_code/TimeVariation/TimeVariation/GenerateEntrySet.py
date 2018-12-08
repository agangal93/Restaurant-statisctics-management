import numpy as np
import pandas as pd
import math
import random
import Common
from scipy.stats import truncnorm

class EntrySet:
    ## The constructor.
    # @param self The object pointer
    def __init__(self):
        H = Common.Helper()
        self.NormDistribution = np.zeros((len(H.GetZoneMap()),len(H.GetCusineMap()),10))
        self.Cusine_val = [0] * len(H.GetCusineMap())
        self.Current_subset = 0


    ## Validate rounding correction result.
    # @param self The object pointer
    #        arr1 Array to validate the sum of
    #        total_arr Expected value array
    def ValidateCorrection(self, arr1, total_arr):
        for row in range(0,len(arr1)):
            assert (sum(arr1[row]) == total_arr[row]),"Rounding correction failed!!!"


    # Calculate normalized weights for each cusine category
    # and get the scaled number of entries of each type
    def GenerateCusineDistribution(self):
        H = Common.Helper()
        num_entries = H.GetNumSubsetEntries()
        for val in range(0, len(H.GetCusineMap())):
            self.Cusine_val[val] = math.floor(float(num_entries)/len(H.GetCusineMap()))

        # Correct the error generated due to rounding
        H.RoundingCorrection(self.Cusine_val,num_entries,len(self.Cusine_val))


    ## Generate Truncated Normal distribution of values for input Zone type
    # @param self The object pointer
    #        ZoneEntry Table of input values to generate normal distribution on
    #        Zone_type Type of Zone used for normalization
    def GenerateTruncatedNormal(self,ZoneEntry):
        H = Common.Helper()
        sd = 5
        for Zone in range(0,len(ZoneEntry[0])):
            for cusine in range(0,len(ZoneEntry)):
                mean_old = ZoneEntry[cusine][Zone]
                low = mean_old - sd
                high = mean_old + sd
                X = truncnorm((low - mean_old) / sd, (high - mean_old) / sd, loc=mean_old, scale=sd)
                self.NormDistribution[Zone][cusine] = np.round(X.rvs(10),2)

    ## Get input data for Zone distribution vs Cusine type from csv file
    # @param self The object pointer
    def GetEntrySet(self):
        H = Common.Helper()

        ## @var df - Pandas Data frame to get Zone entries from csv file
        #
        df = pd.read_csv('Food_Location.csv')

        num_rows_zone = df.shape[0]
        num_columns_zone = df.shape[1]

        ## @var ZoneEntry - numpy array: Food category vs Zone list
        #
        ZoneEntry = np.zeros((num_rows_zone, num_columns_zone - 1))
        for row in range(0,num_rows_zone):
            for column in range(1,num_columns_zone):
                ZoneEntry[row][column-1] = int(df.iloc[row][column] * 100)

        return ZoneEntry

    ## Read and compute Zone entry count Tables
    # @param self The object pointer
    def CreateNormalizedSet(self,ZoneEntry,entryset):
        H = Common.Helper()
        num_entries = H.GetNumSubsetEntries()
        DistInc = H.GetDistIncrease()
        DistDec = H.GetDistDecrease()
        DistGaus = H.GetDistGaussian()

        column_list = []
        # Increase
        for key,val in DistInc.items():
            row = H.GetKeyByValue(H.GetCusineMap(),(H.GetKeyByValue(H.GetCusineType(),key,False)),True)
            column = H.GetKeyByValue(H.GetZoneMap(),val,True)
            if column not in column_list:
                column_list.append(column)
            if entryset == 0:
                ZoneEntry[row][column] = round(min(self.NormDistribution[column][row]),2)
            elif entryset == 1:
                ZoneEntry[row][column] = round(sorted(self.NormDistribution[column][row])[1],2)
            elif entryset == 3:
                ZoneEntry[row][column] = round(sorted(set(self.NormDistribution[column][row]))[-2],2)
            elif entryset == 4:
                ZoneEntry[row][column] = round(max(self.NormDistribution[column][row]),2)
            elif entryset != 2:
                assert(0),"Invalid entry set"

        # Gaussian
        for key,val in DistGaus.items():
            row = H.GetKeyByValue(H.GetCusineMap(),(H.GetKeyByValue(H.GetCusineType(),key,False)),True)
            column = H.GetKeyByValue(H.GetZoneMap(),val,True)
            if column not in column_list:
                column_list.append(column)
            if entryset == 0 or entryset == 4:
                ZoneEntry[row][column] = round(min(self.NormDistribution[column][row]),2)
            elif entryset == 1 or entryset == 3:
                ZoneEntry[row][column] = round(sorted(self.NormDistribution[column][row])[1],2)
            elif entryset != 2:
                assert(0),"Invalid entry set"

        # Decrease
        for key,val in DistDec.items():
            row = H.GetKeyByValue(H.GetCusineMap(),(H.GetKeyByValue(H.GetCusineType(),key,False)),True)
            column = H.GetKeyByValue(H.GetZoneMap(),val,True)
            if column not in column_list:
                column_list.append(column)
            if entryset == 0:
                ZoneEntry[row][column] = round(max(self.NormDistribution[column][row]),2)
            elif entryset == 1:
                ZoneEntry[row][column] = round(sorted(set(self.NormDistribution[column][row]))[-2],2)
            elif entryset == 3:
                ZoneEntry[row][column] = round(sorted(self.NormDistribution[column][row])[1],2)
            elif entryset == 4:
                ZoneEntry[row][column] = round(min(self.NormDistribution[column][row]),2)
            elif entryset != 2:
                assert(0),"Invalid entry set"

        #if Type == "Gaussian":
        #    for row in range(0,len(ZoneEntry)):
        #        if entryset == 0 or entryset == 4:
        #            ZoneEntry[row][column_key] = round(min(self.NormDistribution[row]),2)
        #        elif entryset == 1 or entryset == 3:
        #            ZoneEntry[row][column_key] = round(sorted(self.NormDistribution[row])[1],2)
        #        elif entryset != 2:
        #            assert(0),"Invalid entry set"
        #elif Type == "Increase":
        #    row = H.GetKeyByValue(H.GetCusineMap(),Cusine,True)
        #    if entryset == 0:
        #        ZoneEntry[row][column_key] = round(min(self.NormDistribution[row]),2)
        #    elif entryset == 1:
        #        ZoneEntry[row][column_key] = round(sorted(self.NormDistribution[row])[1],2)
        #    elif entryset == 3:
        #        ZoneEntry[row][column_key] = round(sorted(set(self.NormDistribution[row]))[-2],2)
        #    elif entryset == 4:
        #        ZoneEntry[row][column_key] = round(max(self.NormDistribution[row]),2)
        #    elif entryset != 2:
        #        assert(0),"Invalid entry set"
        #elif Type == "Decrease":
        #    row = H.GetKeyByValue(H.GetCusineMap(),Cusine,True)
        #    if entryset == 0:
        #        ZoneEntry[row][column_key] = round(max(self.NormDistribution[row]),2)
        #    elif entryset == 1:
        #        ZoneEntry[row][column_key] = round(sorted(set(self.NormDistribution[row]))[-2],2)
        #    elif entryset == 3:
        #        ZoneEntry[row][column_key] = round(sorted(self.NormDistribution[row])[1],2)
        #    elif entryset == 4:
        #        ZoneEntry[row][column_key] = round(min(self.NormDistribution[row]),2)
        #    elif entryset != 2:
        #        assert(0),"Invalid entry set"
        #else:
        #    assert(0),"Invalid Distribution Type"

        ## Adjust the remaining entries
        sum_val = 0
        for row in range(0,len(ZoneEntry)):
            sum_val = sum(ZoneEntry[row])
            if 100 - sum_val >= 0:
                error = 100 - sum_val
                error1 = int(error)
                delta = error - error1
                while error1 > 0:
                    column_val = random.randint(0,len(ZoneEntry[0])-1)
                    if column_val not in column_list:
                        ZoneEntry[row][column_val] += 1
                        error1 -= 1
                column_val = random.randint(0,len(ZoneEntry[0])-1)
                ZoneEntry[row][column_val] += delta 
            else:
                error = sum_val - 100
                error1 = int(error)
                delta = error - error1
                while error1 > 0:
                    column_val = random.randint(0,len(ZoneEntry[0])-1)
                    if column_val not in column_list:
                        ZoneEntry[row][column_val] -= 1
                        error1 -= 1
                column_val = random.randint(0,len(ZoneEntry[0])-1)
                ZoneEntry[row][column_val] -= delta

            assert (sum(ZoneEntry[row]) == 100), "Incorrect adjustment for remaining entries"


        for row in range(0,len(ZoneEntry)):
            for column in range(0,len(ZoneEntry[0])):
                ZoneEntry[row][column] = math.floor((ZoneEntry[row][column] * self.Cusine_val[row])/100)
            H.RoundingCorrection(ZoneEntry[row],self.Cusine_val[row],len(ZoneEntry[row]))

        self.ValidateCorrection(ZoneEntry,self.Cusine_val)

        max_length = 0;
        for key,val in H.GetCusineType().items():
            if len(val) > max_length:
                max_length = len(val)

        Cusine_Entry = np.zeros((len(H.GetCusineMap()),len(H.GetZoneMap()),max_length))
        for row in range(0,len(ZoneEntry)):            
            Cusine_len = len(H.GetCusineType().get((H.GetCusineMap().get(row))))
            for column in range(0,len(ZoneEntry[0])):
                for val in range(0,Cusine_len):
                    Cusine_Entry[row][column][val] = math.floor(ZoneEntry[row][column]/Cusine_len)
                H.RoundingCorrection(Cusine_Entry[row][column],ZoneEntry[row][column],Cusine_len)
            self.ValidateCorrection(Cusine_Entry[row],ZoneEntry[row])
        #print("\nError corrected Zone distribution\n")
        #print(ZoneEntry)

        #return ZoneEntry
        return Cusine_Entry,max_length
