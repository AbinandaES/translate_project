import streamlit as st
from googletrans import Translator
st.header('Machine Trnsaltion Demo')
input=st.text_area('Please ENter the text',value='')
option=st.selectbox('To which language you wish to translate this text to?',('Malayalam','Hindi','Tamil'))
if st.button('Translate'):
    translator=Translator()
    translation=translator.translate(input,des=option)
    st.write(translation.text)