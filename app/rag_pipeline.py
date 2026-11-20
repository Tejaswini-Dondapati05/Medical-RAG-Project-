
import requests

from app.embedding import embed_question
from app.vector_stored import search_faiss


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

NOT_FOUND = (
    "The information is not available "
    "in the provided documents."
)


def retrieve_chunks(indices, chunks):

    retrieved_chunks = []

    for i in indices:
        if 0 <= i < len(chunks):
            retrieved_chunks.append(chunks[i])

    return retrieved_chunks


def create_context(retrieved_chunks):

    return "\n\n".join(retrieved_chunks)


def generate_answer(question, context):

    if not context.strip():
        return NOT_FOUND

    prompt = f"""
You are a Medical Document Assistant.

STRICT INSTRUCTIONS:
- Answer ONLY using the provided context.
- Do not use outside knowledge.
- Do not invent medical information.
- If the context does not contain the answer,
  reply exactly:
  {NOT_FOUND}
- Keep the answer clear and simple.

PROVIDED CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            },
            timeout=120
        )

        response.raise_for_status()

        answer = response.json().get("response", "").strip()

        if not answer:
            return NOT_FOUND

        return answer

    except requests.exceptions.RequestException as e:
        print("OLLAMA ERROR:", str(e))
        return "Unable to generate answer. Check Ollama server."


def answer_question(question, index, chunks, k=5):

    if index is None or not chunks:
        return "RAG system is not initialized."

    question_embedding = embed_question(question)

    distances, indices = search_faiss(
        question_embedding,
        index,
        k
    )

    if indices is None or len(indices[0]) == 0:
        return NOT_FOUND

    retrieved_chunks = retrieve_chunks(
        indices[0],
        chunks
    )

    print("\n===== RETRIEVED CHUNKS =====")

    for i, chunk in enumerate(retrieved_chunks):
        print(f"\nChunk {i+1}:")
        print(chunk[:500])

    context = create_context(retrieved_chunks)

    print("\n===== CONTEXT =====")
    print(context)

    answer = generate_answer(
        question,
        context
    )

    return answer
