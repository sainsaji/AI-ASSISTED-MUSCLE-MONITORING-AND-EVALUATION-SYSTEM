import streamlit as st
import subprocess
import sys
from PIL import Image
def run_rec():
	col1, col2= st.columns(2,gap="large")
	def low_activity(level):
		with col1:
			st.header("Mario Jump Game Level:"+level)
			bottom_image = "./images/mario.png"
			if bottom_image is not None:
				image = Image.open(bottom_image)
				new_image = image.resize((600, 400))
				st.image(new_image)
			if st.button('Start Game'):
				subprocess.run([f"{sys.executable}", "Games/Jumping-PyGame/youtubemain.py"])


		with col2:
			st.header("Dino Game Level:"+level)
			bottom_image = "./images/dino.jpeg"
			if bottom_image is not None:
				image = Image.open(bottom_image)
				new_image = image.resize((600, 400))
				st.image(new_image)
			if st.button('Start Dino'):
				subprocess.run([f"{sys.executable}", "D1.py"])
	def med_activity(level):
		with col1:
			st.header("Mario Jump Game Level"+level)
			st.image("https://supermariorun.com/assets/img/stage/mario03.png",use_column_width="auto")
			if st.button('Start Game'):
				subprocess.run([f"{sys.executable}", "Games/Jumping-PyGame/youtubemain.py"])

		with col2:
			st.header("Dino Game Level:"+level)
			st.image("https://www.omgchrome.com/wp-content/uploads/2015/06/chrome-trex-dinosaur.jpg",use_column_width="auto")
			if st.button('Start Dino'):
				subprocess.run([f"{sys.executable}", "D1.py"])
	
	activity_level = "Low"
	if(activity_level=="Low"):
		low_activity(activity_level)
	if(activity_level=="Medium"):
		med_activity(activity_level)