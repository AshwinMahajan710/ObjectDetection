from ultralytics import YOLO
import cv2
import time

# Load a light YOLOv8 model for better speed
model = YOLO('yolov8n.pt')  # Use 'yolov8s.pt' or larger if you have GPU

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if webcam opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop over webcam frames
while True:
    success, frame = cap.read()
    if not success:
        break

    # Optional: measure time for FPS
    start = time.time()

    # Run detection on the frame
    results = model(frame, stream=True)

    # Loop over results and display
    for r in results:
        result_frame = r.plot()
        cv2.imshow('YOLOv8 Real-Time Detection', result_frame)

    # Optional: Print FPS
    end = time.time()
    fps = 1 / (end - start)
    print(f"FPS: {fps:.2f}")

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
