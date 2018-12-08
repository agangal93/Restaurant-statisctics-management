import mysql.connector
import numpy as np
import Common
#import pandas as pd
#import math
#import statistics

## ClusterData - Class for classification of entries from the required dataset 
#
# Classify data based on Zone, Ethnicity and Cusine type
#
class ClusterData:
    def __init__(self):
        self.data = []

    def ClassifyEntry(self, zone_value):
        H = Common.Helper()
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="",
                 database="restaurant"
                 )
        mycursor = mydb.cursor()
        mycursor1 = mydb.cursor()

        mycursor.execute("SELECT * FROM users1 WHERE Zone = '%s'" % zone_value)

        EastZone_data = mycursor.fetchall()
        print(zone_value)
        print("\n")
        subcluster1 = []
        subcluster2 = []
        subcluster3 = []
        subcluster4 = []
        subcluster5 = []
        subcluster6 = []
        subcluster7 = []
        subcluster8 = []
        Cusine_map = H.GetCusineMap()
        for entry in EastZone_data:
            if "Mexican" in entry:
                subcluster1.append(entry)
            elif "Italian" in entry:
                subcluster2.append(entry)
            elif "American" in entry:
                subcluster3.append(entry)
            elif "Chinese" in entry:
                subcluster4.append(entry)
            elif "Mediteranean" in entry:
                subcluster5.append(entry)
            elif "Japanese" in entry:
                subcluster6.append(entry)
            elif "Thai" in entry:
                subcluster7.append(entry)
            elif "Indian" in entry:
                subcluster8.append(entry)

        Cluster_length = np.zeros(len(H.GetCusineMap()))
        Cluster_length = [len(subcluster1),len(subcluster2),len(subcluster3),len(subcluster4),
                          len(subcluster5),len(subcluster6),len(subcluster7),len(subcluster8)]

        Max_ethnicity = []
        Min_ethnicity = []
        Min_cusine = []
        # Find maximum popularity cusine
        max_index = np.argmax(Cluster_length)
        Max_Cusine = H.GetCusineMap().get(max_index)
        print("Most Popular ")
        Max_ethnicity.append(Max_Cusine)
        if max_index == 0:
            Max_cluster = subcluster1
        elif max_index == 1:
            Max_cluster = subcluster2
        elif max_index == 2:
            Max_cluster = subcluster3
        elif max_index == 3:
            Max_cluster = subcluster4
        elif max_index == 4:
            Max_cluster = subcluster5
        elif max_index == 5:
            Max_cluster = subcluster6
        elif max_index == 6:
            Max_cluster = subcluster7
        elif max_index == 7:
            Max_cluster = subcluster8

        # Find Ethnicity component
        Max_Ethnic1 = []
        Max_Ethnic2 = []
        Max_Ethnic3 = []
        Max_Ethnic4 = []
        for entry in Max_cluster:
            if "hispanic" in entry:
                Max_Ethnic1.append(entry)
            elif "white" in entry:
                Max_Ethnic2.append(entry)
            elif "black" in entry:
                Max_Ethnic3.append(entry)
            elif "asian" in entry:
                Max_Ethnic4.append(entry)

        Ethnic_val = np.zeros(len(H.GetEthnicData()))
        Ethnic_val = [len(Max_Ethnic1),len(Max_Ethnic2),len(Max_Ethnic3),len(Max_Ethnic4)]
        max_ethnic_index = np.argmax(Ethnic_val)
        Max_ethnicity.append(H.GetEthnicData().get(max_ethnic_index))

        Max_Ethnic_cluster = []
        if max_ethnic_index == 0:
            Max_Ethnic_cluster = Max_Ethnic1
        elif max_ethnic_index == 1:
            Max_Ethnic_cluster = Max_Ethnic2
        elif max_ethnic_index == 2:
            Max_Ethnic_cluster = Max_Ethnic3
        else:
            Max_Ethnic_cluster = Max_Ethnic4
        
        Cusine_len = len(H.GetCusineType().get(Max_Cusine))
        Dish_count = np.zeros(len(H.GetCusine()))
        Dish_count_1 = []
        # Find the most popular dish for this Cusine type in this Ethnicity
        for entry in Max_Ethnic_cluster:
            Dish = entry[3]
            Dish_column = H.GetCusine().get(Dish)
            Dish_count[Dish_column] += 1

        start_index = [i for i, x in enumerate(Dish_count) if x][0]
        for entry in Dish_count:
            if entry:
                Dish_count_1.append(entry)

        #print(Dish_count_1)
        Max_Dish_index = np.argmax(Dish_count_1)
        Max_ethnicity.append(H.GetKeyByValue(H.GetCusine(),(Max_Dish_index + start_index),True))
       
        print(Max_ethnicity)
        print("\n")
