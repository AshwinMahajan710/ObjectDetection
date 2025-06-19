import cv2
import numpy as np

image = cv2.imread('Resources/cards.jpg') 
width, height = 250, 350  # Define the width and height for the output image
# Define the points for the perspective transformation
pts1 = np.float32([[752, 118], [1120, 265], [540, 668], [871, 830]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# By using wrap perspective exact image have been captured of 5 card
metrix = cv2.getPerspectiveTransform(pts1, pts2)  # Get the perspective transformation matrix
image_output = cv2.warpPerspective(image, metrix, (width, height))  # Apply the perspective transformation
cv2.imshow('Original Image', image)
cv2.imshow('Warped Image', image_output)  # Display the warped image
cv2.waitKey(0)