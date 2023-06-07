import subprocess
import streamlit as st

st.title("Running other streamlit app")
button = st.button("Click Here")

if button == True:
    st.write("Directing to other page")
    subprocess.run(['streamlit', 'run', 'main2.py'])

