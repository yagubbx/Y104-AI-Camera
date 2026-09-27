import os

import cv2
from dotenv import load_dotenv
from ultralytics import YOLO


# .env faylını oxu
load_dotenv()

camera_url = os.getenv("CAMERA_URL")

if not camera_url:
    raise ValueError("CAMERA_URL .env faylında tapılmadı!")


# YOLO modelini yüklə
model = YOLO("yolo11n.pt")


# Ease Life canlı stream-inə qoşul
cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    raise RuntimeError("Kamera stream-i açıla bilmədi!")


print("Kamera qoşuldu!")
print("Çıxmaq üçün Q bas.")


while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame alına bilmədi.")
        break

    # YOLO ilə obyektləri tap
    results = model(frame, verbose=False)

    # Bounding box-ları frame üzərinə çək
    annotated_frame = results[0].plot()

    # Nəticəni göstər
    cv2.imshow("Y104 - YOLO Detection", annotated_frame)

    # Q basıldıqda proqramı bağla
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()