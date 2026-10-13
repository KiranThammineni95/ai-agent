from openai import OpenAI
from dotenv import load_dotenv
import os
#load configuration 
load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)
print("=" * 60)
print(" My AI Assistant")   
print("=" * 60)
 #store the conservation history
messages = []
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")  
        break
    #add the user input to the conversation history
    messages.append({"role": "user", "content": user_input})
    #send the conversation history to the Ollama model and get a response
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    #get the assistant's reply from the response
    assistant_reply = response.choices[0].message.content
    #add the assistant's reply to the conversation history
    messages.append({"role": "assistant", "content": assistant_reply})
    print("\nAssistant:", assistant_reply)