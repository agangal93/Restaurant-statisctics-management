This folder contains the complete code for the Foodbyte software 

To run the code, use Microsoft visual studio 2017 (or higher) with Python packages (sqlconnector(latest version), numpy, pandas, matplotlib) installed or
Ananconda - https://www.anaconda.com/download/

Create a users database in MyPhpAdmin on XAMPP server with following columns - 
(Zone,Cusine_type,Cusine,Ethnicity,Price)

Dataset creation - 
Dataset_cusine.py is the startup file to generate the Zone distribution dataset. 
Time_varation.py is the startup file to generate the Time distribution dataset
Run this file to generate 10000 dataset Table entries. 
Uncomment the SQL query lines to insert entries into the database.

Analysis - 
Clustering.py and Clustering_1.py are used for the respective analysis.
CustomerDensity.py is used for employee shift management.
Inventory.py is used for inventory management.
