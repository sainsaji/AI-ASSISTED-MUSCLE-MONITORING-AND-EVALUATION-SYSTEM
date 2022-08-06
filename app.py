
# Core Pkgs
from select import select
import streamlit as st 
import streamlit.components.v1 as stc 
from home_page import run_home_page
from eda_app import run_eda
from ml_app import run_ml
from Recom import run_Recom
from streamlit_option_menu import option_menu

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Black Friday Sales App</h1>
		<h4 style="color:white;text-align:center;">Happy Thanksgiving</h4>
		</div>
		"""

st.sidebar.title("AIMES")
# 1=sidebar menu, 2=horizontal menu,3=Recommendation, 4=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
                icons=["house", "book", "envelope"],  # optional
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
elif selected == "EDA":
	run_eda()
elif selected == "ML":
	run_ml()
elif selected == "Activity Info":
	run_ml()
elif selected == "Recommendations":
	run_Recom()
else:
    st.subheader("About")
    st.info("Built with Streamlit")
	


# # Core Pkgs
# import streamlit as st 
# import streamlit.components.v1 as stc 
# from home_page import run_home_page
# from eda_app import run_eda
# from ml_app import run_ml
# from streamlit_option_menu import option_menu

# html_temp = """
# 		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
# 		<h1 style="color:white;text-align:center;">Black Friday Sales App</h1>
# 		<h4 style="color:white;text-align:center;">Happy Thanksgiving</h4>
# 		</div>
# 		"""

# def main():
# 	stc.html(html_temp)
# 	menu = ["Home","EDA","ML","About"]
# 	choice = st.sidebar.selectbox("Menu",menu)

# 	if choice == "Home":
# 		run_home_page()
# 		pass
# 	elif choice == "EDA":
# 		run_eda()
# 	elif choice == "ML":
# 		run_ml()
# 	else:
# 		st.subheader("About")
# 		st.info("Built with Streamlit")
# 		st.text("Jesus Saves @JCharisTech")
# 		st.text("Jesse E.Agbe(JCharis)")



# if __name__ == '__main__':
# 	main()
