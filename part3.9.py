import cv2
import numpy as np


cap = cv2.VideoCapture(1)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #hsv hue sat value
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])


    # dark_red = np.unint8([[[12,22,121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    ouverture = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    fermeture = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('ouverture', ouverture)
    cv2.imshow('fermeture', fermeture)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()