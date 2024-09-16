import cv2
import easyocr

print("\n\n\b\t\t\t\tThis is a Sajan Developed Application\n\n")
correct_password = 2006
attempts = 1
for attempt in range(attempts):
    a = int(input("Enter password to Continue: "))
    if a == correct_password:
        print("Access Granted...")
        break
    else:
        print("Wrong Password, try again !")
else:
    print("Access Denied!")
    exit()

# Define the path to the image
image_name = input("enter image name:")

# Read the image
img = cv2.imread(image_name)

# Initialize the text detector
reader = easyocr.Reader(['en'], gpu=False)

# Detect text in the image
text_results = reader.readtext(image_name)


threshold = 0.18
# Draw bounding boxes and text on the image
for bbox, text, score in text_results:
    if score > threshold:
        print("Detected Text:", text)  # Print detected text
        bbox = tuple(map(int, bbox[0])), tuple(map(int, bbox[0]))
        cv2.rectangle(img, bbox[0], bbox[1], (250, 255, 155), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# # Print "RAJALAKSHMI INSTITUTE OF TECHNOLOGY" in ASCII art with #
# ascii_art = """
# ██████╗ ██╗████████╗    ███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗███████╗
# ██╔══██╗██║╚══██╔══╝    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝
# ██████╔╝██║   ██║       ███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   ███████╗
# ██╔══██╗██║   ██║       ╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   ╚════██║
# ██║  ██║██║   ██║       ███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   ███████║
# ╚═╝  ╚═╝╚═╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
# """
#
# print(ascii_art)

# Display the image with bounding boxes and text
cv2.imshow('Detected Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
