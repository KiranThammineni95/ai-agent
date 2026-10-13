
from pathlib import Path

def load_documents():
    documents = {}
    folder = Path("knowledge")

    for file in folder.glob("*.txt"):
        documents[file.stem] = file.read_text(
            encoding="utf-8"
        )

    return documents


def retrieve(question):
    documents = load_documents()
    question = question.lower()

    for filename, content in documents.items():
        if question in filename.lower() or question in content.lower():
            return filename, content

    return None, None