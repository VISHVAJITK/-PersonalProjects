from turtle import color
import cv2 as cv
from cv2 import cvtColor

img = cv.imread('E:\Projects\Face Detection & Recognisation with opencv\data\IMG_20190811_133259.jpg')
resize = cv.resize(img,(800,600))
gray = cv.cvtColor(resize,cv.COLOR_BGRA2GRAY)

haar_face = cv.CascadeClassifier('E:\Projects\Face Detection & Recognisation with opencv\haar_face.xml')
rectangles = haar_face.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 7)
print(f"Number of Faces Detected: {len(rectangles)}")

for x,y,z,w in rectangles:
    cv.rectangle(resize,(x,y),(z+x,w+y),color = (0,255,0),thickness = 4)

cv.imshow('Faces',resize)
cv.waitKey(0)