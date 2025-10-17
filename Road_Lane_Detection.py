#importing files
import cv2
import numpy as np

# Function to make coordinates for the lines to be drawn
def make_coordinates(image,line_parameter):

    slope,intercept =line_parameter
    y1=image.shape[0] # get the height of the image
    y2=int(y1*(3/5)) # get the y-coordinate of the point 3/5ths of the way down the image
    x1=int((y1-intercept)/slope) # calculate the x-coordinate of the point at the bottom of the image
    x2=int((y2-intercept)/slope) # calculate the x-coordinate of the point 3/5ths of the way down the image
    return np.array([x1,y1,x2,y2]) # return the array of coordinates in the format [x1, y1, x2, y2]


# Function to calculate the average slope and intercept for the lines on the left and right sides of the lane
def average_slope_intersept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if(slope<0):
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average=np.average(left_fit,axis=0)
    right_fit_average=np.average(right_fit,axis=0)
    left_line=make_coordinates(image,left_fit_average)
    right_line=make_coordinates(image,right_fit_average)
    return np.array([left_line,right_line])

def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)# convert the image to grayscale
    blur=cv2.GaussianBlur(gray,(5,5),0)
    # apply a Gaussian blur to the image with a
    # skernel size of (5,5)
    # and standard deviation of 0
    canny=cv2.Canny(blur,50,150)
    # apply the Canny edge detection algorithm to the blurred image,
    # with min and max threshold values of 50 and 150 respectively
    return canny

def display_lines(image,lines):
#This function takes in an image and a set of lines, represented as (x1, y1, x2, y2) coordinates
    line_image=np.zeros_like(image) # Create an empty image with the same shape as the input image
    if lines is not None:     # If lines are provided
        for x1,y1,x2,y2 in lines: # Iterate through the lines
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)   # Draw a blue, 10-pixel wide line
                                                # on the empty image from (x1,y1) to (x2,y2)
    return line_image # Return the image with the lines drawn on it

def region_of_interest(image):
    # Get the height of the image

    height=image.shape[0]
    # Define the coordinates of the ROI as a polygon

    polygons=np.array([[(200,height),(1100,height),(550,250)]])
    # Create a black image with the same shape as the input image

    mask=np.zeros_like(image)
    # Fill the polygon defined above with white color on the black image
    cv2.fillPoly(mask,polygons,255)
    # Perform bitwise and operation to keep only the ROI on the original image
    masked_image=cv2.bitwise_and(image,mask)
    # Return the image with the ROI
    return masked_image






# image=cv2.imread('pexels-pixabay-63324.jpg') #working
image=cv2.imread('pexels-photo-1201673.jpg') #working
# image=cv2.imread('IMG20230129145114.jpg') #Uni image

lane_image=np.copy(image)

canny_image=canny(image)

cropped_image=region_of_interest(canny_image)

lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)

averaged_lines=average_slope_intersept(lane_image,lines)

line_image=display_lines(lane_image,averaged_lines)

combo_image=cv2.addWeighted(lane_image,0.5,line_image,1,1)

cv2.imshow("------Road Results------ ",combo_image)
cv2.waitKey(0)