import streamlit as st
from persist import persist




st.info('Insert Descrption')

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/spatial_tf_tab/'

file = open('text_files/spatial_tf_activity_names.txt', 'r')
list = file.read().splitlines()

sample_list = ['MGH258', 'UKF243', 'UKF248', 'UKF251', 'UKF255', 'UKF259', 'UKF260',
                'UKF266', 'UKF269', 'UKF275', 'UKF296', 'UKF304', 'UKF313', 'UKF334',
                'ZH1007inf', 'ZH1007nec', 'ZH1019T1', 'ZH1019inf', 'ZH8811Abulk', 'ZH8811Bbulk',
                'ZH8812bulk', 'ZH881T1', 'ZH881inf', 'ZH916T1', 'ZH916bulk', 'ZH916inf']

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
    
a.subheader('Spatial Plot')            
a.image(f'{IMG_REPO}/spatial_tf_activity/{option2}/{option}.png')
b.subheader('Violin Plot')
b.image(f'{IMG_REPO}/violin_tf_activity/{option2}/{option}.png')