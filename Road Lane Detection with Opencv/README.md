# Road Lane line detection with Opencv

Lane Line detection is a critical component for self driving cars and also for computer vision in general. This concept is used to describe the path for self-driving cars and to avoid the risk of getting in another lane.

In this project, a model is build  to detect lane lines in real-time. We will do this using the concepts of computer vision using OpenCV library. To detect the lane we have to detect the white markings on both sides on the lane.

## Demo
![demo](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/ezgif.com-gif-maker.gif?raw=true)

## Frame Masking and Hough Line Transformation
To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using frame masking. The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we simply update those pixel values to 0 in the NumPy array.

After making we need to detect lane lines. The technique used to detect mathematical shapes like this is called Hough Transform. Hough transformation can detect shapes like rectangles, circles, triangles, and lines.

## Steps:
You can follow the code from above [lane.py](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Road%20Lane%20Detection%20with%20Opencv/lane.py)

- Installation and Imports
```bash
pip install -r requirements.txt
```
- Apply frame masking and find region of interest
- Conversion of pixels to a line in [Hough Transform space](https://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm)
- Create two lines in each frame after Hough transform
- Process each frame of video to detect lane
- Clip the input video to frames and get the resultant output video file