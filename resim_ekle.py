#Resimleri üst üste bastırma

import cv2 as cv
import numpy as np

image1 = cv.imread("1.jpg")
image2 = cv.imread("2.jpg")

weightedsum = cv.addWeighted(image1,0.5,image2,0.4,0)

cv.imshow("resimler",weightedsum)

if cv.waitKey(0) & 0xff == 28:
    cv.destroyAllWindows()
    