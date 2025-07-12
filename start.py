import streamlit as st
from style import page_style, footer
import pandas as pd
from persist import load_widget_state, persist
from views.utils import get_sample_dataframe
from style import define_layout

# --- PAGE SETUP ----

st.set_page_config(
        page_title='GBM',
        page_icon= "./logo/gbm_ribbon.png",
        initial_sidebar_state="expanded",
)

# max_width_str = f"max-width: {80}%;"

# st.markdown(f"""
#         <style>
#         .appview-container .main .block-container{{{max_width_str}}}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

define_layout(max_width='80%', padding_top='2rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem')

# st.markdown(f"""
#     <style>
#         .stSelectbox > label {{
#             # font-size:200%; 
#             font-size: 30px;
#             font-weight:bold; 
#             color: purple;
#         }}
#         .stMultiSelect > label {{
#             font-size:105%; 
#             font-weight:bold; 
#             color:black;
#         }}
#     </style>
#     """, unsafe_allow_html=True)

# ---- start main ---

load_widget_state()

# df_sample = pd.read_csv('./data/dataset.csv')
# df_sample.index = df_sample.index + 1
# st.session_state['df_sample'] = df_sample
df_sample = get_sample_dataframe('./data/dataset.csv')
st.session_state['df_sample'] = df_sample
persist("sample_id")

home_page = st.Page(
    page = "views/home.py",
    title = "Home",
    icon = ":material/chevron_right:"  ,
    default= True,
)

datasets_page = st.Page(
    page = "views/dataset.py",
    title = "Dataset",
    icon = ":material/chevron_right:"  
)

metaprogram_page = st.Page(
    page = "views/metaprogram.py",
    title = "Metaprogram",
    icon = ":material/chevron_right:"    
)

dotplot_page = st.Page(
    page = "views/metaprogram_across_samples.py",
    title = "Metaprogram-specific",  #Metaprogram
    icon = ":material/chevron_right:"  
)

drug2cell_page = st.Page(
    page = "views/drug2cell.py",
    title = "Spatial Drug2Cell score",
    icon = ":material/chevron_right:"
)

heatmap_gene_correlation_page = st.Page(
    page = "views/heatmap_gene_correlation.py",
    title = "Ligand-Receptor-TF-Pathway Correlation",  #Correlation heatmaps
    icon = ":material/chevron_right:"
)

gene_page = st.Page(
    page = "views/spatial_gene.py",
    title = "Spatial gene expression",
    icon = ":material/chevron_right:"
)

s_tf_page = st.Page(
    page = "views/spatial_tf.py",
    title = "Spatial TF activity",
    icon = ":material/chevron_right:"
)

s_pathway_page = st.Page(
    page = "views/spatial_pathway.py",
    title = "Spatial pathway activity",
    icon = ":material/chevron_right:"
)

ligand_page = st.Page(
    page = "views/ligand_receptor_TF_pathway.py",
    title = "Ligand-Receptor-TF-Pathway heatmaps",
    icon = ":material/chevron_right:"
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact us",
    icon = ":material/chevron_right:"
)

citation_page = st.Page(
    page = "views/citation.py",
    title = "Citation",
    icon = ":material/chevron_right:"
)

# -- NAVIGATION --

pg = st.navigation(
    {
        "Overview": [home_page, datasets_page],
        "Analysis by Sample": [metaprogram_page, gene_page, s_tf_page, s_pathway_page , drug2cell_page],  # ligand_page,
        "Analysis across Samples": [ heatmap_gene_correlation_page  , dotplot_page], 
        "Others": [citation_page, contact_page]
    }
)


# -- SHARED ON ALL PAGES --
# st.sidebar.text("Made by Osmanbeyoglu Lab")

# -- RUN NAVIGATION --
pg.run()
st.divider()
st.markdown(footer,unsafe_allow_html=True) 





