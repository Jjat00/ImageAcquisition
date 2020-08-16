# **Image Acquisition for Intrinsic Calibration**

This is a simple application for image acquisition. This in order to carry out an intrinsic calibration of three cameras: RGB camera, depth camera and a thermal camera.
With this application you can manually and automatically save the images of the calibration pattern.

## Manual Acquisition
![depth pattern](public/images/manualAcq.png)

## Automatic Acquisition
![depth pattern](public/images/depthCameraAcq.png)

## dependencies
This project needs **libfreenect** on your computer to enter the microsoft kinect camera. If you are using a different camera you need to modify the file **src/ models/DataAcquisition.py** and ready, you can use the application.

## Project Setup
```
    pip install -r requirements.txt
```
## Run project
```
    python app.py
```

