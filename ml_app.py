import subprocess
import sys
import streamlit as st
from activity_check import high_count
act_lev = ""
def run_cap():
	def start_capture():
		subprocess.run([f"{sys.executable}", "activity_check.py"])
	st.button("Start Monitoring",on_click=start_capture)
run_cap()
st.write(high_count)