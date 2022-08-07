import streamlit as st
import subprocess
import sys

# subprocess.run([f"{sys.executable}", "D1.py"])
# if st.button('Say hello'):
#     subprocess.run([f"{sys.executable}", "D1.py"])
# else:
#     st.write('Executed')

col1, col2= st.columns(2,gap="large")

with col1:
    st.header("Mario Jump Game")
    st.image("https://supermariorun.com/assets/img/stage/mario03.png",use_column_width="auto")
    if st.button('Start Game'):
        subprocess.run([f"{sys.executable}", "Games/Jumping-PyGame/youtubemain.py"])


with col2:
    st.header("Dino Game")
    st.image("https://www.omgchrome.com/wp-content/uploads/2015/06/chrome-trex-dinosaur.jpg",use_column_width="auto")
    if st.button('Start Dino'):
        subprocess.run([f"{sys.executable}", "D1.py"])
