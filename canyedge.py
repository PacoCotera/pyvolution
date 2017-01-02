import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while(1):
    _, img = cap.read()
    edges = cv2.Canny(img, 100, 200)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()