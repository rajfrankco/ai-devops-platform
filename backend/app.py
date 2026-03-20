from flask import Flask, request, jsonify, render_template
from ai_engine import analyze_logs
from db import save_incident

app = Flask(__name__, template_folder="../frontend/templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    logs = request.json.get("logs")
    result = analyze_logs(logs)

    save_incident(logs, str(result))

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)