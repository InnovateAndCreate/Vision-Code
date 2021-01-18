import cv2
import numpy as np

web = cv2.VideoCapture(0)

while True:
    _, frame = web.read()

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
web.release()