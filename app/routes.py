import os, csv  # ← you forgot to import these
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

LLM_ENDPOINT = "https://87b992f4dff5.ngrok-free.app/generate"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        pdf_file = request.files.get("pdf")
        csv_file = request.files.get("csv")
        prompt = request.form.get("prompt", "")

        files = {}
        if pdf_file:
            files["pdf"] = (pdf_file.filename, pdf_file.stream, pdf_file.mimetype)
        if csv_file:
            files["csv"] = (csv_file.filename, csv_file.stream, csv_file.mimetype)

        data = {"prompt": prompt}
        res = requests.post(LLM_ENDPOINT, files=files, data=data)
        res.raise_for_status()

        response_data = res.json()["response"]

        # Save CSV output
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/generated_dialogue.csv", "w", newline="") as f:
            f.write(response_data)

        return jsonify({"message": "Success", "output_path": "outputs/generated_dialogue.csv"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Failed", "error": str(e)}), 500
