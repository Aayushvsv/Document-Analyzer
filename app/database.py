# app/database.py

import pymongo
from datetime import datetime

# We will manage the client and db objects in the main app now.
# This file will just hold the logging function.

def log_to_collection(collection, endpoint: str, request_data: dict, prediction_data: dict):
    """
    Logs the incoming request and the model's prediction to the given MongoDB collection.
    """
    if collection is None:
        print("Warning: Log collection is not available. Skipping log.")
        return

    log_document = {
        "timestamp": datetime.utcnow(),
        "endpoint": endpoint,
        "request": request_data,
        "prediction": prediction_data
    }
    try:
        collection.insert_one(log_document)
        print(f"Logged prediction for endpoint: {endpoint}")
    except Exception as e:
        print(f"Error logging to MongoDB: {e}")

