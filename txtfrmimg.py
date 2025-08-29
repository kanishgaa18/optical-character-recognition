import cv2
import pytesseract

# Set the path to the Tesseract executable
# This is crucial on Windows, as pytesseract needs to know where the engine is.
# Change the path below to match your installation.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from a file
image_path = 'img.png'  # <--- Replace this with your image file's path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Convert the image to grayscale
    # Grayscale conversion often improves OCR accuracy
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the processed image
    extracted_text = pytesseract.image_to_string(gray_image)

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

    # Display the image for a visual check
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()