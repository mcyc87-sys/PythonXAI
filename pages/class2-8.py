import streamlit as st

ss = st.session_state

st.title("Session State Range")

if "ans" not in ss:
    ss.ans = 0

if st.button("Click me +1"):
    ss.ans += 1
    st.rerun()

st.write("ans=", ss.ans)
