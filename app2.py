pip install streamlit
pip install openai  # 만약 OpenAI GPT API를 사용하고자 한다면 이 라이브러리도 설치

import streamlit as st
import openai  # OpenAI GPT를 사용할 경우, 이 라이브러리가 필요합니다.

# OpenAI API 키 설정 (만약 GPT 모델을 사용한다면)
openai.api_key = 'YOUR_API_KEY'

# 챗봇 응답 생성 함수
def generate_response(user_input):
    try:
        # OpenAI GPT API를 사용하여 응답 생성
        response = openai.Completion.create(
            engine="text-davinci-003",  # 또는 "gpt-3.5-turbo" 등 다른 모델을 사용할 수 있습니다.
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit 앱 구성
def chatbot_app():
    st.title("Streamlit 챗봇")

    # 사용자 입력을 받기 위한 텍스트 상자
    user_input = st.text_input("당신의 질문을 입력하세요:")

    # 사용자가 입력을 했을 때 응답 생성
    if user_input:
        # 응답 생성
        bot_response = generate_response(user_input)
        st.write(f"챗봇: {bot_response}")

# 앱 실행
if __name__ == "__main__":
    chatbot_app()
