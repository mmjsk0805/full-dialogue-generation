# 🧠 AI-Powered Therapy Dialogue Generator

This is a full-stack Flask web application that uses the `meta-llama/Llama-3.1-8B-Instruct` model to generate realistic, empathetic therapy dialogues. Users upload a therapy guide chapter (PDF) and a starter dialogue (CSV). The app returns a complete conversation in downloadable CSV format.

---

## 🚀 Demo (Colab + GPU Compatible)

### Try It on Colab:

1. Upload the following files:
   - `run.py`
   - `generate.py`
   - `templates/index.html`
2. Install dependencies:
   ```bash
   pip install flask transformers accelerate PyPDF2 pandas pyngrok
   ```
3. Run the server:
   ```bash
   python run.py
   ```
4. Open the printed `ngrok` URL to access the web app.

---

## 🧰 Tech Stack

- **Frontend**: HTML (file upload interface)
- **Backend**: Flask, PyTorch, Hugging Face Transformers
- **Model**: [`meta-llama/Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- **Libraries**: `transformers`, `torch`, `flask`, `PyPDF2`, `pandas`, `pyngrok`

---

## 📁 File Structure

```
.
├── run.py
├── generate.py
├── templates/
│   └── index.html
├── outputs/
│   └── generated_dialogue.csv
├── requirements.txt
└── README.md
```

---

## 📄 How It Works

1. Upload a **therapy chapter** as a `.pdf`
2. Upload a **starter dialogue** as a `.csv` with two columns: `Patient`, `Therapist`
3. The backend constructs a prompt using both files
4. The LLaMA model generates the rest of the conversation
5. The generated conversation is parsed and returned as a `.csv` file

---

## 🧠 Prompt Template

```
You are a professional therapist. Based on the following therapy guide and ongoing dialogue, continue the conversation empathetically and realistically.

--- Therapy Guide ---
{book_text}

--- Conversation so far ---
{starter_dialogue}

--- Continue the conversation starting as Therapist. Respond with realistic alternating lines between Patient and Therapist until a natural stopping point. ---
```

---

## 📎 Example Input

**CSV Format:**

```csv
Patient,Therapist
I just feel stuck lately.,That's totally understandable. What's been going on?
```

**PDF Format:**

- Any therapy-related chapter or guide, e.g., "Section 5: Enhancing Motivation"

---

## 📥 Output Format

The result is saved and returned as a CSV:

```csv
Patient,Therapist
I've been anxious constantly.,Can you describe when you feel it the most?
Mostly when I wake up.,That’s a common trigger—how do your mornings start?
...
```

---

## 🖥️ Local Usage (Optional)

> For GPU users only (CUDA-enabled environment required)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ⚙️ CUDA Note for Colab or CPU-only Environments

If you're running on Colab without GPU support, update this line:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
```

To:

```python
inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
```

---

## 📄 License

MIT License  
© 2025 [Jaden Moon](https://github.com/mmjsk0805)
