import tensorflow as tf
import numpy as np
from PIL import Image

# Load the pre-trained MobileNet model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Preprocess input image
def preprocess_image(image):
    image = Image.open(image).convert("RGB")
    image = image.resize((224, 224))  # Resize to MobileNet input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Detect objects in the image
def detect_objects(image):
    processed_image = preprocess_image(image)
    
    # Ensure the model is used correctly
    predictions = model.predict(processed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    detected_objects = [label for (_, label, _) in decoded_predictions]
    
    return detected_objects
