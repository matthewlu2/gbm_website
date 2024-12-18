import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram</h1>", unsafe_allow_html=True)  
st.write("")

file = open('text_files/dotplot_tf_names.txt', 'r')
list = file.read().splitlines()


option = st.selectbox(
    'Metaprogram',
    list) 

a, b = st.columns([.95, .05])
a.markdown("<h3 style='text-align: center; color: black;'>TF</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/{option}.png')
a1, b1 = st.columns([.95, .05])
a1.markdown("<h3 style='text-align: center; color: black;'>Pathway</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO_2}/{option}.png')
