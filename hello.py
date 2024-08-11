import streamlit as st
import pandas as pd

st.title("CSV File Uploader and Viewer (Multiple Files)")

# --- File Upload ---
uploaded_file = st.file_uploader("Choose a CSV file", type="csv", accept_multiple_files=True)

# --- Store Uploaded Files in Session State ---
if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []

if uploaded_file is not None:
    for file in uploaded_file:
        try:
            # Read file contents and store in session state
            df = pd.read_csv(file)
            st.session_state["uploaded_files"].append((file.name, df))
            st.success(f"File '{file.name}' uploaded successfully!")
        except Exception as e:
            st.error(f"Error uploading file '{file.name}': {e}")

# --- File Selection and Display ---
if st.session_state["uploaded_files"]:
    file_options = [file[0] for file in st.session_state["uploaded_files"]]
    selected_file = st.selectbox("Select a file to view:", file_options)

    for file_name, df in st.session_state["uploaded_files"]:
        if file_name == selected_file:
            st.write("Top 5 lines of the selected file:")
            st.dataframe(df.head())
            break  # Stop after displaying the selected file
else:
    st.write("No files uploaded yet.")
