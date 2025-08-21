import streamlit as st
from datetime import date

# 별자리 판별 함수
def get_zodiac(month, day):
    zodiac = [
        ("물병자리", (1, 20), (2, 18)),
        ("물고기자리", (2, 19), (3, 20)),
        ("양자리", (3, 21), (4, 19)),
        ("황소자리", (4, 20), (5, 20)),
        ("쌍둥이자리", (5, 21), (6, 21)),
        ("게자리", (6, 22), (7, 22)),
        ("사자자리", (7, 23), (8, 22)),
        ("처녀자리", (8, 23), (9, 22)),
        ("천칭자리", (9, 23), (10, 22)),
        ("전갈자리", (10, 23), (11, 22)),
        ("사수자리", (11, 23), (12, 21)),
        ("염소자리", (12, 22), (1, 19)),
    ]
    for sign, start, end in zodiac:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "알 수 없음"

# 운세 데이터 (별자리 + 성별 + 기분 반영)
fortune_data = {
    "양자리": {
        "남성": {
            "😊 좋음": {"love": "자신감으로 매력 상승!", "money": "투자운이 좋아요.", "health": "에너지 넘침!", "style": "강렬한 색상의 자켓"},
            "😐 보통": {"love": "주변을 잘 살펴보세요.", "money": "지출 관리 필요.", "health": "컨디션 보통.", "style": "심플 캐주얼"},
            "😢 우울": {"love": "친구와 대화가 도움돼요.", "money": "지출은 피하세요.", "health": "휴식 필요.", "style": "편안한 후드티"}
        },
        "여성": {
            "😊 좋음": {"love": "로맨틱한 하루가 될 거예요!", "money": "쇼핑에 행운이!", "health": "활력 가득!", "style": "레드 원피스"},
            "😐 보통": {"love": "상대방을 배려해 보세요.", "money": "소소한 수입이 있어요.", "health": "평범한 하루.", "style": "심플 블라우스"},
            "😢 우울": {"love": "혼자보다 친구와 함께 💕", "money": "지출 조심!", "health": "몸과 마음이 지침.", "style": "파스텔 톤 니트"}
        },
        "기타": {
            "😊 좋음": {"love": "새로운 인연이 찾아올지도?", "money": "뜻밖의 수입!", "health": "건강운 최고!", "style": "트렌디한 아이템"},
            "😐 보통": {"love": "느긋하게 기다려보세요.", "money": "현 상태 유지.", "health": "무난한 하루.", "style": "캐주얼 셔츠"},
            "😢 우울": {"love": "마음을 열면 좋은 일이!", "money": "지출 조심!", "health": "스트레스 주의.", "style": "루즈핏 스타일"}
        }
    },
    # 다른 별자리도 비슷하게 추가 가능 (물고기, 황소 등)
}

st.title("✨ 오늘의 맞춤 운세 & 스타일 추천 ✨")

# 사용자 입력
name = st.text_input("이름을 입력하세요")
gender = st.selectbox("성별을 선택하세요", ["남성", "여성", "기타"])
birthday = st.date_input("생일을 선택하세요", min_value=date(2000, 1, 1), max_value=date(2025, 12, 31))
mood = st.radio("오늘의 기분은 어떤가요?", ["😊 좋음", "😐 보통", "😢 우울"])

if st.button("오늘의 운세 보기"):
    zodiac = get_zodiac(birthday.month, birthday.day)
    
    if zodiac in fortune_data and gender in fortune_data[zodiac]:
        result = fortune_data[zodiac][gender][mood]
        st.subheader(f"🔮 {name}님의 오늘의 운세 ({zodiac})")
        st.write(f"❤️ 사랑운: {result['love']}")
        st.write(f"💰 금전운: {result['money']}")
        st.write(f"💪 건강운: {result['health']}")
        st.write(f"👗 스타일 추천: {result['style']}")
        st.success(f"오늘 하루도 멋지게 보내세요, {name}님!")
    else:
        st.warning("아직 해당 별자리의 운세 데이터가 준비되지 않았습니다 😅")
