import cv2 

img = cv2.imread('images.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('rotacion',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()