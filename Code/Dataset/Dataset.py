import Common
import Location
import CustomerDensity
import Dataethnic

import pandas as pd
import numpy as np

H = Common.Helper()
L = Location.Location()
E = Dataethnic.EthnicState()
C = CustomerDensity.DensityTime()

# Module unit test OR Dataset creation
test = 0

if not test:
    FoodCount = L.CreateLocationDataset()
    EthnicCount = E.CreateEthnicset()
    C.CreateDensityTime(FoodCount,EthnicCount)
else:
    # Zone Test Case
    zone_entry = np.array([[35,21,13,8,6,10,16],
                           [31,17,16,7,7,11,8],
                           [21,19,12,8,19,8,10],
                           [19,15,12,15,20,8,8],
                           [23,18,14,12,16,8,7]])
    FoodCount = L.CreateLocationDataset()

    count = np.zeros((len(zone_entry),len(zone_entry[0])))
    for row in range(0,len(zone_entry)):
        for column in range(0,len(FoodCount[0])):
            Key_1 = H.GetKeyByValue(H.GetFoodEntry(),column,True)
            if H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Pizza":
                count[row][0] += FoodCount[row][column]
            elif H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Bakeries":
                count[row][1] += FoodCount[row][column]
            elif H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Sandwich shop":
                count[row][2] += FoodCount[row][column]
            elif H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Steak and BBQ":
                count[row][3] += FoodCount[row][column]
            elif H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Mexican":
                count[row][4] += FoodCount[row][column]
            elif H.GetKeyByValue(H.GetFoodType(),Key_1,False) == "Ice cream":
                count[row][5] += FoodCount[row][column]
            else:
                count[row][6] += FoodCount[row][column]

    print(count)
    print(zone_entry)
