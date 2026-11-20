import requests

def generate_answer(question, context):

    prompt = f"""
You are a medical document assistant.

Answer only using the provided context.

If the answer is not available, say:
I don't know based on the provided documents.

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]