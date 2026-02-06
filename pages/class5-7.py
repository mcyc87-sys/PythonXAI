import streamlit as st

uploaded_file = st.file_uploader("Upload a picture", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded image", width=300)
