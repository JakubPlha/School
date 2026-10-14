import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Pro školní projekt povolíme CORS všude (později se dá zpřísnit)
CORS(app)

@app.get("/")
def home():
    return "VDF Support Backend is running"

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    student = (data.get("student") or "unknown").strip()

    if not message:
        return jsonify({"error": "message is required"}), 400

    # Zatím fake odpověď (fáze BACKEND)
    reply = f"[DEMO] Přijal jsem dotaz od {student}: {message}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)
