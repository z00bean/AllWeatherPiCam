# Video Recording Script for Raspberry Pi Zero 2 W  

**📌 Work in Progress** – This script is part of an ongoing project to develop a reliable, all-weather, long-term video recording system using the **Raspberry Pi Zero 2 W**.  

## Overview  
This script allows **continuous video recording** with **timestamp overlay**, optimized for low-power operation and storage management. The code leverages **Picamera2** for efficient video capture and supports different resolutions, frame rates, and encoding settings.  

## Features  
- 🎥 **Automatic Continuous Recording** – Captures and saves clips sequentially.  
- ⏳ **Customizable Recording Duration** – Adjustable recording time per clip.  
- 🕒 **Timestamp Overlay** – Embeds real-time timestamps directly into the video.  
- ⚡ **Optimized for Low Power** – Designed for long-term outdoor recording.  
- 📁 **Automatic File Management** – Saves recordings to the `recorded_clips/` directory.  

## Usage  
To start recording, run:  
```bash
python capture_video-RPiZero2-v3.1.2.py```

By default, the script records 30-minute clips (1800 seconds) at 24 FPS. You can modify parameters such as duration, resolution, and frame rate in the record_video() function.

Notes

- This script is continuously evolving as we refine the recording process.
- It is part of a larger project, integrating multiple scripts and hardware optimizations.
- Picamera2 and libcamera are required for this implementation.
