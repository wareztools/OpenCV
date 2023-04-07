import cv2 as cv
import os

cap = cv.VideoCapture("dans.mp4")

try:
    if not os.path.exists("data"):
        os.makedirs("data")

except OSError:
    print("klasör oluşturulurken hata meydana geldi bro")

currentframe = 0


while True:
    ret ,frame = cap.read()
    
    if ret:
        name = "./data/frame" +str(currentframe) + ".jpg"
        print("oluşturuluyor"+name)

        cv.imwrite(name,frame)

        currentframe += 1

    else:
        break

cap.release()
cv.destroyAllWindows()        



