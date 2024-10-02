import streamlit as st

#import streamlit_analytics

#streamlit_analytics.start_tracking()
#streamlit_analytics.stop_tracking()

img = "./images/home1.png"


st.markdown("<h2 style='text-align: center;  color: black;'>Spatial Regulatory Landscape of Glioblastoma Tumor Immune Microenvironment", unsafe_allow_html=True)


st.image(img)

# st.markdown('➡️ Read our paper here: https://www.google.com')    
st.write("Glioblastoma (GBM) presents a formidable challenge in oncology due to its aggressive nature and limited treatment options. The tumor microenvironment (TME) plays a crucial role in shaping cancer phenotypes, including proliferation, invasion, metastasis, and drug resistance. Spatial transcriptomics (ST) technologies provide a promising approach to unravel the complex interactions between tumor cells and their microenvironment. In GBM, the interplay between tumor cells and the immune microenvironment significantly influences disease outcomes.")
st.write("In this study, we analyzed publicly available GBM ST datasets to map the regulatory landscape and ligand-receptor interactions within the GBM TME. We provide access to predicted transcription factor and pathway activities, as well as ligand and receptor expression across samples. Our resource holds great promise for enhancing our understanding of GBM biology, identifying novel therapeutic targets, and ultimately improving treatment strategies and patient outcomes for this devastating disease.")
