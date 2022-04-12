from tkinter import Label
import cv2 as cv
import os
import uuid

face_haar = cv.CascadeClassifier(r'haar_cascade\haarcascade_frontalface_alt.xml')
paths = {
    "face_test_path" : os.path.join('Data','face','test'),
    "face_train_path" : os.path.join('Data','face','train'),

}


lables = ['no_yawn','yawn']
for path in paths.keys():
    for lable in lables:
        for i in os.listdir(os.path.join(paths[path],lable)):
            img = cv.imread(os.path.join(os.path.join(paths[path],lable),i))
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            face_rect = face_haar.detectMultiScale(gray,minNeighbors=4,scaleFactor=1.1)
            if len(face_rect)==0:
                continue
            else:
                for x,y,w,h in face_rect:
                    cv.rectangle(img,(x,y),(x+w,y+h),color=(0,256,0), thickness=2)
                    break
            c_img = img[y:y+h,x:x+w]
            imgname = os.path.join('cropped_data',lable,lable+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv.imwrite(imgname,c_img)
            # cv.imshow(f'img{i}',c_img)
            
  
# cv.waitKey(0)
