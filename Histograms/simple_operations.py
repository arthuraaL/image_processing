import cv2
import numpy as np
import matplotlib.pyplot as plt



gray_img = cv2.cvtColor(cv2.imread('images/home.jpg'), cv2.COLOR_BGR2GRAY)
output_img = np.zeros(gray_img.shape, dtype=gray_img.dtype)

alpha = 1.0 # Simple contrast control
beta = -60   # Simple brightness control

# for height in range(gray_img.shape[0]):
#     for width in range(gray_img.shape[1]):
#         output_img[height, width] = np.clip(alpha * gray_img[height, width] + beta, 0, 255)

bright_img = cv2.convertScaleAbs(gray_img, alpha=1.0, beta=80)
dark_img = cv2.convertScaleAbs(gray_img, alpha=1.0, beta=-80)
low_img = cv2.convertScaleAbs(gray_img, alpha=0.3, beta=0)
high_img = cv2.convertScaleAbs(gray_img, alpha=2.2, beta=0)

plt.subplot(5,2,1), plt.imshow(gray_img, 'gray'), plt.title('Original Image')
plt.subplot(5,2,2), plt.hist(gray_img.ravel(), 256, [0,256])
plt.subplot(5,2,3), plt.imshow(bright_img, 'gray'), plt.title('Brighter Image')
plt.subplot(5,2,4), plt.hist(bright_img.ravel(), 256, [0,256])
plt.subplot(5,2,5), plt.imshow(dark_img, 'gray'), plt.title('Darker Image')
plt.subplot(5,2,6), plt.hist(dark_img.ravel(), 256, [0,256])
plt.subplot(5,2,7), plt.imshow(low_img, 'gray'), plt.title('Low contrast Image')
plt.subplot(5,2,8), plt.hist(low_img.ravel(), 256, [0,256])
plt.subplot(5,2,9), plt.imshow(high_img, 'gray'), plt.title('High contrast Image')
plt.subplot(5,2,10), plt.hist(high_img.ravel(), 256, [0,256])

plt.subplots_adjust(hspace=0.5)
plt.show()

cv2.imwrite('images/original_img.png', gray_img)
cv2.imwrite('images/brighter_img.png', bright_img)
cv2.imwrite('images/darker_img.png', dark_img)
cv2.imwrite('images/low_contrast_img.png', low_img)
cv2.imwrite('images/high_contrast_img.png', high_img)