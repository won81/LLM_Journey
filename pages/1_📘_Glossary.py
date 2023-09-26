import streamlit as st

st.set_page_config(page_title='Glossary - LLM Journey', page_icon=':rabbit:', layout='wide')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/1_📘_Glossary.css")

# Title
st.title('📘 Glossary')

with st.expander("LLM"):
    st.markdown("""
Large Languge Model
대규모 언어 모델
""")
