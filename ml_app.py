import subprocess
import sys
import streamlit as st
act_lev = ""
def run_cap():
	if st.button('Start Monitoring'):
		subprocess.run([f"{sys.executable}", "activity_check.py"])
run_cap()