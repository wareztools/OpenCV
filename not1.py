import cv2 as cv
import numpy as np 

img1 = cv.imread("bit2.png")
img2 = cv.imread("bit1.png")

dest_not1 = cv.bitwise_not(img1,mask = None)
dest_not2 = cv.bitwise_not(img2,mask = None)



cv.imshow("not islemi1",dest_not1)
cv.imshow("not islemi2",dest_not2)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()



