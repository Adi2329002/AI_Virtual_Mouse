# 🖱️ AI Virtual Mouse  
### ✋ Gesture-Based Real-Time Mouse Control using Computer Vision  

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-orange)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)


---

## 📌 Overview

**AI Virtual Mouse** is a real-time gesture-based human-computer interaction system that allows users to control their mouse pointer using hand gestures captured via webcam.

Built using **OpenCV**, **MediaPipe**, and **PyAutoGUI**, this project demonstrates real-time computer vision processing, gesture recognition, coordinate mapping, and OS-level input simulation.

---

## 🎥 Demo

> ✋ Move your index finger → Cursor moves  
> 🤏 Pinch (Thumb + Index) → Left click  
> 🤌 Thumb + Middle → Right click  
> ✊ Hold pinch → Drag  

---

## 🧠 How It Works

Webcam Frame
↓
MediaPipe Hand Landmark Detection
↓
Gesture Recognition Logic
↓
Screen Coordinate Mapping
↓
OS-Level Mouse Control


---

## 🏗️ Project Architecture
```
ai-virtual-mouse/
│
├── src/
│ ├── main.py
│ ├── config.py
│ │
│ ├── core/
│ │ ├── hand_tracker.py
│ │ ├── mouse_controller.py
│ │ └── gesture_detector.py
│
├── requirements.txt
└── README.md

```
---

## ✨ Features

### 🎯 Core Features
- Real-time hand detection
- Index finger tracking
- Smooth mouse movement
- Left click gesture
- Right click gesture
- Drag & drop gesture
- FPS display
- Modular architecture

### ⚙️ Engineering Features
- Config-driven parameters
- Object-oriented design
- Clean separation of concerns
- Performance monitoring
- Reproducible dependency management

---

## 🖥️ Tech Stack

| Technology | Purpose |
|------------|----------|
| **OpenCV** | Frame capture & rendering |
| **MediaPipe** | Hand landmark detection |
| **PyAutoGUI** | OS-level mouse control |
| **NumPy** | Image processing support |

---

## 🧩 Gesture Mapping

| Gesture | Action |
|---------|--------|
| ✋ Index finger movement | Cursor move |
| 🤏 Thumb + Index | Left click |
| 🤌 Thumb + Middle | Right click |
| ✊ Hold pinch | Drag |

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-virtual-mouse.git
cd ai-virtual-mouse

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python -m src.main

```
opencv-python==4.9.0.80
mediapipe==0.10.9
pyautogui==0.9.54
numpy==1.26.4


⚡ Performance

- Real-time FPS monitoring

- Smoothing algorithm for stable cursor control

- Optimized single-hand detection


🧠 Computer Vision Concepts Used

- Landmark detection

- Coordinate normalization

- Euclidean distance calculation

- Frame transformation

- Real-time smoothing interpolation

- Gesture thresholding

📊 FPS Calculation
fps = 1 / (current_time - prev_time)
Displayed in real-time on screen.

🎓 Academic Value

- This project demonstrates:

- Applied Computer Vision

- Human-Computer Interaction

- Real-time System Design

- Modular Software Architecture

- Clean Code Practices

- Performance Engineering

🔮 Future Improvements

- Scroll gesture

- Zoom gesture

- Multi-hand support

- Customizable gesture sensitivity

- GUI control panel

- Cross-platform optimization

- Machine-learning based gesture classifier


👨‍💻 Author

Aditya Alok
B.Tech CSE
Advanced Programming Lab Project


⭐ If You Like This Project

Give it a ⭐ on GitHub!
