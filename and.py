import cv2 as cv
import numpy as np

img1 = cv.imread("bit1.png")
img2 = cv.imread("bit2.png")

and_islemi = cv.bitwise_and(img1,img2,mask = None)

cv.imshow("And işlemi",and_islemi)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()


cv.imwrite("and.png",and_islemi)
print("Kaydedildi \1")
