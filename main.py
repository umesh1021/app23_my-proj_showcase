import streamlit as st

col1,col2 =st.columns(2)

with col1:
    st.image("image/photo.png")

with col2:
    st.title("Umesh Rautgol")
    content="""i am from maharashtra solapur"""
    st.write()