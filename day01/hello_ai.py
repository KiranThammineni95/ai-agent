from openai import OpenAI

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = client.chat.completions.create(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Andhra Pradesh?"
        }
    ]
)

print(response.choices[0].message.content)