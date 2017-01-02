import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    img = frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 50, 150)
    img = cv2.Laplacian(img, cv2.CV_64F)
    img = np.uint8(img)
    img = cv2.blur(img,(3,3))
    #img = cv2.bitwise_not(img)
    cv2.imshow('img',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()