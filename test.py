import streamlit as st
from datetime import datetime
import random

# ===================== 디자인 (CSS) =====================
THEME = """
<style>
.stApp {
  background: linear-gradient(180deg, #0b1020 0%, #1a2240 60%, #233a66 100%);
  color: #fffaf0;
  font-family: 'Comic Sans MS', 'Baloo 2', cursive;
}
.stApp::before{
  content:""; position:fixed; inset:0;
  background-image:url("https://cdn.pixabay.com/photo/2017/08/30/01/05/stars-2695569_1280.png");
  background-size:cover; opacity:.22; z-index:-1;
}
h1 { text-align:center; font-size:2.6rem !important; color:#ffdd93 !important;
     text-shadow:0 3px 10px rgba(0,0,0,.6);}
label, .stMarkdown p, .stMarkdown span { color:#ffeedd !important; font-weight:600; }
div.stButton > button {
  background: linear-gradient(135deg, #ffc6ff, #ffadad);
  color:#442244; font-weight:700; border-radius:20px; border:2px solid #fffaf5;
  padding:.6rem 1.3rem; box-shadow:0 5px 15px rgba(255,182,193,.4);
}
div.stButton > button:hover { filter: brightness(1.08); transform:translateY(-2px) scale(1.03);}
[data-testid="stNotification"], [data-testid="stVerticalBlock"] > div:has(> .stAlert){
  border-radius:20px; background:rgba(255,248,250,.15) !important;
  backdrop-filter: blur(12px); color:#fffaf0 !important; border:1.5px dashed #ffd6f6;
}
img { border-radius:20px !important; box-shadow:0 8px 24px rgba(0,0,0,.4);}
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# ===================== 스티커 랜덤 =====================
STICKERS = [
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f43b.png",  
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f431.png",  
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f430.png",  
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f319.png",  
    "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2b50.png",  
]
for _ in range(5):
    url = random.choice(STICKERS)
    left = random.randint(3, 85); top  = random.randint(72, 92); size = random.randint(64, 96)
    st.markdown(f"""<img src="{url}" style="position:fixed; left:{left}%; top:{top}%;
                width:{size}px; z-index:12; opacity:.95;">""", unsafe_allow_html=True)

# ===================== 별자리 =====================
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
def get_zodiac(month, day):
    for zodiac, ((sm, sd), (em, ed)) in zodiac_dates.items():
        if (month == sm and day >= sd) or (month == em and day <= ed) \
           or (sm < month < em) or (sm > em and (month > sm or month < em)):
            return zodiac
    return None

def fix_url(url):  # Unsplash 이미지 깨짐 방지
    joiner = "&" if "?" in url else "?"
    return f"{url}{joiner}auto=format&fit=crop&w=900&q=80"

# ===================== 48개 추천 데이터 =====================
# 각 혈액형-별자리마다 텍스트와 이미지 지정
style_recommendations = {
    "A": {
        "양자리": ("활동적이면서 스포티한 스타일 추천!", fix_url("https://images.unsplash.com/photo-1519741497674-611481863552")),
        "황소자리": ("편안한 캐주얼로 안정감 있는 느낌!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "쌍둥이자리": ("다채로운 컬러와 패턴으로 개성 표현!", fix_url("https://images.unsplash.com/photo-1593642634311-e4b3a7e3d3b0")),
        "게자리": ("부드러운 색감과 여성스러운 실루엣 추천!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "사자자리": ("강렬한 레드와 골드로 자신감 있는 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "처녀자리": ("심플하고 깔끔한 라인으로 세련된 느낌!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "천칭자리": ("밸런스 잡힌 디자인으로 우아한 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "전갈자리": ("강렬한 블랙과 레드로 신비로운 매력!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "사수자리": ("자유로운 분위기의 캐주얼한 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "염소자리": ("클래식한 디자인으로 고급스러운 느낌!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "물병자리": ("독특한 디자인으로 개성 있는 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "물고기자리": ("몽환적인 색감과 레이스로 로맨틱한 느낌!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
    },
    "B": {
        "양자리": ("활동적이면서 스포티한 스타일 추천!", fix_url("https://images.unsplash.com/photo-1519741497674-611481863552")),
        "황소자리": ("편안한 캐주얼로 안정감 있는 느낌!", fix_url("https://images.unsplash.com/photo-1542060748-10c28b62716c")),
        "쌍둥이자리": ("다채로운 컬러와 패턴으로 개성 표현!", fix_url("https://images.unsplash.com/photo-1593642634311-e4b3a7e3d3b0")),
        "게자리": ("부드러운 색감과 여성스러운 실루엣 추천!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "사자자리": ("강렬한 레드와 골드로 자신감 있는 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "처녀자리": ("심플하고 깔끔한 라인으로 세련된 느낌!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "천칭자리": ("밸런스 잡힌 디자인으로 우아한 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "전갈자리": ("강렬한 블랙과 레드로 신비로운 매력!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "사수자리": ("자유로운 분위기의 캐주얼한 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "염소자리": ("클래식한 디자인으로 고급스러운 느낌!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        "물병자리": ("독특한 디자인으로 개성 있는 스타일!", fix_url("https://images.unsplash.com/photo-1604014230282-3e8e4e5b5b9d")),
        },
::contentReference[oaicite:0]{index=0}}
 

