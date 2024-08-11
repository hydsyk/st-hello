import streamlit as st
import pandas as pd

st.title("CSV File Viewer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Top 5 lines of the uploaded file:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")
