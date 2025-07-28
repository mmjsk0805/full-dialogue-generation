from flask import Flask, render_template
from generate import generate_bp

app = Flask(__name__)
app.register_blueprint(generate_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
