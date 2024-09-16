import cv2
import easyocr

# Input image path from the user
image_path = input("Enter the image path: ")

# Read the image
image_read = cv2.imread(image_path)
reader = easyocr.Reader(['ta'], gpu=False)  # Initialize EasyOCR reader for Tamil language

# Detect text in the image
text_result = reader.readtext(image_path)
threshold = 0.25  # Threshold for text detection confidence score

for bbox, text, score in text_result:
    if score > threshold:
        print("Detected Text:", text)

        # Convert the bounding box coordinates to integers
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))  # Corrected to use bottom-right point

        # Draw a rectangle around detected text
        cv2.rectangle(image_read, top_left, bottom_right, (135, 206, 235), 3)

        # Put the detected text on the image
        cv2.putText(image_read, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# Display the image with detected text
cv2.imshow("Detected Text", image_read)
cv2.waitKey(0)
cv2.destroyAllWindows()
