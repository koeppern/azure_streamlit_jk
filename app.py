# 2023-05-16, J. Köppern

# No Docker


import streamlit as st

st.title("azure_streamlit_jk")

st.write("""2023-05-16, J. Köppern\nazure-streamlit-jk is the name of htis app on zure.""")

st.header("Hsllo. ✴️🙂")

user_name = st.text_input("Enter your name")

if st.button("OK"):
    st.write(f"Hallo, {user_name}.")