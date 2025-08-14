import streamlit as st
import time

# -----------------------
# 페이지 & 스타일
# -----------------------
st.set_page_config(page_title="MBTI 2인 궁합 테스트", page_icon="💌")

st.markdown("""
<style>
body { background: #FFF9FB; }
@keyframes fadeInScale {
    0% { opacity: 0; transform: scale(0.8); }
    100% { opacity: 1; transform: scale(1); }
}
@keyframes shimmer {
    0% { background-position: -200px 0; }
    100% { background-position: 200px 0; }
}
.title {
  text-align:center; font-size: 32px; font-weight: 800; color:#FF6F91;
  padding: 8px 0 2px 0;
}
.sub {
  text-align:center; color:#555; margin-bottom: 12px;
}
.card {
  background:#FFFFFF; border-radius:18px; padding:18px; 
  box-shadow: 0 6px 24px rgba(255,111,145,.15);
  margin: 8px 0;
  animation: fadeInScale 0.5s ease forwards;
}
.score {
  font-size: 32px; font-weight:700; text-align:center; margin: 6px 0 2px 0;
  background: linear-gradient(90deg, #FF6F91, #FFC3A0);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.badge {
  display:inline-block; padding:6px 10px; border-radius:999px; 
  background:#FFE4EC; color:#FF3B7A; font-weight:700; font-size:13px;
}
.pill {
  display:inline-block; padding:6px 10px; border-radius:10px; 
  background:#F6F6FF; margin-right:6px; margin-bottom:6px; font-size:13px;
}
.stButton>button {
  background:#FF9AA2; color:#fff; border-radius:12px; padding:10px 18px;
  font-size:16px; transition:.2s; border:0;
  box-shadow: 0 0 10px rgba(255,111,145,0.5);
}
.stButton>button:hover { background:#FF6F91; transform: translateY(-1px) scale(1.02); box-shadow: 0 0 15px rgba(255,111,145,0.7); }
.hint { color:#777; font-size:13px; text-align:center; }
.sep { height:10px; }
.sparkle {
  background: linear-gradient(90deg, #fff5f7 25%, #ffe4ec 50%, #fff5f7 75%);
  background-size: 200% 100%;
  animation: shimmer 2s infinite linear;
  padding: 10px; border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💌 MBTI 2인 궁합 테스트</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>두 사람의 MBTI를 선택하고 궁합을 확인해보세요! ✨</div>", unsafe_allow_html=True)

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
    if score >= 90: return "💖 환상의 케미!"
    if score >= 80: return "💞 좋은 케미!"
    if score >= 70: return "✨ 무난-좋음"
    if score >= 60: return "🙂 보통"
    if score >= 50: return "🤝 노력형 케미"
    return "🌥️ 도전 필요"

# -----------------------
# 입력 UI
# -----------------------
c1, c2 = st.columns(2)
with c1:
    a = st.selectbox("사람 A의 MBTI", MBTIS, index=MBTIS.index("ENFP"))
with c2:
    b = st.selectbox("사람 B의 MBTI", MBTIS, index=MBTIS.index("INTJ"))

st.markdown("<div class='sep'></div>", unsafe_allow_html=True)

if st.button("궁합 확인하기 💫"):
    score = compatibility_score(a, b)
    notes = dimension_notes(a, b)
    summary = short_summary(score)

    bg_class = "sparkle" if score >= 85 else ""

    st.markdown(f"<div class='card {bg_class}'>", unsafe_allow_html=True)
    st.markdown(f"<div class='score'>{score} / 100</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;margin:0 0 8px 0'>{a} ❤️ {b}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;margin:4px 0 0 0'>{summary}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("**강점/주의 포인트**", unsafe_allow_html=True)
    for n in notes:
        st.markdown(f"<span class='pill'>{n}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='hint'>※ 재미용 간단 테스트입니다 🙂</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("Made with 💝 using Streamlit")
