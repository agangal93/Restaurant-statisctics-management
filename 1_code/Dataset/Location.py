import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import random
#from scipy.stats import norm
import Common

## Location - Class for generation of Location Vs Food Entry matrix
#
# Computes location vs food entry matrix using input CSV file
# 
class Location:
    ## The constructor. Includes Helper object, Food Entry and FoodCount
    # @param self The object pointer
    def __init__(self):
        H = Common.Helper()
        rows = len(H.GetZoneData())
        columns = len(H.GetFoodEntry())
        self.FoodCount = np.zeros((rows,columns))

    ## CreateLocationDataset - Create the Location vs FoodEntry matrix,     
    # @param self The Object pointer
    #
    def CreateLocationDataset(self):
        H = Common.Helper()
        ## @var df - Location vs Food Entry dataframe
        #
        df = pd.read_csv('Statefood.csv')

        ## Zone based location division
        #
        east_food = np.zeros(df.shape[1]-1)
        north_food = np.zeros(df.shape[1]-1)
        west_food = np.zeros(df.shape[1]-1)
        south_food = np.zeros(df.shape[1]-1)
        central_food = np.zeros(df.shape[1]-1)
        for column in range(1,df.shape[1]):
            for row in range(1,df.shape[0]):
                value = df.iloc[row][column]
                if df.iloc[row][0] in H.GetEastZone():
                    east_food[column-1] = east_food[column-1] + value
                elif df.iloc[row][0] in H.GetNorthZone():
                    north_food[column-1] = north_food[column-1] + value
                elif df.iloc[row][0] in H.GetWestZone():
                    west_food[column-1] = west_food[column-1] + value
                elif df.iloc[row][0] in H.GetSouthZone():
                    south_food[column-1] = south_food[column-1] + value
                else:
                    central_food[column-1] = central_food[column-1] + value
            east_food[column-1] = round(east_food[column-1]/len(east_food),2)
            north_food[column-1] = round(north_food[column-1]/len(north_food),2)
            west_food[column-1] = round(west_food[column-1]/len(west_food),2)
            south_food[column-1] = round(south_food[column-1]/len(south_food),2)
            central_food[column-1] = round(central_food[column-1]/len(central_food),2)

        ## Dataset measurement base value 
        #
        base = 10000

        H.CalPercentage(east_food,base)
        H.CalPercentage(north_food,base)
        H.CalPercentage(west_food,base)
        H.CalPercentage(south_food,base)
        H.CalPercentage(central_food,base)
        zone_food = np.stack((east_food,north_food,west_food,south_food,central_food))
        #print(zone_food)

        num_rows = len(zone_food)
        num_columns = len(zone_food[0])

        total_zone = [0] * num_rows
        H.GetTotalForRows(zone_food,total_zone,num_rows)
        #print(total_zone)

        ## Find scaled percentages
        #
        for value in range(0,num_rows):
            H.CalPercentage(zone_food[value],total_zone[value])

        num_entries = H.GetNumEntries()
        entries_per_zone = num_entries/num_rows
        for row in range(0,num_rows):
            for column in range(0,num_columns):
                zone_food[row][column] = math.floor(zone_food[row][column]/100 * entries_per_zone)

        ## Rounding correction
        #
        for row in range(0,num_rows):
            total = sum(zone_food[row,:])
            error = entries_per_zone - total
            assert (error >= 0),"Error should not be negative"
            while error > 0:
                zone_food[row][random.randint(0,num_columns-1)] += 1
                error -= 1

        ## @var TableEntry - Location vs FoodEntry matrix
        #  @var count - Count of each food entry in TableEntry for corresponding location
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
        
        zone_data = H.GetZoneData()
        FoodCategory = np.zeros(max)
        for entry in range(0,num_entries):
            row = random.randint(0,num_rows-1)
            column = random.randint(0, num_columns-1)
            while(count[row][column] >= zone_food[row][column]):
                row = random.randint(0,num_rows-1)
                column = random.randint(0, num_columns-1)
            ZoneValue = zone_data.get(row)
            FoodType = FoodData.get(column)
            FoodCategory = Foodtype.get(FoodType)
            FoodEntry = FoodCategory[random.randint(0,len(FoodCategory)-1)]
            assert (FoodEntry is not None),"Invalid Entry for %r Zone" % ZoneValue
            TableEntry[entry] = [ZoneValue,FoodEntry]
            self.FoodCount[row][H.GetFoodEntry().get(FoodEntry)] += 1
            count[row][column] += 1
        
        return self.FoodCount
        #print(TableEntry)
        #plt.title('PDF')
        #plt.xlabel('Food Type')
        #plt.ylabel('Probability')
        #plt.legend()
        #plt.show()
