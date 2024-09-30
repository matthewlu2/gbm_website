# from streamlit import session_state as _state
import streamlit as st

_PERSIST_STATE_KEY = f"{__name__}_PERSIST"
# st.write(_PERSIST_STATE_KEY)

def persist(key: str) -> str:

    """Mark widget state as persistent."""
    if _PERSIST_STATE_KEY not in st.session_state:
        st.session_state[_PERSIST_STATE_KEY] = set()

    st.session_state[_PERSIST_STATE_KEY].add(key)

    return key


def load_widget_state():

    """Load persistent widget state."""

    if _PERSIST_STATE_KEY in st.session_state:
        st.session_state.update({
            key: value
            for key, value in st.session_state.items()
            if key in st.session_state[_PERSIST_STATE_KEY]
        })
    
def update_widget_state(key, value):
    if _PERSIST_STATE_KEY in st.session_state:
        st.session_state.update({
            key: value
        })