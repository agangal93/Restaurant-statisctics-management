# Written by: Akshay Gangal
# Tested by: Akshay Gangal

import Common
import LocationCusine
import Dataethnic
import GenerateEntrySet
import pandas as pd
import numpy as np
import mysql.connector
import random
import math

## @Package. docstring
#    Dataset creation module.

#    This module creates an artificial dataset based on a mathematical model.
#    It has four clases - LocationCusine, EthnicCusine, DensityTime and Helper.
#    which collect data for different types of input data and generates a table of entries
#    based on initial observations and distributes the results using 
#    a probability distribution function.
#

def GetSelectionRange(Cusine,num_rows,num_columns):

    row_list = [None] * num_rows
    column_list = [[None for x in range(num_columns)] for y in range(num_rows)]
    val = 0
    for row in range(0,num_rows):
        if sum(Cusine[row]) != 0:
            row_list[val] = row
            val += 1

    for row in row_list:
        val = 0
        if row != None:
            for column in range(0, num_columns):
                if Cusine[row][column] != 0:
                    column_list[row][val] = column
                    val += 1

    return row_list, column_list

H = Common.Helper()
G = GenerateEntrySet.EntrySet()
L = LocationCusine.LocationCusine()
E = Dataethnic.EthnicCusine()

ZoneEntry, EthnicEntry, Cusine_count = G.CreateEntrySet()

## @var mydb - SQL connector object.
#
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="restaurant"
)
mycursor = mydb.cursor()

num_cusines = len(H.GetCusineMap())
Cusine = np.zeros((num_cusines,len(EthnicEntry[0]),len(ZoneEntry[0])))

num_rows = len(EthnicEntry[0])
num_columns = len(ZoneEntry[0])
for type in range(0,num_cusines):
    for row in range(0,num_rows):
        for column in range(0,num_columns):
            Cusine[type][row][column] = math.floor(ZoneEntry[type][column] * EthnicEntry[type][row])

for type in range(0, num_cusines):
    for column in range(0,num_columns):
        H.RoundingCorrection(Cusine[type][:,column],ZoneEntry[type][column])

sum_val = 0
for type in range(0,num_cusines):
    sum_val += sum(map(sum,Cusine[type]))
assert(sum_val == H.GetTotalNumEntries()), "Rounding correction error"

num_entries = H.GetTotalNumEntries()
TableEntry = [[]]*num_entries
for entry in range(0,num_entries):
    EntryAdded = False
    while EntryAdded == False:
        type = random.randint(0,num_cusines-1)
        
        if sum(map(sum,Cusine[type])) == 0: # No entries to add
            continue

        Cusine_type = H.GetCusineMap().get(type)
        Cusine_val = H.GetCusineType().get(Cusine_type)
        Cusine_entry = Cusine_val[random.randint(0,len(Cusine_val)-1)]
        assert (Cusine_entry is not None), "Invalid Cusine Entry"

        ## @var row_list - List zones suitable Ethnicty for a given Cusine type
        #  @var column_list - List zones suitable Zones for a given Cusine type and Ethnicity
        row_list, column_list = GetSelectionRange(Cusine[type],num_rows,num_columns)

        if row_list.count(None) == len(row_list):
            continue

        ## @var row_list_mod - Remove None value entries from row_list
        #
        row_list_mod = []
        for x in range(0,len(row_list)):
            if row_list[x] is not None:
                row_list_mod.append(row_list[x])

        assert (row_list_mod)
        Ethnic_Key = row_list_mod[random.randint(0,len(row_list_mod)-1)]
        assert (Ethnic_Key is not None), "Invalid Ethnic key"
        Ethnicity = E.GetEthnicData().get(Ethnic_Key)

        if column_list[Ethnic_Key].count(None) == len(column_list[Ethnic_Key]):
            continue

        ## @var zone_list_mod - Remove None value entries from column_list
        #
        zone_list_mod = []
        for x in range(0,len(column_list[Ethnic_Key])):
            if column_list[Ethnic_Key][x] is not None:
                zone_list_mod.append(column_list[Ethnic_Key][x])

        assert (zone_list_mod)
        Zone_Key = zone_list_mod[random.randint(0,len(zone_list_mod)-1)]
        assert (Ethnic_Key is not None), "Invalid Ethnic key"
        Zone = H.GetZoneMap().get(Zone_Key)

        ## @var Price - Price for given food entry
        #
        Price = H.GetCusinePrice().get(Cusine_entry)
        assert (Cusine[type][Ethnic_Key][Zone_Key] > 0)
        Cusine[type][Ethnic_Key][Zone_Key] -= 1

        TableEntry[entry] = [Zone,Cusine_type,Cusine_entry,Ethnicity,Price]
        ## @var sql - MySQL query to insert the table entry into the database
        #
        sql = "INSERT INTO users1 (Zone,Cusine_type,Cusine,Ethnicity,Price) VALUES (%s,%s,%s,%s,%s)"
        val = (Zone,Cusine_type,Cusine_entry,Ethnicity,Price)
        mycursor.execute(sql, val)
        mydb.commit()

        EntryAdded = True

sum_val = 0
for type in range(0,num_cusines):
    sum_val += sum(map(sum,Cusine[type]))
assert(sum_val == 0),"Not all entries added"

print("\nFinal Dataset\n")
print(TableEntry)

print("\nDataset Created..!!!")