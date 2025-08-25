# Document Intelligence System 🧠

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

An AI-powered web application featuring a fine-tuned document classifier and a Retrieval-Augmented Generation (RAG) system for intelligent question answering, all served via a high-performance FastAPI backend with an interactive frontend.

<img width="1906" height="909" alt="image" src="https://github.com/user-attachments/assets/a486d144-c500-4b5b-b757-21b55df58287" />

## 🚀 Project Overview

This project is a comprehensive **Document Intelligence System** built to perform two core Natural Language Processing tasks with state-of-the-art accuracy:

### 🎯 Document Classification
A machine learning model fine-tuned on the **AG News dataset** to accurately classify text into four distinct categories:
- **World** 🌍 - Global news and international affairs
- **Sports** ⚽ - Athletic events, games, and sports news
- **Business** 💼 - Economic, financial, and corporate news
- **Science/Technology** 🔬 - Scientific discoveries and tech innovations

### 🤖 Question Answering (RAG)
A sophisticated **Retrieval-Augmented Generation** pipeline that delivers contextually accurate answers by:
1. **Retrieving** relevant information from a comprehensive knowledge base of news articles
2. **Augmenting** user queries with retrieved context
3. **Generating** coherent, fact-based responses

The entire system is exposed through a robust, production-ready API built with FastAPI and includes an elegant, responsive frontend for seamless user interaction.

## 🛠️ Core Technologies

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI, Uvicorn | High-performance API server |
| **ML Framework** | PyTorch, Hugging Face Transformers | Model training and inference |
| **Embeddings** | Sentence-Transformers | Text vectorization |
| **Vector Database** | FAISS (Facebook AI Similarity Search) | Efficient similarity search |
| **Frontend** | HTML, Tailwind CSS, JavaScript | Interactive user interface |

### 🤖 Core Models

- **Classification**: `distilbert-base-uncased` (fine-tuned on AG News)
- **Embeddings**: `all-MiniLM-L6-v2` (for text embeddings)
- **Generation**: `gpt2` (for text generation)

## ✨ Features

- 🚀 **RESTful API**: A fully functional API to access the ML models
- 🎯 **High-Accuracy Classifier**: Leverages a fine-tuned transformer model for reliable document categorization
- 🧠 **Context-Aware Q&A**: Uses a RAG pipeline to provide answers grounded in a specific knowledge base, reducing hallucinations
- 💻 **Interactive UI**: A simple, user-friendly frontend to test and demonstrate the system's capabilities
- 🔧 **Well-Structured Code**: The project is organized with a clear separation between the API logic and the machine learning components
- 📊 **Performance Optimized**: Fast inference with efficient model loading
- 📖 **Comprehensive Documentation**: Auto-generated API docs with FastAPI

## 📂 Project Structure

```
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
```

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

Ensure you have the following installed:
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))

### 2. Clone the Repository

```bash
git clone https://github.com/Aayushvsv/Document-Analyzer.git
cd document-intelligence
```

### 3. Create and Activate a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies

Install all the required Python libraries using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

### 1. Start the FastAPI Backend

With your virtual environment activated, run the Uvicorn server from the project's root directory:

```bash
uvicorn app.main:app --reload
```

The server will start, and the ML models will be loaded into memory. You should see a confirmation that the server is running on http://127.0.0.1:8000.

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 2. Access the Frontend and API Docs

| Interface | Access Method | Description |
|-----------|---------------|-------------|
| **Interactive Frontend** | Open `index.html` directly in your web browser | Use the application's UI to test classification and Q&A |
| **API Documentation** | Navigate to http://127.0.0.1:8000/docs | Access the interactive FastAPI documentation where you can test API endpoints |
| **Alternative API Docs** | Navigate to http://127.0.0.1:8000/redoc | ReDoc-style API documentation |

## 💡 How It Works

### 🎯 Document Classification

The classifier is a `distilbert-base-uncased` model that was fine-tuned on the AG News dataset. The classification process works as follows:

