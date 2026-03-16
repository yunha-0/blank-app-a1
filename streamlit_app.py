import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Streamlit 요소 예시",
    page_icon="🎛️",
    layout="wide",
)

st.title("🎈 Streamlit 요소 예시 페이지")
st.markdown(
    "이 페이지는 Streamlit에서 자주 쓰이는 주요 요소들을 보여주는 데모입니다."
)

st.header("1. 텍스트 & 마크다운")
st.write("일반 텍스트를 출력할 때는 `st.write`를 사용합니다.")
st.markdown("""
### 마크다운 표기
- **굵은 글씨**
- *기울임*
- [Streamlit 문서](https://docs.streamlit.io/)
""")

st.header("2. 코드 블록")
code = '''
for i in range(3):
    print(f"Hello {i}")
'''
st.code(code, language="python")

st.header("3. 데이터 표시")

st.subheader("DataFrame")

@st.cache_data
def load_data(rows=20):
    df = pd.DataFrame(
        {
            "x": np.arange(rows),
            "y": np.random.randn(rows).cumsum(),
            "category": np.random.choice(["A", "B", "C"], size=rows),
        }
    )
    return df

sample_df = load_data()
st.dataframe(sample_df)

st.subheader("표(Table)")
st.table(sample_df.head())

st.header("4. 차트")
st.line_chart(sample_df.set_index("x")[["y"]])
st.bar_chart(sample_df["category"].value_counts())

st.header("5. 위젯 (입력 요소)")

# 버튼
if st.button("클릭해보기"):
    st.success("버튼을 눌렀습니다!")

# 체크박스
if st.checkbox("체크박스를 선택하세요"):
    st.info("체크박스가 선택되었습니다.")

# 라디오 버튼
choice = st.radio("라디오 선택", ["옵션 1", "옵션 2", "옵션 3"])
st.write("선택된 항목:", choice)

# 선택 상자
option = st.selectbox("Selectbox", ["빨강", "초록", "파랑"])
st.write("선택한 색:", option)

# 멀티 선택
items = st.multiselect("여러 항목 선택", ["토마토", "바나나", "사과"], default=["토마토"])
st.write("선택된 과일:", items)

# 슬라이더
value = st.slider("슬라이더", min_value=0, max_value=100, value=50)
st.write("현재 값:", value)

# 숫자 입력
number = st.number_input("숫자를 입력하세요", min_value=0, max_value=1000, value=123)
st.write("입력값:", number)

# 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("안녕하세요", name)

# 텍스트 영역
memo = st.text_area("메모")
if memo:
    st.write("입력된 메모:", memo)

# 날짜/시간 입력
d = st.date_input("날짜 선택", value=datetime.date.today())
t = st.time_input("시간 선택", value=datetime.datetime.now().time())
st.write("선택된 시간:", d, t)

# 파일 업로드
uploaded_file = st.file_uploader("파일 업로드", type=["csv", "txt"])
if uploaded_file is not None:
    st.write("업로드된 파일:", uploaded_file.name)
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

st.header("6. 레이아웃")
col1, col2, col3 = st.columns(3)
col1.metric("온도", "22°C", "+1.2°C")
col2.metric("습도", "59%", "-2%")
col3.metric("속도", "5 km/h", "↑ 0.5")

with st.expander("추가 정보 보기"):
    st.write("여기에 추가 설명이나 숨겨진 내용을 넣을 수 있습니다.")

st.sidebar.header("사이드바")
st.sidebar.write("사이드바에 위젯도 넣을 수 있습니다.")
sidebar_option = st.sidebar.radio("사이드바 선택", ["A", "B", "C"])
st.sidebar.write("사이드바에서 선택됨:", sidebar_option)
