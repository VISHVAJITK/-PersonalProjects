# Driver Drowsiness Detection System with OpenCV & Keras

## Demo


A countless number of people drive on the highway day and night. Taxi drivers, bus drivers, truck drivers and people traveling long-distance suffer from lack of sleep. Due to which it becomes very dangerous to drive when feeling sleepy.

The majority of accidents happen due to the drowsiness of the driver. So, to prevent these accidents we will build a system using Python, OpenCV, and Keras which will alert the driver when he feels sleepy.

The objective of this  Python project is to build a drowsiness detection system that will detect that a person’s eyes are closed for a few seconds. This system will alert the driver when drowsiness is detected.

## Driver Drowsiness Detection System

In this Python project, OpenCV is used for gathering the images from webcam and feed them into a Deep Learning model which will classify whether the person’s eyes are ‘Open’ or ‘Closed’. The approach we will be using for this Python project is as follows :

- Step 1 – Take image as input from a camera.

- Step 2 – Detect the face in the image and create a Region of Interest (ROI).

- Step 3 – Detect the eyes from ROI and feed it to the classifier.

- Step 4 – Classifier will categorize whether eyes are open or closed.

- Step 5 – Calculate score to check whether the person is drowsy.

## Driver Drowsiness Detection Dataset
you can download the dataset from [here](https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new).

## Project Prerequisites

- OpenCV – pip install opencv-python (face and eye detection).
- TensorFlow – pip install tensorflow (keras uses TensorFlow as backend).
- Keras – pip install keras (to build our classification model).
- Pygame – pip install pygame (to play alarm sound).

use following command to install neccesary librarise:
```bash
  pip install -r requirements.txt
```

## Steps for Performing Driver Drowsiness Detection
You can check above [model.ipynb](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Drowsiness%20Detection%20with%20opencv%20%26%20keras/model.ipynb) and [detection.py](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Drowsiness%20Detection%20with%20opencv%20%26%20keras/detection.py)  files to build the model.

## Summary
In this Python project, to built a drowsy driver alert system that you can implement in numerous ways. The OpenCV to detect faces and eyes using a haar cascade classifier and then used a CNN model to predict the status.