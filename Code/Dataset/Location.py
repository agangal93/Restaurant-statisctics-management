import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import random
from scipy.stats import norm
import Common

class Location:

    def __init__(self):
        self.east_zone = ["New York", "Maryland", "Virginia", "New Jersey"]
        self.north_zone = ["Wisconsin", "Minnesota", "North Dakota", "Michigan"]
        self.west_zone = ["California", "Washington", "Arizona", "Oregon"]
        self.south_zone = ["Texas", "New Mexico", "Mississippi", "Georgia"]
        self.central_zone = ["Colorado", "Utah", "Nebraska", "Kansas"]
        self.zone_data = {0:"EZ", 1:"NZ", 2:"WZ", 3:"SZ", 4:"CZ"}
    
    def CreateLocationDataset(self):
        H = Common.Helper()
        df = pd.read_csv('Statefood.csv')

        east_food = np.zeros(df.shape[1]-1)
        north_food = np.zeros(df.shape[1]-1)
        west_food = np.zeros(df.shape[1]-1)
        south_food = np.zeros(df.shape[1]-1)
        central_food = np.zeros(df.shape[1]-1)
        for column in range(1,df.shape[1]):
            for row in range(1,df.shape[0]):
                value = df.iloc[row][column]
                if df.iloc[row][0] in self.east_zone:
                    east_food[column-1] = east_food[column-1] + value
                elif df.iloc[row][0] in self.north_zone:
                    north_food[column-1] = north_food[column-1] + value
                elif df.iloc[row][0] in self.west_zone:
                    west_food[column-1] = west_food[column-1] + value
                elif df.iloc[row][0] in self.south_zone:
                    south_food[column-1] = south_food[column-1] + value
                else:
                    central_food[column-1] = central_food[column-1] + value
            east_food[column-1] = round(east_food[column-1]/len(east_food),2)
            north_food[column-1] = round(north_food[column-1]/len(north_food),2)
            west_food[column-1] = round(west_food[column-1]/len(west_food),2)
            south_food[column-1] = round(south_food[column-1]/len(south_food),2)
            central_food[column-1] = round(central_food[column-1]/len(central_food),2)

        # Dataset measurement base value 
        base = 10000

        H.CalPercentage(east_food,base)
        H.CalPercentage(north_food,base)
        H.CalPercentage(west_food,base)
        H.CalPercentage(south_food,base)
        H.CalPercentage(central_food,base)
        zone_food = np.stack((east_food,north_food,west_food,south_food,central_food))
        print(zone_food)

        num_rows = len(zone_food)
        num_columns = len(zone_food[0])

        total_zone = [0] * num_rows
        H.GetTotalForRows(zone_food,total_zone,num_rows)
        print(total_zone)

        # Find scaled percentages
        for value in range(0,num_rows):
            H.CalPercentage(zone_food[value],total_zone[value])

        print("Scaled percentage")
        print(zone_food)

        num_entries = 500

        entries_per_zone = num_entries/num_rows
        for row in range(0,num_rows):
            for column in range(0,num_columns):
                zone_food[row][column] = math.floor(zone_food[row][column]/100 * entries_per_zone)

        # Rounding correction
        for row in range(0,num_rows):
            total = sum(zone_food[row,:])
            error = entries_per_zone - total
            while error > 0:
                zone_food[row][random.randint(0,num_rows-1)] += 1
                error -= 1

        print("Correction") 
        print(zone_food)
        count = np.zeros((num_rows,num_columns))
        Foodtype = H.GetFoodType();
        FoodData = H.GetFoodData();
        TableEntry = list()
        TableEntry = [[]]*num_entries
        max = len(Foodtype.get(FoodData.get(0)))
        # Find max length
        for type in range(1,len(FoodData)):
            if max < len(Foodtype.get(FoodData.get(type))):
                max = len(Foodtype.get(FoodData.get(type)))

        FoodCategory = np.zeros(max)
        for entry in range(0,num_entries):    
            row = random.randint(0,num_rows-1)
            column = random.randint(0, num_columns-1)
            while(count[row][column] >= zone_food[row][column]):
                row = random.randint(0,num_rows-1)
                column = random.randint(0, num_columns-1)
            ZoneValue = self.zone_data.get(row)
            FoodType = FoodData.get(column)
            FoodCategory = Foodtype.get(FoodType)
            FoodEntry = FoodCategory[random.randint(0,len(FoodCategory)-1)]
            TableEntry[entry] = [ZoneValue,FoodEntry]
            count[row][column] += 1

        print(TableEntry)
        #plt.title('PDF')
        #plt.xlabel('Food Type')
        #plt.ylabel('Probability')
        #plt.legend()
        #plt.show()
