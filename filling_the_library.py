from PIL import Image                #открытие изображений
from pytesseract import pytesseract  #чтение текста в изображениях
import cv2                           #нахождение координат на изображении
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# вариант с самым простым чтением изображения c PIL

image = Image.open('images/trial.png')
image = image.resize((2000,1000))
image.save('images/trial.png')
'''
text = pytesseract.image_to_string(image)

print(text[:-1])'''

# вариант с чтением с использованием ограничительной рамки cv2

img = cv2.imread("images/trial.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # перевод изображения в полутоновое, или если я правильно понимаю объект для работы с цветами

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |          # перевод изображения в бинарное, то есть в бело-черное
                                          cv2.THRESH_BINARY_INV) 
cv2.imwrite('threshold_image.jpg',thresh1)                           # сохранение в текущем каталоге

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))   # задаем размер поиска слов, увеличивает точность поиска слов

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 3) # с каждым циклом итерации увеличивается рамка 
cv2.imwrite('dilation_image.jpg',dilation)                           # сохранение в текущем каталоге