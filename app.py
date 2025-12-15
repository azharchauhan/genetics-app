import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("🧬 Genomic Data Analyzer")

# 1. FILE UPLOADER (This is the Magic Button)
uploaded_file = st.file_uploader("Upload your DNA Sequence file (.txt or .csv)", type=['txt', 'csv'])

if uploaded_file is not None:
    # Read the file
    sequence = uploaded_file.read().decode('utf-8').strip()
    st.text_area("Sequence Loaded:", sequence, height=150)
    
    if st.button("Analyze Sequence"):
        dna = sequence.upper()
        
        # Counts
        count_A = dna.count("A")
        count_T = dna.count("T")
        count_G = dna.count("G")
        count_C = dna.count("C")
        total_len = len(dna)
        
        # Metrics
        st.subheader("Analysis Results")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("A", count_A)
        col2.metric("T", count_T)
        col3.metric("G", count_G)
        col4.metric("C", count_C)
        
        # Visualization
        st.subheader("Nucleotide Distribution")
        fig, ax = plt.subplots()
        ax.bar(["A", "T", "G", "C"], [count_A, count_T, count_G, count_C], color=['blue', 'orange', 'green', 'red'])
        ax.set_ylabel("Count")
        ax.set_title("Nucleotide Frequency")
        st.pyplot(fig)

