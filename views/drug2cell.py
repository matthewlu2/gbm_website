import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms

IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
# IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_drug2cell'
# IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/violin_drug2cell'

st.markdown("<h2 style='text-align: center; color: black;'>Drug2Cell Score Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Integrate spatial transcriptomic data with Drug2Cell predictions to map drug sensitivity scores across glioblastoma samples. Identify tumor regions that may respond to specific drugs based on local transcription factor and pathway activity profiles. Compare drug scores across metaprograms to uncover therapeutic targets tied to distinct tumor niches or cellular states. Use the search box to enter drug names and the sample selector to explore across different tumors.")

file = open('text_files/drug2cell_names.txt', 'r')
list = file.read().splitlines()
list = sorted(list)
a, b = st.columns(2)

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

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

a.image(f'{IMG_REPO}/drug_spatial/{option}/{option2}.png')
b.image(f'{IMG_REPO}/drug_violin/{option}/{option2}.png')

IMG_REPO2 = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
st.markdown("<h3 style='text-align: center; color: black;'>Drug2Cell Scores across Metaprogram</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO2}/across_metaprogram_top_drugs_per_sample/{option2}.png')
