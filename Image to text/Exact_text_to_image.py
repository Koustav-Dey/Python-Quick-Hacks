from PIL import Image
from pytesseract import pytesseract


path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = 'download.png'

pytesseract.tesseract_cmd = path

img = Image.open(image)

text = pytesseract.image_to_string(img)
print(text)