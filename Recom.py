import streamlit as st
import subprocess
import sys
from PIL import Image
from ml_app import act_lev
def run_rec():
	col1, col2= st.columns(2,gap="large")
	def show_games(level):
		def img_sizer(bottom_image):
			if bottom_image is not None:
				image = Image.open(bottom_image)
				new_image = image.resize((600, 400))
				return new_image
		with col1:
			st.header("Mario Jump Game Level:"+level)
			bottom_image = "./images/mario.png"
			st.image(img_sizer(bottom_image))
			if st.button('Start Game'):
				subprocess.run([f"{sys.executable}", "Games/Jumping-PyGame/youtubemain.py"])
		with col2:
			st.header("Dino Game Level:"+level)
			bottom_image = "./images/dino.jpeg"
			st.image(img_sizer(bottom_image))
			if st.button('Start Dino'):
				subprocess.run([f"{sys.executable}", "D1.py"])
	activity_level = act_lev
	show_games(activity_level)