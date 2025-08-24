# streamlit run app.py
import streamlit as st
from datetime import datetime
import random

# ===================== 🌙 Dreamy Night-Sky THEME (CSS) =====================
THEME = """
<style>
/* App background: dreamy night gradient */
.stApp {
  background: linear-gradient(180deg, #0b1020 0%, #14213d 50%, #233a66 100%);
  color: #f8f9fa;
  font-family: 'Comic Sans MS', 'Baloo 2', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}

/* Tiny stars overlay */
.stApp::before{
  content:"";
  position:fixed; inset:0;
  background-image:url("https://cdn.pixabay.com/photo/2017/08/30/01/05/stars-2695569_1280.png");
  background-size:cover;
  opacity:.18;
  pointer-events:none;
  z-index:-1;
}

/* Title */
h1, .stMarkdown h1 {
  text-align:center;
  font-size:2.8rem !important;
  color:#ffe066 !important;
  text-shadow:0 3px 14px rgba(0,0,0,.45);
  margin-top:.5rem;
}

/* Inputs card feel */
.block-container { padding-top: 1.2rem; }
.css-1vbkxwb, .stSelectbox, .stDateInput { filter: drop-shadow(0 6px 16px rgba(0,0,0,.15)); }

/* Labels */
label, .stMarkdown p { color:#f1f3f5 !important; }

/* Button (primary) */
div.stButton > button {
  background: linear-gradient(135deg, #ffb4a2, #ffa69e);
  color: #1b1b1b;
  font-weight: 700;
  border-radius: 18px;
  border: 0;
  padding: .6rem 1.1rem;
  box-shadow: 0 6px 18px rgba(255,166,158,.35);
}
div.stButton > button:hover { filter: brightness(1.05); transform: translateY(-1px); }

/* Result cards (glassmorphism) */
[data-testid="stNotification"], [data-testid="stVerticalBlock"] > div:has(> .stAlert){
  border-radius: 18px !important;
  background: rgba(255,255,255,.08) !important;
  backdrop-filter: blur(8px);
}

/* Image soft shadow + rounded */
img { border-radius: 18px !important; box-shadow: 0 8px 28px rgba(0,0,0,.35); }
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# =============== Cute Sticker Sprinkles (Twemoji PNG, no hotlink issues) ===============
STICKERS = [
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f43b.png",  # bear face
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f431.png",  # cat face
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2b50.png",  # star
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f319.png",  # crescent moon
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f430.png",  # rabbit face
]
for _ in range(4):  # show 4 random stickers near the bottom like stickers
    url = random.choice(STICKERS)
    left = random.randint(2, 85)    # %
    top  = random.randint(70, 92)   # %
    size = random.randint(60, 96)   # px
    st.markdown(
        f"""<img src="{url}" style="
            position:fixed; left:{left}%; top:{top}%;
            width:{size}px; z-index:12; opacity:.92;">""",
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

# Ensure Unsplash image URLs always render (thumb params)
def fix_url(url: str) -> str:
    joiner = "&" if "?" in url else "?"
    return f"{url}{joiner}auto=format&fit=crop&w=900&q=80"

