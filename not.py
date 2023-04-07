import cv2 as cv
import numpy as np 

img1 = cv.imread("bit2.png")
img2 = cv.imread("bit1.png")

not_islemi = cv.bitwise_not(img1,img2,mask = None)

cv.imshow("not islemi",not_islemi)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()


cv.imwrite("not.png",not_islemi)
print("kaydedildi")

