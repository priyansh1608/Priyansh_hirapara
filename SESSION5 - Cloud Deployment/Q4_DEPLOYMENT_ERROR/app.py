"""
4.  Simulate a basic deployment issue: remove 'streamlit' from your requirements.txt, try 
    to deploy your app on Streamlit Cloud, and note the error message you receive. Then, fix
    the issue and redeploy successfully.<br><br><em><strong>Hint:</strong> Take a screenshot 
    of the error and the fixed deployment page.</em>
"""
import streamlit as st

st.set_page_config(
    page_title="Deployment Test",
    page_icon=""
)

st.title("Deployment Test")

st.write("My Streamlit application is running successfully!")

st.success("Deployment fixed successfully!")