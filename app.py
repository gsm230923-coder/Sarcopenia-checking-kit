pip install streamlit
import streamlit as st

st.title("근감소증 간이 진단 프로그램")

score = 0

# 성별
gender = st.radio("성별을 선택하세요", ["남", "여"])

# 악력
grip = st.number_input("악력 (kg)", min_value=0.0)

if gender == "남":
    if grip >= 28:
        score += 0
    elif grip >= 24:
        score += 1
    else:
        score += 2
else:
    if grip >= 18:
        score += 0
    elif grip >= 15:
        score += 1
    else:
        score += 2

# 보행 시간
time = st.number_input("6m 걷는 시간 (초)", min_value=0.1)
speed = 6 / time

if speed >= 1.0:
    score += 0
elif speed >= 0.8:
    score += 1
else:
    score += 2

# 의자 일어나기
chair = st.number_input("30초 의자 일어나기 횟수", min_value=0)

if gender == "남":
    if chair >= 14:
        score += 0
    elif chair >= 10:
        score += 1
    else:
        score += 2
else:
    if chair >= 12:
        score += 0
    elif chair >= 8:
        score += 1
    else:
        score += 2

# 계단
stairs = st.number_input("30초 계단 오르기 개수", min_value=0)

if stairs >= 20:
    score += 0
elif stairs >= 10:
    score += 1
else:
    score += 2

# 낙상
fall = st.number_input("1년 낙상 횟수", min_value=0)

if fall == 0:
    score += 0
elif fall <= 3:
    score += 1
else:
    score += 2


if st.button("결과 확인"):
    st.subheader(f"총 점수: {score}")

    if score >= 4:
        st.error("근감소증 의심군입니다.")
    else:
        st.success("정상 범위입니다.")
streamlit run app.py