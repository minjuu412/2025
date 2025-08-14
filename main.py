import streamlit as st

# HTML/CSS 스타일 적용
st.markdown("""
    <style>
    body {
        background-color: #FFF9F9;
    }
    .question-card {
        background-color: #FFECEC;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #FF9AA2;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #FF6F91;
        color: white;
    }
    .result-card {
        background-color: #FFDDE1;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        font-size: 20px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 질문 데이터
questions = [
    {"type": "EI", "q": "사람 많은 모임이 있을 때 나는?", "a": ("에너지가 충전된다 (E)", "에너지가 소모된다 (I)")},
    {"type": "EI", "q": "휴일 계획은?", "a": ("친구와 약속을 많이 잡는다 (E)", "혼자만의 시간을 보낸다 (I)")},
    {"type": "SN", "q": "문제를 해결할 때 나는?", "a": ("사실과 데이터 위주로 생각한다 (S)", "직관과 가능성을 본다 (N)")},
    {"type": "SN", "q": "대화를 할 때 나는?", "a": ("구체적인 예시를 많이 든다 (S)", "추상적인 아이디어를 이야기한다 (N)")},
    {"type": "TF", "q": "결정을 내릴 때 나는?", "a": ("논리와 원칙을 따른다 (T)", "사람의 감정을 고려한다 (F)")},
    {"type": "TF", "q": "상대방과 갈등이 생기면?", "a": ("논리적으로 문제를 분석한다 (T)", "감정을 이해하고 풀려고 한다 (F)")},
    {"type": "JP", "q": "여행을 갈 때 나는?", "a": ("계획을 미리 세운다 (J)", "즉흥적으로 간다 (P)")},
    {"type": "JP", "q": "일정을 관리할 때 나는?", "a": ("체계적으로 기록한다 (J)", "필요할 때만 체크한다 (P)")}
]

# MBTI 설명
mbti_info = {
    "INTJ": "전략적이고 계획적인 성향, 목표 지향적.",
    "INTP": "논리적이고 분석적인 성향, 아이디어 탐구를 좋아함.",
    "ENTJ": "리더십이 강하고 목표 달성에 능숙함.",
    "ENTP": "창의적이고 도전적인 성향, 새로운 아이디어를 즐김.",
    "INFJ": "깊은 통찰력과 이상주의적 성향.",
    "INFP": "이상적이고 가치 중심적인 성향.",
    "ENFJ": "사람들을 이끄는 능력과 따뜻한 배려심.",
    "ENFP": "열정적이고 창의적인 성향, 새로운 경험을 좋아함.",
    "ISTJ": "신중하고 책임감이 강하며 체계적인 성향.",
    "ISFJ": "배려심이 깊고 성실하며 안정적인 성향.",
    "ESTJ": "조직적이고 실용적인 성향, 강한 추진력.",
    "ESFJ": "친절하고 사교적인 성향, 타인을 돕는 것을 즐김.",
    "ISTP": "문제 해결 능력이 뛰어나고 실용적인 성향.",
    "ISFP": "온화하고 예술적인 성향, 자유를 중시함.",
    "ESTP": "활동적이고 즉흥적인 성향, 모험을 즐김.",
    "ESFP": "사교적이고 에너지가 넘치는 성향."
}

# 페이지 설정
st.set_page_config(page_title="고등학생 MBTI 검사", page_icon="🎀")
st.title("🎀 고등학생 전용 MBTI 검사 🎀")
st.write("8문항으로 귀엽고 빠르게 MBTI를 알아보세요! 💖")

# 사용자 답변 저장
answers = {}
for idx, q in enumerate(questions):
    st.markdown(f"<div class='question-card'><b>{idx+1}. {q['q']}</b></div>", unsafe_allow_html=True)
    choice = st.radio("", q["a"], index=None, key=f"q{idx}")
    answers[idx] = choice

# 검사 버튼
if st.button("✨ 검사 결과 보기 ✨"):
    if None in answers.values():
        st.warning("모든 질문에 답해주세요! 💌")
    else:
        score = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        for idx, ans in answers.items():
            if ans.endswith("(E)"): score["E"] += 1
            if ans.endswith("(I)"): score["I"] += 1
            if ans.endswith("(S)"): score["S"] += 1
            if ans.endswith("(N)"): score["N"] += 1
            if ans.endswith("(T)"): score["T"] += 1
            if ans.endswith("(F)"): score["F"] += 1
            if ans.endswith("(J)"): score["J"] += 1
            if ans.endswith("(P)"): score["P"] += 1

        mbti_result = (
            ("E" if score["E"] > score["I"] else "I") +
            ("S" if score["S"] > score["N"] else "N") +
            ("T" if score["T"] > score["F"] else "F") +
            ("J" if score["J"] > score["P"] else "P")
        )

        st.markdown(f"<div class='result-card'>💖 당신의 MBTI는 <b>{mbti_result}</b> 입니다! 💖<br>{mbti_info[mbti_result]}</div>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.caption("Made with 💝 for High School Students using Streamlit")

