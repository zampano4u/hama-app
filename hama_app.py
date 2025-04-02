import streamlit as st

st.set_page_config(page_title="HAM-A 불안 평가", layout="centered")

st.title("Hamilton Anxiety Rating Scale, HAM-A")
st.write("불안 수준을 평가하기 위한 해밀턴 불안 척도입니다. 각 문항에 가장 적절한 항목을 선택해주세요.")

questions = [
    {
        "id": 1,
        "title": "불안한 기분",
        "options": [
            "없다 (0)",
            "경도 – 걱정, 불안 (1)",
            "중등도 – 긴장감, 공포 (2)",
            "고도 – 일상생활 방해 (3)",
            "매우 고도 – 거의 기능 상실 (4)"
        ]
    },
    {
        "id": 2,
        "title": "긴장감",
        "options": [
            "없다 (0)",
            "경도 – 예민함, 안절부절 (1)",
            "중등도 – 가벼운 떨림 (2)",
            "고도 – 몸이 뻣뻣함, 땀, 얼굴 붉어짐 (3)",
            "매우 고도 – 심각한 떨림, 혼란 (4)"
        ]
    },
    {
        "id": 3,
        "title": "공포",
        "options": [
            "없다 (0)",
            "경도 – 가벼운 공포 (1)",
            "중등도 – 특정 대상 공포 (2)",
            "고도 – 사회적 공포 포함 (3)",
            "매우 고도 – 지속적 공포 및 회피 (4)"
        ]
    },
    {
        "id": 4,
        "title": "불면증",
        "options": [
            "없다 (0)",
            "경도 – 잠들기 어려움 (1)",
            "중등도 – 자주 깸 (2)",
            "고도 – 잠 거의 못 잠 (3)",
            "매우 고도 – 전혀 잠들지 못함 (4)"
        ]
    },
    {
        "id": 5,
        "title": "지적 기능 저하",
        "options": [
            "없다 (0)",
            "경도 – 집중력 저하 (1)",
            "중등도 – 기억력 감소 (2)",
            "고도 – 사고 흐름 방해 (3)",
            "매우 고도 – 사고 정지 수준 (4)"
        ]
    },
    {
        "id": 6,
        "title": "우울한 기분",
        "options": [
            "없다 (0)",
            "경도 – 슬픔, 낙담 (1)",
            "중등도 – 울고 싶음 (2)",
            "고도 – 자책, 무가치감 (3)",
            "매우 고도 – 자살 사고 동반 (4)"
        ]
    },
    {
        "id": 7,
        "title": "신체적 증상 (근육)",
        "options": [
            "없다 (0)",
            "경도 – 경미한 통증, 긴장감 (1)",
            "중등도 – 어깨 결림, 목 뻣뻣 (2)",
            "고도 – 경련, 움직임 제한 (3)",
            "매우 고도 – 일상 기능 저해 (4)"
        ]
    },
    {
        "id": 8,
        "title": "신체적 증상 (감각)",
        "options": [
            "없다 (0)",
            "경도 – 저림, 감각 둔화 (1)",
            "중등도 – 따끔거림, 귀울림 (2)",
            "고도 – 어지러움, 시야흐림 (3)",
            "매우 고도 – 방향감각 상실 (4)"
        ]
    },
    {
        "id": 9,
        "title": "심혈관계 증상",
        "options": [
            "없다 (0)",
            "경도 – 두근거림 (1)",
            "중등도 – 가슴 압박감, 통증 (2)",
            "고도 – 호흡 곤란, 빈맥 (3)",
            "매우 고도 – 실신, 긴급 대응 필요 (4)"
        ]
    },
    {
        "id": 10,
        "title": "호흡기계 증상",
        "options": [
            "없다 (0)",
            "경도 – 숨참 느낌 (1)",
            "중등도 – 과호흡 (2)",
            "고도 – 질식 공포 (3)",
            "매우 고도 – 호흡 거의 불가 (4)"
        ]
    },
    {
        "id": 11,
        "title": "위장관계 증상",
        "options": [
            "없다 (0)",
            "경도 – 입마름, 속 불편함 (1)",
            "중등도 – 복통, 설사, 오심 (2)",
            "고도 – 구토, 소화 불가 (3)",
            "매우 고도 – 섭취 불가능 (4)"
        ]
    },
    {
        "id": 12,
        "title": "비뇨생식기계 증상",
        "options": [
            "없다 (0)",
            "경도 – 빈뇨, 요의 증가 (1)",
            "중등도 – 성욕 감소 (2)",
            "고도 – 발기부전/월경 이상 (3)",
            "매우 고도 – 생식기 기능 소실 (4)"
        ]
    },
    {
        "id": 13,
        "title": "자율신경계 증상",
        "options": [
            "없다 (0)",
            "경도 – 땀, 창백함 (1)",
            "중등도 – 어지러움, 열감 (2)",
            "고도 – 혈압 변동 (3)",
            "매우 고도 – 쇼크 증상 (4)"
        ]
    },
    {
        "id": 14,
        "title": "면담 시 행동",
        "options": [
            "없다 (0)",
            "경도 – 손 움직임 증가 (1)",
            "중등도 – 안절부절, 불편해함 (2)",
            "고도 – 비언어적 초조 (3)",
            "매우 고도 – 통제 불가능한 불안행동 (4)"
        ]
    },
]

responses = []
for q in questions:
    selected = st.selectbox(f"{q['id']}. {q['title']}", q["options"], key=q["id"])
    score = int(selected.split("(")[-1].replace(")", ""))
    responses.append((q["id"], q["title"], selected, score))

# 점수 계산
total_score = sum(score for (_, _, _, score) in responses)

# 임상적 해석
if total_score <= 7:
    interpretation = "불안 거의 없음"
elif 8 <= total_score <= 14:
    interpretation = "경도 불안"
elif 15 <= total_score <= 23:
    interpretation = "중등도 불안"
elif 24 <= total_score <= 30:
    interpretation = "심한 불안"
else:
    interpretation = "매우 심한 불안"

# 출력
if st.button("결과 보기"):
    output = "**Hamilton Anxiety Rating Scale, HAM-A**\n\n"
    for qid, title, text, score in responses:
        output += f"{qid}. {title}: {text}\n"
    output += f"\n총점: {total_score}\n임상적 해석: {interpretation}"
    st.code(output)
