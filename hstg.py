import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("FltFace.jpg", cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Resim')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Histogram Eşitleme')
plt.imshow(equ, cmap='gray')

plt.show()