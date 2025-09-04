from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image, lang="eng+ind")  # eng = English, ind = Indonesia

    return jsonify({"text": text})

@app.route("/")
def home():
    return "🚀 OCR API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
