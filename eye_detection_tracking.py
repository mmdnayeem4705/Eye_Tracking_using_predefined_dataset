import cv2
import winsound  # For beep sound, specific to Windows
import time

# Initialize the classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Open the webcam capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Eye-closed detection variables
eyes_closed = False
beep_playing = False
alert_playing = False
closed_start_time = None
warning_count = 0
EYES_CLOSED_THRESHOLD = 15  # seconds (updated as per requirement)
EYES_OPEN_RESET_THRESHOLD = 3  # seconds

last_eyes_open_time = time.time()
event_registered = False  # To ensure only one count per closed-eyes event

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    eyes_detected = False

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # Detect eyes in the region of interest (ROI)
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            eyes_detected = True
            # Draw rectangles around detected eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    current_time = time.time()

    if eyes_detected:
        # Eyes are open, reset timers and stop sounds if needed
        if beep_playing or alert_playing:
            winsound.PlaySound(None, winsound.SND_ASYNC)
            beep_playing = False
            alert_playing = False
        closed_start_time = None
        event_registered = False
        last_eyes_open_time = current_time
        # Reset warning count if eyes have been open for a while
        if warning_count > 0 and (current_time - last_eyes_open_time) > EYES_OPEN_RESET_THRESHOLD:
            warning_count = 0
    else:
        # Eyes are closed
        if closed_start_time is None:
            closed_start_time = current_time
            event_registered = False
        closed_duration = current_time - closed_start_time
        if closed_duration >= EYES_CLOSED_THRESHOLD and not event_registered:
            warning_count += 1
            event_registered = True
            if warning_count < 4:
                if not beep_playing:
                    winsound.PlaySound("beep_sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                    beep_playing = True
                    alert_playing = False
            else:
                if not alert_playing:
                    winsound.PlaySound("alert_sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                    alert_playing = True
                    beep_playing = False

    # Display the real-time output with face and eye tracking
    cv2.imshow('Eye Tracking', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()