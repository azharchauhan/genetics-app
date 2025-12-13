import streamlit as st
import matplotlib.pyplot as plt

st.title("🧬 DNA Nucleotide Counter")

sequence = st.text_area("Paste your DNA Sequence here:", height=150)

if st.button("Analyze Sequence"):
    dna = sequence.upper()
    
    # 1. Counts
    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")
    
    # 2. Output Text
    st.write(f"**Total Length:** {len(dna)}")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("A", count_A)
    col2.metric("T", count_T)
    col3.metric("G", count_G)
    col4.metric("C", count_C)
    
    # 3. THE VISUALIZATION (New Part)
    st.subheader("Nucleotide Distribution")
    
    # Create the figure (The Canvas)
    fig, ax = plt.subplots()
    
    # Create the bars
    # X-axis labels, Y-axis values, Colors
    ax.bar(["A", "T", "G", "C"], [count_A, count_T, count_G, count_C], color=['blue', 'orange', 'green', 'red'])
    
    # Label the axes
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Frequency")
    
    # Show it in Streamlit
    st.pyplot(fig)
