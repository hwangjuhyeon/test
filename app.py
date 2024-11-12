import streamlit as st
st.header("안녕하세요")
st.write("만나서 반갑습니다.")

st.link_button("유튜브 바로가기","https://www.youtube.com")
st.link_button("네이버 바로가기","https://www.naver.com")

import openai
openai.api_key="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"

completion = openai.ChatCompletion.create(
  model="gpt-4o-mini", 
  messages=[{"role": "user", "content": "Who won the world series in 2020?"}]
)

print(completion.choices[0].message.content)
