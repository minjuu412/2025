import streamlit as st
from datetime import datetime
import random

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

# 혈액형 + 별자리 스타일 추천
style_recommendations = {
    "A": {"양자리": "활동적이면서 스포티한 스타일 추천!", "황소자리": "편안한 캐주얼로 안정감 있는 느낌!", "쌍둥이자리": "트렌디한 아이템으로 변화를 줘보세요.", "게자리": "따뜻한 색감의 포근한 스타일!", "사자자리": "화려한 액세서리로 포인트!", "처녀자리": "깔끔하고 미니멀한 스타일 추천.", "천칭자리": "밸런스 좋은 세련된 스타일!", "전갈자리": "강렬한 컬러로 개성 표현!", "사수자리": "자유로운 분위기의 캐주얼 추천.", "염소자리": "클래식하고 단정한 스타일!", "물병자리": "독특하고 실험적인 패션 시도!", "물고기자리": "로맨틱하고 부드러운 스타일."},
    "B": {"양자리": "스포티하면서 밝은 컬러 추천!", "황소자리": "자연스러운 톤으로 편안하게.", "쌍둥이자리": "톡톡 튀는 포인트 아이템 필수!", "게자리": "포근하고 따뜻한 느낌 추천.", "사자자리": "눈에 띄는 화려한 스타일 OK!", "처녀자리": "깔끔하게 정돈된 스타일 추천.", "천칭자리": "조화로운 패션으로 균형 유지!", "전갈자리": "미스터리한 느낌의 컬러 추천.", "사수자리": "자유로운 무드의 캐주얼 스타일.", "염소자리": "단정하고 클래식한 아이템 추천.", "물병자리": "독특함을 살린 실험적 패션.", "물고기자리": "부드럽고 몽환적인 스타일 추천."},
    "AB": {"양자리": "활기찬 느낌과 개성 강조!", "황소자리": "편안하고 자연스러운 스타일 추천.", "쌍둥이자리": "다양한 스타일 믹스 시도 가능!", "게자리": "따뜻하고 포근한 무드 강조.", "사자자리": "강렬한 포인트 아이템 필수!", "처녀자리": "깔끔하게 정돈된 세련된 느낌.", "천칭자리": "밸런스를 맞춘 심플한 스타일.", "전갈자리": "독특한 포인트로 개성 표현.", "사수자리": "자유롭고 활동적인 스타일 추천.", "염소자리": "클래식하고 안정감 있는 느낌.", "물병자리": "실험적인 디자인 도전 추천.", "물고기자리": "부드럽고 로맨틱한 스타일 강조."},
    "O": {"양자리": "에너지 넘치는 스포티 캐주얼 추천!", "황소자리": "자연스러운 컬러와 편안함!", "쌍둥이자리": "포인트 아이템으로 변화를!", "게자리": "따뜻한 색감으로 포근함 연출.", "사자자리": "화려한 스타일로 시선 집중!", "처녀자리": "깔끔하고 단정한 느낌 유지.", "천칭자리": "세련된 밸런스 스타일 추천.", "전갈자리": "강렬한 컬러로 개성 표현!", "사수자리": "활동적인 캐주얼 스타일 추천.", "염소자리": "클래식하게 안정감 있게.", "물병자리": "독창적인 아이템으로 개성 표현.", "물고기자리": "몽환적이고 로맨틱한 스타일 추천."},
}

# 기본 패션 이미지 URL 모음 (Unsplash)
fashion_images = [
    "https://images.unsplash.com/photo-1520975918311-6c2c1c4c9b89",
    "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
    "https://images.unsplash.com/photo-1521335629791-ce4aec67dd53",
    "https://images.unsplash.com/photo-1542060748-10c28b62716c",
    "https://images.unsplash.com/photo-1539008835657-9e67d1fc8e2f",
    "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb",
    "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
]

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
st.write("혈액형과 생일을 입력하면 오늘의 외출 스타일과 패션 이미지를 추천해드립니다!")

blood_type = st.selectbox("혈액형을 선택하세요", ["A", "B", "AB", "O"])

# 생일 입력 (2000 ~ 2025)
min_date = datetime(2000, 1, 1)
max_date = datetime(2025, 12, 31)
birthday = st.date_input("생일을 선택하세요", value=datetime.today(), min_value=min_date, max_value=max_date)

month = birthday.month
day = birthday.day
zodiac = get_zodiac(month, day)

if st.button("스타일 추천 받기"):
    if zodiac:
        style_message = style_recommendations[blood_type][zodiac]
        st.success(f"당신의 별자리는 **{zodiac}** 입니다! 🎯")
        st.info(f"오늘의 외출 스타일 추천: {style_message}")

        # 랜덤 이미지 표시
        image_url = random.choice(fashion_images)
        st.image(image_url, caption=f"{blood_type} {zodiac} 스타일", use_column_width=True)
    else:
        st.error("별자리를 계산할 수 없습니다. 날짜를 확인해주세요.")
