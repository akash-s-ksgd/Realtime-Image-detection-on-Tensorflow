from flask import Flask, request, jsonify
from flask_cors import CORS
from detection import detect_objects
from database import get_recognized_objects

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    """Handles image detection requests"""
    print(f"🔹 Received {request.method} request at /detect")  # Debug log

    if 'image' not in request.files:
        print("❌ Error: No image uploaded")
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    detected_objects = detect_objects(image)

    return jsonify({"detected_objects": detected_objects})

@app.route('/recognized', methods=['GET'])
def recognized():
    return jsonify(get_recognized_objects())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
