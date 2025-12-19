import streamlit as st
import pandas as pd

st.set_page_config(page_title="Universal Lab", page_icon="🧪")

st.title("🧪 The Universal Data Lab")
st.markdown("Upload any medical CSV to Clean, Engineer, and Analyze.")

# --- 1. THE RECEPTIONIST (Uploader) ---
uploaded_file = st.file_uploader("Upload Messy CSV", type=["csv"])

if uploaded_file:
    # Load the data into a 'Smart Object' (DataFrame)
    df = pd.read_csv(uploaded_file)
    df_clean = df.copy() # Make a copy so we don't ruin the original

    st.write("### 📋 Patient Data Preview")
    st.dataframe(df.head())

    # --- 2. THE SURGICAL STATION (Cleaning) ---
    st.divider()
    st.header("🔪 Data Surgery")
    
    col1, col2 = st.columns(2)
    with col1:
        target_col = st.selectbox("Select Column to Fix:", df.columns)
    with col2:
        method = st.radio("Treatment:", ["Median", "Mode", "Drop"])

    if st.button("Apply Surgery"):
        if method == "Median":
            df_clean[target_col] = pd.to_numeric(df_clean[target_col], errors='coerce')
            val = df_clean[target_col].median()
            df_clean[target_col] = df_clean[target_col].fillna(val)
        elif method == "Mode":
            val = df_clean[target_col].mode()[0]
            df_clean[target_col] = df_clean[target_col].fillna(val)
        else:
            df_clean = df_clean.dropna(subset=[target_col])
        st.success(f"Fixed {target_col}!")

    # --- 3. THE BRAIN STATION (Feature Engineering) ---
    st.divider()
    st.header("🧠 Medical Engineering")
    new_col = st.text_input("New Column Name (e.g., BMI)")
    formula = st.text_input("Formula (e.g., Weight / (Height ** 2))")
    
    if st.button("Create Feature"):
        try:
            df_clean[new_col] = df_clean.eval(formula)
            st.success(f"Created {new_col}!")
        except Exception as e:
            st.error(f"Error: {e}")

    # --- 4. THE DETECTIVE (EDA & Heatmap) ---
    st.divider()
    st.header("🔍 Data Detective")
    
    if st.checkbox("Show Correlation Heatmap"):
        numeric_df = df_clean.select_dtypes(include=['number'])
        corr = numeric_df.corr()
        st.write("### 🌡️ Correlation X-Ray (Pearson r)")
        st.dataframe(corr.style.background_gradient(cmap='coolwarm'))
        
    # --- 5. DISCHARGE (Download) ---
    st.divider()
    csv = df_clean.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Download Cleaned Data", data=csv, file_name="cleaned_data.csv")
    
