import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import random
from scipy.stats import norm

class ethnicState:

    def __init__(self):
        self.ethnic = ["white","black","hispianic","asian"]
        self.east_zone = ["New York", "Maryland", "Virginia", "New Jersey"]
        self.north_zone = ["Wisconsin", "Minnesota", "North Dakota", "Michigan"]
        self.west_zone = ["California", "Washington", "Arizona", "Oregon"]
        self.south_zone = ["Texas", "New Mexico", "Mississippi", "Georgia"]
        self.central_zone = ["Colorado", "Utah", "Nebraska", "Kansas"]
        self.zone_data = {0:"EZ", 1:"NZ", 2:"WZ", 3:"SZ", 4:"CZ"}
        self.ethnic_data = {0:"white", 1:"black", 2:"hispianic", 3:"asian"}

    def GetZoneDistribution(self):
        return self.zone_data

    def CalPercentage(self,arr,base):
        for row in range(0,len(arr)):
            arr[row] = round((arr[row]/base)*100,2)

E = ethnicState()
df = pd.read_csv('ethnicity.csv')

east_food = np.zeros(df.shape[1]-1)
north_food = np.zeros(df.shape[1]-1)
west_food = np.zeros(df.shape[1]-1)
south_food = np.zeros(df.shape[1]-1)
central_food = np.zeros(df.shape[1]-1)
for column in range(1,df.shape[1]):
    for row in range(1,df.shape[0]):
        value = df.iloc[row][column]
        if df.iloc[row][0] in E.east_zone:
            east_food[column-1] = east_food[column-1] + value
        elif df.iloc[row][0] in E.north_zone:
            north_food[column-1] = north_food[column-1] + value
        elif df.iloc[row][0] in E.west_zone:
            west_food[column-1] = west_food[column-1] + value
        elif df.iloc[row][0] in E.south_zone:
            south_food[column-1] = south_food[column-1] + value
        else:
            central_food[column-1] = central_food[column-1] + value
    east_food[column-1] = round(east_food[column-1]/len(east_food),2)
    north_food[column-1] = round(north_food[column-1]/len(north_food),2)
    west_food[column-1] = round(west_food[column-1]/len(west_food),2)
    south_food[column-1] = round(south_food[column-1]/len(south_food),2)
    central_food[column-1] = round(central_food[column-1]/len(central_food),2)

base = 10000
#F.CalPercentage(east_food,base)
#F.CalPercentage(north_food,base)
#F.CalPercentage(west_food,base)
#F.CalPercentage(south_food,base)
#F.CalPercentage(central_food,base)
zone_food = np.stack((east_food,north_food,west_food,south_food,central_food))
print(zone_food)

num_rows = len(zone_food)
num_columns = len(zone_food[0])

print(num_rows)
print(num_columns)
total_zone = [0] * num_rows
for value in range(0,num_rows):
    total_zone[value] = sum(zone_food[value,:])
print(total_zone)

# Find scaled percentages
for value in range(0,num_rows):
    E.CalPercentage(zone_food[value],total_zone[value])

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
        zone_food[row][random.randint(0,num_columns-1)] += 1
        error -= 1

print("Correction") 
print(zone_food)
count = np.zeros((num_rows,num_columns))
TableEntry = list()
TableEntry = [[]]*num_entries
for entry in range(0,num_entries):
    row = random.randint(0,num_rows-1)
    column = random.randint(0, num_columns-1)
    while(count[row][column] >= zone_food[row][column]):
        row = random.randint(0,num_rows-1)
        column = random.randint(0, num_columns-1)
    ZoneValue = E.zone_data.get(row)
    ethnic = E.ethnic_data.get(column)
    TableEntry[entry] = [ZoneValue,ethnic]
    count[row][column] += 1

#num_datasets = 3
#num_entries_per_set = math.floor(num_entries/num_datasets)
print(TableEntry)
#plt.title('PDF')
#plt.xlabel('Food Type')
#plt.ylabel('Probability')
#plt.legend()
#plt.show()

