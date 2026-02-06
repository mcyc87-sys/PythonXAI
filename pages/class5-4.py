import streamlit as st

st.chat_message("user").write("This is user message")
st.chat_message("assistant").write("This is assistant message")


# Sample chat record
history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
    {
        "role": "assistant",
        "content": "The World Series was played at Dodger Stadium in Los Angeles.",
    },
]


# Use loop to display chat history
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="✨").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
