import streamlit as st
import pandas as pd

st.title("CSV File Uploader and Viewer (Temporary Storage)")

# --- File Upload ---
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    try:
        # Store file in session state
        st.session_state["uploaded_file"] = uploaded_file
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error uploading file: {e}")

# --- File Display ---
if "uploaded_file" in st.session_state:
    try:
        df = pd.read_csv(st.session_state["uploaded_file"])
        st.write("Top 5 lines of the uploaded file:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")
