import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("zim.png")
with col2:
    st.title("Ilai Aloni")
    content = """ Shit about me
    """
    st.info(content)

st.subheader("Below you can find some apps I have built in Python. Feel free to contact me!")

# Contact me Page



