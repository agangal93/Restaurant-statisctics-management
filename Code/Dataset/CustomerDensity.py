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
        self.customer_per_time = {"Breakfast":15, "Lunch":30, "Snacks":5, "Dinner":50}
        self.num_customers_per_day = 500

    def GetKeyByValue(self,dictOfWords, Value):
        for (key, value) in dictOfWords.items():
            if Value in value:
                break
        return key

    def GetFoodCategory(self,Time):
        return self.GetKeyByValue(self.food_type,Time)

    def RoundingCorrection(self,arr,perc):
        entries_per_type = math.floor((perc/100)*self.num_customers_per_day)
        length = len(arr)
        for row in range(0,length):
            total = sum(arr)
            error = entries_per_type - total
            while error > 0:
                arr[random.randint(0,length-1)] += 1
                error -= 1

    def CreateDensityTime(self):
        H = Common.Helper()

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
            base = (base/100)*self.num_customers_per_day
            Time_list[row][1] = math.floor((Time_list[row][1]/100)*base)

        #print(Time_list)
        Breakfast_density = []
        Lunch_density = []
        Snacks_density = []
        Dinner_density = []
        for row in range(0,num_rows):
            if Time_list[row][0] in self.breakfast_time:
                Breakfast_density.append(Time_list[row][1])
            elif Time_list[row][0] in self.lunch_time:
                Lunch_density.append(Time_list[row][1])
            elif Time_list[row][0] in self.snacks_time:
                Snacks_density.append(Time_list[row][1])
            else:
                Dinner_density.append(Time_list[row][1])
        
        self.RoundingCorrection(Breakfast_density,self.customer_per_time.get("Breakfast"))
        self.RoundingCorrection(Lunch_density,self.customer_per_time.get("Lunch"))
        self.RoundingCorrection(Snacks_density,self.customer_per_time.get("Snacks"))
        self.RoundingCorrection(Dinner_density,self.customer_per_time.get("Dinner"))

        total_timezone = [0] * 4
        for row in range(0,num_rows):
            if Time_list[row][0] in self.breakfast_time:
                total_timezone[0] += Time_list[row][1]
            elif Time_list[row][0] in self.lunch_time:
                total_timezone[1] += Time_list[row][1]
            elif Time_list[row][0] in self.snacks_time:
                total_timezone[2] += Time_list[row][1]
            else:
                total_timezone[3] += Time_list[row][1]
        
        # Rounding correction
        length1 = len(self.breakfast_time)
        length2 = length1+len(self.lunch_time)
        length3 = length2+len(self.snacks_time)
        Time_list[random.randint(0,length1-1)][1] += (sum(Breakfast_density) - total_timezone[0])
        Time_list[random.randint(length1,length2-1)][1] += (sum(Lunch_density) - total_timezone[1])
        Time_list[random.randint(length2,length3-1)][1] += (sum(Snacks_density) - total_timezone[2])
        Time_list[random.randint(length3,len(Time_list)-1)][1] += (sum(Dinner_density) - total_timezone[3])
        #print(Time_list)
        TableEntry = list()
        TableEntry = [[]]*self.num_customers_per_day
        count = np.zeros(num_rows)
        for entry in range(0,self.num_customers_per_day):
            row = random.randint(0,num_rows-1)
            while(count[row] >= Time_list[row][1]):
                row = random.randint(0,num_rows-1)
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
        
        # Final entry values
        print(TableEntry)
