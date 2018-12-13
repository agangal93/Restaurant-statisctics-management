# Written by: Akshay Gangal
# Tested by: Akshay Gangal

import Common
import GenerateEntrySet
import numpy as np
import random
from copy import copy, deepcopy
import mysql.connector

## @Package. docstring
#    Time variation dataset creation module.

#    This module creates an artificial dataset using truncated normal distribution.
#    It collect data for different types of input observations and generates a table of entries
#    based on initial observations and distributes the results using 
#    normal distribution function.
#

H = Common.Helper()
G = GenerateEntrySet.EntrySet()

## @var subsets - Number of subsets in the dataset
subsets = H.GetNumSubsets()
## @var mydb - SQL connector object.
###
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="restaurant"
)
mycursor = mydb.cursor()

G.GenerateCusineDistribution()
ZoneEntry_org = G.GetEntrySet()
G.GenerateTruncatedNormal(ZoneEntry_org)
num_entries = H.GetNumSubsetEntries()
# Create a normalized entry set for all subsets of inputs.
#  Combine all values using random assignments to create a psuedo random dataset.
for set in range(0,subsets):
    ZoneEntry = deepcopy(ZoneEntry_org)
    CusineEntry,maxlength = G.CreateNormalizedSet(ZoneEntry,set)

    TableEntry = [[]] * num_entries
    count = np.zeros((len(CusineEntry),len(CusineEntry[0]),maxlength))
    for entry in range(0,num_entries):
        row = random.randint(0,len(CusineEntry)-1)
        column = random.randint(0,len(CusineEntry[0])-1)
        cusine_length = len(H.GetCusineType().get(H.GetCusineMap().get(row)))
        val = random.randint(0,cusine_length-1)
        while count[row][column][val] >= CusineEntry[row][column][val]:
            row = random.randint(0,len(CusineEntry)-1)
            column = random.randint(0,len(CusineEntry[0])-1)
            cusine_length = len(H.GetCusineType().get(H.GetCusineMap().get(row)))
            val = random.randint(0,cusine_length-1)

        Zone = H.GetZoneMap().get(column)
        Cusine_type = H.GetCusineMap().get(row)
        Cusine = H.GetCusineType().get(Cusine_type)
        assert (val < len(Cusine)), "Incorrect length computation"
        Cusine_entry = Cusine[val]
        Price = H.GetCusinePrice().get(Cusine_entry)
        assert (Cusine_entry is not None),"Invalid Entry for %r Zone" % Zone

        TableEntry[entry] = [Zone,Cusine_type,Cusine_entry,Price]
        ### @var sql - MySQL query to insert the table entry into the database
        ##
        sql = "INSERT INTO variation (Zone,Cusine_type,Cusine,Price) VALUES (%s,%s,%s,%s)"
        val_1 = (Zone,Cusine_type,Cusine_entry,Price)
        mycursor.execute(sql, val_1)
        mydb.commit()

        count[row][column][val] += 1

    # Final Dataset
    print("\nSet - ",set)
    print(TableEntry)

