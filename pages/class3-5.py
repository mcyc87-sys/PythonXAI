import streamlit as st
import random
import time

ss = st.session_state

if "target" not in ss:
    ss.target = random.randint(0, 100)

if "min_val" not in ss:
    ss.min_val = 0

if "max_val" not in ss:
    ss.max_val = 100

st.title("Guess the Number Game")

num = st.number_input(
    f"請輸入一個{ss.min_val}到{ss.max_val}之間的整數:",
    min_value=ss.min_val,
    max_value=ss.max_val,
    step=1,
)

if st.button("guess"):
    if num < ss.target:
        st.success("太小了")
        ss.min_val = num + 1
    elif num > ss.target:
        st.success("太大了")
        ss.max_val = num - 1
    else:
        st.success("恭喜你猜對了")
        # Reset the game
        st.balloons
        ss.target = random.randint(0, 100)
        ss.min_val = 0
        ss.max_val = 100
    time.sleep(1)
    st.rerun()
