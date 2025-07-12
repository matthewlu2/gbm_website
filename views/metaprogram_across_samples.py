import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram-specific</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Compare how regulatory features linked to transcriptional metaprograms vary across multiple glioblastoma samples.<br>
  • TF: Examine transcription factors associated with each metaprogram to see which are consistently or differentially active across tumors.<br>
  • Pathway: Explore pathway activation linked to specific metaprograms, uncovering shared or distinct signaling programs.<br>
  • Drug: Assess predicted drug response signatures tied to different metaprograms, highlighting therapeutic vulnerabilities across the cohort.<br>
Use interactive plots and selectors to identify regulatory patterns and drug sensitivities tied to key malignant and non-malignant programs."


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