1. **Input Processing**: When the API receives a piece of text, it's tokenized using the DistilBERT tokenizer
2. **Model Inference**: The tokenized text is passed to a Hugging Face pipeline
3. **Prediction**: The model outputs a prediction with confidence scores for each category
4. **Response**: Returns the predicted category and confidence score

```python
# Example classification flow
text = "Apple announces new iPhone with AI features"
result = classifier_pipeline(text)
# Output: {"label": "Sci/Tech", "score": 0.94}
```

### 🤖 Question Answering (RAG)

The RAG system follows a sophisticated three-step process:

#### 1. **Retrieve** 🔍
- The user's question is converted into a vector embedding using the `all-MiniLM-L6-v2` model
- This embedding is used to perform a similarity search in the FAISS vector index
- The system finds the most relevant documents from the knowledge base

#### 2. **Augment** 📝
- The retrieved documents are combined with the original question
- This creates a detailed, context-rich prompt that provides relevant background information

#### 3. **Generate** ✨
- The augmented prompt is fed to the `gpt2` model
- The model generates a final answer based on the provided context
- This approach significantly reduces hallucinations and improves factual accuracy

```python
# Example RAG flow
question = "What are the latest developments in AI?"
# 1. Retrieve relevant documents
embeddings = embedding_model.encode(question)
relevant_docs = faiss_index.search(embeddings, k=5)

# 2. Augment with context
context = "\n".join(relevant_docs)
prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"

# 3. Generate response
answer = generation_model(prompt)
```

## 🔌 API Reference

### Endpoints

The API provides the following endpoints:

#### Document Classification
```http
POST /classify
Content-Type: application/json

{
  "text": "Your text to classify here..."
}
```

**Response:**
```json
{
  "category": "Business",
  "confidence": 0.94,
  "text": "Your input text...",
  "processing_time": 0.12
}
```

#### Question Answering
```http
POST /ask
Content-Type: application/json

{
  "question": "Your question here..."
}
```

**Response:**
```json
{
  "answer": "Generated answer based on retrieved context...",
  "sources": ["Relevant document 1", "Relevant document 2"],
  "processing_time": 1.23
}
```

## 🧪 Testing the System

### Via Web Interface
1. Open the `index.html` file in your browser
2. **Test Classification**: 
   - Enter news text like "Tesla reports record quarterly earnings"
   - Observe the predicted category (likely "Business")
3. **Test Q&A**: 
   - Ask questions like "What are recent tech innovations?"
   - Review the generated answers based on the knowledge base

### Via API (using curl)
```bash
# Test classification
curl -X POST "http://127.0.0.1:8000/classify" \
     -H "Content-Type: application/json" \
     -d '{"text": "The Lakers won the championship game last night"}'

# Test question answering
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are recent sports news?"}'
```

## 📊 Performance & Specifications

| Metric | Value | Notes |
|--------|-------|-------|
| **Classification Accuracy** | ~95% | On AG News test set |
| **Response Time** | <200ms | Classification endpoint |
| **RAG Response Time** | 1-2s | Including retrieval + generation |
| **Memory Usage** | ~2-3GB | All models loaded |
| **Supported Text Length** | Up to 512 tokens | DistilBERT limit |

## 🚀 Deployment Options

### Local Development
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Production Deployment
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Commit your changes**: `git commit -m 'Add some amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Areas for Contribution
- 🐛 Bug fixes and improvements
- ✨ New features and enhancements
- 📖 Documentation improvements
- 🧪 Adding test coverage
- 🚀 Performance optimizations
- 🎨 UI/UX enhancements

## 🙏 Acknowledgments

- **Hugging Face** for providing the transformer models and pipeline infrastructure
- **Facebook AI Research** for FAISS vector similarity search
- **AG News Dataset** for training data
- **FastAPI** team for the excellent web framework
- **PyTorch** and **Sentence-Transformers** communities

