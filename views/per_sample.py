import streamlit as st


def load_metaprogram():
    from views.metaprogram import main
    main()


st.sidebar.button("Page 1", on_click=load_metaprogram)
st.sidebar.button("Page 2")
st.sidebar.button("Page 3")

