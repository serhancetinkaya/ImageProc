import numpy as np
import cv2

img = cv2.imread("WIN_20170511_13_06_18_Pro.jpg", cv2.IMREAD_GRAYSCALE)
row, col = img.shape

def intToBitArray(img):
    bit_list = []

    for i in range(row):
        for j in range(col):
             bit_list.append(np.binary_repr(img[i][j], width=8))

    return bit_list

imgIn1D = intToBitArray(img)
imgIn2D = np.reshape(imgIn1D, (row, col))

def bitplane(bit_img_val, img_1d):
    bit_list = [int(i[bit_img_val]) for i in img_1d]
    return bit_list

eight_bit_img = np.array(bitplane(0, imgIn1D)) * 128

seven_bit_img = np.array(bitplane(1, imgIn1D)) * 64

combine = eight_bit_img + seven_bit_img
comb = np.reshape(combine, (row, col))

cv2.imwrite("comb.jpeg", comb)

eight_bit_img = np.reshape(eight_bit_img, (row, col))
cv2.imwrite("8bitvalue.jpg", eight_bit_img)

seven_bit_img = np.reshape(seven_bit_img, (row, col))
cv2.imwrite("7bitvalue.jpg", seven_bit_img)

gray = cv2.imread("WIN_20170511_13_06_18_Pro.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.jpeg", gray)
