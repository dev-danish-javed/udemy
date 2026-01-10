import streamlit as st

st.header("streamlit widgets")

name =  st.text_input("Enter your name")
age = st.slider("Enter your age", min_value=18, max_value=100, value=18)
options = ["Java", "Python", "Node"]

if name:
    st.write(f'Hello {name}! You are {age} years old.')
