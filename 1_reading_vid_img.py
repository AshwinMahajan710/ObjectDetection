import cv2

# img = cv2.imread("Resources/car1.jpeg", cv2.IMREAD_COLOR)  # read the image
# cv2.imshow("Car Image", img)  # display the image
# print(img.shape)  # print the shape of the image
# cv2.waitKey(0)  # wait for a key press

# Reading of video is frame  by frame
# vid = cv2.VideoCapture("Resources/elon.mp4")  # read the video

# while True:
#     success, img = vid.read()  # read the video frame by frame
#     print(img.shape)  # print the shape of the image
#     cv2.imshow("Video Frame", img)  # display the video frame
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # wait for a key press
#         break

# Reading from webcam
vid = cv2.VideoCapture(0)  # We can pass pass id as per camera connected to the system
vid.set(3, 640) # 3 if for width
vid.set(4, 480) # 4 is for height 

while True:
    success, img = vid.read()  
    cv2.imshow("Webcam Frame", img)  
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break