import streamlit as st

st.set_page_config(page_title="HAM-A 해밀턴 불안척도", layout="wide")

st.title("Hamilton Anxiety Rating Scale, HAM-A")
st.markdown("")

st.markdown("**각 항목에 대해 내담자의 상태에 가장 적절한 설명을 선택하세요.**")

# 문항 정의
questions = {
    1: "1. 불안한 기분",
    2: "2. 긴장감",
    3: "3. 공포",
    4: "4. 불면증",
    5: "5. 지적 기능 저하",
    6: "6. 우울한 기분",
    7: "7. 신체적 증상 (근육)",
    8: "8. 신체적 증상 (감각)",
    9: "9. 심혈관계 증상",
    10: "10. 호흡기계 증상",
    11: "11. 위장관계 증상",
    12: "12. 비뇨생식기계 증상",
    13: "13. 자율신경계 증상",
    14: "14. 면담 시 행동",
}

choices = [
    ("없음", 0),
    ("경도 (mild)", 1),
    ("중등도 (moderate)", 2),
    ("심함 (severe)", 3),
    ("매우 심함 (very severe)", 4),
]

responses = {}

with st.form("hama_form"):
    for i in range(1, 15):
        options = [f"{label} ({score})" for label, score in choices]
        selected = st.selectbox(f"{questions[i]}", options, key=f"q{i}")
        score = int(selected.split("(")[-1].strip(")"))
        responses[i] = score

    submitted = st.form_submit_button("점수 계산 및 결과 보기")

if submitted:
    total_score = sum(responses.values())

    if total_score <= 7:
        interpretation = "불안 거의 없음"
    elif total_score <= 14:
        interpretation = "경도 불안"
    elif total_score <= 23:
        interpretation = "중등도 불안"
    elif total_score <= 30:
        interpretation = "심한 불안"
    else:
        interpretation = "매우 심한 불안"

    # 출력 형식
    st.markdown("\n\n**Hamilton Anxiety Rating Scale, HAM-A**\n")

    for i in range(1, 15):
        selected_label = [label for label, score in choices if score == responses[i]][0]
        st.markdown(f"{questions[i]} → {selected_label} ({responses[i]})")

    st.markdown("\n")
    st.markdown(f"총점: {total_score}  \n임상적 해석: {interpretation}")

