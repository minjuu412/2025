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

# 혈액형 + 별자리 스타일 추천 및 이미지
style_recommendations = {
    "A": {
        "양자리": ("활동적이면서 스포티한 스타일 추천!", "https://images.unsplash.com/photo-1519741497674-611481863552"),
        "황소자리": ("편안한 캐주얼로 안정감 있는 느낌!", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "쌍둥이자리": ("트렌디한 아이템으로 변화를 줘보세요.", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "게자리": ("따뜻한 색감의 포근한 스타일!", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
        "사자자리": ("화려한 액세서리로 포인트!", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "처녀자리": ("깔끔하고 미니멀한 스타일 추천.", "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb"),
        "천칭자리": ("밸런스 좋은 세련된 스타일!", "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"),
        "전갈자리": ("강렬한 컬러로 개성 표현!", "https://images.unsplash.com/photo-1514995669114-6081e934b693"),
        "사수자리": ("자유로운 분위기의 캐주얼 추천.", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "염소자리": ("클래식하고 단정한 스타일!", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "물병자리": ("독특하고 실험적인 패션 시도!", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "물고기자리": ("로맨틱하고 부드러운 스타일.", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
    },
    "B": {
        "양자리": ("스포티하면서 밝은 컬러 추천!", "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"),
        "황소자리": ("자연스러운 톤으로 편안하게.", "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb"),
        "쌍둥이자리": ("톡톡 튀는 포인트 아이템 필수!", "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"),
        "게자리": ("포근하고 따뜻한 느낌 추천.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "사자자리": ("눈에 띄는 화려한 스타일 OK!", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "처녀자리": ("깔끔하게 정돈된 스타일 추천.", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "천칭자리": ("조화로운 패션으로 균형 유지!", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
        "전갈자리": ("미스터리한 느낌의 컬러 추천.", "https://images.unsplash.com/photo-1514995669114-6081e934b693"),
        "사수자리": ("자유로운 무드의 캐주얼 스타일.", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "염소자리": ("단정하고 클래식한 아이템 추천.", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "물병자리": ("독특함을 살린 실험적 패션.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "물고기자리": ("부드럽고 몽환적인 스타일 추천.", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
    },
    "AB": {
        "양자리": ("유니크하면서도 활동적인 스타일!", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "황소자리": ("고급스러우면서 차분한 스타일.", "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb"),
        "쌍둥이자리": ("창의적인 패션 아이템 조합!", "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"),
        "게자리": ("부드럽고 포근한 감각적인 스타일.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "사자자리": ("대담하고 카리스마 있는 패션 추천!", "https://images.unsplash.com/photo-1514995669114-6081e934b693"),
        "처녀자리": ("깔끔하면서 디테일에 강한 스타일.", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "천칭자리": ("밸런스 있는 우아한 스타일!", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
        "전갈자리": ("강렬하고 매혹적인 패션 추천.", "https://images.unsplash.com/photo-1519741497674-611481863552"),
        "사수자리": ("자유분방한 스타일로 개성 발산!", "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"),
        "염소자리": ("단정하고 깔끔한 클래식 패션.", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "물병자리": ("독창적이고 실험적인 스타일 시도.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "물고기자리": ("로맨틱하면서 감성적인 분위기.", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
    },
    "O": {
        "양자리": ("파워풀하고 자신감 넘치는 스타일!", "https://images.unsplash.com/photo-1514995669114-6081e934b693"),
        "황소자리": ("안정감 있고 실용적인 스타일.", "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb"),
        "쌍둥이자리": ("활발하고 재밌는 패션 아이템!", "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53"),
        "게자리": ("따뜻하고 감성적인 분위기의 스타일.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "사자자리": ("화려하고 눈길 끄는 패션 추천!", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "처녀자리": ("깔끔하고 단정한 아이템 선택.", "https://images.unsplash.com/photo-1512436991641-6745cdb1723f"),
        "천칭자리": ("세련되면서 우아한 스타일!", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
        "전갈자리": ("비밀스러운 매력이 있는 스타일.", "https://images.unsplash.com/photo-1519741497674-611481863552"),
        "사수자리": ("모험심 넘치는 자유로운 패션.", "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c"),
        "염소자리": ("전통적이고 클래식한 스타일 추천.", "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89"),
        "물병자리": ("독창적이고 실험적인 아이템 활용.", "https://images.unsplash.com/photo-1542060748-10c28b62716c"),
        "물고기자리": ("감성적이고 로맨틱한 스타일.", "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f"),
    }
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
        st.image(image_url, caption=f"{blood_type} {zodiac} 스타일", use_column_width=True)
    else:
        st.error("추천 데이터를 찾을 수 없습니다. 다른 입력을 시도해보세요.")
