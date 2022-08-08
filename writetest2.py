import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pygsheets
import pandas as pd
gc = pygsheets.authorize(service_file='./key/key.json')

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows


sh = gc.open('test_sheet')
wks = sh[0]
row_count = len(wks.get_all_records()) + 2
st.write("current row:"+str(row_count))


sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

ds = pd.DataFrame(rows)
st.table(ds)
last_user = ds.iloc[-1].values[0]
st.write(last_user)
st.write("Total Rows:"+str(len(ds.index)))
