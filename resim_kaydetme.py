import cv2 as cv
import os 

path = r"resim.jpg"

dizin = r"C:\Users\titan\Desktop"

img = cv.imread(path,0)



os.chdir(dizin)



print("Kaydedilmeden once :")
print(os.listdir(dizin))

filename = "monsterfindikli.jpg"

cv.imwrite(filename,img)



print("Kaydedildikten sonra :",os.listdir(dizin))
print("kaydedildi \1")

cv.destroyAllWindows()