import cv2
import winsound  # For beep sound, specific to Windows

# Initialize the classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Open the webcam capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Eye-closed detection variables
eyes_closed = False
beep_playing = False  # Flag to track if beep is playing

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # Detect eyes in the region of interest (ROI)
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) < 2:  # Both eyes are closed
            if not beep_playing:
                # Start beep sound when eyes are closed
                winsound.PlaySound("beep_sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                beep_playing = True  # Set beep playing flag to true
        else:
            if beep_playing:
                # Stop the beep sound when eyes are open
                winsound.PlaySound(None, winsound.SND_ASYNC)
                beep_playing = False  # Reset beep playing flag

        # Draw rectangles around detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the real-time output with face and eye tracking
    cv2.imshow('Eye Tracking', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()