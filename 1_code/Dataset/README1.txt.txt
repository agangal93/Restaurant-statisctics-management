This folder contains the code to generate the artificial dataset.

To run the code, use Microsoft visual studio 2017 (or higher) with Python packages (sqlconnector(latest version), numpy, pandas, matplotlib) or
Ananconda - https://www.anaconda.com/download/

Create a users database in MyPhpAdmin on XAMPP server with following columns - 
(Time,Zone,Type_of_Food,Food,Price,Density,Ethnicity)

Dataset.py is the startup file. Run this file to generate 500 dataset Table entries. 
Uncomment the SQL query lines to insert entries into the database.
