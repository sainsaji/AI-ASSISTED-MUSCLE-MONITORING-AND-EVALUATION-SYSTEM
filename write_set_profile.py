from operator import contains
import pygsheets
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import date
import streamlit as st



#authorization
gc = pygsheets.authorize(service_file='./key/key.json')

#setting profile coloumns
profile_info= {
    'profile_id':[],
    'name':[],
    'age':[],
    'contact' :[],
    'activity_level':[],
    'date':[]
            }

#convert columns to data frame
ds = pd.DataFrame(profile_info)

#open sheet
sh = gc.open('test_sheet')

#select work sheet and write dataframe

#select the first sheet 
wks = sh[0]
#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(ds,(1,1))

#create writer funtion to write to profile
def profile_writer(name,age,contact):
    row_count = len(wks.get_all_records()) + 2
    id=row_count-1
    activity_level = ""
    now_date = str(date.today())
    data1=[id,name,age,contact,activity_level,now_date]
    wks.append_table(data1,start='2')

# profile_writer(name="test",age="22",contact="91173377373")

st.title("Registartion")
st.subheader("Enter the details")
with st.form(key="reg_form"):
    name = st.text_input("Enter Your Name")
    contact = st.text_input("Enter Your number")
    age = st.slider("Enter your age")
    sub = st.form_submit_button("Submit",on_click=profile_writer(name,age,contact))
    if sub:
        st.write("Written to DB")

