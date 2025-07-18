import streamlit as st
from persist import persist


st.markdown("<h2 style='text-align: center; color: black;'>Pathway Activity Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("View spatially inferred pathway activities across glioblastoma samples using the SPAN framework. Explore how major signaling and metabolic pathways—such as hypoxia, proliferation, and immune signaling—are distributed within the tumor microenvironment. Overlay pathway maps on histology images to uncover spatial heterogeneity and identify pathway activation linked to specific malignant or non-malignant programs. Comparative violin plots let you explore pathway variation across metaprograms. Use the search box and sample selector to navigate.")

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_pw_tab/'

file = open('text_files/spatial_pw_activity_names.txt', 'r')
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
    'Pathway',
    (list)) 

# a.subheader('Spatial Plot')
a.image(f'{IMG_REPO}/spatial_pw_activity/HALLMARK_{option2}/{option}.png')
# b.subheader('Violin Plot')
b.image(f'{IMG_REPO}/violin_pw_activity/HALLMARK_{option2}/{option}.png')


IMG_REPO2 = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
st.markdown("<h3 style='text-align: center; color: black;'>Pathway Activity across Metaprograms</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO2}/across_metaprogram_top_pathways_per_sample/{option}.png')
