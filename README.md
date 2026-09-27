# Y104 AI Camera

A real-time object detection project using a Y104 Wi-Fi camera, Home Assistant, OpenCV, and YOLO11.

## Overview

This project connects a Y104 Wi-Fi camera to a Python-based computer vision pipeline for real-time object detection.

The camera stream is accessed through the Ease Life integration in Home Assistant and exposed as an HTTP-FLV stream. OpenCV reads the live video stream, while YOLO11 detects objects in each frame and displays bounding boxes and class labels in real time.

## Architecture

```text
Y104 Wi-Fi Camera
        ↓
Ease Life Cloud
        ↓
Home Assistant
        ↓
HTTP-FLV Stream
        ↓
OpenCV
        ↓
YOLO11
        ↓
Real-Time Object Detection
```

## Features

- Real-time video streaming from a Y104 Wi-Fi camera
- Real-time object detection with YOLO11
- Live bounding boxes and class labels
- OpenCV-based video processing
- Home Assistant integration
- HTTP-FLV stream support
- Environment variable configuration
- Secure proxy token handling

## Technologies

- Python
- OpenCV
- Ultralytics YOLO11
- Home Assistant
- Docker
- Ease Life Camera Integration
- HTTP-FLV
- python-dotenv

## Project Structure

```text
Y104-AI-Camera/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The `.env` file, virtual environment, Python cache files, and YOLO model weights are excluded from Git using `.gitignore`.

## Requirements

Before running the project, make sure you have:

- Python installed
- Docker running
- Home Assistant running
- Ease Life Camera integration configured
- A working Y104 camera stream

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yagubbx/Y104-AI-Camera.git
cd Y104-AI-Camera
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can allow it temporarily for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root.

You can use `.env.example` as a template:

```env
CAMERA_URL=http://localhost:8765/live/YOUR_DEVICE_ID.flv?token=YOUR_PROXY_TOKEN
```

Replace:

- `YOUR_DEVICE_ID` with your Ease Life camera device ID.
- `YOUR_PROXY_TOKEN` with your Home Assistant Ease Life proxy token.

> **Important:** Never commit your real `.env` file or proxy token to GitHub.

## Running the Project

Make sure Docker and Home Assistant are running and the Ease Life camera integration is available.

Then run:

```bash
python main.py
```

YOLO11 will automatically download the required model weights on the first run if they are not already available.

A window will open displaying the live camera stream with detected objects, bounding boxes, and class labels.

Press **Q** to stop the application.

## How It Works

The video pipeline works as follows:

1. The Y104 camera provides video through the Ease Life cloud.
2. Home Assistant connects to the camera using the Ease Life Camera integration.
3. The integration exposes the live video through an HTTP-FLV proxy.
4. OpenCV connects to the HTTP-FLV stream and reads video frames.
5. Each frame is passed to YOLO11.
6. YOLO11 detects supported objects in the frame.
7. OpenCV displays the processed video with bounding boxes and class labels.

## Future Improvements

Possible improvements include:

- Multi-object tracking
- Person counting
- Vehicle detection and counting
- Detection event logging
- Restricted-area detection
- Automatic alerts and notifications
- Web dashboard
- Database integration
- Performance optimization

## Security

Sensitive information such as camera URLs and proxy tokens should be stored only in the `.env` file.

The `.env` file is excluded from Git and should never be uploaded to a public repository.

Do not expose the Home Assistant FLV proxy port directly to the public Internet.

## Author

**Yagub Khalilli**

AI Engineering | Computer Vision | Machine Learning