import streamlit as st
import openai
from utils import load_openai_api

ss = st.session_state

openai_api_key = load_openai_api()

if "history" not in ss:
    ss.history = []

if "system_message" not in ss:
    ss.system_message = "請用繁體中文進行後續對話"

if "model" not in ss:
    ss.model = "gpt-5.1-chat-latest"

col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    ss.system_message = col1.text_input("請輸入系統提示詞", ss.system_message)

with col2:
    ss.model = st.selectbox(
        "AI模型",
        [
            "gpt-5.1-chat-latest",
            "gpt-5.1",
            "gpt-5",
        ],
    )

with col3:
    if st.button("🗑️"):
        ss.history = []
        ss.rerun()

for message in ss.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="✨").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])

prompt = st.chat_input("請輸入你的問題：")
if prompt:
    ss.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model=ss.model,
        messages=[
            {"role": "system", "content": ss.system_message},
        ]
        + ss.history,
    )
    assistant_message = response.choices[0].message.content
    ss.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
