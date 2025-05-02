import streamlit as st
import requests
import base64
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="생성형 매니저봇 애순", page_icon="🤖", layout="centered")
st.markdown('<style>* {font-family: "Nanum Gothic", sans-serif;}</style>', unsafe_allow_html=True)

# 타이틀 및 설명
st.title("💬 매니저봇 애순 (GPT 연동 v21.0)")
st.caption("설계사 사장님들의 질문에 친절하게 응답하는 충청호남본부 전용 매니저봇입니다")

# 캐릭터 이미지 로드
def load_avatar_base64(image_path="managerbot_character.webp"):
    try:
        with open(image_path, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode()
            return f"data:image/webp;base64,{b64}"
    except:
        return None

avatar_url = load_avatar_base64()

# 웰컴 메시지 출력
if avatar_url:
    welcome_html = f"""
    <div style='display: flex; align-items: flex-start; gap: 1rem; margin-top: 1rem;'>
        <img src='{avatar_url}' width='64px' style='border-radius: 12px;' />
        <div style='background: #f3f6fc; padding: 1rem 1.2rem; border-radius: 15px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05); font-size: 15px; line-height: 1.6;'>
            <strong style='font-size: 18px;'>사장님, 안녕하세요!</strong><br/>
            저는 앞으로 사장님들 업무를 도와드리는<br/>
            <strong>충청호남본부 매니저봇 '애순'</strong>이에요.<br/><br/>
            매니저님께 여쭤보시기 전에<br/>
            저 애순이한테 먼저 물어봐 주세요!<br/>
            제가 아는 건 바로, 친절하게 알려드릴게요!<br/><br/>
            사장님들이 더 빠르고, 더 편하게 영업하실 수 있도록<br/>
            늘 옆에서 든든하게 함께하겠습니다.<br/>
            잘 부탁드려요! 😊
        </div>
    </div>
    """
    st.markdown(welcome_html, unsafe_allow_html=True)

# 시스템 프롬프트 불러오기
with open("aesoon_prompt_v1.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력 처리
user_input = st.chat_input("사장님, 궁금한 내용 자유롭게 입력해 주세요!")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("애순이가 답변을 생각하고 있어요..."):
            try:
                payload = {
                    "messages": [{"role": "system", "content": system_prompt}] + st.session_state.messages
                }
                response = requests.post("http://localhost:8000/managerbot", json=payload)
                reply = response.json().get("reply", "애순이가 지금은 답변을 드릴 수 없어요.")
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error("❌ 애순이 응답을 받지 못했어요. 네트워크 또는 서버 오류일 수 있어요.")