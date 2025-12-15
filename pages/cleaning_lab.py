import streamlit as st
import pandas as pd

st.title("🧽 Data Cleaning Lab")

# 1. LOAD THE DATA
try:
    # Note: We still look for the CSV in the main folder
    df = pd.read_csv("patients_messy.csv")
    st.success("✅ Patient Data Loaded Successfully!")
except FileNotFoundError:
    st.error("❌ File not found. Did you upload 'patients_messy.csv'?")
    st.stop()

# 2. VISUAL INSPECTION
st.subheader("1. The Raw Data (Visual Check)")
st.write("Look closely. Can you spot the 'NaN' values?")
st.dataframe(df)

# 3. THE X-RAY
st.subheader("2. The X-Ray Report (Missing Values)")
missing_values = df.isnull().sum()
st.text(missing_values)

# 4. TYPE CHECK
st.subheader("3. Data Type Check")
st.text(df.dtypes)
