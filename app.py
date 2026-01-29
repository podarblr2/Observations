from flask import Flask, request, send_file
import uuid
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Backend is live!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <- THIS is important
    app.run(host="0.0.0.0", port=port)



