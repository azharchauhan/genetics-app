import streamlit as st

st.title("🧬 DNA Nucleotide Counter")
st.write("This app counts the nucleotide frequency in your DNA sequence.")

sequence = st.text_area("Paste your DNA Sequence here:", height=150)

if st.button("Analyze Sequence"):
    dna = sequence.upper()
    
    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")
    
    total_len = len(dna)
    
    if total_len > 0:
        gc_content = (count_G + count_C) / total_len * 100
    else:
        gc_content = 0

    st.subheader("Analysis Results")
    st.write(f"**Total Length:** {total_len} base pairs")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Adenine (A)", count_A)
    col2.metric("Thymine (T)", count_T)
    col3.metric("Guanine (G)", count_G)
    col4.metric("Cytosine (C)", count_C)
    
    st.info(f"**GC Content:** {gc_content:.2f}%")
