import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/metaprogram_tab/'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'
IMG_REPO_4 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_drug_score'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram Maps</h1>", unsafe_allow_html=True)  
st.write("")


st.info("Visualize the spatial distribution of 14 transcriptional metaprograms within glioblastoma tissue samples. These metaprograms capture key malignant subtypes—such as mesenchymal, neural progenitor-like, and proliferative states—as well as important non-malignant populations, including immune, vascular, and glial cells. Use the interactive map to select and explore metaprograms, viewing their spatial localization alongside histology images.")
df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = st.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 

b1, c1, d1 = st.columns([.003, .1, .1])
b, c, d = st.columns([.002, .12, .12])

c1.markdown("<h4 style='text-align: center; color: black;'>H&E Stain</h4>", unsafe_allow_html=True)
c1.image(f'{IMG_REPO}/he_stain/{option}.png')

d1.write("")
d1.write("")
d1.markdown( f'<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Sample {option}</p>',  unsafe_allow_html=True) 
d1.write("")


sample_items = df_sample[df_sample['Sample-ID']== option].iloc[0]

for index, value in sample_items.items():
    d1.markdown(f"**{index}** : {value}", True)




b2, c2, d2 = st.columns([.0001, .08, .1])           
c2.markdown("<h4 style='text-align: center; color: black;'>Metaprogram Proportion</h4>", unsafe_allow_html=True)
d2.markdown("<h4 style='text-align: center; color: black;'>Metaprogram</h4>", unsafe_allow_html=True)
# c.write("")

b3, c3, d3 = st.columns([.002, .12, .12])
c3.image(f'{IMG_REPO}/pie_metaprogram/{option}.png')
d3.write("")
d3.write("")
d3.write("")
d3.write("")
d3.write("")
d3.image(f'{IMG_REPO}/metaprogram/{option}.png')


d_mp = get_sample_metaprograms("./data/sample_metaprograms.pkl")
l_mp = d_mp[option]

option_mp = st.selectbox(
    'Metaprogram',
    l_mp
)

# one1, two1, three1= st.columns([0.001, .20, .18])
# one, two, three= st.columns([0.001, .25, .18])


# two1.markdown("<h3 style='text-align: center; color: black;'>Metaprograms</h1>", unsafe_allow_html=True)
# three1.markdown("<h3 style='text-align: center; color: black;'>Single Metaprogram</h1>", unsafe_allow_html=True)


# two.image(f'{IMG_REPO}/metaprogram/{option}.png')
b4, c4 = st.columns([0.2, 0.6])
c4.image(f'{IMG_REPO}/metaprogram_{option_mp}/{option}.png')


