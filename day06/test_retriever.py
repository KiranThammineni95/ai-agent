from retriever import retrieve
from retriever import load_documents

documents = load_documents()
filename, content = retrieve("weather")
print(filename)
print()
print(content)


     