# Face Recognition and Aadhaar Details Retrieval

## Overview

This project uses the `face_recognition` library along with `OpenCV` to detect and recognize faces from a webcam feed. Recognized faces are associated with Aadhaar details. Additionally, unknown faces can be registered with new Aadhaar details and stored for future recognition.

## Features

- **Face Detection and Recognition**: Recognizes faces from a webcam feed.
- **Aadhaar Details Retrieval**: Displays Aadhaar details for recognized faces.
- **New Face Registration**: Allows registering new faces with Aadhaar details via dialog boxes.
- **Data Storage**: Saves new face images and details in a CSV file and a directory.
- 
## Code Explanation

The code is divided into several sections:

### Initial Setup
- Load and encode known face images.
- Define Aadhaar details for these faces.

### Video Capture
- Capture video from the webcam using `cv2.VideoCapture(0)`.
- Process each frame to detect faces and compare them with known faces.

### Face Recognition
- For recognized faces, display their Aadhaar details.
- For unknown faces, prompt the user to register them with a name and Aadhaar details.

### Registering New Faces
- Save the new face image and Aadhaar details.
- Append the new face data to a CSV file `registered_faces_data.csv`.

### Running the Application
- To start the application, simply run the script. Press 'q' to quit the webcam feed.

