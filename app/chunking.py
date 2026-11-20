
def chunk_document(document):

    chunk_size = 500
    chunk_overlap = 50

    chunks = []

    start = 0

    while start < len(document):

        end = min(start + chunk_size, len(document))

        chunk = document[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    print("Total chunks created:", len(chunks))

    return chunks
