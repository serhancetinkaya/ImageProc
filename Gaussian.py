import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("WIN_20170511_13_06_18_Pro.jpg", cv2.IMREAD_GRAYSCALE)

kernel_size = (5, 5)
sigma = 1.5
filtered_img = cv2.GaussianBlur(img, kernel_size, sigma)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Resim')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Gaussian Filtre Uygulanmış Resim')
plt.imshow(filtered_img, cmap='gray')

plt.show()