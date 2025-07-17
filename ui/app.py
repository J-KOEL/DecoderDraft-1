import streamlit as st
from logic.decoder import decode_catalog_number

st.title("10250T Catalog Decoder")

catalog_number = st.text_input("Enter Catalog Number")

if catalog_number:
    result = decode_catalog_number(catalog_number)
    st.write("Decoded Result:", result)

