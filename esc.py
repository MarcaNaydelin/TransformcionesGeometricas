import cv2
import numpy as np


img = cv2.imread('images.jpg', 0)
height, width = img.shape
scaled_img = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Scaled', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()