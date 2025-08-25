Document Intelligence System 🧠
An AI-powered web application featuring a fine-tuned document classifier and a Retrieval-Augmented Generation (RAG) system for question answering, all served via a FastAPI backend and an interactive frontend.

<img width="1785" height="890" alt="image" src="https://github.com/user-attachments/assets/e1ba9aeb-cda1-4c70-af74-fb6b5163f83f" />

(Optional: Add a screenshot of your index.html in action here!)

🚀 Project Overview
This project is a comprehensive Document Intelligence System built to perform two core Natural Language Processing tasks:

Document Classification: A machine learning model fine-tuned on the AG News dataset to accurately classify text into categories like World, Sports, Business, and Sci/Tech.

Question Answering (RAG): A Retrieval-Augmented Generation pipeline that answers user questions by first retrieving relevant information from a knowledge base of news articles and then generating a coherent answer.

The entire system is exposed through a robust API built with FastAPI and includes a simple, clean frontend for easy interaction.

🛠️ Core Technologies
Backend: FastAPI, Uvicorn

Machine Learning: PyTorch, Hugging Face Transformers, Sentence-Transformers

Vector Database: FAISS (Facebook AI Similarity Search)

Frontend: HTML, Tailwind CSS, JavaScript

Core Models:

distilbert-base-uncased (fine-tuned for classification)

all-MiniLM-L6-v2 (for text embeddings)

gpt2 (for text generation)

✨ Features
RESTful API: A fully functional API to access the ML models.

High-Accuracy Classifier: Leverages a fine-tuned transformer model for reliable document categorization.

Context-Aware Q&A: Uses a RAG pipeline to provide answers grounded in a specific knowledge base, reducing hallucinations.

Interactive UI: A simple, user-friendly frontend to test and demonstrate the system's capabilities.

Well-Structured Code: The project is organized with a clear separation between the API logic and the machine learning components.

📂 Project Structure
document_intelligence/
├── app/
│   ├── ml/
│   │   ├── assets/
│   │   │   ├── final_classification_model/
│   │   │   ├── faiss_index.bin
│   │   │   └── knowledge_base.json
│   │   ├── classifier.py
│   │   └── rag.py
│   ├── main.py
│   └── models.py
├── venv/
├── index.html
├── requirements.txt
└── README.md

⚙️ Setup and Installation
Follow these steps to get the project running on your local machine.

1. Prerequisites
Python 3.8+

Git

2. Clone the Repository
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd document-intelligence

3. Create and Activate a Virtual Environment
On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

4. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

▶️ Running the Application
1. Start the FastAPI Backend
With your virtual environment activated, run the Uvicorn server from the project's root directory.

uvicorn app.main:app --reload

The server will start, and the ML models will be loaded into memory. You should see a confirmation that the server is running on http://127.0.0.1:8000.

2. Access the Frontend and API Docs
Interactive Frontend: Open the index.html file directly in your web browser to use the application.

API Documentation: Navigate to http://127.0.0.1:8000/docs in your browser to access the interactive FastAPI documentation, where you can test the API endpoints directly.

💡 How It Works
Document Classification
The classifier is a distilbert-base-uncased model that was fine-tuned on the AG News dataset. When the API receives a piece of text, it's passed to a Hugging Face pipeline which tokenizes the text and feeds it to the model to get a prediction and a confidence score.

Question Answering (RAG)
The RAG system follows a three-step process:

Retrieve: The user's question is converted into a vector embedding. This embedding is used to perform a similarity search in the FAISS vector index to find the most relevant documents from the knowledge base.

Augment: The retrieved documents are combined with the original question to form a detailed prompt.

Generate: This augmented prompt is fed to a gpt2 model, which generates a final answer based on the provided context.
