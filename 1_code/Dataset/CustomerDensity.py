import mysql.connector
import numpy as np
import pandas as pd
import math
import statistics
import random
import Common
import Location
import Dataethnic

## DensityTime - Class for generation of Customer Density Vs Time matrix
#
# The input for this class will be the Location and Ethnicity matrices. It will combine these inputs
# with the Desnity time data to generate the final Dataset. Each table entry will be inserted into a MySQL database
#  
class DensityTime:
    ## The constructor. Includes Time division, food type and customer specific dictionaries
    # @param self The object pointer
    def __init__(self):
        self.breakfast_time = ["06:00", "07:00", "08:00","09:00","10:00","11:00"]
        self.lunch_time = ["12:00", "13:00", "14:00","15:00"]
        self.snacks_time = ["16:00", "17:00"]
        self.dinner_time = ["18:00", "19:00", "20:00","21:00","22:00","23:00"]
        self.food_type = {"Breakfast":self.breakfast_time,"Lunch":self.lunch_time,"Snacks":self.snacks_time,"Dinner":self.dinner_time}
        self.customer_per_time = {"Breakfast":15, "Lunch":30, "Snacks":5, "Dinner":50}
        self.breakfast_menu = []
        self.lunch_menu = []
        self.snacks_menu = []
        self.dinner_menu = []
        self.num_customers = 500        
        self.TableEntry = list()

    ## GetFoodCategory - Get the Food Category for a specific Time input.
    # @param self The object pointer, Time
    # @return Key       
    def GetFoodCategory(self,Time):
        H = Common.Helper()
        return H.GetKeyByValue(self.food_type,Time,False)

    ## RoundingCorrection - Correct the error generated during rounding of floating point values to floor integers
    # @param self The object pointer, array, percentage conversion
    #
    def RoundingCorrection(self,arr,perc):
        assert (self.num_customers > 0),"Num of customers should be positive"
        entries_per_type = math.floor((perc/100)*self.num_customers)
        length = len(arr)
        for row in range(0,length):
            total = sum(arr)
            error = entries_per_type - total
            assert (error >= 0),"Error should not be negative"
            while error > 0:
                arr[random.randint(0,length-1)] += 1
                error -= 1

    ## GetRandomizationRange - Generate a random range of input values for zone and ethnicity based on the 
    #                          computation of previous entries
    # @param - self The object pointer, FoodEntry, FoodCount Table, EthnicCount Table
    # @return - zone_key_list, ethnic_key_list
    def GetRandomizationRange(self,FoodEntry,FoodCount,EthnicCount):
        H = Common.Helper()
        D = Dataethnic.EthnicState()

        zone_key_list = [] * len(H.GetZoneData())
        ethnic_key_list = [[None for x in range(len(D.GetEthnicData()))] for y in range(len(H.GetZoneData()))] 
        index = H.GetFoodEntry().get(FoodEntry)
        assert (index is not None),"Index value should be valid"
        for zone in range(0,len(H.GetZoneData())):
            if FoodCount[zone][index] != 0:
                zone_key_list.append(zone)

        column = 0
        for ethnic in range(0,len(D.GetEthnicData())):
            for zone in zone_key_list:
                if EthnicCount[zone][ethnic] != 0:
                    ethnic_key_list[zone][column] = ethnic
            column += 1

        return zone_key_list,ethnic_key_list

    ## CreateDensityTime - Create the Customer Density vs Time matrix, merge the entries and insert into SQL database
    # @param self The Object pointer, FoodCount table, EthnicCount Table
    #
    def CreateDensityTime(self,FoodCount,EthnicCount):
        H = Common.Helper()
        D = Dataethnic.EthnicState()

        ## @var mydb - SQL connector object.
        #
        #mydb = mysql.connector.connect(
        #  host="localhost",
        #  user="root",
        #  passwd="",
        #  database="restaurant"
        #)
        #mycursor = mydb.cursor()

        self.breakfast_menu += H.Foodtype.get("Bakeries")
        self.breakfast_menu += H.Foodtype.get("Sandwich shop")

        self.lunch_menu += H.Foodtype.get("Pizza")
        self.lunch_menu += H.Foodtype.get("Mexican")

        self.snacks_menu += H.Foodtype.get("Bakeries")
        self.snacks_menu += H.Foodtype.get("Sandwich shop")
        self.snacks_menu += H.Foodtype.get("Ice cream")

        self.dinner_menu += H.Foodtype.get("Steak and BBQ")
        self.dinner_menu += H.Foodtype.get("Chinese")

        self.num_customers = H.GetNumEntries()
        ## @var df - Pandas Data frame to get entries from csv file
        #
        df = pd.read_csv('TimeVsCustomer.csv')
        num_rows = df.shape[0] - 1
        num_columns = df.shape[1]
        ## @var Time_list - Customer Density list for each time zone
        #
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
            base = (base/100)*self.num_customers
            assert (base > 0), "Invalid base"
            Time_list[row][1] = math.floor((Time_list[row][1]/100)*base)

        #print(Time_list)
        ## @var Breakfast_density, Lunch_density, Snacks_density, Dinner_density - Cusomter density for respective zones
        #
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
        
        ## Add Rounding Correction for each time zone.
        #
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
        
        ## Remove the error introduced during earlier steps
        #
        length1 = len(self.breakfast_time)
        length2 = length1 + len(self.lunch_time)
        length3 = length2 + len(self.snacks_time)
        Time_list[random.randint(0,length1-1)][1] += (sum(Breakfast_density) - total_timezone[0])
        Time_list[random.randint(length1,length2-1)][1] += (sum(Lunch_density) - total_timezone[1])
        Time_list[random.randint(length2,length3-1)][1] += (sum(Snacks_density) - total_timezone[2])
        Time_list[random.randint(length3,len(Time_list)-1)][1] += (sum(Dinner_density) - total_timezone[3])

        ## @ self.TableEntry - Combined table entries size - num_customers
        self.TableEntry = [[]]*self.num_customers
        count = np.zeros(num_rows)
        for entry in range(0,self.num_customers):
            EntryAdded = False
            while EntryAdded == False:
                row = random.randint(0,num_rows-1)
                ## @var FoodCategory - Type of Food according to the time zone
                #
                FoodCategory = self.GetFoodCategory(Time_list[row][0])
                if FoodCategory == "Breakfast":
                    Entry_Value = self.breakfast_menu[random.randint(0,len(self.breakfast_menu)-1)]
                elif FoodCategory == "Lunch":
                    Entry_Value = self.lunch_menu[random.randint(0,len(self.lunch_menu)-1)]
                elif FoodCategory == "Snacks":
                    Entry_Value = self.snacks_menu[random.randint(0,len(self.snacks_menu)-1)]
                else:
                    Entry_Value = self.dinner_menu[random.randint(0,len(self.dinner_menu)-1)]

                assert (Entry_Value is not None), "Invalid Food Entry"
                Type_of_Food = H.GetFoodCategory(Entry_Value)
                ## @var zone_key_list - List zones suitable for a given FoodEntry
                #  @var ethnic_key_list - List of ethnicities for a given list of Zones
                zone_key_list, ethnic_key_list = self.GetRandomizationRange(Entry_Value,FoodCount,EthnicCount)

                if not zone_key_list:
                    continue

                retry_count = 10
                ## @var Zone_Key - random value from zone_key_list
                #  @var Zone - Zone value for Zone_Key
                #
                Zone_Key = zone_key_list[random.randint(0,len(zone_key_list)-1)]
                assert (Zone_Key is not None), "Invalid Zone key"
                Zone = H.GetZoneData().get(Zone_Key)
                if FoodCount[Zone_Key][H.GetFoodEntry().get(Entry_Value)] == 0:
                    while (FoodCount[Zone_Key][H.GetFoodEntry().get(Entry_Value)] == 0) and (retry_count > 0):
                        Zone_Key = random.randint(0,len(H.GetZoneData())-1)
                        Zone = H.GetZoneData().get(Zone_Key)
                        retry_count -= 1
                    if retry_count == 0:
                        continue

                if not ethnic_key_list[Zone_Key]:
                    continue

                ## @var ethnic_list_mod - Remove None value entries from ethnic_key_list
                #
                ethnic_list_mod = []
                for x in range(0,len(ethnic_key_list[Zone_Key])):
                    if ethnic_key_list[Zone_Key][x] is not None:
                        ethnic_list_mod.append(ethnic_key_list[Zone_Key][x])

                retry_count = 20
                ## @var Ethnic_Key - random value from ethnic_mod_list
                #  @var Ethnicity - Ethnicity value for Ethnic_key
                #
                Ethnic_Key = ethnic_list_mod[random.randint(0,len(ethnic_list_mod)-1)]
                assert (Ethnic_Key is not None), "Invalid Ethnic key"
                Ethnicity = D.GetEthnicData().get(Ethnic_Key)
                if EthnicCount[Zone_Key][Ethnic_Key] == 0:
                    while (EthnicCount[Zone_Key][Ethnic_Key] == 0) and (retry_count > 0):
                        Ethnic_Key = random.randint(0,len(D.GetEthnicData())-1)
                        Ethnicity = D.GetEthnicData().get(Ethnic_Key)
                        retry_count -= 1
                    if retry_count == 0:
                        continue

                ## @var Price - Price for given food entry
                #
                Price = H.GetPriceItem().get(Entry_Value)
                assert (FoodCount[Zone_Key][H.GetFoodEntry().get(Entry_Value)] > 0)
                FoodCount[Zone_Key][H.GetFoodEntry().get(Entry_Value)] -= 1
                assert (EthnicCount[Zone_Key][Ethnic_Key] > 0)
                EthnicCount[Zone_Key][Ethnic_Key] -= 1

                self.TableEntry[entry] = [Time_list[row][0],Zone,Type_of_Food,Entry_Value,Price,Time_list[row][1],Ethnicity]

                ## @var sql - MySQL query to insert the table entry into the database
                #
                #sql = "INSERT INTO users (Time,Zone,Type_of_Food,Food,Price,Density,Ethnicity) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                #val = (Time_list[row][0],Zone,Type_of_Food,Entry_Value,Price,Time_list[row][1],Ethnicity)
                #mycursor.execute(sql, val)
                #mydb.commit()
                count[row] += 1
                EntryAdded = True
        # Final entry values
        print(self.TableEntry)
