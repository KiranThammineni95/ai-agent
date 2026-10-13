from openai import OpenAI
from dotenv import load_dotenv
import os

from tools import (
    get_current_time, 
    roll_dice, 
    generate_password
)

from tool_manager import execute_tool

#load configuration
load_dotenv()

#create AI client
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)
print("=" * 40)
print(" My AI Assistant")
print("=" * 40 )
role = {
    "1":"you are a friendly school teacher . Explain concepts in simple language with real-life examples.",
    "2":"you are a senior python developer .explain concepts clearly and always include python examples.",
    "3":"you are a exprience travel guide. Recommend places,food , transportation and travel tips.",
    "4":"you are a motivational coach Encourage the userand givr practical advice with a positive attitude.",
    "5":"you are a professional interviewer . ask one interview question at atime and provide feedback on the user's answer."
}

print("\n Chooose Your  Assistant\n")

print("1. School Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice : ")

messages = [
    {
      "role": "system",
      "content": role.get(choice, "You are a helpful AI assistant.")
      }
]

while True:
    user_input = input("\nYou: ")
    tools_result= execute_tool(user_input)
    if tools_result:
        print("\nAssistant:", tools_result)
        continue
        

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    ai_reply = response.choices[0].message.content
    print("\nAssistant:", ai_reply)
    messages.append({ "role": "assistant", "content": ai_reply })
