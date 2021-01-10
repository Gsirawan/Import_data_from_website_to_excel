#!/usr/bin/env python
# coding: utf-8

import pandas as pd
line = "============================================================================================"


#loading the wikipedia webpage into the dataframe
data_tables = pd.read_html(input("Please write the full link of your data webpage source:\n"))


#Extract the table in the webpage
table_number = int(input("Please enter the table number (you can find it in the source page):\n"))
the_table = data_tables[table_number]

#display the shape of the dataframe to get the rows count
print(line)
print("the Data Frame shape is : ", the_table.shape)
print(line)

#overview for the table 
the_table.head()


#Save your datafarm table to CSV file
try:
    the_table.to_csv(input(r"Please write the csv file name that want to save (filename.csv): "), index = False)
    print(line)
    print("The file has been successfully saved :)")
except:
    print("Something went wrong while saving the csv file!")

#End




