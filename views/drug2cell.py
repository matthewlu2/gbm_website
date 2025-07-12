import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_drug2cell'
IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/violin_drug2cell'

st.markdown("<h2 style='text-align: center; color: black;'>Spatial Drug2Cell score</h1>", unsafe_allow_html=True)  
st.write("")

file = open('text_files/drug2cell_names.txt', 'r')
list = file.read().splitlines()

a, b = st.columns(2)

option = b.selectbox(
    'drug2cell',
    list)

df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()

option2 = a.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 

a.image(f'{IMG_REPO}/{option}/{option2}.png')
b.image(f'{IMG_REPO2}/{option}/{option2}.png')