# ===================== 48 combos: blood type × zodiac → (message, image) =====================
style_recommendations = {
    "A": {
        "양자리": ("활동적이면서 스포티한 스타일 추천!", fix_url("https://images.unsplash.com/photo-1519741497674-611481863552")),
        "황소자리": ("편안한 캐주얼로 안정감 있는 느낌!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "쌍둥이자리": ("트렌디한 아이템으로 변화를 줘보세요.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "게자리": ("따뜻한 색감의 포근한 스타일!", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
        "사자자리": ("화려한 액세서리로 포인트!", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "처녀자리": ("깔끔하고 미니멀한 스타일 추천.", fix_url("https://images.unsplash.com/photo-1555685812-4b943f1cb0eb")),
        "천칭자리": ("밸런스 좋은 세련된 스타일!", fix_url("https://images.unsplash.com/photo-1512436991641-6745cdb1723f")),
        "전갈자리": ("강렬한 컬러로 개성 표현!", fix_url("https://images.unsplash.com/photo-1514995669114-6081e934b693")),
        "사수자리": ("자유로운 분위기의 캐주얼 추천.", fix_url("https://images.unsplash.com/photo-1503342217505-b0a15ec3261c")),
        "염소자리": ("클래식하고 단정한 스타일!", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "물병자리": ("독특하고 실험적인 패션 시도!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "물고기자리": ("로맨틱하고 부드러운 스타일.", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
    },
    "B": {
        "양자리": ("스포티하면서 밝은 컬러 추천!", fix_url("https://images.unsplash.com/photo-1503342217505-b0a15ec3261c")),
        "황소자리": ("자연스러운 톤으로 편안하게.", fix_url("https://images.unsplash.com/photo-1555685812-4b943f1cb0eb")),
        "쌍둥이자리": ("톡톡 튀는 포인트 아이템 필수!", fix_url("https://images.unsplash.com/photo-1512436991641-6745cdb1723f")),
        "게자리": ("포근하고 따뜻한 느낌 추천.", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "사자자리": ("눈에 띄는 화려한 스타일 OK!", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "처녀자리": ("깔끔하게 정돈된 스타일 추천.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "천칭자리": ("조화로운 패션으로 균형 유지!", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
        "전갈자리": ("미스터리한 느낌의 컬러 추천.", fix_url("https://images.unsplash.com/photo-1514995669114-6081e934b693")),
        "사수자리": ("자유로운 무드의 캐주얼 스타일.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "염소자리": ("단정하고 클래식한 아이템 추천.", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "물병자리": ("독특함을 살린 실험적 패션.", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "물고기자리": ("부드럽고 몽환적인 스타일 추천.", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
    },
    "AB": {
        "양자리": ("개성과 자유분방함이 돋보이는 스타일!", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "황소자리": ("안정적인 톤의 클래식 패션.", fix_url("https://images.unsplash.com/photo-1555685812-4b943f1cb0eb")),
        "쌍둥이자리": ("다양한 패턴을 믹스 매치해보세요.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "게자리": ("따뜻하고 감성적인 스타일 추천.", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "사자자리": ("자신감 있는 강렬한 룩!", fix_url("https://images.unsplash.com/photo-1503342217505-b0a15ec3261c")),
        "처녀자리": ("깔끔하고 정돈된 느낌의 패션.", fix_url("https://images.unsplash.com/photo-1512436991641-6745cdb1723f")),
        "천칭자리": ("세련된 컬러 매치 추천!", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
        "전갈자리": ("시크하면서도 강렬한 스타일!", fix_url("https://images.unsplash.com/photo-1514995669114-6081e934b693")),
        "사수자리": ("자유로운 감성의 보헤미안 룩.", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "염소자리": ("단정하고 품격 있는 패션.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "물병자리": ("실험적이고 창의적인 패션 추천!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "물고기자리": ("몽환적이고 부드러운 분위기의 스타일.", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
    },
    "O": {
        "양자리": ("활발하고 캐주얼한 스타일!", fix_url("https://images.unsplash.com/photo-1519741497674-611481863552")),
        "황소자리": ("편안하면서도 안정적인 룩.", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "쌍둥이자리": ("다채로운 액세서리로 포인트!", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "게자리": ("따뜻한 무드의 감성적인 패션.", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
        "사자자리": ("강렬하고 화려한 스타일!", fix_url("https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89")),
        "처녀자리": ("깔끔한 모던 스타일 추천.", fix_url("https://images.unsplash.com/photo-1555685812-4b943f1cb0eb")),
        "천칭자리": ("밸런스 있는 세련된 느낌!", fix_url("https://images.unsplash.com/photo-1512436991641-6745cdb1723f")),
        "전갈자리": ("카리스마 있는 다크 스타일!", fix_url("https://images.unsplash.com/photo-1514995669114-6081e934b693")),
        "사수자리": ("자유로운 캐주얼 스타일.", fix_url("https://images.unsplash.com/photo-1503342217505-b0a15ec3261c")),
        "염소자리": ("전통적이고 고급스러운 스타일.", fix_url("https://images.unsplash.com/photo-1521335629791-ce4aec67dd53")),
        "물병자리": ("독창적이고 개성 강한 스타일.", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "물고기자리": ("로맨틱하고 부드러운 스타일 추천.", fix_url("https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f")),
    },
}

# ===================== UI =====================
st.title("✨ 오늘의 외출 스타일 추천 ✨")

blood_type = st.selectbox("혈액형을 선택하세요", ["A", "B", "AB", "O"])

min_date = datetime(2000, 1, 1)
max_date = datetime(2025, 12, 31)
birthday = st.date_input("생일을 선택하세요", value=datetime.today(), min_value=min_date, max_value=max_date)

month = birthday.month
day = birthday.day
zodiac = get_zodiac(month, day)

if st.button("스타일 추천 받기"):
    if zodiac and blood_type in style_recommendations and zodiac in style_recommendations[blood_type]:
        msg, img = style_recommendations[blood_type][zodiac]
        st.success(f"당신의 별자리는 **{zodiac}** 입니다! 🎯")
        st.info(f"오늘의 외출 스타일 추천: {msg}")
        st.image(img, caption=f"{blood_type}형 {zodiac} 스타일", use_column_width=True)
    else:
        st.error("추천 데이터를 찾을 수 없습니다. 입력을 확인해주세요.")
