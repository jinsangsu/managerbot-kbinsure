
import streamlit as st
import streamlit.components.v1 as components

# 키워드 기반 유도형 응답 사전
prompting_responses = {
    "자동이체": "사장님, 자동이체 관련해서 어떤 내용을 도와드릴까요? 등록, 변경, 해지 중 무엇이 궁금하신가요?",
    "타인카드": "사장님, 타인명의 카드 등록과 관련된 서류가 필요하신가요? 어떤 상황인지 말씀해주시면 자세히 안내드릴게요!",
    "무이자": "사장님, 무이자 할부에 대해 문의주셨군요. 차량, 금액, 카드사 중 어떤 부분이 궁금하신가요?",
    "스캔": "사장님, 어떤 문서를 스캔하시려는 건가요? 장기, 입출금, 재무, 고객 서류 중에서 알려주시면 안내드리겠습니다!",
    "승환": "사장님, 계약이 승환인지 여부를 확인하고 싶으신가요? 계약자 정보나 청약화면 확인 방법을 도와드릴까요?",
    "배서": "사장님, 배서와 관련해 어떤 처리를 원하시나요? 변경, 해지, 특약 추가 중 어떤 상황인지 말씀 부탁드립니다!",
    "카드": "사장님, 카드 등록, 변경, 해지 중 어떤 내용을 안내드릴까요? 사용 중인 카드 종류도 함께 알려주시면 좋습니다!",
    "스캔업무": "사장님, 어떤 문서를 스캔하시려는 건가요? 장기, 입출금, 재무, 고객 서류 중에서 알려주시면 안내드리겠습니다!",
    "계약": "사장님, 계약과 관련된 문의시 매니저에게 확인 후 안내드릴게요!"
}

def find_prompt_response(user_input):
    for keyword, response in prompting_responses.items():
        if keyword in user_input:
            return response
    return "사장님, 잠시만요! 매니저에게 확인 후 바로 안내드리겠습니다."

def main():
    st.set_page_config(page_title="매니저봇", page_icon="🤖", layout="centered")

    # 상단 타이틀 + 캐릭터 이미지 정식 출력 (st.columns 사용)
    col1, col2 = st.columns([8, 1])
    with col1:
        st.markdown("## 사장님, 안녕하세요!")
    with col2:
        st.image("managerbot_character.webp", width=48)

    st.markdown("궁금하신 것이 있으시죠? 저 매니저봇이 항상 옆에서 도와드리겠습니다. 업무 관련 궁금하신 내용은 매니저한테 가시기 전에 저부터 불러주세요!!!")

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    with st.form(key="input_form", clear_on_submit=True):
        user_input = st.text_input("사장님, 무엇이 궁금하신가요?", key="user_input")
        submitted = st.form_submit_button("질문하기")

    if submitted and user_input:
        response = find_prompt_response(user_input)
        st.session_state.conversation.append((user_input, response))
        st.rerun()

    # 대화 출력
    for question, answer in st.session_state.conversation:
        with st.container():
            st.markdown(f"💬 **질문:** {question}")
            st.markdown(f"🤖 **매니저봇 답변:** {answer}")
            st.markdown("---")

    # 자동 스크롤
    st.markdown("<div id='bottom_scroll_target'></div>", unsafe_allow_html=True)
    components.html("""
        <script>
            const target = document.getElementById("bottom_scroll_target");
            if (target) {
                setTimeout(() => {
                    target.scrollIntoView({ behavior: "smooth" });
                }, 100);
            }
        </script>
    """, height=0)

if __name__ == "__main__":
    main()
