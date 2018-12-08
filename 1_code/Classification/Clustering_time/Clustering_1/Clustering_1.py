import mysql.connector
import numpy as np
import Common
import matplotlib.pyplot as plt
#import pandas as pd
#import math
#import statistics

# Classify data based on variation in time from the entries in each subset
#
H = Common.Helper()
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="restaurant"
            )
mycursor = mydb.cursor()
#mycursor1 = mydb.cursor()
#mycursor2 = mydb.cursor()

num_entries = H.GetNumSubsetEntries()
num_subsets = H.GetNumSubsets()

subcluster_Inc = np.zeros((len(H.GetDistIncrease()),num_subsets))
subcluster_Dec = np.zeros((len(H.GetDistDecrease()),num_subsets))
subcluster_Gaus = np.zeros((len(H.GetDistGaussian()),num_subsets))
Increase = [[]] * len(H.GetDistIncrease())
index = 0
for key,val in H.GetDistIncrease().items():
    Increase[index] = [key,val]
    index += 1

Decrease = [[]] * len(H.GetDistDecrease())
index = 0
for key,val in H.GetDistDecrease().items():
    Decrease[index] = [key,val]
    index += 1

Gaussian = [[]] * len(H.GetDistGaussian())
index = 0
for key,val in H.GetDistGaussian().items():
    Gaussian[index] = [key,val]
    index += 1

mycursor.execute("SELECT * FROM variation")
for set in range(0,num_subsets):
    Datset_table = mycursor.fetchmany(num_entries)

    for entry in Datset_table:
        found = False
        # Increase
        count = 0
        for inc_entry in Increase:
            if inc_entry[0] in entry and inc_entry[1] in entry:
                subcluster_Inc[count][set] += 1
                found= True
                break
            count += 1


        # Decrease
        if not found:
            count = 0
            for dec_entry in Decrease:
                if dec_entry[0] in entry and dec_entry[1] in entry:
                    subcluster_Dec[count][set] += 1
                    found = True
                    break
                count += 1

        # Gaussian
        if not found:
            count = 0
            for gaus_entry in Gaussian:
                if gaus_entry[0] in entry and gaus_entry[1] in entry:
                    subcluster_Gaus[count][set] += 1
                    break
                count += 1

t = np.arange(0, 10, 2)

# Scale up values for a month
for count in range(0,len(subcluster_Inc)):
    for set in range(0,len(subcluster_Inc[0])):
        subcluster_Inc[count][set] = subcluster_Inc[count][set] * 10

for count in range(0,len(subcluster_Dec)):
    for set in range(0,len(subcluster_Dec[0])):
        subcluster_Dec[count][set] = subcluster_Dec[count][set] * 10

for count in range(0,len(subcluster_Gaus)):
    for set in range(0,len(subcluster_Gaus[0])):
        subcluster_Gaus[count][set] = subcluster_Gaus[count][set] * 10

print("Cluster data")
print("Increase\n")
print(subcluster_Inc)
print("\nDecrease\n")
print(subcluster_Dec)
print("\nGaussian\n")
print(subcluster_Gaus)

# Increase
fig = plt.figure()
for val in range(0,len(subcluster_Inc)):
    subplt = "13" + str(val + 1)
    ax = fig.add_subplot(subplt)
    ax.plot(t,subcluster_Inc[val])
    ax.grid()
    title = H.GetKeyByValue(H.GetDistIncrease(),H.GetZoneMap().get(val),True) + " - " + H.GetZoneMap().get(val)
    ax.set_title(title)
    ax.set_xlabel('Months');
    ax.set_ylabel('Orders');

plt.show()

fig = plt.figure()
for val in range(0,len(subcluster_Dec)):
    subplt = "13" + str(val + 1)
    ax = fig.add_subplot(subplt)
    ax.plot(t,subcluster_Dec[val])
    ax.grid()
    title = H.GetKeyByValue(H.GetDistDecrease(),H.GetZoneMap().get(val),True) + " - " + H.GetZoneMap().get(val)
    ax.set_title(title)
    ax.set_xlabel('Months');
    ax.set_ylabel('Orders');

plt.show()

fig = plt.figure()
for val in range(0,len(subcluster_Gaus)):
    subplt = "13" + str(val + 1)
    ax = fig.add_subplot(subplt)
    ax.plot(t,subcluster_Gaus[val])
    ax.grid()
    title = H.GetKeyByValue(H.GetDistGaussian(),H.GetZoneMap().get(val),True) + " - " + H.GetZoneMap().get(val)
    ax.set_title(title)
    ax.set_xlabel('Months');
    ax.set_ylabel('Orders');

plt.show()
