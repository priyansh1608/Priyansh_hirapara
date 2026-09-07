"""
5.   After deploying your app online, share your live project link with a friend and ask them to
    test it on their phone. Write down one feedback point they give and how you would improve your
    app based on it.
"""
import streamlit as st

st.set_page_config(
    page_title="My Project",
    page_icon=""
)

st.title("My Streamlit Project")

st.write("Welcome to my deployed Streamlit application!")

st.header("About My App")

st.write(
    "This application was created as part of my Streamlit deployment practical."
)

st.success("Thank you for visiting my app")