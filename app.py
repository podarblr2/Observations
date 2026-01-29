from flask import Flask, request, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    data = request.json
    teacher = data.get("teacher_name", "Unknown Teacher")

    filename = f"/tmp/{uuid.uuid4()}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "LESSON OBSERVATION FORM")
    c.drawString(100, 760, f"Teacher Name: {teacher}")

    c.showPage()
    c.save()

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run()
