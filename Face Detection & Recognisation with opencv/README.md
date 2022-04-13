# Face Detection & Recognisation with opencv
"Face detection is a computer technology that determines the locations and sizes of human faces in arbitrary (digital) images. It detects facial features and ignores anything else, such as buildings, trees and bodies. Face detection can be regarded as a more general case of face localization. In face localization, the task is to find the locations and sizes of a known number of faces (usually one)." - wiki - [Face detection](https://en.wikipedia.org/wiki/Face_detection)

In this demo, we will take an image and search for human faces in it. We are going to use a pre-trained classifier to perform this search. 
For the uninitiated, OpenCV is a Python library which is mainly used in various computer vision problems.
Here, we are using the “haarcascade_frontalface_default.xml” as our model from the opencv github repository.

## Task 
A classifier is buit to recognise the faces of celebraties using haar_face.xml and cascade_classiffier.

## Install opencv
```bash
pip install opencv-python
```

## Steps
### step1: Training model
Check the [face_recognition.py](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Face%20Detection%20%26%20Recognisation%20with%20opencv/face_recognition/face_recognition.py) for training the model. In this process, we are downloading the har_face.xml for training the model and saving the train model in [face_trained.yml](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Face%20Detection%20%26%20Recognisation%20with%20opencv/face_recognition/face_trained.yml) file similarly saving labels in [label.npy](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Face%20Detection%20%26%20Recognisation%20with%20opencv/face_recognition/labels.npy) file.
### step2: testing
you can test the classifier by usin [face_detect.py](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Face%20Detection%20%26%20Recognisation%20with%20opencv/face_recognition/face_detect.py) file. check for detail.

## output:
#### Face Detection:

![face](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/face%20detection.png?raw=true)

#### Face Recognition(classification):


![recog1](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/madona.png?raw=true)
![ben](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/elton.png?raw=true)
