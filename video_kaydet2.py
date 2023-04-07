import cv2 as cv

cap = cv.VideoCapture(0) # 0 varsayılan cameran / test.mp4 okuma veya ip camera http://33.32.33.22:9090/video

if(cap.isOpened == False):
    print("Dosya okunamadı")

frame_widht = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_widht,frame_height)

result = cv.VideoWriter("ornek.avi",cv.VideoWriter_fourcc(*'MJPG'),10,size)

while True:
    ret,frame = cap.read()
    result.write(frame)
    cv.imshow("video",frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

    else:
        break

    cap.release()
    result.release()

    cv.destroyAllWindows()
    print("Başarıyla kaydedildi ve çerezler temizlendi \1")

