import cv2 as cv
import numpy as np


cap = cv.VideoCapture("/test.mp4")

while(cap.isOpened() == False):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow(frame)

        if cv.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
