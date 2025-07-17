import streamlit as st
from logic.decoder import decode_catalog_number

st.set_page_config(page_title="10250T Catalog Decoder", layout="centered")

st.title("🔍 10250T Catalog Decoder")

st.markdown("""
Enter a 10250T catalog number (e.g., `10250T-A1`, `10250T-LR`, `10250T-PPG`) to decode its attributes.
""")

catalog_number = st.text_input("Catalog Number", placeholder="e.g. 10250T-A1")

if catalog_number:
    result = decode_catalog_number(catalog_number)
    st.subheader("Decoded Result")
    for key, value in result.items():
        st.write(f"**{key}**: {value}")
