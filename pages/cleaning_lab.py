import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaning Lab", page_icon="🧽")

st.title("🧽 Data Cleaning Lab: The Surgery")

# 1. LOAD DATA
try:
    df = pd.read_csv("patients_messy.csv")
    # Make a copy so we can compare "Before" vs "After" later
    df_clean = df.copy()
except FileNotFoundError:
    st.error("❌ File not found.")
    st.stop()

# SHOW RAW DATA
st.subheader("1. The Patient (Raw Data)")
st.write("Notice the missing Ages (NaN) and text in Sugar ('High').")
st.dataframe(df.head()) # .head() shows just top rows

# --- THE SURGERY SECTION ---
st.divider()
st.header("🔪 Performing Surgery")

# STEP A: Fix the "Sugar" Column (Coercion)
# Problem: "High" is text. We force it to be a Number.
# If it fails, it becomes NaN.
df_clean['Fasting_Sugar'] = pd.to_numeric(df_clean['Fasting_Sugar'], errors='coerce')

st.write("✅ Step A: Converted 'Sugar' to numbers. 'High' became NaN.")

# STEP B: Fill the "Age" Holes (Imputation)
# Logic: Calculate Median Age -> Fill NaN with it
median_age = df_clean['Age'].median()
df_clean['Age'] = df_clean['Age'].fillna(median_age)

st.write(f"✅ Step B: Filled missing Ages with the Median: **{median_age:.1f} years**")

# STEP C: Fill the "Sugar" Holes (Imputation)
# Now that "High" is NaN, we need to fill those gaps too!
median_sugar = df_clean['Fasting_Sugar'].median()
df_clean['Fasting_Sugar'] = df_clean['Fasting_Sugar'].fillna(median_sugar)

st.write(f"✅ Step C: Filled missing Sugar with the Median: **{median_sugar:.1f} mg/dL**")

# --- FINAL RESULT ---
st.divider()
st.subheader("🎉 The Result: Clean Data")
st.write("No more missing values. Ready for AI.")

col1, col2 = st.columns(2)
with col1:
    st.caption("BEFORE (Dirty)")
    st.write(df.isnull().sum())
with col2:
    st.caption("AFTER (Clean)")
    st.write(df_clean.isnull().sum())

st.success("Surgery Successful! All counts are zero.")
st.dataframe(df_clean)
