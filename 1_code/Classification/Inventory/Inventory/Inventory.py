# Written by: Akshay Gangal
# Tested by: Akshay Gangal

import mysql.connector
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from collections import defaultdict
from heapq import nlargest,nsmallest
import Common

## @Package. docstring
#    Inventory management module.

#    This module updates the inventory based on the artificial dataset.
#    It maintains statistics of the most consumed and least consumed ingredients
#    and updates the database with the alerts for out of stock ingredients 
#
H = Common.Helper()

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="restaurant"
            )
mycursor = mydb.cursor()
mycursor1 = mydb.cursor()
mycursor2 = mydb.cursor()
num_items = len(H.GetCusine())
CusineList = [[]] * num_items
num_subsets = H.GetNumSubsets()
num_entries = H.GetNumSubsetEntries()

## Read the Food item vs Ingredient list
#
df = pd.read_csv("FoodList1.csv")

## Group food ingredients be name
#
foodToIngredient = defaultdict(list)
grouped = df.groupby('Food')
for name,group in grouped:
    for val in range(0,len(group)):
        foodToIngredient[name].append(str(group.Ingredients.iloc[val]) + "," + str(group.Quantity.iloc[val]) + "," + str(group.Unit.iloc[val]))

## Read the Ingredient list
#
Ingredientdf = pd.read_csv("Ingredients1.csv")
Ingredientlist = Ingredientdf.values

num_ing = len(Ingredientlist)
InitialStock = np.zeros(num_ing)
for val in range(0,len(Ingredientlist)):
    InitialStock[val] = Ingredientlist[val][1]

found_ing = False
## Read all entries from database and group them into subsets based on days.
#
mycursor.execute("SELECT * FROM variation")
for set in range(0,num_subsets):
    Dataset = mycursor.fetchmany(num_entries)

    for entry in Dataset:
        Cusine = entry[3]       # Get the cusine entry
        Ingredient_val = foodToIngredient[Cusine]

        ## Update the Ingredient list with the new ingredient count modified by the current entry from database
        #
        for data in Ingredient_val:
            Value = data.split(',')
            IngredientEntry = Value[0]
            IngredientQuantity = float(Value[1])
            for row in range(0,len(Ingredientlist)):
                if IngredientEntry == Ingredientlist[row][0]:
                    assert(Ingredientlist[row][1] > 20), "Insufficient stock\n"
                    Ingredientlist[row][1] -= IngredientQuantity
                    found_ing = True
                    break;
            assert(found_ing), "Ingredient not found in the list\n"

    Ingredientdf = pd.DataFrame(data=Ingredientlist, index=Ingredientdf.index, columns=Ingredientdf.columns)
    Ingredientdf.to_csv("InventoryList_%d.csv"%(set+1),encoding='utf-8')
print("\nUpdated List\n")
print(Ingredientlist)

ConsumptionIng = np.zeros((num_ing,num_subsets))

for set in range(0,num_subsets):
    IngredientDay = pd.read_csv("InventoryList_%d.csv"%(set+1))
    IngredientDay = IngredientDay.values
    for ing in range(0,num_ing):
        ConsumptionIng[ing][set] = IngredientDay[ing][2]

RateConsumption = np.zeros(num_ing)
# Record all ingredients whose currently quantity is less than 30% of the initial stock.
threshold = 0.3
StockAvailable = []
Consumptionall = [[]] * num_ing
for ing in range(0,len(ConsumptionIng)):
    RateConsumption[ing] = (max(ConsumptionIng[ing]) - min(ConsumptionIng[ing])) / num_subsets
    stock = min(ConsumptionIng[ing]) / InitialStock[ing]
    if stock <= threshold:
        StockAvailable.append([IngredientDay[ing][1],(stock*100)])
    Consumptionall[ing] = [IngredientDay[ing][1],RateConsumption[ing]]

#print("Consumption of all ingredients\n")
#print(Consumptionall)
most_consumed = nlargest(10,RateConsumption)

## Insert most consumed, least consumed items into Inventory Database
#
ingredient_consumed = []
found = False
for value in most_consumed:
    for entry in Consumptionall:
        if (value in entry) and (entry[0] not in ingredient_consumed):
            ingredient_consumed.append(entry[0])
            found = True
            break
    assert(found),"Entry not found\n"

for val in range(0,len(most_consumed)):
    sql_1 = "INSERT INTO Inventory (ItemName,Priority,Rate) VALUES (%s,%s,%s)"
    val_1 = (ingredient_consumed[val],"H",str(most_consumed[val]))
    mycursor1.execute(sql_1, val_1)
    mydb.commit()

#pos = np.arange(len(ingredient_consumed))
#plt.bar(pos, most_consumed, align='center', alpha=0.5)
#plt.xticks(pos, ingredient_consumed, ha='right', rotation=20, fontsize=10)
#plt.ylabel('Consumption rate per day')
#plt.title('Most consumed ingredients')
#plt.show()

least_consumed = nsmallest(10,RateConsumption)

ingredient_consumed = []
found = False
for value in least_consumed:
    for entry in Consumptionall:
        if (value in entry) and (entry[0] not in ingredient_consumed):
            ingredient_consumed.append(entry[0])
            found = True
            break
    assert(found),"Entry not found\n"

for val in range(0,len(most_consumed)):
    sql_1 = "INSERT INTO Inventory (ItemName,Priority,Rate) VALUES (%s,%s,%s)"
    val_1 = (ingredient_consumed[val],"L",str(least_consumed[val]))
    mycursor1.execute(sql_1, val_1)
    mydb.commit()

#pos = np.arange(len(ingredient_consumed))
#plt.bar(pos, least_consumed, align='center', alpha=0.5)
#plt.xticks(pos, ingredient_consumed, ha='right', rotation=20, fontsize=10)
#plt.ylabel('Consumption rate per day')
#plt.title('Least consumed ingredients')
#plt.show()

## Insert alerts section items into LowStock Database
#
print("Low Stock Availability list")
print(StockAvailable)
for val in range(0,len(StockAvailable)):
    Stocklist = StockAvailable[val]
    sql_1 = "INSERT INTO LowStock (ItemName,Perc) VALUES (%s,%s)"
    val_1 = (Stocklist[0],str(Stocklist[1]))
    mycursor2.execute(sql_1, val_1)
    mydb.commit()
