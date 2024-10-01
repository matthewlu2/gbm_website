import streamlit as st
import urllib.request
from persist import persist


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_data/main/spatial_gene_tab/'


st.markdown("<h2 style='text-align: center; color: black;'>Spatial gene expression</h1>", unsafe_allow_html=True)  

file = open('text_files/spatial_gene_names_10.txt', 'r')
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
    'Gene',
    list)

def url_is_alive(url):
    """
    Checks that a given URL is reachable.
    :param url: A URL
    :rtype: bool
    """
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False

image_na = "./logo/no_available_icon.png"
a.subheader('Spatial Plot')
image_spatial = f"{IMG_REPO}/spatial_expression/{option2}/{option}.png"
if url_is_alive(image_spatial):
    a.image(image_spatial)
else:
    a.image(image_na)
b.subheader('Violin Plot')
image_violin = f"{IMG_REPO}/violin_expression/{option2}/{option}.png"
if url_is_alive(image_violin):
    b.image(image_violin)
else:
    b.image(image_na)
