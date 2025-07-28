from flask import Flask, render_template
from generate import generate_bp

# Initialize the Flask app
app = Flask(__name__)

# Register the blueprint that handles the /generate route
app.register_blueprint(generate_bp)

@app.route("/")
def index():
    # Render the main upload interface
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
