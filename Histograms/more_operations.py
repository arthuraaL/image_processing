import cv2
import numpy as np
import matplotlib.pyplot as plt


def equalization(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_hist = cv2.calcHist([image], [0], None, [256], [0,256])
    eq_img = cv2.equalizeHist(image) #analogous to the cumulative density function
    eq_hist = cv2.calcHist([eq_img], [0], None, [256], [0,256])

    plt.subplot(221), plt.imshow(image, 'gray')
    plt.subplot(222), plt.plot(gray_hist)
    plt.subplot(223), plt.imshow(eq_img, 'gray')
    plt.subplot(224), plt.plot(eq_hist)
    plt.show()
        



if __name__ == '__main__':
    image = cv2.imread('images/darker_img.png', 0)
    equalization(image)