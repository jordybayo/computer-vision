import cv2
import numpy as np

cap = cv2.VideoCapture(1)

record = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outering.avi', record, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()