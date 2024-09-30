import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer

st.info('Insert Descrption')

file2 = open('text_files/correlation_per_gene_names.txt', 'r')
list2 = file2.read().splitlines()

option2 = st.selectbox(
    'Gene',
    list2) 

pdf_viewer(input = f'data/correlation_per_gene/{option2}.pdf')
