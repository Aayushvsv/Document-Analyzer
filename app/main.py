# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import ClassifyRequest, AnswerRequest, ClassifyResponse, AnswerResponse
from .ml.classifier import classify_text
from .ml.rag import get_rag_answer

# --- Application Initialization ---
app = FastAPI(
    title="Document Intelligence System API",
    description="API for classifying documents and answering questions using RAG.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows your frontend to communicate with your backend.
# The '*' allows all origins, which is fine for development.
# For production, you would restrict this to your frontend's actual domain.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- API Endpoints ---

@app.get("/", tags=["General"])
def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the Document Intelligence System API!"}


@app.post("/classify", response_model=ClassifyResponse, tags=["Machine Learning"])
def classify_document(request: ClassifyRequest):
    """
    Classifies the input text into one of four categories.
    """
    prediction = classify_text(request.text)
    return prediction


@app.post("/answer", response_model=AnswerResponse, tags=["Machine Learning"])
def answer_question(request: AnswerRequest):
    """
    Answers a question based on a pre-built knowledge base using RAG.
    """
    answer = get_rag_answer(request.question)
    return answer
