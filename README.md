# 🚨 theftdetection - Gesture-Based Theft Detection System

**theftdetection** is a Python-based system for detecting suspicious gestures in video footage, built as a computer science project. Leveraging MediaPipe’s Pose estimation and OpenCV, it tracks body landmarks (wrists, hips) to identify potential theft behaviors, like hands nearing the torso. It computes real-time confidence scores for suspicious vs. normal actions, making it a robust tool for security analysis. 🌟

## 📋 Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- 📹 **Video Analysis**: Processes video input (e.g., `shoplifting_clip.mp4`) to detect gestures.
- 🕺 **Pose Tracking**: Identifies key landmarks (wrists, hips) with MediaPipe Pose.
- 🚨 **Gesture Detection**: Flags suspicious actions based on hand-to-torso proximity.
- 📊 **Confidence Scores**: Calculates suspicious/normal confidence using distance metrics.
- 🎨 **Visual Feedback**: Overlays landmarks and labels (e.g., “Suspicious: 82.50%”) on frames.
- 🛠️ **Flexible Setup**: Supports video files or webcam input with easy configuration.

## 🛠️ Technologies
```yaml
Core:
  - Python: 3.8+ 🐍
  - OpenCV: ^4.8.0 📷
  - MediaPipe: ^0.10.0 🤖
  - NumPy: ^1.24.0 🔢
Tools:
  - Git: Version control 🔗
  - VS Code: IDE 💻
Environment:
  - pip: Package manager 📦
Planned:
  - YOLO: Item detection integration 🎯
  - Flask: Web-based monitoring UI 🌐
