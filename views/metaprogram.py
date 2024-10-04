import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/metaprogram_tab/'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/dotplot_tf_activity'
IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/dotplot_pw_activity'


st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram</h1>", unsafe_allow_html=True)  
st.write("")


df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = st.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 

b2, c2, d2 = st.columns([.001, .10, .1])
b, c, d = st.columns([.02, .12, .12])

c2.markdown("<h3 style='text-align: center; color: black;'>HE Stain</h1>", unsafe_allow_html=True)

d2.markdown("<h3 style='text-align: center; color: black;'>Metaprogram Proportion</h1>", unsafe_allow_html=True)
c.write("")

c.image(f'{IMG_REPO}/he_stain/{option}.png')
d.image(f'{IMG_REPO}/pie_metaprogram/{option}.png')



# -- Single Metaprogram Images --

# def url_is_alive(url):
#     """
#     Checks that a given URL is reachable.
#     :param url: A URL
#     :rtype: bool
#     """
#     request = urllib.request.Request(url)
#     request.get_method = lambda: 'HEAD'
#     try:
#         urllib.request.urlopen(request)
#         return True
#     except urllib.request.HTTPError:
#         return False
    
# metaprograms = ['AC','Chromatin.Reg','Inflammatory.Mac','MES.Ast','MES.Hyp','MES','Mac','NPC','Neuron','OPC','Oligo','Prolif.Metab','Reactive.Ast','Vasc']
# l_mp = []
# for mp in metaprograms:
#     urlpath = f"https://github.com/matthewlu2/gbm_data/blob/main/metaprogram_tab/metaprogram_{mp}/{option}.png"
#     if url_is_alive(urlpath):
#         # l_mp.append(f'{IMG_REPO}/metaprogram_{mp}/{option}.png')
#         l_mp.append(mp)

d_mp = get_sample_metaprograms("./data/sample_metaprograms.pkl")
l_mp = d_mp[option]

option_mp = st.selectbox(
    'Metaprogram',
    l_mp
)

one1, two1, three1= st.columns([0.001, .20, .18])
one, two, three= st.columns([0.001, .25, .18])


two1.markdown("<h3 style='text-align: center; color: black;'>Metaprograms</h1>", unsafe_allow_html=True)
three1.markdown("<h3 style='text-align: center; color: black;'>Single Metaprogram</h1>", unsafe_allow_html=True)


two.image(f'{IMG_REPO}/metaprogram/{option}.png')
three.image(f'{IMG_REPO}/metaprogram_{option_mp}/{option}.png')



st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by TF</h1>", unsafe_allow_html=True)


st.image(f'{IMG_REPO_2}/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by Pathway</h1>", unsafe_allow_html=True)

i, j = st.columns([.11, .95])
j.image(f'{IMG_REPO_3}/{option}.png')
