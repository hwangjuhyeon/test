import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "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"  # 여기에 실제 OpenAI API 키를 입력하세요.

# 챗봇 응답 생성 함수
def generate_response(user_input):
    try:
        # 최신 API 방식 사용 (openai.completions.create)
        response = openai.completions.create(
            model="gpt-4-mini",  # GPT-4 mini 모델 사용
            prompt=user_input,
            max_tokens=150  # 원하는 토큰 수로 응답 길이 설정
        )
        return response['choices'][0]['text'].strip()
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
