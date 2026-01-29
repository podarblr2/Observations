from flask import Flask, request, send_file
from flask_cors import CORS
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    data = request.json or {}
    teacher = data.get("teacher_name", "Unknown Teacher")

    file_path = f"/tmp/{uuid.uuid4()}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)

    c.drawString(100, 800, "LESSON OBSERVATION FORM")
    c.drawString(100, 760, f"Teacher Name: {teacher}")

    c.showPage()
    c.save()

    return send_file(file_path, as_attachment=True)
