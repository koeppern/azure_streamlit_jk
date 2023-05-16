# 2023-05-16, J. Köppern

# No Docker


import streamlit as st

st.title("azure_streamlit_jk")

st.write("*DOCUMENTATION IS MISSING")

st.write("""2023-05-16, J. Köppern\n\nazure-streamlit-jk is the name of htis app on Azure.""")

st.header("Hsllo. ✴️🙂")

user_name = st.text_input("Enter your name")

if st.button("OK"):
    st.write(f"Hallo, {user_name}.")