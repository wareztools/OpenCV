import cv2 as cv
import numpy as np

image1 = cv.imread("star.png")
image2 = cv.imread("4gen.png")


sub = cv.subtract(image1, image2)

cv.imshow("pencere",sub)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

cv.imwrite("kaydedilen_resim.png",sub)
print("kaydedildi")