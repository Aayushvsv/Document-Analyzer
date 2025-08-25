# test_db.py
# A simple script to test the connection to the local MongoDB server.

import pymongo
from datetime import datetime

MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"

print("--- Starting MongoDB Connection Test ---")

try:
    # 1. Try to connect to the server
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=5000)
    
    # 2. Ping the server to confirm the connection
    client.admin.command('ping')
    print("✅ Connection Successful: Ping to the server was successful.")
    
    # 3. Get the database and collection
    db = client.get_database("doc_intelligence_db")
    log_collection = db.get_collection("api_logs")
    print(f"✅ Successfully accessed database '{db.name}' and collection '{log_collection.name}'.")

    # 4. Try to write one test document
    test_log = {
        "timestamp": datetime.utcnow(),
        "endpoint": "/test",
        "message": "This is a successful test write from the script."
    }
    result = log_collection.insert_one(test_log)
    print(f"✅ Successfully wrote one document to the database.")
    print(f"   -> Inserted ID: {result.inserted_id}")

    print("\n--- TEST SUCCEEDED ---")
    print("You should now see the 'doc_intelligence_db' database in MongoDB Compass.")

except Exception as e:
    print("\n--- TEST FAILED ---")
    print(f"❌ An error occurred: {e}")
    print("\nPlease check that your MongoDB server is running and accessible.")

