import streamlit as st
import matplotlib.pyplot as plt

st.title("🧬 Genomic Data Analyzer")

# THE SWITCH (This creates the Toggle)
input_method = st.radio("Choose Input Method:", ["Paste Sequence", "Upload File"])

sequence = "" 

# OPTION A: PASTE
if input_method == "Paste Sequence":
    text_input = st.text_area("Paste your DNA Sequence here:", height=150)
    if text_input:
        sequence = text_input

# OPTION B: UPLOAD
elif input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload your DNA file (.txt)", type=['txt'])
    if uploaded_file is not None:
        sequence = uploaded_file.read().decode('utf-8')
        st.info("File Loaded Successfully!")

# THE ANALYSIS (Runs only if sequence is not empty)
if len(sequence) > 0:
    if st.button("Analyze Sequence"):
        dna = sequence.upper().strip()
        
        # Metrics
        count_A = dna.count("A")
        count_T = dna.count("T")
        count_G = dna.count("G")
        count_C = dna.count("C")
        
        st.subheader("Results")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("A", count_A)
        col2.metric("T", count_T)
        col3.metric("G", count_G)
        col4.metric("C", count_C)
        st.write(f"**Total Length:** {len(dna)} bp")
        
        # Chart
        st.subheader("Nucleotide Distribution")
        fig, ax = plt.subplots()
        ax.bar(["A", "T", "G", "C"], [count_A, count_T, count_G, count_C], color=['blue', 'orange', 'green', 'red'])
        st.pyplot(fig)
        
