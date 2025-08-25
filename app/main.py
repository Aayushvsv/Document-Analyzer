# app/main.py

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .models import ClassifyRequest, AnswerRequest, ClassifyResponse, AnswerResponse
from .ml.classifier import classify_text
from .ml.rag import get_rag_answer
from .database import log_to_collection
import pymongo
from pymongo.collection import Collection

# --- Database Connection (Simpler, More Robust Approach) ---
# We establish the connection once when the application module is first loaded.
try:
    print("Connecting to MongoDB...")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.get_database("doc_intelligence_db")
    # Ping the server to confirm a successful connection
    client.admin.command('ping')
    print("✅ MongoDB connection successful.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    db = None

# --- Dependency for Database Collection ---
def get_log_collection() -> Collection | None:
    """
    A FastAPI dependency that provides the 'api_logs' collection to endpoints.
    """
    if db is not None:
        return db.get_collection("api_logs")
    return None

# --- Application Initialization ---
app = FastAPI(
    title="Document Intelligence System API",
    description="API for classifying documents and answering questions using RAG.",
    version="1.0.0",
)

# --- CORS Middleware ---
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
    return {"message": "Welcome to the Document Intelligence System API!"}


@app.post("/classify", response_model=ClassifyResponse, tags=["Machine Learning"])
def classify_document(
    request: ClassifyRequest,
    log_collection: Collection = Depends(get_log_collection)
):
    """
    Classifies text and logs the request/response to MongoDB.
    """
    prediction = classify_text(request.text)
    log_to_collection(
        collection=log_collection,
        endpoint="/classify",
        request_data={"text": request.text},
        prediction_data=prediction
    )
    return prediction


@app.post("/answer", response_model=AnswerResponse, tags=["Machine Learning"])
def answer_question(
    request: AnswerRequest,
    log_collection: Collection = Depends(get_log_collection)
):
    """
    Answers a question and logs the request/response to MongoDB.
    """
    answer = get_rag_answer(request.question)
    log_to_collection(
        collection=log_collection,
        endpoint="/answer",
        request_data={"question": request.question},
        prediction_data=answer
    )
    return answer
