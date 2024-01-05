import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("FltFace.jpg", cv2.IMREAD_GRAYSCALE)

kernel_size = 5
filtered_img = cv2.blur(img, (kernel_size, kernel_size))

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Resim')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Ortalama Filtre Uygulanmış Resim')
plt.imshow(filtered_img, cmap='gray')

plt.show()