
import faiss
import numpy as np


def create_faiss_index(embeddings):

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    print("Vectors stored:", index.ntotal)

    return index


def search_faiss(question_embeddings, index, k=5):

    question_embeddings = np.asarray(
        question_embeddings,
        dtype="float32"
    )

    k = min(k, index.ntotal)

    if k == 0:
        return None, np.empty((1, 0), dtype=int)

    distances, indices = index.search(
        question_embeddings,
        k
    )

    return distances, indices
