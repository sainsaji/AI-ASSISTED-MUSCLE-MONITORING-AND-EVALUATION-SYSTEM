import subprocess
import sys
import streamlit as st
def run_cap():
	def start_capture():
		subprocess.run([f"{sys.executable}", "activity_check.py"])
	cap_button = st.button("Start Capturing")
	if cap_button:
		start_capture()
run_cap()
