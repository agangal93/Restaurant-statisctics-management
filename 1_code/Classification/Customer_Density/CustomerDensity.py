# Written by: Yashasvi Khatavakar
# Tested by: Yashasvi Khatavakar

import mysql.connector
import numpy as np
import random
import datetime
from datetime import date
from datetime import timedelta
#import pandas as pd
#import math
#import statistics





w={'8-12':13,'10-2':25,'2-6':38,'6-10':50}

#print('choose time')
#print(' 8-12')
#print('  10-2')
#print(' 2-6')
#print(' 6-10')
#y=input("enter your choice")


mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="",
                 database="restaurant"
                 )
mycursor = mydb.cursor()
mycursor1 = mydb.cursor()        

mycursor.execute("SELECT * FROM details WHERE Shift = '8-12'"  )
result = mycursor.fetchall()


mycursor.execute("SELECT * FROM details WHERE Shift = '10-2'"  )
result1 = mycursor.fetchall()


mycursor.execute("SELECT * FROM details WHERE Shift = '2-6'"  )
result2 = mycursor.fetchall()


mycursor.execute("SELECT * FROM details WHERE Shift = '6-10'"  )
result3 = mycursor.fetchall()


date1 = datetime.date(2018, 12, 6)
date2 = datetime.date(2018, 12, 18)
day = datetime.timedelta(days=10)

def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

for d in daterange(date1, date2):
    a= random.sample(result,5)
    a1= random.sample(result1,12)
    a2= random.sample(result2,9)
    a3= random.sample(result3,20)

    for i in range(0,len(a)):
        
        a_1=a[i]
        sql = "INSERT INTO allocation (Emp_ID,Name,Shift ,Date) VALUES (%s,%s,%s, %s)"
        val = (a_1[0],a_1[1],a_1[2],d)
        mycursor1.execute(sql, val)
        mydb.commit()


    for i in range(0,len(a1)):
        
        a_1=a1[i]
        sql = "INSERT INTO allocation (Emp_ID,Name,Shift ,Date) VALUES (%s,%s,%s, %s)"
        val = (a_1[0],a_1[1],a_1[2],d)
        mycursor1.execute(sql, val)
        mydb.commit()

    for i in range(0,len(a2)):
        a_1=a2[i]
        
        sql = "INSERT INTO allocation (Emp_ID,Name,Shift ,Date) VALUES (%s,%s,%s, %s)"
        val = (a_1[0],a_1[1],a_1[2],d)
        mycursor1.execute(sql, val)
        mydb.commit()


    for i in range(0,len(a3)):
        a_1=a3[i]
        
        sql = "INSERT INTO allocation (Emp_ID,Name,Shift ,Date) VALUES (%s,%s,%s, %s)"
        val = (a_1[0],a_1[1],a_1[2],d)
        mycursor1.execute(sql, val)
        mydb.commit()