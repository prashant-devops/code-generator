# frontend/__init__.py

import streamlit as st
from .streamlit_app import main

st.set_page_config(page_title="Code Generator")

if __name__ == "__main__":
    main()