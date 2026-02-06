import streamlit as st
import openai
import base64
from utils import load_openai_api

openai.api_key = load_openai_api()

st.title("🤖 AI Image Generator")

st.header("From words to images")

size = st.selectbox(
    "圖像尺寸",
    ["1024x1024", "1536x1024", "1024x1536", "auto"],
    help="方形圖片生成速度最快，預設為 1024x1024 像素",
)

quality = st.selectbox(
    "圖像品質",
    ["auto", "low", "medium", "high"],
    help="品質越高，生成時間越長，費用也越高",
)

output_format = st.selectbox(
    "Output format",
    ["png", "jpg", "jpeg"],
    help="Choose the format of the output image",
)
background = st.selectbox(
    "Background choices",
    ["auto", "transparent"],
    help="Transparent background only works with png or webP format",
)

if background == "transparent" and output_format == "jpeg":
    st.warning("Transparent background only works with png or webP format")

if output_format in ["webp", "jpeg"]:
    output_compression = st.slider(
        "Compression rate",
        min_value=0,
        max_value=100,
        value=75,
        help="The lower the value, the smaller the file size, but the slower the generation speed",
    )

promt_text = st.text_input("prompt：")

moderation = st.selectbox(
    "Moderation",
    ["auto", "low"],
    help="auto Auto is the standard filter, which is recommended for general use. low Filters out explicit content, including nudity, violence, and profanity.",
)

if st.button("Generate image"):
    with st.spinner("Generating image..."):

        try:
            params = {
                "model": "gpt-image-1.5",
                "prompt": promt_text,
                "n": 1,
                "size": size,
                "quality": quality,
            }

            if background != "auto":
                params["background"] = background

            generatedImage = openai.images.generate(**params)

            image_base64 = generatedImage.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            st.image(image_bytes)

            token_cost = {
                "1024x1024": {"low": 272, "medium": 1056, "high": 4160},
                "1024x1536": {"low": 408, "medium": 1584, "high": 6240},
                "1536x1024": {"low": 400, "medium": 1568, "high": 6208},
            }

            if quality != "auto" and size != "auto":
                try:
                    est_tokens = token_cost[size][quality]
                    st.info(f"預估使用約 {est_tokens} 個圖像 token，加上少量文字 token")
                except:
                    pass

            st.download_button(
                label="下載圖片",
                data=image_bytes,
                file_name=f"generated_image.{output_format}",
                mime=f"image/{output_format}",
            )

        except Exception as e:
            st.error(f"生成圖片時發生錯誤: {e}")