##############################################################################################

        # Find minimum popularity cusine
        min_index = np.argmin(Cluster_length)
        Min_Cusine = H.GetCusineMap().get(min_index)
        print("Least Popular ")
        Min_ethnicity.append(Min_Cusine)
        if min_index == 0:
            Min_cluster = subcluster1
        elif min_index == 1:
            Min_cluster = subcluster2
        elif min_index == 2:
            Min_cluster = subcluster3
        elif min_index == 3:
            Min_cluster = subcluster4
        elif min_index == 4:
            Min_cluster = subcluster5
        elif min_index == 5:
            Min_cluster = subcluster6
        elif min_index == 6:
            Min_cluster = subcluster7
        elif min_index == 7:
            Min_cluster = subcluster8

        assert(max_index != min_index), "Incorrect Clustering\n"
        # Find Ethnicity component
        Min_Ethnic1 = []
        Min_Ethnic2 = []
        Min_Ethnic3 = []
        Min_Ethnic4 = []
        for entry in Min_cluster:
            if "hispanic" in entry:
                Min_Ethnic1.append(entry)
            elif "white" in entry:
                Min_Ethnic2.append(entry)
            elif "black" in entry:
                Min_Ethnic3.append(entry)
            elif "asian" in entry:
                Min_Ethnic4.append(entry)

        Ethnic_val1 = np.zeros(len(H.GetEthnicData()))
        Ethnic_val1 = [len(Min_Ethnic1),len(Min_Ethnic2),len(Min_Ethnic3),len(Min_Ethnic4)]
        max_ethnic_index = np.argmax(Ethnic_val1)
        Min_ethnicity.append(H.GetEthnicData().get(max_ethnic_index))

        Min_Ethnic_cluster = []
        if max_ethnic_index == 0:
            Min_Ethnic_cluster = Min_Ethnic1
        elif max_ethnic_index == 1:
            Min_Ethnic_cluster = Min_Ethnic2
        elif max_ethnic_index == 2:
            Min_Ethnic_cluster = Min_Ethnic3
        else:
            Min_Ethnic_cluster = Min_Ethnic4
        
        Dish_count = np.zeros(len(H.GetCusine()))
        Dish_count_1 = []
        # Find the most popular dish for this Cusine type in this Ethnicity
        for entry in Min_Ethnic_cluster:
            Dish = entry[3]
            Dish_column = H.GetCusine().get(Dish)
            Dish_count[Dish_column] += 1

        start_index = [i for i, x in enumerate(Dish_count) if x][0]
        for entry in Dish_count:
            if entry:
                Dish_count_1.append(entry)

        #print(Dish_count_1)
        Min_Dish_index = np.argmax(Dish_count_1)
        Min_ethnicity.append(H.GetKeyByValue(H.GetCusine(),(Min_Dish_index + start_index),True))

        print(Min_ethnicity)
        print("\n")
        sql_1 = "INSERT INTO cluster (Zone,Cusine_type,Cusine,Ethnicity) VALUES (%s,%s,%s,%s)"
        val_1 = (zone_value,Max_ethnicity[0],Max_ethnicity[2],Max_ethnicity[1])
        mycursor1.execute(sql_1, val_1)
        mydb.commit()
        sql_1 = "INSERT INTO cluster (Zone,Cusine_type,Cusine,Ethnicity) VALUES (%s,%s,%s,%s)"
        val_1 = (zone_value,Min_ethnicity[0],Min_ethnicity[2],Min_ethnicity[1])
        mycursor1.execute(sql_1, val_1)
        mydb.commit()
