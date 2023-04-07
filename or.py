import cv2 as cv
import numpy as np

img1 = cv.imread("bit1.png")

img2 = cv.imread("bit2.png")

or_islem = cv.bitwise_or(img1,img2,mask = None)

cv.imshow("or",or_islem)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

cv.imwrite("or.png",or_islem)
print("Kaydedildi.")