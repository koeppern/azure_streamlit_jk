# 2023-05-16, J. Köppern

# No Docker


import streamlit as st

st.title("Hsllo. ✴️🙂")

user_name = st.text_input("Enter your name")

if st.button("OK"):
    st.write(f"Hallo, {user_name}.")