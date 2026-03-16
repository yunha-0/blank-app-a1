import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="자기소개",
    page_icon="🎛️",
    layout="wide",
)

st.title("🎈 '박윤하' 자기소개 페이지")
st.markdown(
    " "
)

st.markdown("""
### 1. 개인정보
- **성명 : 박윤하**
- **성별 : 여성**
- **생일 : 2004.11.29**
""")

st.markdown("""
### 2. 좋아하는 것
- **동물 : [시베리안 허스키](https://ko.wikipedia.org/wiki/%EC%8B%9C%EB%B2%A0%EB%A6%AC%EC%95%88_%ED%97%88%EC%8A%A4%ED%82%A4)**
- **음식 : [감자](https://terms.naver.com/entry.naver?docId=4368418&cid=42776&categoryId=59916), [옥수수](https://terms.naver.com/entry.naver?docId=568620&cid=46640&categoryId=46640)**
- **캐릭터 : [스파이더맨](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%8C%8C%EC%9D%B4%EB%8D%94%EB%A7%A8), [아히루노페클](https://namu.wiki/w/%EC%95%84%ED%9E%88%EB%A3%A8%EB%85%B8%ED%8E%98%ED%81%B4)**
""")

st.markdown("""
### 3. 싫어하는 것
- **거미**
- **다리 다섯개 이상인 것**
""")
