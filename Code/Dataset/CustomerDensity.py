import numpy as np
import pandas as pd
import math
import statistics
import random
import Common

class DensityTime:

    def __init__(self):
        self.breakfast_time = ["06:00", "07:00", "08:00","09:00","10:00","11:00"]
        self.lunch_time = ["12:00", "13:00", "14:00","15:00"]
        self.snacks_time = ["16:00", "17:00"]
        self.dinner_time = ["18:00", "19:00", "20:00","21:00","22:00","23:00"]
        self.food_type = {"Breakfast":self.breakfast_time,"Lunch":self.lunch_time,"Snacks":self.snacks_time,"Dinner":self.dinner_time}
        self.customer_per_time = {"Breakfast":50, "Lunch":200, "Snacks":20, "Dinner":230}

    def GetKeyByValue(self,dictOfWords, Value):
        for (key, value) in dictOfWords.items():
            if Value in value:
                break
        return key

    def GetFoodCategory(self,Time):
        return self.GetKeyByValue(self.food_type,Time)

    def CreateDensityTime(self):
        H = Common.Helper()

        num_customers_per_day = 500
        breakfast_menu = []
        breakfast_menu.append(H.Foodtype.get("Bakeries"))
        breakfast_menu.append(H.Foodtype.get("Sandwich shop"))

        lunch_menu = []
        lunch_menu.append(H.Foodtype.get("Pizza"))
        lunch_menu.append(H.Foodtype.get("Mexican"))

        snacks_menu = []
        snacks_menu.append(H.Foodtype.get("Bakeries"))
        snacks_menu.append(H.Foodtype.get("Sandwich shop"))
        snacks_menu.append(H.Foodtype.get("Ice cream"))

        dinner_menu = []
        dinner_menu.append(H.Foodtype.get("Steak and BBQ"))
        dinner_menu.append(H.Foodtype.get("Chinese"))

        df = pd.read_csv('TimeVsCustomer.csv')
        num_rows = df.shape[0] - 1
        num_columns = df.shape[1]
        Time_list = [[0 for x in range(num_columns)] for x in range(num_rows)]
        for row in range(0,num_rows):
            for column in range(0,num_columns):
                Time_list[row][column] = df.iloc[row][column]
        
        for row in range(0,num_rows):
            if Time_list[row][0] in self.breakfast_time:
                base = self.customer_per_time.get("Breakfast")
            elif Time_list[row][0] in self.lunch_time:
                base = self.customer_per_time.get("Lunch")
            elif Time_list[row][0] in self.snacks_time:
                base = self.customer_per_time.get("Snacks")
            else:
                base = self.customer_per_time.get("Dinner")
            Time_list[row][1] = math.floor((Time_list[row][1]/100)*base)

        print(Time_list)

        # Add correction


        TableEntry = list()
        TableEntry = [[]]*num_customers_per_day
        count = np.zeros(num_rows)
        for entry in range(0,num_customers_per_day):
            row = random.randint(0,num_rows-1)
            #while(count[row] >= Time_list[row][1]):
            #    row = random.randint(0,num_rows-1)
            FoodCategory = self.GetFoodCategory(Time_list[row][0])
            if FoodCategory == "Breakfast":
                FoodEntry = breakfast_menu[random.randint(0,len(breakfast_menu)-1)]
            elif FoodCategory == "Lunch":
                FoodEntry = lunch_menu[random.randint(0,len(lunch_menu)-1)]
            elif FoodCategory == "Snacks":
                FoodEntry = snacks_menu[random.randint(0,len(snacks_menu)-1)]
            else:
                FoodEntry = dinner_menu[random.randint(0,len(dinner_menu)-1)]
            Entry_Value = FoodEntry[random.randint(0,len(FoodEntry)-1)]
            TableEntry[entry] = [Time_list[row][0],Time_list[row][1],Entry_Value]
            count[row] += 1

        print(count)
        print(TableEntry)
