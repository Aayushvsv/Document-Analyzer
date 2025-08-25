# app/ml/classifier.py

from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch
import os
from pathlib import Path

# --- Configuration ---
# Get the absolute path to the current file's directory
current_dir = Path(__file__).parent
# The folder name is 'final_classification_model'
CLASSIFICATION_MODEL_PATH = str(current_dir / "assets" / "final_classification_model")

# Define the class names for the AG News dataset
CLASS_NAMES = ['World', 'Sports', 'Business', 'Sci/Tech']


# --- Model Loading ---
print("Loading classification model components from local assets...")

# Verify the model directory exists
if not os.path.exists(CLASSIFICATION_MODEL_PATH):
    raise FileNotFoundError(f"Model directory not found: {CLASSIFICATION_MODEL_PATH}")

# Load the tokenizer and model from the local directory
try:
    tokenizer = AutoTokenizer.from_pretrained(CLASSIFICATION_MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(CLASSIFICATION_MODEL_PATH)
    print("✅ Classification model components loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

print("Creating classification pipeline...")
device = 0 if torch.cuda.is_available() else -1
classifier_pipeline = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    device=device
)
print("✅ Classification pipeline created successfully!")

# --- Prediction Function ---
def classify_text(text: str) -> dict:
    """
    Classifies the input text using the fine-tuned model.
    """
    prediction = classifier_pipeline(text)[0]
    label_id = int(prediction['label'].split('_')[1])
    predicted_class = CLASS_NAMES[label_id]
    confidence = prediction['score']

    return {
        "predicted_class": predicted_class,
        "confidence": confidence
    }
