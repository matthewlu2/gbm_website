import streamlit as st
from style import page_style, footer
import pandas as pd
from persist import load_widget_state

# --- PAGE SETUP ----

st.set_page_config(
        page_title='GBM',
        page_icon= "./logo/gbm_ribbon.png",
        initial_sidebar_state="expanded",
)

max_width_str = f"max-width: {80}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---- start main ---

load_widget_state()

df_sample = pd.read_csv('./data/dataset.csv')
df_sample.index = df_sample.index + 1
st.session_state['df_sample'] = df_sample

home_page = st.Page(
    page = "views/home.py",
    title = "Home",
    icon = ":material/home:",
    default= True,
)

datasets_page = st.Page(
    page = "views/datasets.py",
    title = "Datasets",
    icon = ":material/dataset:"
)

metaprogram_page = st.Page(
    page = "views/metaprogram.py",
    title = "Metaprogram",
    icon = ":material/computer:"    
)

dotplot_pw_page = st.Page(
    page = "views/dotplot_pw_across_samples.py",
    title = "Metaprogram Pathway Across Sample",
    icon = ":material/blur_linear:"  
)

dotplot_tf_page = st.Page(
    page = "views/dotplot_tf_across_samples.py",
    title = "Metaprogram TF Across Sample",
    icon = ":material/blur_linear:"  
)

dotplot_tf_correlation_page = st.Page(
    page = "views/dotplot_tf_correlation.py",
    title = "TF Correlation",
    icon = ":material/blur_linear:"  
)

heatmap_gene_correlation_page = st.Page(
    page = "views/heatmap_gene_correlation.py",
    title = "Gene Correlation",
    icon = ":material/labs:"
)

gene_page = st.Page(
    page = "views/spatial_gene.py",
    title = "Spatial Gene Expression",
    icon = ":material/genetics:"
)

s_tf_page = st.Page(
    page = "views/spatial_tf.py",
    title = "Spatial TF Activity",
    icon = ":material/cycle:"
)

s_pathway_page = st.Page(
    page = "views/spatial_pathway.py",
    title = "Spatial Pathway Activity",
    icon = ":material/footprint:"
)

ligand_page = st.Page(
    page = "views/ligand_receptor.py",
    title = "Ligand-Receptor-TF-Pathway",
    icon = ":material/settings_input_antenna:"
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact Us",
    icon = ":material/contact_page:"
)

# -- NAVIGATION --

pg = st.navigation(
    {
        "Overview": [home_page, datasets_page],
        "Single Sample": [metaprogram_page, gene_page, s_pathway_page,  s_tf_page, ligand_page],
        "Multiple Sample": [ heatmap_gene_correlation_page  , dotplot_tf_page, dotplot_pw_page], 
        "Contact": [contact_page,]
    }
)


# -- SHARED ON ALL PAGES --
# st.sidebar.text("Made by Osmanbeyoglu Lab")

# -- RUN NAVIGATION --
pg.run()
st.divider()
st.markdown(footer,unsafe_allow_html=True) 





