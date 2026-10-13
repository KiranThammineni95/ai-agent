
from openai import OpenAI
from dotenv import load_dotenv
import os

from retriever import load_documents
from test_embedding import create_embedding
from similarity import cosine_similarity

# Load documents
documents = load_documents()

# Create embeddings for all documents
documents_embeddings = {}

for filename, content in documents.items():
    documents_embeddings[filename] = create_embedding(content)

# Load configuration
load_dotenv()

# Create AI client
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

    # Create embedding for the question
    question_embedding = create_embedding(user_input)

    # Find the most relevant document
    best_score = -1
    best_document = None

    for filename, embedding in documents_embeddings.items():
        score = cosine_similarity(question_embedding, embedding)

        if score > best_score:
            best_score = score
            best_document = filename

    # Check whether a document was found
    if best_document is None:
        print("Assistant: No documents found.")
        continue

    # Get the retrieved document content
    context = documents[best_document]

    # Build the prompt
    prompt = f"""
Answer the question using only the following information.
If the answer is not present, say you don't know based on the provided information.

Context:
{context}

Question:
{user_input}

Answer:
"""

    # Generate the answer using Ollama
    response = client.chat.completions.create(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nAssistant:", response.choices[0].message.content)