from PIL import Image
import pytesseract
import cv2
import numpy as np


def spot_vertical_text(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Use HoughLines to detect lines in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

    # Loop through the lines and filter out vertical lines
    for line in lines:
        rho, theta = line[0]
        if np.pi / 4 < theta < 3 * np.pi / 4:
            # Draw the line on the original image
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display the result
    cv2.imshow('Detected Lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Use pytesseract for OCR on the detected lines
    text = pytesseract.image_to_string(Image.fromarray(img))

    return text

if __name__ == ("__main__"):
    image_path = input("Enter the path to the image: ")
    spotted_text = spot_vertical_text(image_path)
    print("Spotted Text:\n", spotted_text)