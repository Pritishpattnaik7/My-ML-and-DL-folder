import cv2

img = cv2.imread('dog.png')
gray = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)  #for grayscale image

cv2.imshow('Dog Image', img)   #title, img
cv2.imshow('Dog Grayscale', gray)

cv2.waitKey(0)  #waiting time
cv2.destroyAllWindows()

