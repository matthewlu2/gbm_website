import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer

st.markdown("<h2 style='text-align: center; color: black;'>Ligand–Receptor–TF–Pathway Correlation</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Explore spatial correlations between ligand expression, receptor expression, transcription factor activities, and pathway activities across glioblastoma samples. This helps reveal intercellular signaling and regulatory interactions shaping the tumor microenvironment. Interactive clustered heatmaps display Pearson correlation coefficients, allowing you to identify ligand–receptor–TF–pathway relationships that are conserved or variable across tumors. Use the search and filter options to select genes, TFs, pathways, or drugs, and explore their spatial correlations across different patients.")

file2 = open('text_files/correlation_per_gene_names.txt', 'r')
list2 = file2.read().splitlines()

option2 = st.selectbox(
    'Gene',
    list2) 

pdf_viewer(input = f'data/correlation_per_gene/{option2}.pdf')
