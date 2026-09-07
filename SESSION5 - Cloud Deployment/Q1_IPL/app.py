"""
1.  Create a simple Streamlit app in a file called app.py that 
   displays your favorite IPL team's name and logo, then deploy
 it to Streamlit Cloud and share your live app link.
"""
import streamlit as st

st.set_page_config(
    page_title="My IPL Team",
    page_icon=""
)

st.title("My Favorite IPL Team")

st.header("Chennai Super Kings")

st.write("My favorite IPL team is Chennai Super Kings (CSK).")

st.image(
    "https://upload.wikimedia.org/wikipedia/en/2/2b/Chennai_Super_Kings_Logo.svg",
    width=250
)

st.success("Whistle Podu! ")