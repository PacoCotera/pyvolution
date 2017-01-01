import numpy as np
import cv2
from matplotlib import pyplot as plt

"""
img = cv2.imread('panda.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('pandagray.jpg',img)
"""

"""
img = cv2.imread('panda.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    print("Pressed ESC key")
else:
    print("Pressed key: [", k,"]")
cv2.destroyAllWindows()
"""

img = cv2.imread('panda.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

