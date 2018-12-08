import mysql.connector
import numpy as np
#import pandas as pd
#import math
#import statistics

mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
         database="menu"
         )
mycursor = mydb.cursor()
Cusine_price = [["Chilaquiles",5.00],["Tacos",6.50],["Enchiladas",5.99],["Quesadillas",6.19],["Pepperoni pizza",15.50],["Spaghetti and meatballs",7.69],["Fettuccine Alfredo",12.99],
                ["Chicken parmesan",16.99],["Turkey and Cheese Sandwich",6.49],["BBQ Bacon Cheeseburger",6.29],["Chicken Fried Steak",11.99],["Chicken Chow Mein",7.35],["Beef Lo Mein",7.75],
                 ["Fried Dumpling",4.95],["Falafel",2.99],["Fattet Hummus",6.99],["Spanakopita",9.95],["Sushi",10.50],["Sashimi",15.99],["Tempura",11.00],["Tonkatsu",15.99],["Tom Yum Goong",8.50],
                  ["Khao Soi",6.50],["Pad See ew",6.99],["Butter Chicken",9.59],["Tandoori Chicken",8.39],["Alu Gobi",5.99]]

for i in range(0,len(Cusine_price)):
   sql = "INSERT INTO fooditem(Fooditem,Price) VALUES (%s,%s)"
   val=Cusine_price[i]

   mycursor.execute(sql,val)
   mydb.commit()
