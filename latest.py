import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from pytesseract import image_to_string

# Initialize pre-trained MobileNetV2 model for object detection
def load_object_detection_model():
    model = MobileNetV2(weights="imagenet")
    return model

# Function to detect objects in an image
def detect_objects(image, model):
    # Resize image to 224x224 (MobileNetV2 input size)
    resized_image = cv2.resize(image, (224, 224))
    expanded_image = np.expand_dims(resized_image, axis=0)
    preprocessed_image = preprocess_input(expanded_image)

    # Predict objects
    predictions = model.predict(preprocessed_image)
    decoded_predictions = decode_predictions(predictions, top=5)[0]

    # Display results
    for _, label, confidence in decoded_predictions:
        print(f"Detected: {label} with confidence {confidence:.2f}")

# Function to extract text from an image (OCR)
def extract_text(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = image_to_string(gray_image)
    return text

# Function to detect landmarks (placeholder for custom CNN model)
def detect_landmarks(image):
    # Placeholder for a custom CNN model trained on landmark datasets
    print("Landmark detection is not implemented in this example.")
    # You can train a custom CNN model for landmark detection using datasets like Google Landmarks.

# Function to detect products (placeholder for custom CNN model)
def detect_products(image):
    # Placeholder for a custom CNN model trained on product datasets
    print("Product detection is not implemented in this example.")
    # You can train a custom CNN model for product detection using datasets like Open Images.

# Main function
def main():
    # Load image
    image_path = input("Enter the path:")  # Replace with your image path
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found.")
        return

    # Load object detection model
    print("Loading object detection model...")
    object_detection_model = load_object_detection_model()

    # Detect objects
    print("Detecting objects...")
    detect_objects(image, object_detection_model)

    # Extract text
    print("Extracting text...")
    text = extract_text(image)
    print(f"Extracted Text: {text}")

    # Detect landmarks
    print("Detecting landmarks...")
    detect_landmarks(image)

    # Detect products
    print("Detecting products...")
    detect_products(image)

if __name__ == "__main__":
    main()