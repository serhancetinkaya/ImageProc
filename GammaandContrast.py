import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("FltFace.jpg", cv2.IMREAD_GRAYSCALE)

gamma = 1.5

gamma_corrected = np.power(img / 255.0, gamma) * 255.0
gamma_corrected = np.uint8(gamma_corrected)

min_val, max_val, _, _ = cv2.minMaxLoc(img)
contrast_stretched = cv2.convertScaleAbs(img, alpha=255.0 / (max_val - min_val), beta=-min_val * 255.0 / (max_val - min_val))

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title('Orijinal Resim')
plt.imshow(img, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Gamma Düzeltme (Gamma = 1.5)')
plt.imshow(gamma_corrected, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Kontrast Germe')
plt.imshow(contrast_stretched, cmap='gray')

plt.show()