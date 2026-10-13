from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)
print("=" * 40)
print(" My AI Assistant")
print("=" * 40 )
messages = []

while True:
    user_input = input("\nYou: ")
    messages.append({"role": "user", "content": user_input})

    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")  
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    ai_reply = response.choices[0].message.content
    print("\nAssistant:", ai_reply)
    #save the AI's reply to the conversation history
    messages.append({"role": "assistant",
                      "content": ai_reply}
                      )
    print("\nConversation History:")
    for message in messages:
        role = message["role"]
        content = message["content"]
        print(f"{role.capitalize()}: {content}")
        print("\n----------Consevation History----------")
        for message in messages:
           print(message)
           print("---------------------------------------")
