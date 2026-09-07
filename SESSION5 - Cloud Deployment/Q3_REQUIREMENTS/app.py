"""
3.  Create a requirements.txt file listing all Python packages your app needs 
  (for example: streamlit, pandas, numpy), upload it with your project, and explain in one
   sentence why requirements.txt is important for cloud deployment.
"""
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Requirements Demo",
    page_icon=""
)

st.title("Requirements.txt Demo")

st.write("Required Python packages are installed successfully.")

data = {
    "Package": ["Streamlit", "Pandas", "NumPy"],
    "Purpose": [
        "Create web app",
        "Data handling",
        "Numerical operations"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)

numbers = np.array([10, 20, 30, 40, 50])

st.write("NumPy Average:", np.mean(numbers))