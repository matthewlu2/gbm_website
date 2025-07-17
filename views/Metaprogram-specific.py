import streamlit as st
from views.utils import get_sample_metaprograms

IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
# IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
# IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'
# IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_drug_score'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram-specific</h1>", unsafe_allow_html=True)  
st.write("")

st.info("""Compare how regulatory features linked to transcriptional metaprograms vary across multiple glioblastoma samples.  
• **TF**: Examine transcription factors associated with each metaprogram to see which are consistently or differentially active across tumors.  
• **Pathway**: Explore pathway activation linked to specific metaprograms, uncovering shared or distinct signaling programs.  
• **Drug**: Assess predicted drug response signatures tied to different metaprograms, highlighting therapeutic vulnerabilities across the cohort.  
Use interactive plots and selectors to identify regulatory patterns and drug sensitivities tied to key malignant and non-malignant programs.""")

# file = open('text_files/dotplot_tf_names.txt', 'r')
# list = file.read().splitlines()


# option = st.selectbox(
#     'Metaprogram',
#     list) 

# a, b = st.columns([.95, .05])
# a.markdown("<h3 style='text-align: center; color: black;'>TF</h1>", unsafe_allow_html=True)
# st.image(f'{IMG_REPO}/{option}.png')

# a1, b1 = st.columns([.95, .05])
# a1.markdown("<h3 style='text-align: center; color: black;'>Pathway</h1>", unsafe_allow_html=True)
# st.image(f'{IMG_REPO_2}/{option}.png')

# a2, b2 = st.columns([.95, .05])
# a2.markdown("<h3 style='text-align: center; color: black;'>Drug Score</h1>", unsafe_allow_html=True)
# st.image(f'{IMG_REPO_3}/{option}.png')


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
