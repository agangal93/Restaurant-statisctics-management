import mysql.connector
import numpy as np
import names
#import pandas as pd
#import math
#import statistics

mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
         database="employee_shifts"
         )
mycursor = mydb.cursor()

info=[["Vc26","Victorina","8-12"],["Mo01","Mosies","8-12"],["Br96","Breanean","8-12"],["Jp67","Jay","8-12"],["An55","Anna","8-12"],["Jo97","John","8-12"],["Sa10","Sana","8-12"],["Ch45","Christy","8-12"],["Ta14","Tara","8-12"],["Mo33","Moly","8-12"],["Ji33","Jimmy","10-2"],
      ["Za97","Zara","10-2"],["Ot43","Otha","10-2"],["Sa12","Sama","10-2"],["Vi34","Vito","10-2"],["Ga11","Garnet","10-2"],["Ka71","Katrina","10-2"],["An09","Anushka","10-2"],["Sa89","Saba","10-2"],["De51","Deepika","10-2"],["El94","Eloise","10-2"],["Ni33","Nick","10-2"],["Gr34","Grant","10-2"],["Hy54","Hyo","10-2"],["Na76","Narata","10-2"],
      ["Xi61","Xialongu","2-6"],["Lu50","Luigi","2-6"],["Je00","Jewell","2-6"],["Sa18","Santo","2-6"],["Wi43","Will","2-6"],["Po88","Pooja","2-6"],["Mo17","Montana","2-6"],["Ho17","Hoyt","2-6"],["Ai27","Aileen","2-6"],["As34","Asha","2-6"],["Pa12","Padmaja","2-6"],["Pa37","Palmer","2-6"],
      ["Sa73","Sajata","6-10"],["Ja37","Jani","6-10"],["Sh04","Shubham","6-10"],["We08","Weitein","6-10"],["Xi51","Xilu","6-10"],["Ni22","Nicholass","6-10"],["Pi99","Priyanka","6-10"],["Sa26","Samaira","6-10"],["Ha21","Harlan","6-10"],["Gi81","Ginana","6-10"],["Di41","Diara","6-10"],["Sa101","Salman","6-10"],["Sa875","Shaid","6-10"],["Su63","Surbhi","6-10"],["Fa41","Fannah","6-10"],["Su81","Suhani","6-10"],["Yn21","Ynchungi","6-10"],["Zu03","Zunanio","6-10"],["Zu37","Zuchai","6-10"],["Ce343","Cedric","6-10"],]


for i in range(0,57):
   sql = "INSERT INTO details(ID,Name,Shift) VALUES (%s,%s,%s)"
   val=info[i]

   mycursor.execute(sql,val)
   mydb.commit()



