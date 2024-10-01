import streamlit as st
import pandas as pd
from persist import update_widget_state
# from st_aggrid import AgGrid, GridOptionsBuilder

st.markdown("<h2 style='text-align: center; color: black;'>Dataset</h1>", unsafe_allow_html=True)  
st.info("Explore samples by searching for specific entries. For individual samples, you will find clinical information, H&E stained images, metaprogram annotations, spatial mRNA expression, transcription factor (TF) and pathway activity visualizations as well as TF-pathway-ligand-receptor correlation heatmaps. For multiple samples, we offer comparative analysis for TF/pathway metaprogram associations and single gene expression correlations with TF and pathway activity across the samples.")

a, b = st.columns([2.3, 20])



# -- TABLE --
df_sample = st.session_state.df_sample
st.markdown("""
    <style>
        .stTable tr {
            height: 56px; # use this to adjust the height
        }
    </style>
""", unsafe_allow_html=True)

b.table(df_sample)        

sample_list = df_sample['Sample-ID'].values.tolist()
a.text("")
a.text("")
a.text("")
a.text("")
for i in range(26):
    if a.button("Analysis", i):
        update_widget_state('sample_id', sample_list[i])
        st.switch_page("views/metaprogram.py")

# a.text("")
# a.text("")
# a.text("")
# a.text("")
# a.button("Analysis", 1)
# a.button("Analysis", 2)
# a.button("Analysis", 3)
# a.button("Analysis", 4)
# a.button("Analysis", 5)
# a.button("Analysis", 6)
# a.button("Analysis", 7)
# a.button("Analysis", 8)
# a.button("Analysis", 9)
# a.button("Analysis", 10)
# a.button("Analysis", 11)
# a.button("Analysis", 12)
# a.button("Analysis", 13)
# a.button("Analysis", 14)
# a.button("Analysis", 15)
# a.button("Analysis", 16)
# a.button("Analysis", 17)
# a.button("Analysis", 18)
# a.button("Analysis", 19)
# a.button("Analysis", 20)
# a.button("Analysis", 21)
# a.button("Analysis", 22)
# a.button("Analysis", 23)
# a.button("Analysis", 24)
# a.button("Analysis", 25)
# a.button("Analysis", 26)




# grid_builder = GridOptionsBuilder.from_dataframe(df)
# grid_options = grid_builder.build()

# grid_options['columnDefs'][0]['checkboxSelection'] = True

# AgGrid(data=df, gridOptions=grid_options, key='grid1')