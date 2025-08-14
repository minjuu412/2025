import streamlit as st

# 페이지 상태 관리
if "show_results" not in st.session_state:
    st.session_state.show_results = False

# CSS 스타일 적용
st.markdown("""
    <style>
    body {
        background-color: #FFF9F9;
    }
    .title {
        font-size: 30px;
        font-weight: bold;
        color: #FF6F91;
        text-align: center;
        padding: 10px;
    }
    .stButton>button {
        background-color: #FF9AA2;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF6F91;
        color: white;
        transform: scale(1.05);
    }
    .result-card {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        font-size: 18px;
    }
    .good {
        background-color: #FFECEC;
    }
    .neutral {
        background-color: #FFF6E5;
    }
    </style>
""", unsafe_allow_html=True)

# 간단한 MBTI 궁합 데이터 예시
compatibility = {
    ("INTJ", "ENFP"): {"score": "💖 95%", "desc": "서로의 부족한 부분을 보완하고, 창의성과 실행력이 잘 어울립니다."},
    ("ENFP", "INTJ"): {"score": "💖 95%", "desc": "서로의 부족한 부분을 보완하고, 창의성과 실행력이 잘 어울립니다."},
    ("ISTJ", "ESFP"): {"score": "💞 90%", "desc": "현실적인 계획과 활발함이 조화를 이룹니다."},
    ("ESFP", "ISTJ"): {"score": "💞 90%", "desc": "현실적인 계획과 활발함이 조화를 이룹니다."},
    ("INFJ", "ENFP"): {"score": "💗 92%", "desc": "꿈과 가치관을 공유하고 서로를 격려합니다."},
    ("ENFP", "INFJ"): {"score": "💗 92%", "desc": "꿈과 가치관을 공유하고 서로를 격려합니다."},
}

# MBTI 목록
mbti_list = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

# 제목
st.set_page_config(page_title="MBTI 3인 궁합 테스트", page_icon="💌")
st.markdown("<div class='title'>💌 MBTI 3인 궁합 테스트 💌<br>✨ 귀엽고 예쁘게 궁합 보기 ✨</div>", unsafe_allow_html=True)

# 궁합 표시 함수
def show_compat(pair):
    if pair in compatibility:
        data = compatibility[pair]
        st.markdown(
            f"<div class='result-card good'><b>{pair[0]} ❤️ {pair[1]}</b><br>점수: {data['score']}<br>{data['desc']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='result-card neutral'><b>{pair[0]} ❤️ {pair[1]}</b><br>🤔 데이터가 없습니다.</div>",
            unsafe_allow_html=True
        )

# 홈 화면
if not st.session_state.show_results:
    st.write("당신과 친구 2명의 MBTI를 선택하면, 각 조합의 궁합을 알려드립니다! 🎀")
    col1, col2, col3 = st.columns(3)
    with col1:
        user_mbti = st.selectbox("당신", mbti_list, key="user")
    with col2:
        friend1_mbti = st.selectbox("친구 1", mbti_list, key="friend1")
    with col3:
        friend2_mbti = st.selectbox("친구 2", mbti_list, key="friend2")

    if st.button("✨ 궁합 확인하기 ✨"):
        st.session_state.show_results = True
        st.session_state.results = [
            (user_mbti, friend1_mbti),
            (user_mbti, friend2_mbti),
            (friend1_mbti, friend2_mbti)
        ]

# 결과 화면
else:
    st.subheader("🔍 궁합 결과")
    for pair in st.session_state.results:
        show_compat(pair)

    if st.button("🏠 홈으로 돌아가기"):
        st.session_state.show_results = False
        st.experimental_rerun()

# 푸터
st.markdown("---")
st.caption("Made with 💝 for Fun using Streamlit")

