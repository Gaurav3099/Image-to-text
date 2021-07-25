#pip install tesseract : Image to Text library 
#pip install pytesseract
#tesseract installer : https://github.com/UB-Mannheim/tesseract/wiki
#pip install Pillow : Python Image Library
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
	name=input('Enter name of image: ')
	img = Image.open(name)
	text = pytesseract.image_to_string(img)
	print(text)

	remember = open("data.txt", "w")
	remember.write(text)
	remember.close()

convert()

