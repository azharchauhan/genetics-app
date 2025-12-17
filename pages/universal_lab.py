import streamlit as st
import pandas as pd

st.set_page_config(page_title="Universal Lab", page_icon="🧪")

st.title("🧪 The Universal Data Cleaner")
st.markdown("Upload **ANY** CSV file. This tool will help you clean it without writing code.")

# 1. THE UNIVERSAL UPLOADER
# We don't say "pd.read_csv('patients.csv')" anymore.
# We let the user pick the file.
uploaded_file = st.file_uploader("Upload your messy CSV", type=["csv"])

if uploaded_file is None:
    st.info("Waiting for file...")
    st.stop()  # Stop here until file is uploaded

# Load the data
df = pd.read_csv(uploaded_file)
df_clean = df.copy()

st.write("### 1. Preview Data")
st.dataframe(df.head())

# Show current missing values
st.write("### 2. Diagnosis (Missing Values)")
st.write(df.isnull().sum())

# 2. THE UNIVERSAL SURGERY
st.divider()
st.header("🔪 Surgical Station")

# A. SELECT COLUMN (The Dropdown)
# Since we don't know the column names, we ask Python to list them.
target_col = st.selectbox("Which column do you want to fix?", df.columns)

# B. CHOOSE METHOD
method = st.radio("How should we fix it?", 
                  ["Fill with Median (Numbers)", 
                   "Fill with Mode (Text/Categories)", 
                   "Drop Rows (Delete)"])

# C. THE BUTTON
if st.button("Apply Treatment"):
    
    # LOGIC 1: FILL MEDIAN
    if method == "Fill with Median (Numbers)":
        try:
            # Force to number first (handling "High" etc)
            df_clean[target_col] = pd.to_numeric(df_clean[target_col], errors='coerce')
            median_val = df_clean[target_col].median()
            df_clean[target_col] = df_clean[target_col].fillna(median_val)
            st.success(f"Filled {target_col} with Median: {median_val}")
        except:
            st.error("Could not calculate median. Is this a text column?")

    # LOGIC 2: FILL MODE (For Text like 'Gender')
    elif method == "Fill with Mode (Text/Categories)":
        mode_val = df_clean[target_col].mode()[0]
        df_clean[target_col] = df_clean[target_col].fillna(mode_val)
        st.success(f"Filled {target_col} with Mode: {mode_val}")

    # LOGIC 3: DROP ROWS
    elif method == "Drop Rows (Delete)":
        df_clean = df_clean.dropna(subset=[target_col])
        st.success(f"Dropped rows with missing {target_col}")

    # SHOW RESULT
    st.write("### 3. Post-Op Results")
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Original Missing")
        st.write(df[target_col].isnull().sum())
    with col2:
        st.caption("Remaining Missing")
        st.write(df_clean[target_col].isnull().sum())

# 3. DISCHARGE PATIENT (Download)
st.divider()
st.subheader("💾 Discharge Patient")

# Convert dataframe to CSV for download
csv = df_clean.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Clean CSV",
    data=csv,
    file_name="clean_data_export.csv",
    mime="text/csv"
)
