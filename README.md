Project Title: Eye Tracking Using Predefined Dataset

Project Structure:
- eye_detection_tracking.py: Main Python script for real-time face and eye detection and alerting.
- alert_sound.mp3: Sound file used for alerting when eyes are closed for a long period.
- README.md: Basic project description and usage.
- (Requires haarcascade_frontalface_default.xml and haarcascade_eye.xml for detection.)

How It Works:
1. The script uses OpenCV to access the webcam and detect faces and eyes in real time.
2. It loads pre-trained Haar cascade classifiers for face and eye detection.
3. For each frame from the webcam:
   - Faces are detected and highlighted with rectangles.
   - Within each detected face, eyes are detected and highlighted.
   - If two or more eyes are detected, the system considers the eyes open.
   - If no eyes are detected for a continuous period (default 15 seconds), it triggers a warning.
   - The first three warnings play a looping beep sound ("beep_sound.wav").
   - On the fourth warning and beyond, a more urgent alert sound ("alert_sound.wav") is played.
   - When eyes are reopened, the sound stops and the warning count can reset after a period.

Final Output:
- A real-time video window showing the webcam feed with rectangles around detected faces and eyes.
- Audio alerts (beep or alert sound) play if eyes are closed for too long.
- The program can be exited by pressing 'q'.

Requirements:
- Python with OpenCV (`cv2`) and winsound (Windows only).
- Haar cascade XML files for face and eye detection.
- Sound files: "beep_sound.wav" and "alert_sound.wav" in the same directory.

This project demonstrates a simple drowsiness or attention monitoring system using computer vision and
