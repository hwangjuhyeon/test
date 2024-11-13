import streamlit as st

st.header("안녕하세요")
st.write("만나서 반갑습니다.")

st.link_button("유튜브 바로가기","https://www.youtube.com")
st.link_button("네이버 바로가기","https://www.naver.com")
st.link_button("구글 바로가기","https://www.google.com")

from openai import OpenAI

client=OpenAI
client.api_key=api

if 'key' not in st.session_state:
    st.session_state['key'] = 'hello'

st.write(st.session_state.key)

st.text_input("Your name", key="name") 
st.session_state.name

st.page_link("https://www.google.com", label="Google", icon="🌎")

api_key = st.text_input("OpenAI API Key", type='password')
client = OpenAI(api_key=api_key)

prompt = st.text_area("Prompt")
messages = [
    {"role": "user", "content": prompt}
]
