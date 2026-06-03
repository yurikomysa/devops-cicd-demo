from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "DevOps CI/CD Pipeline працює!", "version": os.getenv("APP_VERSION", "2.0")}

@app.route("/health")
def health():
    return jsonify({"status": "OK", "service": "web-api"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)