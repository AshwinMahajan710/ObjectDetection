import cv2
import numpy as np

img = cv2.imread('Resources/lambo.png')  # read the image in color format\
img2 = cv2.resize(img, (640, 480))  # resize the image to 640x480
print(img.shape)  # print the shape of the original image
cv2.imshow('Lambo Image', img2)  # display the resized image
cv2.imshow('Original Lambo Image', img)  # display the original image
crop_img = img[0:200, 0:200]  # crop the image from (0,0) to (200,200)
cv2.imshow('Cropped Image', crop_img)  # display the cropped image
cv2.waitKey(0)  # wait for a key press
cv2.destroyAllWindows()  # close all windows