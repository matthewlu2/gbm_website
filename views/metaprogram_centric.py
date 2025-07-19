import streamlit as st

IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram-Centric Comparison</h1>", unsafe_allow_html=True)  
st.write("")

st.info("""Compare how regulatory features linked to transcriptional metaprograms vary across multiple glioblastoma samples.  
• **TF**: Examine transcription factors associated with each metaprogram to see which are consistently or differentially active across tumors.  
• **Pathway**: Explore pathway activation linked to specific metaprograms, uncovering shared or distinct signaling programs.  
• **Drug**: Assess predicted drug response signatures tied to different metaprograms, highlighting therapeutic vulnerabilities across the cohort.  
Use interactive plots and selectors to identify regulatory patterns and drug sensitivities tied to key malignant and non-malignant programs.""")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

file = open('text_files/metaprogram_names.txt', 'r')
list = file.read().splitlines()

option_mp = st.selectbox(
    'Metaprogram',
    list) 

st.markdown("<h3 style='text-align: center; color: black;'>Top TFs across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_transcriptions_per_metaprogram/{option_mp}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Top pathways across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_pathways_per_metaprogram/{option_mp}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Top drugs across samples</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_sample_top_drugs_per_metaprogram/{option_mp}.png')