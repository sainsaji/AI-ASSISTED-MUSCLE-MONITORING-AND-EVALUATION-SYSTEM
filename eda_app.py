# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
from collections.abc import Iterable
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Create a connection object.

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
def run_table():
	credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
	)
	conn = connect(credentials=credentials)

	@st.cache(ttl=600)
	def run_query(query):
		rows = conn.execute(query, headers=1)
		rows = rows.fetchall()
		return rows

	sheet_url = st.secrets["private_gsheets_url"]
	rows = run_query(f'SELECT * FROM "{sheet_url}"')
	test = run_query(f'SELECT age FROM "{sheet_url}"')
	print(type(test))
	df = pd.DataFrame(rows)
	st.table(df)

	# arr = np.random.normal(1, 1, size=100)
	# fig, ax = plt.subplots()
	# ax.hist(arr, bins=20)

	# st.pyplot(fig)

