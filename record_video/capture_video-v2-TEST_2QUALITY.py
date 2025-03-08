from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from libcamera import controls  # for auto focus- fast focus
from libcamera import Transform
import time
import os
from datetime import datetime

# Ensure the recorded_clips folder exists
SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

def record_video(duration=120, resolution=(1280, 720), fps=24, transform=Transform(vflip=1)):
    picam2 = Picamera2()
    #spicam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})
    mode = picam2.sensor_modes[0]
    #sensor = {'output_size': mode['size'], 'bit_depth': mode['bit_depth']}
    
    picam2.configure(picam2.create_video_configuration(main={"size": resolution, "format": "YUV420"}, \
                                    #sensor=sensor, \
                                    controls={'FrameRate': fps}))
    picam2.start()
    
    quality = Quality.MEDIUM  # Start with MEDIUM quality
    
    while True:  # Infinite loop to keep recording
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        quality_str = "MEDIUM" if quality == Quality.MEDIUM else "HIGH"
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}_{quality_str}.mp4")

        print(f"Recording: {filename} at resolution {resolution} with quality {quality}")
        
        video_config = picam2.create_video_configuration(main={"size": resolution})
        picam2.start_and_record_video(filename, quality=quality, config=video_config, duration=duration, show_preview=False, audio=False)
        
        print(f"Saved: {filename}")
        
        # Toggle quality for the next clip
        quality = Quality.HIGH if quality == Quality.MEDIUM else Quality.MEDIUM

if __name__ == "__main__":
    record_video()
