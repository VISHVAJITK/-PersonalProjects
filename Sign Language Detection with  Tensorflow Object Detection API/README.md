# Tensorflow Object Detection Walkthrough
This set of Notebooks provides a complete set of code to be able to train and leverage your own custom object detection model using the Tensorflow Object Detection API.
![imag](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/Screenshot%202022-04-13%20150857.png?raw=true)

## Demo

Link: https://remarkable-mousse-36b43a.netlify.app

## Steps
## Step 1. 
Clone this repository: https://github.com/VISHVAJITK/-PersonalProjects/tree/main/Sign%20Language%20Detection%20with%20%20Tensorflow%20Object%20Detection%20API

## Step 2. 
Create a new virtual environment 


```bash
 python -m venv tfod
```
## Step 3. 
Activate your virtual environment

```bash
source tfod/bin/activate # Linux
.\tfod\Scripts\activate # Windows 
```

## Step 4.
Install dependencies and add virtual environment to the Python Kernel

```bash
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=tfodj
```

## Step 5.
Collect images using the Notebook1. data_Collection.ipynb - ensure you change the kernel to the virtual environment as shown below
<img src="https://i.imgur.com/8yac6Xl.png"> 


## Step 6.
Manually divide collected images into two folders train and test. So now all folders and annotations should be split between the following two folders. 
\TFODCourse\Tensorflow\workspace\images\train 
\TFODCourse\Tensorflow\workspace\images\test

## Step 7.
Begin training process by opening  tutorial.ipynb, this notebook will walk you through installing Tensorflow Object Detection, making detections, saving and exporting your model. 

## Step 8.
During this process the Notebook will install Tensorflow Object Detection. You should ideally receive a notification indicating that the API has installed successfully at Step 8 with the last line stating OK.  
<img src="https://i.imgur.com/FSQFo16.png">
If not, resolve installation errors by referring to the Error Guide [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/) in this folder.

## Step 9.
Once you get to step 6. Train the model, inside of the notebook, you may choose to train the model from within the notebook. I have noticed however that training inside of a separate terminal on a Windows machine you're able to display live loss metrics. 
<img src="https://i.imgur.com/K0wLO57.png"> 


## Step 10.
 You can optionally evaluate your model inside of Tensorboard. Once the model has been trained and you have run the evaluation command under Step 7. Navigate to the evaluation folder for your trained model e.g. 
<pre> cd Tensorlfow/workspace/models/my_ssd_mobnet/eval</pre> 
and open Tensorboard with the following command
<pre>tensorboard --logdir=. </pre>
Tensorboard will be accessible through your browser and you will be able to see metrics including mAP - mean Average Precision, and Recall.
<br />