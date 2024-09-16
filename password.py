import cv2
import easyocr
import matplotlib.pyplot as plt

# Define the path to the image
image_name = 'rit.jpg'

# Read the image
img = cv2.imread(image_name)

# Initialize the text detector
reader = easyocr.Reader(['en'], gpu=False)

# Detect text in the image
text_results = reader.readtext(image_name)

threshold = 0.25
# Draw bounding boxes and text on the image
for bbox, text, score in text_results:
    if score > threshold:
        print("Detected Text:", text)  # Print detected text
        bbox = tuple(map(int, bbox[0])), tuple(map(int, bbox[2]))
        cv2.rectangle(img, bbox[0], bbox[1], (0, 255, 0), 2)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# Display the image with bounding boxes and text using matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Print "RAJALAKSHMI INSTITUTE OF TECHNOLOGY" in ASCII art with #
ascii_art = """
██████╗ ██╗████████╗    ███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗███████╗
██╔══██╗██║╚══██╔══╝    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝
██████╔╝██║   ██║       ███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   ███████╗
██╔══██╗██║   ██║       ╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   ╚════██║
██║  ██║██║   ██║       ███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   ███████║
╚═╝  ╚═╝╚═╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
"""

print(ascii_art)
