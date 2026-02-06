import openai
from dotenv import load_dotenv
import os

load_dotenv()  # load .env file stuff

# setting API key
openai.api_key = os.getenv("OPENAI_API_KEY")

message = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    message.append({"role": "system", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-5.1-chat-latest",
        messages=message,
    )

    assistant_message = response.choices[0].message.content
    print(f"AI:{assistant_message}")
