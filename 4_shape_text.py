import cv2
import numpy as np

# img = np.zeros((256, 256, 3), dtype=np.uint8) # For zeros
img = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8) # for random values

# Create some shapes on the image
cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)  # draw a blue line from (0,0) to (255,255)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(img, (128, 128), 50, (0, 0, 255), -1)  # draw a filled red circle at (128,128) with radius 50
cv2.putText(img, 'OpenCV Shapes', (50, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # add text

print(img.shape)  # print the shape of the image
cv2.imshow('Black Image', img)  # display the black image
cv2.waitKey(0)  # wait for a key press