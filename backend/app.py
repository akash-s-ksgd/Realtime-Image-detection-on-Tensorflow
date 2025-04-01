from flask import Flask, request, jsonify
from flask_cors import CORS
from detection import detect_objects
from database import get_recognized_objects

app = Flask(__name__)
CORS(app)  # Enable CORS globally

@app.route('/detect', methods=['POST', 'OPTIONS'])
def detect():
    # Ensure a file was uploaded
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']

    # Debugging: Log image details
    print(f"Received image: {image.filename}, Type: {image.content_type}")

    try:
        detected_objects = detect_objects(image)
        return jsonify({"detected_objects": detected_objects})
    except Exception as e:
        print(f"Error during detection: {str(e)}")
        return jsonify({"error": "Detection failed", "details": str(e)}), 500

@app.route('/recognized', methods=['GET'])
def recognized():
    try:
        recognized_objects = get_recognized_objects()
        return jsonify(recognized_objects)
    except Exception as e:
        print(f"Error fetching recognized objects: {str(e)}")
        return jsonify({"error": "Failed to fetch recognized objects", "details": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Flask server on http://127.0.0.1:8000")
    print("📌 Available Routes:")
    print(app.url_map)  # Print all routes for debugging

    app.run(host="0.0.0.0", port=8000, debug=True)
