from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.pdf_loader import load_pdf
from app.chunking import chunk_document
from app.embedding import create_embedding
from app.vector_stored import create_faiss_index
from app.rag_pipeline import answer_question


# Global variables
index = None
chunks = None

@asynccontextmanager
async def lifespan(app: FastAPI):

    global index, chunks

    print("Loading PDF documents...")

    try:
        document = load_pdf("data")
        chunks = chunk_document(document)

        print("Total chunks:", len(chunks))

        chunk_embeddings = create_embedding(chunks)

        index = create_faiss_index(chunk_embeddings)

        print("Vectors stored:", index.ntotal)
        print("RAG system initialized successfully!")

    except Exception as e:
        print("RAG INITIALIZATION FAILED:", str(e))
        index = None
        chunks = None

    yield

    print("Application shutting down...")


app = FastAPI(lifespan=lifespan)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Medical AI API is running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    if index is None or chunks is None:
        raise HTTPException(
            status_code=503,
            detail="RAG system is not initialized"
        )

    try:
        answer = answer_question(
            request.question,
            index,
            chunks,
            k=3
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )