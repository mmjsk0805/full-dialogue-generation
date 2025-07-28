import pandas as pd
import PyPDF2
import csv
import requests
from flask import request, jsonify, send_file, Blueprint

generate_bp = Blueprint("generate", __name__)

COLAB_BACKEND_URL = "https://87b992f4dff5.ngrok-free.app/generate"

def parse_pdf(file_stream):
    reader = PyPDF2.PdfReader(file_stream)
    return "\n".join([page.extract_text() for page in reader.pages])

def parse_csv(file_stream):
    df = pd.read_csv(file_stream)
    return "\n".join([f"{row['Patient']}\n{row['Therapist']}" for _, row in df.iterrows()])

def build_prompt(book_text, starter_dialogue):
    return f"""
You are a professional therapist. Based on the following therapy guide and ongoing dialogue, continue the conversation empathetically and realistically.

--- Therapy Guide ---
{book_text}

--- Conversation so far ---
{starter_dialogue}

--- Continue the conversation starting as Therapist. Respond with realistic alternating lines between Patient and Therapist until a natural stopping point. ---
"""

@generate_bp.route("/generate", methods=["POST"])
def generate_dialogue():
    try:
        files = {
            "pdf": request.files["pdf"],
            "csv": request.files["csv"]
        }

        response = requests.post(COLAB_BACKEND_URL, files=files)

        if response.status_code == 200:
            output_path = "generated_dialogue.csv"
            with open(output_path, "wb") as f:
                f.write(response.content)
            return send_file(output_path, as_attachment=True)
        else:
            return jsonify({"response": f"Colab Error: {response.text}"}), 500

    except Exception as e:
        return jsonify({"response": f"Proxy Error: {str(e)}"}), 500