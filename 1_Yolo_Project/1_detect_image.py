from ultralytics import YOLO
import os
import cv2

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Define folders
image_folder = 'Resources'
output_folder = 'Outputs'

# Create Outputs folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all files in Resources
names = os.listdir(image_folder)

for name in names:
    if not name.lower().endswith(('.jpg', '.png', '.jpeg')):
        continue  # Skip non-image files

    image_path = os.path.join(image_folder, name)

    # Run detection
    results = model(image_path)

    # Get the result image with bounding boxes
    result_img = results[0].plot()

    # Display in a single OpenCV window
    cv2.imshow("YOLO Detection", result_img)

    # Save the image to Outputs folder with same name
    save_path = os.path.join(output_folder, name)
    cv2.imwrite(save_path, result_img)

    # Wait 500ms between images, press 'q' to quit
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

# Close OpenCV window
cv2.destroyAllWindows()
