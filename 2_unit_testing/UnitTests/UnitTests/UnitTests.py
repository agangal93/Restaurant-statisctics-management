import sys
import random
import pandas as pd
import numpy as np
import Common

# Compare the update count of ingredients
def UpdateAvailableCount(Action):
    H = Common.Helper()

    # Initial List
    Ingredientdf = pd.read_csv("Ingredients1.csv")
    Ingredientlist = Ingredientdf.values
    num_ing = len(Ingredientlist)

    row = random.randint(0,num_ing-1)
    Ingredient = Ingredientlist[row][0]

    Change = random.randint(1,50)

    # Update values
    if Action == "Stock":
        Ingredientlist[row][1] += Change
        expected_value = Ingredientlist[row][1]
    elif Action == "Consume":
        Ingredientlist[row][1] -= Change
        expected_value = Ingredientlist[row][1]
    else:
        assert(0)

    Ingredientdf = pd.DataFrame(data=Ingredientlist, index=Ingredientdf.index, columns=Ingredientdf.columns)
    Ingredientdf.to_csv("InventoryList_1.csv",encoding='utf-8')

    # Read new list and compare the count
    Ingredientdf1 = pd.read_csv("InventoryList_1.csv")
    Ingredientlist_new = Ingredientdf1.values
    
    if Ingredientlist_new[row][2] == expected_value:
        print("Test passed")
    else:
        print("Test failed")


def UpdateIngredient(Ingredient):

    print("Ingredient - %s"%Ingredient)
    Ingredientdf = pd.read_csv("Ingredients1.csv")
    Ingredientlist = Ingredientdf.values
    num_ing = len(Ingredientlist)

    #row = Ingredientlist.index(Ingredient)
    row = np.in1d(Ingredientlist[:,0],Ingredient)
    row_val = np.argmax(row)
    Ingredientlist = np.delete(Ingredientlist,row_val,0)

    if Ingredient in Ingredientlist:
        print("Test failed");
    else:
        print("Test passed");
        

def CheckRefill(Ingredient, change_value, condition):

    print("Ingredient - %s"%Ingredient)
    print("Stock value = %d"%change_value)
    Ingredientdf = pd.read_csv("Ingredients1.csv")
    Ingredientlist = Ingredientdf.values
    num_ing = len(Ingredientlist)

    row = np.in1d(Ingredientlist[:,0],Ingredient)
    row_val = np.argmax(row)
    row = row_val

    New_value = Ingredientlist[row][1] * change_value / 100
    if condition == "Refill":
        change_value = change_value - 1
    elif condition == "InStock":
        change_value = change_value + 1
    else:
        assert(0)

    Ingredientlist[row][1] = Ingredientlist[row][1] - ((Ingredientlist[row][1] * (100 - change_value)) / 100)

    Ingredientdf = pd.DataFrame(data=Ingredientlist, index=Ingredientdf.index, columns=Ingredientdf.columns)
    Ingredientdf.to_csv("InventoryList_3.csv",encoding='utf-8')

    # Read new list and compare the count
    Ingredientdf1 = pd.read_csv("InventoryList_3.csv")
    Ingredientlist_new = Ingredientdf1.values

    if condition == "Refill":
        if Ingredientlist_new[row][2] < New_value:
            print("Test passed")
        else:
            print("Test failed")
    elif condition == "InStock":
        if Ingredientlist_new[row][2] >= New_value:
            print("Test passed")
        else:
            print("Test failed")
    else:
        assert(0)

# Unit tests - Run all the module unit tests based on multiple input conditions

H = Common.Helper()
#Inventory tests
print("Unit tests")
print("Inventory\n")

print("\nUpdate Available Count Test")
print("Stock test")
UpdateAvailableCount("Stock")
print("Consume test")
UpdateAvailableCount("Consume")

print("\nUpdate Ingredient Test")
for Ingredient in H.GetIngredientTestList():
    UpdateIngredient(Ingredient)

threshold = 30
print("\nCheck Refill Test")
for Ingredient in H.GetIngredientTestList():
    if random.randint(0,1) is 0:
        condition = "Refill"
        stock_val = random.randint(1,threshold)
    else:
        condition = "InStock"
        stock_val = random.randint(threshold + 1, 90)
    #print("Expected stock value - %d"%stock_val)
    CheckRefill(Ingredient,stock_val,condition)

