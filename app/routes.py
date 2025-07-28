import os, csv  
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

# Initialize the Flask app and enable CORS to allow cross-origin requests
app = Flask(__name__)
CORS(app)

# This is the endpoint of the language model running on Colab via ngrok
LLM_ENDPOINT = "https://87b992f4dff5.ngrok-free.app/generate"

@app.route("/")
def index():
    # Render the main HTML page with the file upload form
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        # Retrieve uploaded PDF and CSV files from the form
        pdf_file = request.files.get("pdf")
        csv_file = request.files.get("csv")

        # Optional custom prompt provided by the user (not used yet)
        prompt = request.form.get("prompt", "")

        # Prepare files for sending to the backend language model
        files = {}
        if pdf_file:
            files["pdf"] = (pdf_file.filename, pdf_file.stream, pdf_file.mimetype)
        if csv_file:
            files["csv"] = (csv_file.filename, csv_file.stream, csv_file.mimetype)

        # Send the prompt and files to the Colab-hosted LLM server
        data = {"prompt": prompt}
        res = requests.post(LLM_ENDPOINT, files=files, data=data)
        res.raise_for_status()

        # Get the generated CSV string from the model's response
        response_data = res.json()["response"]

        # Save the generated CSV to the local outputs directory
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/generated_dialogue.csv", "w", newline="") as f:
            f.write(response_data)

        # Respond to the frontend with success and output path info
        return jsonify({"message": "Success", "output_path": "outputs/generated_dialogue.csv"})

    except Exception as e:
        # Log and return any errors that occur during processing
        print("Error:", e)
        return jsonify({"message": "Failed", "error": str(e)}), 500
