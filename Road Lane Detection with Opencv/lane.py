import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('image\lane.png')
lane_img = np.copy(img)

def canny(image):
    gray = cv.cvtColor(image,code = cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    canny = cv.Canny(blur,50,150)
    return canny

def area_of_interest(image):
    blank = np.zeros(shape = image.shape[:2], dtype= 'uint8')
    coordinates = np.array([[(200,image.shape[0]-1),(1100,image.shape[0]-1),(550,250)]])
    triangle = cv.fillPoly(blank,coordinates,color= 255)
    masked_image = cv.bitwise_and(image,triangle)
    return masked_image


def make_cordinates(parameters, lane_image):
    slope, intercept = np.average(parameters, axis= 0)
    y1 = lane_image.shape[0]
    y2 = int(y1*0.6)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return (x1,y1,x2,y2)
    
def display_lines(cropped_image,lane_image):
    lines = cv.HoughLinesP(cropped_image,2,np.pi/180,100,minLineLength=40,maxLineGap=5)
    line_image = np.zeros_like(lane_image)
    left_line =[]
    right_line = []
    if lines is not None:
        for line in lines:
            x1, y1, x2,y2 = line.reshape(4)
            slope, intercept = np.polyfit((x1,x2),(y1,y2),deg= 1)
            if slope <0:
                left_line.append((slope, intercept))
            else:
                right_line.append((slope, intercept))

    lx1,ly1,lx2,ly2 = make_cordinates(left_line, lane_image)
    rx1,ry1,rx2,ry2 = make_cordinates(right_line, lane_image)
    cv.line(line_image,(lx1,ly1),(lx2,ly2), color= (255,0,0), thickness= 10)
    cv.line(line_image,(rx1,ry1),(rx2,ry2), color= (255,0,0), thickness= 10)
    final_image = cv.addWeighted(lane_image,0.8,line_image,1,1)
    return final_image

cap = cv.VideoCapture(r'image\test2.mp4')

while True:
    _ , frame = cap.read()
    gradient = canny(frame)
    masked_image = area_of_interest(gradient)
    final_image = display_lines(masked_image,frame)
    cv.imshow('Result',final_image)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


