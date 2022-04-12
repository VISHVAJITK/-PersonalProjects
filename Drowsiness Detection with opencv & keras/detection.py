import cv2 as cv
from cv2 import waitKey
from keras.models import load_model
import numpy as np


face_model = load_model(r"saved_models\face_model.h5")
# face_model = pickle.load(r'saved_models\yawn_mouths.pickle')
eye_model = load_model(r"saved_models\cnnCat2.h5")
eye_lables = ['Closed',"Open"]
face_lables = ['No_yawn',"Yawn"]


cap = cv.VideoCapture(0)
haar_face = cv.CascadeClassifier(r"haar_cascade\haarcascade_frontalface_alt.xml")
haar_leye = cv.CascadeClassifier(r"haar_cascade\haarcascade_lefteye_2splits.xml")
haar_reye = cv.CascadeClassifier(r"haar_cascade\haarcascade_righteye_2splits.xml")

count=0
score=0
font = cv.FONT_HERSHEY_COMPLEX_SMALL



labels = [] 

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
    leye_rect = haar_leye.detectMultiScale(gray)
    reye_rect = haar_reye.detectMultiScale(gray)


    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),color = (0,256,0),thickness= 2)
        # face = frame`[y:y+h,x:x+w`]
        face = frame.copy()
        face = cv.resize(face, (256,256))
        face= np.reshape(face,(1,256,256,3))
        fpred = face_model.predict(face)
        if(np.argmax(fpred)==1):
            face_result='Yawn'
        elif(np.argmax(fpred)==0):
            face_result='No_yawn'
        print(face_result)


    for (x,y,w,h) in leye_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),color = (0,256,0),thickness= 2)
        l_eye = frame[y:y+h,x:x+w]
        l_eye = cv.cvtColor(l_eye,cv.COLOR_BGR2GRAY)
        l_eye = cv.resize(l_eye, (24,24))
        l_eye = l_eye.reshape(24,24,-1)
        l_eye = np.expand_dims(l_eye,axis=0)
        lpred = eye_model.predict(l_eye)
        if(np.argmax(lpred)==1):
            lbl='Open'
        elif(np.argmax(lpred)==0):
            lbl='Closed'

        # print(lbl)


    for (x,y,w,h) in reye_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),color = (0,256,0),thickness= 2)
        r_eye = frame[y:y+h,x:x+w]
        r_eye = cv.cvtColor(r_eye,cv.COLOR_BGR2GRAY)
        r_eye = cv.resize(r_eye, (24,24))
        r_eye = r_eye.reshape(24,24,-1)
        r_eye = np.expand_dims(r_eye,axis=0)
        rpred = eye_model.predict(r_eye)
        if(np.argmax(rpred)==1):
            rbl='Open'
        elif(np.argmax(rpred)==0):
            rbl='Closed'
        # print(rbl)

    if face_result == 'Yawn':
        cv.putText(frame,'Yawn',(100,100-20), font, 1,(255,255,255),1,cv.LINE_AA)

    cv.imshow('Detection', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

# http://192.168.249.128:8080/


