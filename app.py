
# Core Pkgs
from select import select
import streamlit as st 
import streamlit.components.v1 as stc 
from home_page import run_home_page
from eda_app import run_table
from ml_app import run_cap
from Recom import run_rec
from streamlit_option_menu import option_menu
import pygsheets
import pandas as pd
import random
from google.oauth2 import service_account
from gsheetsdb import connect



gc = pygsheets.authorize(service_file='./key/key.json')
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Black Friday Sales App</h1>
		<h4 style="color:white;text-align:center;">Happy Thanksgiving</h4>
		</div>
		"""

st.sidebar.title("AIMES")
# 1=sidebar menu, 2=horizontal menu,3=Recommendation, 4=horizontal menu w/ custom menu
EXAMPLE_NO = 1

registered = False

with st.sidebar:
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

    for row in rows:
        st.write(f"Name: {row.name}")
        st.write(f"Age: {row.age}")
    def reg():
        if "first" not in st.session_state:
            st.session_state.first = ""
            st.session_state.last = "18"

        st.button(
            "Register",
            on_click=username_form,
            args=([st.session_state.first + "" + st.session_state.last]),
        )


    def show_names():
        st.write("Name:"+st.session_state.first)
        st.write("Age:"+st.session_state.last)
        st.write("Registered")
        
        # Create empty dataframe
        df = pd.DataFrame()

            #input


            # Create a column
        df['name'] = [st.session_state.first]
        df['age'] = [st.session_state.last]
        df['id'] = [1]

            #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
        sh = gc.open('test_sheet')
            #select the first sheet 
        wks = sh[0]
            #update the first sheet with df, starting at cell B2. 
        wks.set_dataframe(df,(1,1))
        st.write("Entry Written to google sheets")
        st.experimental_singleton.clear()
            
        

    def username_form(name):
        with st.form(key="test", clear_on_submit=True):
            col1, col2 = st.columns(2)
            fname = col1.text_input("Firstname", name.split()[0], key="first")
            age = col2.text_input("Age", name.split()[-1], key="last")
            submit = st.form_submit_button(
                "Submit", on_click=show_names
            )
            
            
            

    reg()
    
        
        

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Activity Info", "Display Table","Visualizations","Recommendations","Game Stats"],  # required
                icons=["house", "book", "table","bar-chart","person","joystick"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
	
    if example == 4:
        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
	

    if example == 5:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

	


selected = streamlit_menu(example=EXAMPLE_NO)
if selected == "Home":
	run_home_page()
	pass
elif selected == "Activity Info":
	run_cap()
elif selected == "Recommendations":
	run_rec()
elif selected == "Display Table":
    run_table()


	



