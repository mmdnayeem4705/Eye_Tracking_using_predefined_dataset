# 👁️ Eye Tracking & Drowsiness Detection System

## 🚀 Project Overview

The **Eye Tracking & Drowsiness Detection System** is a real-time computer vision application that monitors a user's eye activity through a webcam. Using OpenCV and Haar Cascade Classifiers, the system detects faces and eyes continuously and provides audio alerts when eyes remain closed for an extended period.

This project is designed to enhance **driver safety**, **attention monitoring**, and **fatigue detection** by warning users before dangerous situations occur.

---

## ✨ Features

✅ Real-time face detection using Haar Cascade Classifier

✅ Continuous monitoring of eye status (Open/Closed)

✅ Automatic warning system for prolonged eye closure

✅ Multi-level alert mechanism

---

## 🛠️ Technologies Used

| Technology                  | Purpose                            |
| --------------------------- | ---------------------------------- |
| 🐍 Python                   | Core Programming Language          |
| 👁️ OpenCV                  | Computer Vision & Image Processing |
| 🎥 Webcam                   | Live Video Capture                 |
| 🔊 Winsound                 | Audio Alert System (Windows)       |
| 📊 Haar Cascade Classifiers | Face & Eye Detection               |

---

## 📁 Project Structure

```text
Eye-Tracking-System/
│
├── eye_detection_tracking.py
├── alert_sound.wav
├── beep_sound.wav
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
├── README.md
```

### 📄 File Description

#### 🐍 eye_detection_tracking.py

Main Python script responsible for:

* Capturing webcam feed
* Detecting faces
* Detecting eyes
* Monitoring eye closure duration
* Triggering warning alerts

#### 🔊 beep_sound.wav

Used for the warning levels.

#### 📚 haarcascade_frontalface_default.xml

Pre-trained model for face detection.
---

## ⚙️ How the System Works

### Step 1: Webcam Initialization 🎥

The system starts by accessing the user's webcam and capturing video frames in real time.

---

### Step 2: Face Detection 😊

Using the Haar Cascade Face Classifier:

* Faces are identified in every frame.
* Bounding rectangles are drawn around detected faces.

---

### Step 3: Eye Detection 👁️

Within each detected face:

* Eye regions are analyzed.
* Eyes are highlighted using rectangles.
* Eye count is monitored continuously.

---

### Step 4: Eye State Analysis 🧠

#### Eyes Open ✅

If two or more eyes are detected:

* User is considered alert.
* Warning timer resets.
* Audio alerts stop automatically.

#### Eyes Closed ⚠️

If no eyes are detected:

* Timer starts counting.
* Closure duration is monitored.

---

### Step 5: Warning System 🔔

If eyes remain closed for more than **15 seconds**:

#### Warning Level 1️⃣

🔊 Beep sound plays.

#### Warning Level 2️⃣

🔊 Beep sound repeats.

#### Warning Level 3️⃣

🔊 Beep sound repeats again.

#### Warning Level 4️⃣ and Beyond 🚨

An emergency alert sound is triggered:

```text
alert_sound.wav
```

This indicates a potentially dangerous level of drowsiness.

---

## 📊 Detection Flow

```text
Start Webcam
      │
      ▼
Detect Face
      │
      ▼
Detect Eyes
      │
      ├───────────────► Eyes Open ✅
      │                     │
      │                     ▼
      │               Reset Timer
      │
      ▼
Eyes Closed ❌
      │
      ▼
Count Duration
      │
      ▼
15 Seconds Passed?
      │
      ├── No ➜ Continue Monitoring
      │
      └── Yes ➜ Trigger Warning Alert 🔔
```

---

## 💻 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/eye-tracking-system.git
```

### 2️⃣ Navigate to Project

```bash
cd eye-tracking-system
```

### 3️⃣ Install Dependencies

```bash
pip install opencv-python
```

---

## ▶️ Run the Project

```bash
python eye_detection_tracking.py
```

---

## 🎯 Output

The application displays:

✅ Live webcam feed

✅ Face detection rectangles

✅ Eye detection rectangles

✅ Real-time eye tracking

✅ Audio warnings for prolonged eye closure

✅ Emergency alert system for repeated drowsiness

---

## 📸 Sample Output

```text
Face Detected 😊
Eyes Detected 👀

Status: ALERT ✅
```

When eyes remain closed:

```text
Status: DROWSINESS DETECTED ⚠️
Warning Level: 1️⃣
```

Critical stage:

```text
Status: EMERGENCY ALERT 🚨
Warning Level: 4️⃣
```

---

## 🎯 Applications

🚗 Driver Drowsiness Detection

🏭 Industrial Worker Monitoring

🎓 Student Attention Monitoring

🏥 Patient Observation Systems

🛡️ Workplace Safety Solutions

✈️ Transportation Safety Systems


## ⭐ Conclusion

This project demonstrates how Computer Vision and Artificial Intelligence can be used to improve road safety and attention monitoring through real-time eye tracking and drowsiness detection. The system provides instant feedback and multi-level alerts to help prevent accidents caused by fatigue and loss of attention.
