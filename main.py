import streamlit as st

# MBTI 데이터 (16가지)
mbti_data = {
    "INTJ": {
        "desc": "전략적이고 계획적인 성향, 목표 지향적.",
        "best_match": "ENFP",
        "reason": "창의성과 실행력이 균형을 이루어 시너지 효과."
    },
    "INTP": {
        "desc": "논리적이고 분석적인 성향, 아이디어 탐구를 좋아함.",
        "best_match": "ENTJ",
        "reason": "체계적인 리더십과 창의적 문제 해결이 조화를 이룸."
    },
    "ENTJ": {
        "desc": "리더십이 강하고 목표를 달성하는 데 능숙함.",
        "best_match": "INTP",
        "reason": "아이디어와 실행력이 결합되어 강력한 팀을 형성."
    },
    "ENTP": {
        "desc": "창의적이고 도전적인 성향, 새로운 아이디어를 즐김.",
        "best_match": "INFJ",
        "reason": "비전을 공유하며 서로의 성장을 도모."
    },
    "INFJ": {
        "desc": "깊은 통찰력과 이상주의적 성향.",
        "best_match": "ENFP",
        "reason": "꿈과 가치관을 공유하고 서로 격려."
    },
    "INFP": {
        "desc": "이상적이고 가치 중심적인 성향.",
        "best_match": "ENFJ",
        "reason": "서로의 가치와 목표를 지지하며 성장."
    },
    "ENFJ": {
        "desc": "사람들을 이끄는 능력과 따뜻한 배려심.",
        "best_match": "INFP",
        "reason": "서로의 꿈을 실현하도록 돕는 이상적인 관계."
    },
    "ENFP": {
        "desc": "열정적이고 창의적인 성향, 새로운 경험을 좋아함.",
        "best_match": "INTJ",
        "reason": "자유로운 발상과 체계적인 계획이 조화를 이룸."
    },
    "ISTJ": {
        "desc": "신중하고 책임감이 강하며 체계적인 성향.",
        "best_match": "ESFP",
        "reason": "균형 잡힌 현실감각과 에너지가 어우러짐."
    },
    "ISFJ": {
        "desc": "배려심이 깊고 성실하며 안정적인 성향.",
        "best_match": "ESFP",
        "reason": "따뜻함과 활발함이 서로를 보완."
    },
    "ESTJ": {
        "desc": "조직적이고 실용적인 성향, 강한 추진력.",
        "best_match": "ISTP",
        "reason": "계획성과 유연성이 조화를 이루어 효율적."
    },
    "ESFJ": {
        "desc": "친절하고 사교적인 성향, 타인을 돕는 것을 즐김.",
        "best_match": "ISFP",
        "reason": "배려와 자유로움이 균형을 이루는 관계."
    },
    "ISTP": {
        "desc": "문제 해결 능력이 뛰어나고 실용적인 성향.",
        "best_match": "ESTJ",
        "reason": "실행력과 조직력이 함께하면 효율성 극대화."
    },
    "ISFP": {
        "desc": "온화하고 예술적인 성향, 자유를 중시함.",
        "best_match": "ESFJ",
        "reason": "자유로움과 안정감이 어우러지는 관계."
    },
    "ESTP": {
        "desc": "활동적이고 즉흥적인 성향, 모험을 즐김.",
        "best_match": "ISFJ",
        "reason": "안정성과 에너지가 서로를 보완."
    },
    "ESFP": {
        "desc": "사교적이고 에너지가 넘치는 성향.",
        "best_match": "ISTJ",
        "reason": "현실적인 계획과 활발함이 조화를 이룸."
    }
}

# Streamlit 앱 설정
st.set_page_config(page_title="MBTI 궁합 추천", page_icon="💡")

st.title("💡 MBTI 성격 & 궁합 추천")
st.write("당신의 MBTI를 선택하면 성격 설명과 최고의 궁합을 알려드립니다.")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI는?", sorted(mbti_data.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"📌 {selected_mbti}의 성격")
    st.write(mbti_data[selected_mbti]["desc"])
    
    st.subheader("💞 최고의 궁합")
    best = mbti_data[selected_mbti]["best_match"]
    st.write(f"**{best}** — {mbti_data[selected_mbti]['reason']}")

# 푸터
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
