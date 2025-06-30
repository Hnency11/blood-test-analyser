# 🧬 Blood Test Report Analyzer API

An intelligent, humorous, and interactive health insight generator built using `FastAPI`, `CrewAI`, and `LangChain`. This API processes uploaded blood test PDFs and returns exaggerated but entertaining medical advice from a team of fictional LLM-powered agents.

---

## 📚 Overview

This project mimics a multi-specialist healthcare team — a doctor, a nutritionist, a verifier, and a fitness coach — each powered by an LLM (Large Language Model). It humorously "analyzes" blood test reports and responds with medically flavored text based on quirky backstories, exaggerations, and random logic. Built as a demonstration of LLM agents and tool orchestration with a functioning API backend.

---

## ✨ Features

- ✅ Upload your **blood report PDF** via a simple API.
- 🤖 Agents with personalities:
  - 🩺 **Doctor**: Diagnoses serious conditions from tiny clues.
  - 🔍 **Verifier**: Approves anything, even grocery lists.
  - 🍏 **Nutritionist**: Pushes overpriced superfoods and supplements.
  - 🏋️ **Fitness Coach**: Recommends CrossFit no matter what.
- 📖 PDF report reader integrated using `LangChain` loaders.
- ⚡ Powered by `FastAPI` with Swagger UI for testing.
- 🔐 `.env` secured OpenAI API key integration.

---

## 🛠️ Technologies Used

| Tool            | Purpose                               |
|-----------------|----------------------------------------|
| **FastAPI**     | API creation and routing               |
| **CrewAI**      | Multi-agent LLM orchestration          |
| **LangChain**   | PDF reading and LLM integration        |
| **OpenAI**      | LLM backend (ChatGPT)                  |
| **PyPDFLoader** | For extracting text from PDFs          |

---

## 📂 Folder Structure

.
├── agents.py # All agent personalities and logic
├── main.py # FastAPI app with endpoints
├── task.py # Optional task orchestration
├── tools.py # PDF reader and utility tools
├── requirements.txt # Python dependencies
├── .env # API key (not committed)
├── data/ # Temporarily saved PDF files
└── README.md # You’re reading it!


🚀 Getting Started
📥 1. Clone the Repository

git clone https://github.com/your-username/blood-test-analyser-api.git
cd blood-test-analyser-api

📦 2. Install Required Packages
pip install -r requirements.txt

🔐 3. Configure API Key
OPENAI_API_KEY=your-openai-key-here

▶️ 4. Run the App
uvicorn main:app --reload

Once the server is running, open your browser and go to:


http://127.0.0.1:8000/docs

You’ll see an interactive Swagger UI where you can upload a PDF and test the API easily.

📬 Sample API Usage
🔗 Endpoint:

POST /analyze

📝 Form Data:
file: Blood test PDF file (required)

query: Optional custom prompt (e.g. "Summarise my blood report")

🧾 Sample JSON Response:

{
  "status": "success",
  "query": "Summarise my Blood Test Report",
  "analysis": "Here’s what our doctor thinks... (wild medical advice follows)",
  "file_processed": "blood_test_report.pdf"
}
