import pygsheets
import pandas as pd
import random
import streamlit as st
#authorization
gc = pygsheets.authorize(service_file='./key/key.json')

# Create empty dataframe
df = pd.DataFrame()

info_list = []
#input
name = str(input("Enter Name:"))
age= str(input("Enter Age:"))
id = n = random.randint(0,100)

info_list.append(name)
info_list.append(age)
# Create a column
df['name'] = [info_list[0]]
df['age'] = [info_list[1]]
df['id'] = [id]

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('test_sheet')
#select the first sheet 
wks = sh[1]
#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))

