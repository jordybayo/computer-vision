import cv2
import numpy as np


img = cv2.imread('bookpage.jpg')


retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('gris', grayscale)
cv2.imshow('function gaussiene', gaus)
cv2.imshow('function otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()