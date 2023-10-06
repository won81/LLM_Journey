import streamlit as st

st.set_page_config(page_title='예제 - LLM Journey', page_icon=':rabbit:', layout='wide')

st.title('🐇 예제')

with st.expander("Zero-shot Prompting"):
    st.markdown("""
Large Languge Model
대규모 언어 모델
""")

with st.expander("Few-shot Prompting"):
    st.markdown("""
Large Languge Model
대규모 언어 모델
""")
