# streamlit run app.py
import streamlit as st
from datetime import datetime
import random

# ===================== 🌙 Dreamy Cute Night-Sky THEME (CSS) =====================
THEME = """
<style>
/* App background: dreamy night gradient */
.stApp {
  background: linear-gradient(180deg, #0b1020 0%, #1a2240 60%, #233a66 100%);
  color: #fffaf0;
  font-family: 'Comic Sans MS', 'Baloo 2', cursive, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}

/* Tiny stars overlay */
.stApp::before{
  content:"";
  position:fixed; inset:0;
  background-image:url("https://cdn.pixabay.com/photo/2017/08/30/01/05/stars-2695569_1280.png");
  background-size:cover;
  opacity:.22;
  pointer-events:none;
  z-index:-1;
}

/* Title */
h1, .stMarkdown h1 {
  text-align:center;
  font-size:2.8rem !important;
  color:#ffdd93 !important;   /* 밝은 파스텔 노랑 */
  text-shadow:0 3px 10px rgba(0,0,0,.6);
  margin-top:.5rem;
}

/* Subtext, labels */
label, .stMarkdown p, .stMarkdown span {
  color:#ffeedd !important;   /* 따뜻한 아이보리 */
  font-weight:600;
}

/* Input widgets */
.css-1vbkxwb, .stSelectbox, .stDateInput {
  filter: drop-shadow(0 6px 16px rgba(0,0,0,.25));
  border-radius:12px;
}

/* Button */
div.stButton > button {
  background: linear-gradient(135deg, #ffc6ff, #ffadad);
  color: #442244;
  font-weight: 700;
  border-radius: 20px;
  border: 2px solid #fffaf5;
  padding: .6rem 1.3rem;
  box-shadow: 0 5px 15px rgba(255,182,193,.4);
  transition: all .2s ease;
}
div.stButton > button:hover {
  filter: brightness(1.08);
  transform: translateY(-2px) scale(1.03);
}

/* Result cards (glassmorphism) */
[data-testid="stNotification"], [data-testid="stVerticalBlock"] > div:has(> .stAlert){
  border-radius: 20px !important;
  background: rgba(255, 248, 250, .15) !important;
  backdrop-filter: blur(12px);
  color: #fffaf0 !important;
  border: 1.5px dashed #ffd6f6;
}

/* Image */
img {
  border-radius: 20px !important;
  box-shadow: 0 8px 24px rgba(0,0,0,.4);
}
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# =============== Cute Sticker Sprinkles ===============
STICKERS = [
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f43b.png",  # bear
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f431.png",  # cat
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f430.png",  # rabbit
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f319.png",  # moon
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2b50.png",  # star
]
for _ in range(5):  
    url = random.choice(STICKERS)
    left = random.randint(3, 85)    
    top  = random.randint(72, 92)   
    size = random.randint(64, 96)   
    st.markdown(
        f"""<img src="{url}" style="
            position:fixed; left:{left}%; top:{top}%;
            width:{size}px; z-index:12; opacity:.95;">""",
        unsafe_allow_html=True
    )

# ===================== Zodiac ranges =====================
zodiac_dates = {
    "양자리": ((3, 21), (4, 19)),
    "황소자리": ((4, 20), (5, 20)),
    "쌍둥이자리": ((5, 21), (6, 20)),
    "게자리": ((6, 21), (7, 22)),
    "사자자리": ((7, 23), (8, 22)),
    "처녀자리": ((8, 23), (9, 22)),
    "천칭자리": ((9, 23), (10, 22)),
    "전갈자리": ((10, 23), (11, 21)),
    "사수자리": ((11, 22), (12, 21)),
    "염소자리": ((12, 22), (1, 19)),
    "물병자리": ((1, 20), (2, 18)),
    "물고기자리": ((2, 19), (3, 20)),
}
def get_zodiac(month: int, day: int) -> str | None:
    for zodiac, ((sm, sd), (em, ed)) in zodiac_dates.items():
        if (month == sm and day >= sd) or (month == em and day <= ed) \
           or (sm < month < em) \
           or (sm > em and (month > sm or month < em)):
            return zodiac
    return None

# Ensure Unsplash URLs render
def fix_url(url: str) -> str:
    joiner = "&" if "?" in url else "?"
    return f"{url}{joiner}auto=format&fit=crop&w=900&q=80"

# ===================== Style DB (예시: 일부만 표시) =====================
style_recommendations = {
    "A": {
        "양자리": ("활동적이면서 스포티한 스타일 추천!", fix_url("https://images.unsplash.com/photo-1519741497674-611481863552")),
        "황소자리": ("편안한 캐주얼로 안정감 있는 느낌!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        # ... 나머지도 동일하게 입력
    },
    # B, AB, O도 동일하게...
}

# ===================== UI =====================
st.title("🌙✨ 오늘의 외출 스타일 추천 ✨⭐")

blood_type = st.selectbox("혈액형을 선택하세요", ["A", "B", "AB", "O"])
min_date = datetime(2000, 1, 1)
max_date = datetime(2025, 12, 31)
birthday = st.date_input("생일을 선택하세요", value=datetime.today(), min_value=min_date, max_value=max_date)

month, day = birthday.month, birthday.day
zodiac = get_zodiac(month, day)

if st.button("⭐ 스타일 추천 받기 ⭐"):
    if zodiac and blood_type in style_recommendations and zodiac in style_recommendations[blood_type]:
        msg, img = style_recommendations[blood_type][zodiac]
        st.success(f"당신의 별자리는 **{zodiac}** 입니다! 🌟")
        st.info(f"오늘의 추천: {msg}")
        st.image(img, caption=f"{blood_type}형 {zodiac} 스타일", use_column_width=True)
    else:
        st.error("추천 데이터를 찾을 수 없습니다. 입력을 확인해주세요.")
