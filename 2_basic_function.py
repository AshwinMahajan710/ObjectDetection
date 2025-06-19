import cv2

img = cv2.imread('Resources/lena.png', cv2.IMREAD_COLOR)  # read the image in color format
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert the image from BGR to RGB format just for trial

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert the image to grayscale
new_img = cv2.GaussianBlur(img, (7, 7), 8)  # This will blur the image
border_img = cv2.Canny(img, 100, 200)  
another_border_img = cv2.Canny(new_img, 100, 200)  

# The conlucion is that the edge detection works better on the blurred image
cv2.imshow('Lena Image', img)  # display the image
cv2.imshow('Border Image', border_img)  # display the edge detected image
cv2.imshow('Blurred Image', new_img)  # display the blurred image
cv2.imshow('Another Border Image', another_border_img)  # display the edge detected image from blurred image
cv2.waitKey(0)  # wait for a key press