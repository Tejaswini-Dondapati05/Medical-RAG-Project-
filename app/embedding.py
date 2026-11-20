
import numpy as np
from sentence_transformers import SentenceTransformer

# Load local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(chunks):

    embeddings = model.encode(
        chunks,
        batch_size=16,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return np.asarray(embeddings, dtype="float32")


def embed_question(question):

    embedding = model.encode(
        [question],
        convert_to_numpy=True
    )

    return np.asarray(embedding, dtype="float32")
