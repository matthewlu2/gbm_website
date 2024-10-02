import streamlit as st
from persist import persist



st.markdown("<h2 style='text-align: center; color: black;'>Spatial TF activity</h1>", unsafe_allow_html=True)  
st.write("")

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/spatial_tf_tab/'

file = open('text_files/spatial_tf_activity_names.txt', 'r')
list = file.read().splitlines()

a, b = st.columns(2)


df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = a.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 


option2 = b.selectbox(
    'TF',
    list) 
    
# a.subheader('Spatial Plot')            
a.image(f'{IMG_REPO}/spatial_tf_activity/{option2}/{option}.png')
# b.subheader('Violin Plot')
b.image(f'{IMG_REPO}/violin_tf_activity/{option2}/{option}.png')
