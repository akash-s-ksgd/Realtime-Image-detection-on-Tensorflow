from flask import Flask, request, jsonify
from detection import detect_objects
from database import save_recognized_object, get_recognized_objects

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if image is None:
        return jsonify({"error": "No image uploaded"}), 400

    detected_objects = detect_objects(image)
    return jsonify({"detected_objects": detected_objects})


@app.route('/recognized', methods=['GET'])
def recognized():
    return jsonify(get_recognized_objects())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)


