import streamlit as st
from datetime import datetime
import random

# ----------------- 스타일 (디자인용 CSS) -----------------
page_bg = """
<style>
.stApp {
    background: linear-gradient(to bottom, #0d1b2a, #1b263b, #415a77);
    color: #f1faee;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* 별 효과 */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url("https://cdn.pixabay.com/photo/2017/08/30/01/05/stars-2695569_1280.png");
    background-size: cover;
    opacity: 0.15;
    z-index: -1;
}

/* 제목 */
h1 {
    text-align: center;
    font-size: 3em !important;
    color: #ffe066 !important;
    text-shadow: 2px 2px 6px #00000088;
}

/* 버튼 꾸미기 */
button[kind="primary"] {
    background-color: #ffb4a2 !important;
    border-radius: 20px !important;
    color: white !important;
    font-weight: bold !important;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

/* 카드 효과 */
.stSuccess, .stInfo {
    border-radius: 20px;
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(8px);
    padding: 15px;
    font-size: 1.1em;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------- 랜덤 스티커 -----------------
stickers = [
    "https://cdn-icons-png.flaticon.com/512/616/616408.png",  # 곰돌이
    "https://cdn-icons-png.flaticon.com/512/1864/1864514.png", # 고양이
    "https://cdn-icons-png.flaticon.com/512/1829/1829586.png", # 별
    "https://cdn-icons-png.flaticon.com/512/1234/1234551.png", # 달
    "https://cdn-icons-png.flaticon.com/512/742/742751.png"   # 토끼
]

# 스티커를 여러 개 랜덤으로 뿌리기
for i in range(3):  # 최대 3개 스티커
    sticker_url = random.choice(stickers)
    left = random.randint(0, 80)   # 화면 좌측~우측 %
    top = random.randint(60, 90)   # 화면 아래쪽 %
    size = random.randint(60, 100) # 크기 px
    
    st.markdown(
        f"""
        <img src="{sticker_url}" 
             style="position:fixed; left:{left}%; top:{top}%; 
                    width:{size}px; z-index:10;">
        """,
        unsafe_allow_html=True
    )

# ----------------- 앱 본문 -----------------
st.title("✨ 오늘의 외출 스타일 추천 ✨")

blood_type = st.selectbox("혈액형을 선택하세요", ["A", "B", "AB", "O"])
min_date = datetime(2000, 1, 1)
max_date = datetime(2025, 12, 31)
birthday = st.date_input("생일을 선택하세요", value=datetime.today(), min_value=min_date, max_value=max_date)
import streamlit as st
from datetime import datetime

# 12별자리 날짜 구간
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

# 이미지 URL 뒤에 썸네일 파라미터 붙이기 함수
def fix_url(url):
    return f"{url}?auto=format&fit=crop&w=800&q=80"

# 혈액형 + 별자리 스타일 추천 및 이미지
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

# 별자리 계산 함수
def get_zodiac(month, day):
    for zodiac, ((start_month, start_day), (end_month, end_day)) in zodiac_dates.items():
        if (month == start_month and day >= start_day) or \
           (month == end_month and day <= end_day) or \
           (start_month < month < end_month) or \
           (start_month > end_month and (month > start_month or month < end_month)):
            return zodiac
    return None

# Streamlit UI
st.title("오늘의 외출 스타일 추천 💃🕺")
st.write("혈액형과 생일을 입력하면 오늘의 외출 스타일과 어울리는 이미지를 추천해드립니다!")

blood_type = st.selectbox("혈액형을 선택하세요", ["A", "B", "AB", "O"])

# 생일 입력 (2000 ~ 2025)
min_date = datetime(2000, 1, 1)
max_date = datetime(2025, 12, 31)
birthday = st.date_input("생일을 선택하세요", value=datetime.today(), min_value=min_date, max_value=max_date)

month = birthday.month
day = birthday.day
zodiac = get_zodiac(month, day)

if st.button("스타일 추천 받기"):
    if zodiac and blood_type in style_recommendations and zodiac in style_recommendations[blood_type]:
        style_message, image_url = style_recommendations[blood_type][zodiac]
        st.success(f"당신의 별자리는 **{zodiac}** 입니다! 🎯")
        st.info(f"오늘의 외출 스타일 추천: {style_message}")
        st.image(image_url, caption=f"{blood_type}형 {zodiac} 스타일", use_column_width=True)
    else:
        st.error("추천 데이터를 찾을 수 없습니다. 다른 입력을 시도해보세요.")

