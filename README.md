# 🧠 AI-Powered Therapy Dialogue Generator

[![Run in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmjsk0805/full-dialogue-generation/blob/main/llama3_server.ipynb)

This is a full-stack Flask web application and Google Colab-compatible notebook that generates realistic, empathetic therapy dialogues using Meta’s `LLaMA 3.1 8B Instruct` model. The app allows users to upload a therapy guide (PDF) and a starter dialogue (CSV), and it completes the conversation in a natural, therapist-guided format.

---

## 📌 Overview

This project supports research and training in mental health by simulating full therapist–patient sessions. It’s designed for psychologists, researchers, and developers who want to experiment with AI-generated therapeutic conversations grounded in expert-authored source material.

---

## 🚀 How to Run the App

This project uses a hybrid setup:

- The **language model runs on Google Colab** (with GPU support)
- The **Flask web interface runs locally** and sends requests to the Colab server

---

### 🔐 Step 1: Hugging Face Authentication

To access the gated `meta-llama/Llama-3.1-8B-Instruct` model:

1. Visit: [https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)  
   → Click **“Access repository”** and wait for approval.

2. In Colab, authenticate:

   ```python
   from huggingface_hub import login
   login()
   ```

3. Paste your [Hugging Face access token](https://huggingface.co/settings/tokens) when prompted.

Without this, loading the model will result in a 401 error.

---

### 🌐 Step 2: ngrok Authentication (for URL tunneling)

To expose the Flask server from Colab:

1. Sign up or log in at: [https://dashboard.ngrok.com](https://dashboard.ngrok.com)

2. Copy your personal authtoken from the dashboard.

3. In Colab, register your token:
   ```python
   !ngrok config add-authtoken YOUR_NGROK_TOKEN_HERE
   ```

This will allow your server to be publicly accessible via a temporary `ngrok` URL.

---

### ⚙️ Step 3: Launch the App

1. Open [`llama3_server.ipynb`](https://colab.research.google.com/github/mmjsk0805/full-dialogue-generation/blob/main/llama3_server.ipynb) in Colab.

2. Run all cells.  
   This will:

   - Load the model
   - Start a Flask API server
   - Print an `ngrok` URL like `https://abc123.ngrok-free.app`

3. Copy that URL and paste it into both of the following files in your local repo:

   - `routes.py`
   - `generate.py`

   ```python
   LLM_ENDPOINT = "https://abc123.ngrok-free.app/generate"
   ```

4. In your local terminal:

   ```bash
   python run.py
   ```

5. Visit `http://127.0.0.1:5000` in your browser to use the app.

---

## 🧪 Example Input Files

You can test the app using the same files shown in the screenshots:

- 📄 [Therapy Guide PDF](examples/Section_5_Enhancing_Motivation.pdf)
- 💬 [Starter Dialogue CSV](examples/Formatted_Dialogue_CSV.csv)

Upload both in the web app or Colab notebook to generate a complete therapy session.

---

## 📁 Project Structure

```
.
├── run.py                   # Starts local Flask server
├── generate.py             # Sends prompt to Colab model endpoint
├── routes.py               # Handles upload and frontend routing
├── llama3_server.ipynb     # Google Colab backend server
├── templates/
│   └── index.html          # File upload UI
├── examples/               # Sample input files (PDF, CSV)
├── screenshots/            # App preview images
├── outputs/                # Generated dialogues
├── requirements.txt
└── README.md
```

---

## 📤 Output Format

The output is saved and returned as a downloadable CSV, like:

```csv
Patient,Therapist
I've been anxious constantly.,Can you describe when you feel it the most?
Mostly when I wake up.,That’s a common trigger—how do your mornings start?
...
```

---

## 🧠 Prompt Design

The core of this app is the structured prompt passed to the LLaMA model:

```text
You are a professional therapist. Based on the following therapy guide and ongoing dialogue, continue the conversation empathetically and realistically.

--- Therapy Guide ---
{book_text}

--- Conversation so far ---
{starter_dialogue}

--- Continue the conversation starting as Therapist. Respond with realistic alternating lines between Patient and Therapist until a natural stopping point. ---
```

---

## 🖼️ Screenshots

### 🔹 Upload Interface

Users upload a therapy guide and starter dialogue.

![Start Page](screenshots/startpage.png)

---

### 🔹 After Upload

Files are processed and sent to the model for generation.

![Upload Complete](screenshots/startpage2.png)

---

### 🔹 Output Result

The user receives a downloadable CSV of the generated conversation.

![Generated CSV Preview](screenshots/resultDialogue.png)

---

## ⚙️ GPU vs CPU Notes

If you're using a GPU (recommended), use:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
```

On a CPU-only setup (e.g. some Colab environments), replace with:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
```

---

## 🛠️ Future Improvements

- [ ] Add automatic GPU/CPU fallback
- [ ] Live chatbot interface with memory
- [ ] Style customization (e.g., CBT, DBT, motivational)
- [ ] Hugging Face Spaces deployment
- [ ] Human-in-the-loop editing and scoring

---

## ⚠️ Compatibility Disclaimer

This app was tested on a specific setup (Python 3.10, GPU-enabled Colab, macOS local server).  
While it should work broadly, **you may need to tweak environment variables or dependencies** on different machines.

The focus of this repo is to **share the architecture, model interface, and user experience design**, not to guarantee cross-platform deployment.

Feel free to open an issue or contact me if you run into trouble—I’m happy to help!

---

## 📜 License

MIT License  
© 2025 [Jaden Moon](https://github.com/mmjsk0805)
