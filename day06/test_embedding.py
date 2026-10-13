
from openai import OpenAI
from similarity import cosine_similarity

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)
def create_embedding(content):
    embedding1 = client.embeddings.create(
        model ="nomic-embed-text",
        input = content
    ).data[0].embedding 
    return embedding1

text1 = "python is a programming language."
text2 = "The weather is sunny today."

print("Text 1:", text1)
print("Text 2:", text2)

embedding1 = client.embeddings.create(
    model="nomic-embed-text",
    input=text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model="nomic-embed-text",
    input=text2
).data[0].embedding

print("First embedding preview:", embedding1[:5])
print("Second embedding preview:", embedding2[:5])
print("Embeddings identical:", embedding1 == embedding2)

score = cosine_similarity(embedding1, embedding2)

print("Cosine similarity:", score)