import streamlit as st
import random

st.title("🎲 주사위 굴리기")

# 주사위 숫자 선택
col1, col2 = st.columns(2)

with col1:
    dice_num = st.selectbox("주사위 개수", [1, 2, 3, 4, 5, 6])

with col2:
    if st.button("🎲 굴리기!", use_container_width=True):
        results = [random.randint(1, 6) for _ in range(dice_num)]
        st.session_state.results = results

# 결과 표시
if "results" in st.session_state:
    st.divider()
    st.subheader("결과")
    
    # 각 주사위 결과 표시
    cols = st.columns(len(st.session_state.results))
    for i, (col, result) in enumerate(zip(cols, st.session_state.results)):
        with col:
            st.metric(f"주사위 {i+1}", result, delta=None)
    
    st.divider()
    st.write(f"**합계: {sum(st.session_state.results)}**")
    st.balloons()
