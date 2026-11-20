
def retrieve_chunks(indices, chunks):

    retrieved_chunks = []

    for i in indices:
        if 0 <= i < len(chunks):
            retrieved_chunks.append(chunks[i])

    return retrieved_chunks


def create_context(retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    return context
