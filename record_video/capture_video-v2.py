# to do: save as mp4 to reduce size of videos
# https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
# ffmpeg output
# fps 

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from libcamera import controls # for auto focus- fast focus
from libcamera import Transform
import time
import os
from datetime import datetime

# Ensure the recorded_clips folder exists
SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

# resolution=(1280,720) # resolution = (1920, 1080)
def record_video(duration=120, quality = Quality.MEDIUM, resolution=(1280,720), fps=24, transform=Transform(vflip=1)):# resolution = (1920, 1080)): #Quality.HIGH
    picam2 = Picamera2()
    #picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast}) # RPi camera module3 only
    #video_config = picam2.create_video_configuration(main={"size": resolution})
    mode=picam2.sensor_modes[0]
    #sensor={'output_size': mode['size'],'bit_depth':mode['bit_depth']}
    video_config = picam2.create_video_configuration(main={"size": resolution,"format":"YUV420"},
                                                 #sensor=sensor,
                                                 controls={'FrameRate':fps})
    picam2.configure(video_config)

    picam2.start()  # Start the camera

    while True:  # Infinite loop to keep recording
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4") #.h264") #h264 for method picam2.start_recording(encoder, filename)  

        print(f"Recording: {filename} at resolution {resolution}")
        
        '''
        # WORKS
        encoder = H264Encoder(bitrate=10000000)  # Define H.264 encoder
        picam2.start_recording(encoder, filename)  
        time.sleep(duration)  # Record for the given duration
        picam2.stop_recording()
        '''
        video_config = picam2.create_video_configuration(main={"size":resolution})
        picam2.start_and_record_video(filename, quality=quality, config=video_config, duration=duration, show_preview=False, audio=False)

        print(f"Saved: {filename}")

if __name__ == "__main__":
    record_video()  
