import streamlit as st
from style import page_style, footer
import pandas as pd
from persist import load_widget_state, persist
from views.utils import get_sample_dataframe
from style import define_layout
st.cache_data.clear()
st.cache_resource.clear()
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
    icon = ":material/home:",   #":material/chevron_right:"  ,
    default= True,
)

datasets_page = st.Page(
    page = "views/dataset.py",
    title = "Dataset Explorer",
    icon = ":material/table_chart:"  
)

metaprogram_page = st.Page(
    page = "views/metaprogram.py",
    title = "Metaprogram Maps",
    icon = ":material/data_array:"    
)

metaprogram_feature_page = st.Page(
    page = "views/metaprogram_feature.py",
    title = "Metaprogram-Associated Features",
    icon = ":material/extension:"    
)

dotplot_page = st.Page(
    page = "views/Metaprogram-specific.py",
    title = "Metaprogram-Centric Comparison",  #Metaprogram
    icon = ":material/bar_chart:"  
)

drug2cell_page = st.Page(
    page = "views/drug2cell.py",
    title = "Drug2Cell Score Maps",
    icon = ":material/medication:"
)

heatmap_gene_correlation_page = st.Page(
    page = "views/Ligand–Receptor–TF–Pathway_Correlation.py",
    title = "L-R-TF-Pathway-Drug Correlation Heatmap",  #Correlation heatmaps
    icon = ":material/loop:"
)

gene_page = st.Page(
    page = "views/spatial_gene.py",
    title = "Gene Expression Maps",
    icon = ":material/biotech:"
)

s_tf_page = st.Page(
    page = "views/spatial_tf.py",
    title = "TF Activity Maps",
    icon = ":material/psychology:"
)

s_pathway_page = st.Page(
    page = "views/spatial_pathway.py",
    title = "Pathway Activity Maps",
    icon = ":material/shuffle:"
)

# ligand_page = st.Page(
#     page = "views/ligand_receptor_TF_pathway.py",
#     title = "Ligand-Receptor-TF-Pathway heatmaps",
#     icon = ":material/chevron_right:"
# )

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact us",
    icon = ":material/send:"
)

citation_page = st.Page(
    page = "views/citation.py",
    title = "Citation",
    icon = "📚"
)

# -- NAVIGATION --

pg = st.navigation(
    {
        "": [home_page, datasets_page],
        "Analysis of Individual Samples": [metaprogram_page, metaprogram_feature_page, gene_page, s_tf_page, s_pathway_page , drug2cell_page],  # ligand_page,
        "Comparison Across Samples": [dotplot_page,  heatmap_gene_correlation_page], 
        "Support": [citation_page, contact_page]
    }
)



# -- SHARED ON ALL PAGES --
# st.sidebar.text("Made by Osmanbeyoglu Lab")

# -- RUN NAVIGATION --
pg.run()
st.divider()
st.markdown(footer,unsafe_allow_html=True) 


