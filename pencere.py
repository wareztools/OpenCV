import cv2 as cv

path = "resim.jpg"

img = cv.imread(path)

cv.namedWindow("test",cv.WINDOW_AUTOSIZE)

cv.imshow("test",img)

cv.waitKey(0)

cv.destroyAllWindows()