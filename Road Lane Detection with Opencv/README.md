# Road Lane line detection with Opencv

Lane Line detection is a critical component for self driving cars and also for computer vision in general. This concept is used to describe the path for self-driving cars and to avoid the risk of getting in another lane.

In this project, a model is build  to detect lane lines in real-time. We will do this using the concepts of computer vision using OpenCV library. To detect the lane we have to detect the white markings on both sides on the lane.

## Demo


## Frame Masking and Hough Line Transformation
To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using frame masking. The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we simply update those pixel values to 0 in the NumPy array.

After making we need to detect lane lines. The technique used to detect mathematical shapes like this is called Hough Transform. Hough transformation can detect shapes like rectangles, circles, triangles, and lines.

