# 🧠 AI-Powered Therapy Dialogue Generator

[![Run in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmjsk0805/full-dialogue-generation/blob/main/llama3_server.ipynb)

A full-stack Flask web application and Google Colab-compatible notebook powered by the `meta-llama/Llama-3.1-8B-Instruct` model. This project generates full, realistic therapy dialogues based on expert-authored chapters and partial conversations.

---

## 📌 Project Overview

This tool supports mental health research and education by generating synthetic therapist–patient conversations. Given a therapy guide (PDF) and a starter dialogue (CSV), it completes the session with alternating, empathetic lines between the two roles. It’s ideal for psychologists, AI researchers, and instructors experimenting with AI in therapeutic contexts.

---

## 🚀 Getting Started

### 🖥️ Option 1: Run Locally (GPU Required)

> For users who want a full-featured local Flask app with model inference.

```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python run.py
```

Then open `http://127.0.0.1:5000` in your browser to use the app.

---

### 🔗 Option 2: [Run in Google Colab](https://colab.research.google.com/github/mmjsk0805/full-dialogue-generation/blob/main/llama3_server.ipynb)

> For quick testing using GPU in the cloud.

#### Instructions:

1. Open the notebook `llama3_server.ipynb` in Colab.
2. Upload the following files:
   - `run.py`
   - `generate.py`
   - `templates/index.html`
3. Install required packages:
   ```bash
   pip install flask transformers accelerate PyPDF2 pandas pyngrok
   ```
4. Run the server:
   ```bash
   python run.py
   ```
5. Open the generated `ngrok` link to access the web interface.

---

## 📁 Project Structure

```
.
├── run.py                   # Starts Flask server
├── generate.py             # Model interaction and prompt generation
├── extract_dialogue.py     # Optional CSV post-processing
├── llama3_server.ipynb     # Colab notebook interface
├── templates/
│   └── index.html          # File upload UI
├── dialogues/              # Sample input CSVs
├── outputs/                # Generated CSVs
├── models/                 # Saved models (optional)
├── requirements.txt
└── README.md
```

---

## 📄 About `llama3_server.ipynb`

This Colab notebook provides an interactive environment to:

- Load the LLaMA 3.1 Instruct model from Hugging Face
- Accept user-uploaded PDFs and CSVs
- Construct a prompt and generate realistic dialogue
- Return results as a downloadable CSV

It’s ideal for GPU-powered experimentation or demonstrations without setting up a full backend.

---

## 🧠 Prompt Design

```text
You are a professional therapist. Based on the following therapy guide and ongoing dialogue, continue the conversation empathetically and realistically.

--- Therapy Guide ---
{book_text}

--- Conversation so far ---
{starter_dialogue}

--- Continue the conversation starting as Therapist. Respond with realistic alternating lines between Patient and Therapist until a natural stopping point. ---
```

---

## 📥 Input Formats

### 🗂️ Therapy Guide (PDF)

Upload any chapter or section from a professional therapy guide.

### 💬 Starter Dialogue (CSV)

CSV with `Patient` and `Therapist` columns:

```csv
Patient,Therapist
I just feel stuck lately.,That's totally understandable. What's been going on?
```

---

## 📤 Output Format

Generated CSV:

```csv
Patient,Therapist
I've been anxious constantly.,Can you describe when you feel it the most?
Mostly when I wake up.,That’s a common trigger—how do your mornings start?
...
```

---

## ⚙️ CUDA vs CPU Settings

If you're using a **GPU**, make sure this is in your model call:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
```

If you're on **CPU-only environments** (like non-GPU Colab), change to:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
```

---

## 📜 License

MIT License  
© 2025 [Jaden Moon](https://github.com/mmjsk0805)
