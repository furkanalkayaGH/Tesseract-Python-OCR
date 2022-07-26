import cv2
import pytesseract
from pytesseract import  Output
from tesseract import *

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('C:\MicrosoftTeams-image_1.png', 0)

# Simple thresholding
ret,thresh1 = cv2.threshold(img,210 ,255 ,cv2.THRESH_BINARY)

# Resize Image
scale_percent = 70  # percent of original size
width = int(thresh1.shape[1] * scale_percent / 100)
height = int(thresh1.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(thresh1, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)

# Detect Text Boxes
d = pytesseract.image_to_data(resized,output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    resized = cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 0, 255), 2)

extracted_text = pytesseract.image_to_string(resized, lang='tur')

print(extracted_text)


cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()