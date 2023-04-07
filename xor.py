import cv2 as cv
import numpy as np 

img1 = cv.imread("bit1.png")

img2 = cv.imread("bit2.png")

xor_islemi = cv.bitwise_xor(img1,img2,mask = None)

cv.imshow("xor",xor_islemi)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()



cv.imwrite("xor.png",xor_islemi)
print("Kaydedildi.")