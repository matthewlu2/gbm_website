import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms

IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'

IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'
IMG_REPO_4 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_drug_score'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram Related Molecular Features</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Use the interactive map to select and explore metaprogram related molecular features such as transcription factor and pathway activities, as well as predicted drug sensitivities across each sample.")

df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = st.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 



st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by TF</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_metaprogram_top_transcriptions_per_sample/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by Pathway</h1>", unsafe_allow_html=True)

i, j = st.columns([.11, .95])
j.image(f'{IMG_REPO}/across_metaprogram_top_pathways_per_sample/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by Drug2Cell</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_metaprogram_top_drugs_per_sample/{option}.png')


d_mp = get_sample_metaprograms("./data/sample_metaprograms.pkl")
l_mp = d_mp[option]

option_mp = st.selectbox(
    'Metaprogram',
    l_mp
)
st.markdown("<h3 style='text-align: center; color: black;'>Top TFs across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_transcriptions_per_metaprogram/{option_mp}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Top pathways across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_pathways_per_metaprogram/{option_mp}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Top drugs across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_drugs_per_metaprogram/{option_mp}.png')
