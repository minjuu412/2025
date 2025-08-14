import streamlit as st

# -----------------------
# 페이지 & 스타일
# -----------------------
st.set_page_config(page_title="MBTI 2인 궁합 테스트", page_icon="💌")

st.markdown("""
<style>
body { background: #FFF9FB; }
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
}
.score {
  font-size: 28px; font-weight:700; text-align:center; margin: 6px 0 2px 0;
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
}
.stButton>button:hover { background:#FF6F91; transform: translateY(-1px) scale(1.02); }
.select label { font-weight:700; color:#444; }
.hint { color:#777; font-size:13px; text-align:center; }
.sep { height:10px; }
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

# 인기 조합 보너스(양방향 포함)
BONUS = {
    ("INTJ","ENFP"): 8, ("ENFP","INTJ"): 8,
    ("INFJ","ENFP"): 6, ("ENFP","INFJ"): 6,
    ("ISTJ","ESFP"): 6, ("ESFP","ISTJ"): 6,
    ("INTP","ENTJ"): 5, ("ENTJ","INTP"): 5,
    ("ISFP","ESFJ"): 5, ("ESFJ","ISFP"): 5,
    ("ISTP","ESTJ"): 5, ("ESTJ","ISTP"): 5,
}

# 각 축 설명(같음/보완)
DIM_TEXT = {
    "E": ("둘 다 외향적이라 에너지가 UP! 함께 활동 계획 세우기 좋아요.", "에너지가 다른 만큼 서로 페이스 조절이 필요해요."),
    "I": ("둘 다 내향적이라 편안한 분위기 유지에 강점!", "서로의 휴식/활동 리듬을 이해하려는 노력이 포인트."),
    "S": ("현실 감각이 비슷해 실행력이 좋습니다.", "상상과 현실의 밸런스를 맞추면 시너지!"),
    "N": ("아이디어 대화가 술술~ 비전 공유에 강점!", "한쪽은 비전, 한쪽은 현실 체크로 균형을 잡아보세요."),
    "T": ("논리/원칙이 통일되어 의사결정이 빠릅니다.", "논리 vs 감정의 관점 차이를 존중하는 대화가 필요해요."),
    "F": ("감정 공감이 잘 맞아 관계 만족도가 높아요.", "상대의 감정 신호를 놓치지 않도록 주의!"),
    "J": ("계획형 콤비라 일정/약속 관리가 안정적!", "자유도와 안정감의 균형 잡기가 관건."),
    "P": ("유연하게 즉흥 즐기기 GOOD!", "서로의 자유/계획 선호를 미리 합의하면 편해요.")
}

# -----------------------
# 점수 규칙
# - 기본 50점
# - 같은 글자당 +12.5 (최대 +50 → 100)
# - 일부 인기 조합 보너스 +5~8
# -----------------------
def compatibility_score(a: str, b: str):
    base = 50.0
    same = sum(1 for x, y in zip(a, b) if x == y)
    score = base + same * 12.5
    score += BONUS.get((a,b), 0)

    # 캡핑
    score = max(0, min(100, round(score, 1)))
    return score

def dimension_notes(a: str, b: str):
    notes = []
    for i, (x, y) in enumerate(zip(a, b)):
        dim_pair = ["EI","SN","TF","JP"][i]
        if x == y:
            notes.append(f"{dim_pair}: {DIM_TEXT[x][0]}")
        else:
            # 상보 설명은 서로 다른 경우 x 기준 문구의 보완 설명 사용
            notes.append(f"{dim_pair}: {DIM_TEXT[x][1]}")
    return notes

def short_summary(score):
    if score >= 90: return "💖 환상의 케미! 서로가 서로의 최애 팀메이트."
    if score >= 80: return "💞 케미 좋음! 대체로 잘 맞고 성장 가능성 높아요."
    if score >= 70: return "✨ 무난-좋음. 몇 가지만 맞추면 훨씬 좋아져요."
    if score >= 60: return "🙂 보통. 관점 차이를 이해하면 편해져요."
    if score >= 50: return "🤝 노력형 케미. 소통 루틴을 만들면 안정됩니다."
    return "🌥️ 도전! 규칙/대화 방식 합의가 핵심 포인트."

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

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='score'>궁합 점수: <span class='badge'>{score}</span> / 100</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;margin:0 0 8px 0'>{a} ❤️ {b}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;margin:4px 0 0 0'>{summary}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("**강점/주의 포인트**", unsafe_allow_html=True)
    for n in notes:
        st.markdown(f"<span class='pill'>{n}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='hint'>※ 재미용 간단 테스트입니다. 실제 궁합은 개인차가 큽니다 🙂</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("Made with 💝 using Streamlit")


# 푸터
st.markdown("---")
st.caption("Made with 💝 for Fun using Streamlit")

