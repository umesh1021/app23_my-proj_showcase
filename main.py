import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1,col2 =st.columns(2)


with col1:
    st.image("images/umesh.jpg",width=400)

with col2:
    st.title("Umesh Rautgol")
    content="""I am from maharashtra solapur , school-Indian model school solapur ,currently persuing B.TeCH in Information Technology at Pillai College of Engineering Panvel ."""
    st.info(content)


content2=""" below u will find apps created by me feel free to contact me !!"""

st.write(content2)


col3,empty_column,col4 =st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']}")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']}")

