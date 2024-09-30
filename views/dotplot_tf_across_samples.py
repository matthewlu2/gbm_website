import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/dotplot_tf_activity'

st.info('Insert Descrption')

file = open('text_files/dotplot_tf_names.txt', 'r')
list = file.read().splitlines()


option = st.selectbox(
    'Metaprogram',
    list) 

st.image(f'{IMG_REPO}/{option}.png')
