# 실행 명령어: streamlit run ham_a_app.py
# 필요한 라이브러리 설치: pip install streamlit

import streamlit as st

# HAM-A 항목 정의
ham_a_items = [
    {"id": 1, "question_ko": "불안한 기분", "question_en": "Anxious mood", "description_ko": "걱정, 최악의 상황을 예상함, 공포감, 짜증", "description_en": "Worries, anticipation of the worst, fearful anticipation, irritability."},
    {"id": 2, "question_ko": "긴장감", "question_en": "Tension", "description_ko": "긴장된 느낌, 피로감, 과민한 놀람 반응, 쉽게 눈물이 남, 떨림, 안절부절 못함, 이완 불가", "description_en": "Feelings of tension, fatigability, startle response, moved to tears easily, trembling, feelings of restlessness, inability to relax."},
    {"id": 3, "question_ko": "공포", "question_en": "Fears", "description_ko": "어둠, 낯선 사람, 혼자 있음, 동물, 교통, 군중 등에 대한 공포", "description_en": "Of dark, of strangers, of being left alone, of animals, of traffic, of crowds."},
    {"id": 4, "question_ko": "불면증", "question_en": "Insomnia", "description_ko": "잠들기 어려움, 자주 깨는 수면, 피로를 동반한 불충분한 수면, 악몽, 야경증", "description_en": "Difficulty in falling asleep, broken sleep, unsatisfying sleep and fatigue on waking, dreams, nightmares, night terrors."},
    {"id": 5, "question_ko": "지적 기능 저하", "question_en": "Intellectual", "description_ko": "집중력 저하, 기억력 저하", "description_en": "Difficulty in concentration, poor memory."},
    {"id": 6, "question_ko": "우울한 기분", "question_en": "Depressed mood", "description_ko": "흥미 상실, 취미 생활의 즐거움 부족, 우울감, 조기 각성, 하루 중 기분 변동", "description_en": "Loss of interest, lack of pleasure in hobbies, depression, early waking, diurnal swing."},
    {"id": 7, "question_ko": "신체적 증상 (근육)", "question_en": "Somatic (muscular)", "description_ko": "통증, 경련, 뻣뻣함, 근간대성 경련, 이갈이, 불안정한 목소리, 근긴장 증가", "description_en": "Pains and aches, twitching, stiffness, myoclonic jerks, grinding of teeth, unsteady voice, increased muscular tone."},
    {"id": 8, "question_ko": "신체적 증상 (감각)", "question_en": "Somatic (sensory)", "description_ko": "이명, 시야 흐림, 냉감 및 온감, 허약감, 찌릿한 감각", "description_en": "Tinnitus, blurring of vision, hot and cold flushes, feelings of weakness, pricking sensation."},
    {"id": 9, "question_ko": "심혈관계 증상", "question_en": "Cardiovascular symptoms", "description_ko": "심계항진, 가슴 통증, 혈관 박동, 실신 느낌, 심장박동 누락 느낌", "description_en": "Tachycardia, palpitations, pain in chest, throbbing of vessels, fainting feelings, missing beat."},
    {"id": 10, "question_ko": "호흡기계 증상", "question_en": "Respiratory symptoms", "description_ko": "흉부 압박, 질식감, 한숨, 호흡곤란", "description_en": "Pressure or constriction in chest, choking feelings, sighing, dyspnea."},
    {"id": 11, "question_ko": "위장관계 증상", "question_en": "Gastrointestinal symptoms", "description_ko": "삼킴 곤란, 가스, 복통, 작열감, 복부 팽만감, 메스꺼움, 구토, 장운동, 체중 감소, 변비", "description_en": "Difficulty in swallowing, wind abdominal pain, burning sensations, abdominal fullness, nausea, vomiting, borborygmi, looseness of bowels, loss of weight, constipation."},
    {"id": 12, "question_ko": "비뇨생식기계 증상", "question_en": "Genitourinary symptoms", "description_ko": "배뇨 빈도 증가, 절박뇨, 무월경, 월경과다, 성욕 감퇴, 조루, 발기부전", "description_en": "Frequency of micturition, urgency of micturition, amenorrhea, menorrhagia, development of frigidity, premature ejaculation, loss of libido, impotence."},
    {"id": 13, "question_ko": "자율신경계 증상", "question_en": "Autonomic symptoms", "description_ko": "구강건조, 안면홍조, 창백, 다한증, 어지럼증, 긴장성 두통, 털섬모기립", "description_en": "Dry mouth, flushing, pallor, tendency to sweat, giddiness, tension headache, raising of hair."},
    {"id": 14, "question_ko": "면담 시 행동", "question_en": "Behavior at interview", "description_ko": "안절부절못함, 떨림, 얼굴 긴장, 한숨, 빠른 호흡, 창백, 연하 행동 등", "description_en": "Fidgeting, restlessness or pacing, tremor of hands, furrowed brow, strained face, sighing or rapid respiration, facial pallor, swallowing, etc."}
]

ham_a_choices = [
    {"score": 0, "label_en": "Not present", "label_ko": "없음"},
    {"score": 1, "label_en": "Mild", "label_ko": "경미함"},
    {"score": 2, "label_en": "Moderate", "label_ko": "중간 정도"},
    {"score": 3, "label_en": "Severe", "label_ko": "심함"},
    {"score": 4, "label_en": "Very severe", "label_ko": "매우 심함"}
]

st.set_page_config(page_title="HAM-A 평가", layout="centered")

if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(ham_a_items)

st.title("Hamilton Anxiety Rating Scale (HAM-A)")

with st.form("ham_a_form"):
    for i, item in enumerate(ham_a_items):
        options = [f"{c['score']} - {c['label_ko']}" for c in ham_a_choices]
        default_score = st.session_state.answers[i] if st.session_state.answers[i] is not None else 0
        default_index = next((idx for idx, c in enumerate(ham_a_choices) if c["score"] == default_score), 0)
        selected = st.selectbox(f"{item['id']}. {item['question_ko']} - {item['description_ko']}", options, index=default_index, key=f"q{i}")
        st.session_state.answers[i] = int(selected.split(" - ")[0])
    submitted = st.form_submit_button("평가 완료")

if submitted:
    st.subheader("Evaluation Result")

    total_score = sum(st.session_state.answers)

    # 임상적 해석 기준
    # 0–17점: Mild anxiety
    # 18–24점: Mild to Moderate anxiety
    # 25–30점: Moderate to Severe anxiety
    # 31점 이상: Very severe anxiety

    interpretation = ""
    if total_score < 18:
        interpretation = "Mild anxiety"
    elif 18 <= total_score <= 24:
        interpretation = "Mild to Moderate anxiety"
    elif 25 <= total_score <= 30:
        interpretation = "Moderate to Severe anxiety"
    else:
        interpretation = "Very severe anxiety"

    result_lines = ["Hamilton Anxiety Rating Scale (HAM-A)\n"]
    for i, item in enumerate(ham_a_items):
        choice_score = st.session_state.answers[i]
        choice_label = [c["label_en"] for c in ham_a_choices if c["score"] == choice_score][0]
        line = f"{item['id']}. {item['question_en']} ({item['description_en']}): ({choice_score}) {choice_label}"
        result_lines.append(line)

    result_lines.append("")
    result_lines.append(f"Total Score: {total_score}")
    result_lines.append(f"Clinical Interpretation: {interpretation}")

    st.code("\n".join(result_lines))
