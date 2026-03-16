# Simple Vision Recorder: A Functional Tool for Real-Time Monitoring

This repository provides a functional video recording application using OpenCV. It is designed for monitoring RTSP streams with interactive features to enhance visual analysis.

---

## Features

* **Interactive Zoom**: Step-by-step digital zoom (1.0x to 5.0x) using Z/X keys.
* **ROI Navigation**: Real-time movement within the zoomed area using WASD keys.
* **Live Tuning**: On-the-fly brightness adjustment (B/N keys) for optimized visibility.
* **Recording UI**: Dedicated monitoring interface with a "REC" status indicator and telemetry dashboard.
* **Stability Fix**: Fixed 20.0 FPS and DIVX codec integration to resolve MPEG-4 timebase standard issues.

---

## Controls

| Key | Function | Detail |
| :--- | :--- | :--- |
| **Space** | **Record** | Toggles recording on/off |
| **W / A / S / D** | **Navigate** | Shifts the focus area while zoomed |
| **Z / X** | **Zoom** | Adjusts zoom level (0.5x increments) |
| **B / N** | **Exposure** | Increases or decreases brightness |
| **ESC** | **Quit** | Saves files and exits the program safely |

---

## Preview
<p align="center">
  <img src="./output.gif" width="600">
  <br>
  <em><strong>Demonstration</strong>: Dynamic ROI navigation and zoom control during a recording session.</em>
</p>

---

## Output

* **File Format**: `.avi` (DIVX Codec)
* **Frame Rate**: Fixed at 20.0 FPS for file stability.
* **Recording Mode**: "Clean Capture" logic is applied (UI elements are excluded from the saved video).
* **Storage Path**: Recordings are saved as `output.avi` in the project root directory.
