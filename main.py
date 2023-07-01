import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1,col2 =st.columns(2)


with col1:
    st.image("images/photo.png",width=600)

with col2:
    st.title("Umesh Rautgol")
    content="""i am from maharashtra solapur"""
    st.info(content)


content2=""" below u will find apps created by me feel free to contact me !!"""

st.write(content2)


col3,col4 =st.columns(2)

df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])