#DOES NOT WORK

'''
✔ Uses libcamera-vid's built-in --datetime (no need for OpenCV or manual frame processing).
✔ Efficient and optimized since libcamera-vid handles encoding.
✔ Saves in .mp4 format directly.
✔ Less CPU usage than processing frames with OpenCV.
'''
import os
import time
import subprocess
from datetime import datetime

# Ensure the recorded_clips folder exists
SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

def record_video(duration=60, resolution=(1280, 720), fps=24):
    # Generate output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4")

    # Construct the libcamera-vid command with datetime overlay
    cmd = [
        "libcamera-vid",
        "-t", str(duration * 1000),  # Convert duration to milliseconds
        "--width", str(resolution[0]),
        "--height", str(resolution[1]),
        "--framerate", str(fps),
        "--datetime",  # Enables timestamp overlay
        "-o", filename  # Output file
    ]

    print(f"Recording: {filename} with timestamp overlay")
    subprocess.run(cmd)  # Run the command

    print(f"Saved: {filename}")

if __name__ == "__main__":
    record_video(duration=60)
