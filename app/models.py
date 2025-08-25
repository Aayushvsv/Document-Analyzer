# app/models.py

from pydantic import BaseModel

# --- Request Models ---
# These models define the structure of the data we expect in a request.

class ClassifyRequest(BaseModel):
    """
    Defines the structure for a classification request.
    It expects a single field 'text' which is a string.
    """
    text: str

class AnswerRequest(BaseModel):
    """
    Defines the structure for a question-answering (RAG) request.
    It expects a single field 'question' which is a string.
    """
    question: str


# --- Response Models ---
# These models define the structure of the data our API will send back.

class ClassifyResponse(BaseModel):
    """
    Defines the structure for a classification response.
    It will return the predicted class name and the confidence score.
    """
    predicted_class: str
    confidence: float

class AnswerResponse(BaseModel):
    """
    Defines the structure for a question-answering (RAG) response.
    It will return the generated answer as a string.
    """
    answer: str
