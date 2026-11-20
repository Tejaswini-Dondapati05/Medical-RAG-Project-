# Medical RAG Chatbot using Ollama

## Project Overview
Developed an AI-powered Medical RAG Chatbot that answers user questions based on medical documents using Retrieval-Augmented Generation (RAG). It retrieves relevant document chunks using FAISS and generates context-aware responses using Ollama.

## Project Location
Local Development Path: `C:\Users\donda\OneDrive\Desktop\Medical`

## Technologies Used
- Python
- Ollama
- FAISS Vector Database
- Embeddings
- Streamlit
- Retrieval-Augmented Generation (RAG)

## Project Structure
```text
Medical/
│
├── app/
│   ├── embedding.py
│   ├── vector_stored.py
│   └── rag_pipeline.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features
- Medical document-based question answering
- Text embedding generation
- FAISS similarity search
- Relevant document retrieval
- Local LLM integration using Ollama
- Context-aware answers

## Installation and Execution

### 1. Clone the Repository
```bash
git clone https://github.com/Tejaswini-Dondapati05/Medical-RAG-Project-.git
cd Medical-RAG-Project-
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment (Windows)
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file and add your required API keys locally. Never upload this file to GitHub.

### 6. Start Ollama
Make sure Ollama is installed and running. Download the model required by the project.

### 7. Run FastAPI Backend
Open the first terminal:
```bash
uvicorn api:app --reload
```

FastAPI server:
`http://127.0.0.1:8000`

API documentation:
`http://127.0.0.1:8000/docs`

### 8. Run Streamlit Frontend
Open a second terminal and activate the virtual environment:
```bash
venv\Scripts\activate
streamlit run main.py
```

Streamlit application:
`http://localhost:8501`

## Technologies Used
- Python
- FastAPI
- Streamlit
- Ollama
- FAISS
- Embeddings
- Retrieval-Augmented Generation (RAG)

## Security
`.env`, API keys, virtual environments and cache files are excluded from GitHub.

## Author
Tejaswini Dondapati
```
