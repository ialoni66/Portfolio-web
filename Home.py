import streamlit as st
import pandas

zim = "https://www.nicepng.com/png/detail/82-828227_zim-yelling-invader-zim-zim.png"
gir = "https://www.nicepng.com/png/detail/44-441373_gir-in-pig-photo-invader-zim-gir-pig.png"

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(zim, width=300)
    #st.image(gir)
with col2:
    st.title("Ilai Aloni")
    content = """ Shit about me
    """
    st.info(content)

st.subheader("Below you can find some apps I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code] ({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code] ({row['url']})")
