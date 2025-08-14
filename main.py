import streamlit as st

# -----------------------
# 페이지 & 스타일
# -----------------------
st.set_page_config(page_title="☁️ MBTI 하늘 궁합 테스트", page_icon="☁️")

st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #B5EFFF 0%, #FFD6F6 100%);
    font-family: 'Segoe UI', sans-serif;
}
@keyframes fadeUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
.cloud-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(8px);
    border-radius: 20px;
    padding: 20px;
    margin: 12px 0;
    box-shadow: 0 8px 30px rgba(255,255,255,0.6);
    animation: fadeUp 0.8s ease forwards;
}
.score {
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    background: radial-gradient(circle at 50% 50%, #FFD54F, #FF6F91);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 4px rgba(255,255,255,0.6));
}
.stButton>button {
    background: linear-gradient(90deg, #A7E9FF, #FFD6F6);
    color: #333;
    border-radius: 25px;
    padding: 10px 22px;
    font-size: 16px;
    border: none;
    box-shadow: 0 6px 20px rgba(255,255,255,0.7);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(255,255,255,0.9);
}
.mbti-pill {
    display:inline-block; 
    padding: 6px 10px; 
    margin: 4px;
    background: rgba(255,255,255,0.7);
    border-radius: 12px;
    font-size: 13px;
    box-shadow: 0 3px 8px rgba(255,255,255,0.5);
}
.subtitle {
    text-align:center; 
    color:#fff; 
    font-size:16px;
    margin-bottom: 16px;
    text-shadow: 0 1px 4px rgba(0,0,0,0.15);
}
.title {
    text-align:center; 
    font-size: 34px; 
    font-weight: 900; 
    color: white; 
    text-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# 데이터
# -----------------------
MBTIS = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

BONUS = {
    ("INTJ","ENFP"): 8, ("ENFP","INTJ"): 8,
    ("INFJ","ENFP"): 6, ("ENFP","INFJ"): 6,
    ("ISTJ","ESFP"): 6, ("ESFP","ISTJ"): 6,
    ("INTP","ENTJ"): 5, ("ENTJ","INTP"): 5,
    ("ISFP","ESFJ"): 5, ("ESFJ","ISFP"): 5,
    ("ISTP","ESTJ"): 5, ("ESTJ","ISTP"): 5,
}

DIM_TEXT = {
    "E": ("둘 다 외향적이라 에너지가 UP!", "에너지가 다른 만큼 서로 페이스 조절 필요"),
    "I": ("둘 다 내향적이라 편안함 👍", "서로의 휴식/활동 리듬 이해 필요"),
    "S": ("현실 감각이 비슷해 실행력 GOOD", "상상과 현실의 밸런스를 맞추면 시너지!"),
    "N": ("아이디어 대화 술술~", "비전-현실 밸런스 조절 필요"),
    "T": ("논리/원칙 통일 → 의사결정 빠름", "논리 vs 감정 존중 필수"),
    "F": ("감정 공감이 잘 맞음", "감정 신호 놓치지 않기"),
    "J": ("계획형 콤비라 안정적", "자유도와 안정감 균형 필요"),
    "P": ("즉흥 즐기기 잘 맞음", "자유/계획 선호 미리 합의"),
}

def compatibility_score(a: str, b: str):
    base = 50.0
    same = sum(1 for x, y in zip(a, b) if x == y)
    score = base + same * 12.5
    score += BONUS.get((a,b), 0)
    return max(0, min(100, round(score, 1)))

def dimension_notes(a: str, b: str):
    notes = []
    for i, (x, y) in enumerate(zip(a, b)):
        dim_pair = ["EI","SN","TF","JP"][i]
        if x == y:
            notes.append(f"{dim_pair}: {DIM_TEXT[x][0]}")
        else:
            notes.append(f"{dim_pair}: {DIM_TEXT[x][1]}")
    return notes

def short_summary(score):
    if score >= 90: return "🌈 환상의 케미!"
    if score >= 80: return "☀️ 좋은 케미!"
    if score >= 70: return "💙 무난-좋음"
    if score >= 60: return "⛅ 보통"
    if score >= 50: return "🤝 노력형 케미"
    return "🌧️ 도전 필요"

# -----------------------
# UI
# -----------------------
st.markdown("<div class='title'>☁️ MBTI 궁합 테스트</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>두 사람의 MBTI를 선택하고 하늘 위에서 궁합을 확인하세요</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    a = st.selectbox("사람 A", MBTIS, index=MBTIS.index("ENFP"))
with col2:
    b = st.selectbox("사람 B", MBTIS, index=MBTIS.index("INTJ"))

if st.button("궁합 확인하기 ✨"):
    score = compatibility_score(a, b)
    notes = dimension_notes(a, b)
    summary = short_summary(score)

    st.markdown("<div class='cloud-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='score'>{score} / 100</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; margin-top:0'>{a} ☁️ {b}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; margin-top:8px'>{summary}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='cloud-card'>", unsafe_allow_html=True)
    st.markdown("**구름 속 분석**", unsafe_allow_html=True)
    for n in notes:
        st.markdown(f"<span class='mbti-pill'>{n}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ☁️ and 💙 using Streamlit")

