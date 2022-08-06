# import streamlit as st
# from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="Multipage App",
#     page_icon="👋",
# )

# st.title("Main Page")
# st.sidebar.success("Select a page above.")




# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

from calendar import c
import streamlit as st
from multiapp import MultiApp
from pages import a_info, display_T, recom # import your app modules here
from icons import che # import your app modules here
app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Home", a_info.app)
app.add_app("Data", display_T.app)
app.add_app("Check", che.app)
# The main app
app.run()