import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai_api_key = load_openai_api()

st.title("🤖 AI Image Generator")

uploaded_file = st.file_uploader("Upload a picture", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded image", width=300)

    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    image_base64 = encode_image("temp_image.png")

promt = st.text_input("請輸入你的問題：")
if promt:
    response = openai.chat.completions.create(
        model="gpt-5.1-chat-latest",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": promt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                    },
                ],
            },
        ],
    )

    assistant_message = response.choices[0].message.content
    st.write(assistant_message)
