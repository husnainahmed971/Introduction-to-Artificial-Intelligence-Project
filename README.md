# Road Lane Detection (Basic Implementation)

# Overview
  
This project is the simplest implementation of Road Lane Detection using basic computer vision techniques in Python and OpenCV.
It detects lane markings on the road from a static image by identifying edges and fitting lines to represent the lanes.
The implementation is ideal for beginners who want to understand how classical computer vision can be used for lane detection before moving toward advanced approaches.

# Features
- Detects lane lines from an image using Canny Edge Detection and Hough Transform.
- Focuses detection on the Region of Interest (ROI) to avoid unnecessary areas.
- Draws detected lane lines on the original image.
- Easy to understand and modify for learning purposes.

# Techniques Used

- **Canny Edge Detection:** Detects lane boundaries by finding edges in the image.
- **Hough Transform:** Identifies straight line segments that represent lane markings.
-** Region of Interest (ROI):** Masks unnecessary parts of the image to focus only on the road area.
- **Line Averaging:** Smoothens the left and right lane lines for a cleaner output.
  
**Note:** Techniques like Color Thresholding, Perspective Transform, Kalman Filter, or Deep Learning are not used in this version.

# Requirements
- Python 3.x
- OpenCV
- NumPy
  
# Author
Husnain Ahmed

Simplest implementation of Road Lane Detection using Python and OpenCV for educational purposes.
