import os

import cv2
from dotenv import load_dotenv
from ultralytics import YOLO


# Load environment variables from the .env file
load_dotenv()

camera_url = os.getenv("CAMERA_URL")

if not camera_url:
    raise ValueError("CAMERA_URL was not found in the .env file!")


# Load the YOLO object detection model
model = YOLO("yolo11n.pt")


# Connect to the Ease Life live camera stream
cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    raise RuntimeError("Could not open the camera stream!")


print("Camera connected!")
print("Press Q to exit.")


while True:
    # Read the next frame from the live camera stream
    ret, frame = cap.read()

    if not ret:
        print("Could not read a frame from the camera stream.")
        break

    # Run YOLO object detection on the current frame
    results = model(frame, verbose=False)

    # Draw detected objects, bounding boxes, and class labels
    annotated_frame = results[0].plot()

    # Display the processed live video
    cv2.imshow("Y104 - YOLO Detection", annotated_frame)

    # Exit the application when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release the camera stream and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()