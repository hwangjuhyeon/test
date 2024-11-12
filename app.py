import streamlit as st
st.header("안녕하세요")
st.write("만나서 반갑습니다.")

st.link_button("유튜브 바로가기","https://www.youtube.com")
st.link_button("네이버 바로가기","https://www.naver.com")
st.link_button("구글 바로가기","https://www.google.com")

from openai import OpenAI

api=st.text_input("API_KEY")

client=OpenAI
client.api_key=api

def ask_openai(question, chat_log=None):
    if chat_log is None:
        chat_log = []
    messages = [{"role": "user", "content": msg} for msg in chat_log]
    messages.append({"role": "user", "content": question})
    # new openai 반영.
    response = client.chat.completions.create(
        model="gpt-4.o-mini",
        messages=messages
    )
    # new openai 반영.
    answer = response.choices[0].message.content
    return answer

def chat():
    st.write("chatting is started. If you want to exit, enter 'exit'.")
    chat_log = []
    while True:
        user_input = st.text_input("User: ")
        if user_input.lower() == 'exit':
            st.write("Exiting...")
            break
        response = ask_openai(user_input, chat_log)
        st.write(f"AI bot: {response}")
        chat_log.extend([user_input, response])

if __name__ == "__main__":
    chat()
