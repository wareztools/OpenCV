import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
#cap = cv.VideoCapture("http://88.22.112.23:8080/video") uzak ip camera
#cap = cv.VideoCapture("video.mp4") video okuma

if not cap.isOpened():
    print("Kameraya Baglanılamadı !")
    exit()

while True:
    ret,frame = cap.read()

    if not ret:
        print("Görüntü alınamadı !")
        break

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow("camera",frame)

    if cv.waitKey(1) == ord("q"):
        break
