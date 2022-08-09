import streamlit as st
def start_capture():
    st.write("After Click")
def run_cap():
    cap_button = st.button("Start Capturing",on_click=start_capture) # Give button a variable name
    if cap_button: # Make button a condition.
        start_capture()
run_cap()
