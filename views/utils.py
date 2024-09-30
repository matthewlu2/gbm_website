import pandas as pd
import streamlit as st
import pickle


@st.cache_data
def get_sample_dataframe(filepath):
    df_sample = pd.read_csv(filepath)
    df_sample.index = df_sample.index + 1
    return(df_sample)

@st.cache_data
def get_sample_metaprograms(filepath):
    with open(filepath, 'rb') as f:
        d = pickle.load(f)
    return(d)