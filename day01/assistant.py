from openai import OpenAI
from dotenv import load_dotenv
import os

#load configuration
load_dotenv()

#Create AI client 
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

print("=" * 60)
print(" My AI Assistant")
print("=" * 60)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")  
        break

    response = client.chat.completions.create(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAssistant:", response.choices[0].message.content)