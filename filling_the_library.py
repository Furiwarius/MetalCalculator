from PIL import Image                #открытие изображений
from pytesseract import pytesseract  #чтение текста в изображениях
import cv2                           #нахождение координат на изображении

image = Image.open('images/пробный.png')
image = image.resize((1200,600))
image.save('images/пробный.png')

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(image)

print(text[:-1])