from ultralytics import YOLO
import os
import cv2

model = YOLO('yolov8s.pt')

vid_path = 'Resources/elon.mp4'
cap = cv2.VideoCapture(vid_path)

while True:
    success, img = cap.read()
    if not success:
        break

    # Run detection with streaming enabled (returns a generator)
    res = model(img, stream=True)

    for r in res:
        # Show result frame
        cv2.imshow('YOLO Detection', r.plot())

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
