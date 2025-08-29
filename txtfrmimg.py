import cv2
import pytesseract
from PIL import Image  

image_path = 'img.png'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_,binarized = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

pil_image = Image.fromarray(binarized)

extracted_text = pytesseract.image_to_string(pil_image)

print("Extracted Text:")
print(extracted_text)

cv2.imshow("Binarized Image", binarized)
cv2.waitKey(0)
cv2.destroyAllWindows()