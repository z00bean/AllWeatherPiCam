# WORKS:
# Use this version
from picamera2 import MappedArray, Picamera2
from picamera2.encoders import H264Encoder, Quality
from libcamera import controls # for auto focus- fast focus
from libcamera import Transform
import time
import os
from datetime import datetime
import cv2

# Ensure the recorded_clips folder exists
SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

# resolution=(1280,720) # resolution = (1920, 1080)
def record_video(duration=60, quality = Quality.MEDIUM, resolution=(1280,720), fps=24, transform=Transform(vflip=1)):# resolution = (1920, 1080)): #Quality.HIGH
    picam2 = Picamera2()
    #picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})
    #video_config = picam2.create_video_configuration(main={"size": resolution})
    mode=picam2.sensor_modes[0]
    #sensor={'output_size': mode['size'],'bit_depth':mode['bit_depth']}
    video_config = picam2.create_video_configuration(main={"size": resolution,"format":"YUV420"},
                                                 #sensor=sensor,
                                                 controls={'FrameRate':fps})
    picam2.configure(video_config)

    colour = (255, 255, 255)
    origin = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    thickness = 1
    def apply_timestamp(request):
        timestamp = time.strftime("%Y-%m-%d %X")
        with MappedArray(request, "main") as m:
            cv2.putText(m.array, timestamp, origin, font, scale, colour, thickness, cv2.LINE_AA)

    picam2.pre_callback = apply_timestamp

    picam2.start()  # Start the camera

    while True:  # Infinite loop to keep recording
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4") #.h264") #h264 for method picam2.start_recording(encoder, filename)  

        print(f"Recording: {filename} at resolution {resolution}")
        
        video_config = picam2.create_video_configuration(main={"size":resolution})
        picam2.start_and_record_video(filename, quality=quality, config=video_config, duration=duration, show_preview=False, audio=False)

        print(f"Saved: {filename}")

if __name__ == "__main__":
    record_video(duration=1800, fps=24)  


'''
import time
import cv2
import os
from datetime import datetime
from picamera2 import MappedArray, Picamera2
from picamera2.encoders import H264Encoder

#WORKS- SLOW

SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())

color1 = (255, 255, 255)  # Green text
origin = (10, 30)  # Upper left corner
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.6
thickness = 2

def apply_timestamp(request):
    timestamp = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        #cv2.putText(m.array, timestamp, origin, font, scale, color1, thickness)
        cv2.putText(m.array, now, origin, cv2.FONT_HERSHEY_SIMPLEX, scale, color1, 1, cv2.LINE_AA)


picam2.pre_callback = apply_timestamp

encoder = H264Encoder(10000000)

try:
    while True:  # Continuous recording
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.h264")
        
        print(f"Recording: {filename}")
        picam2.start_recording(encoder, filename)
        time.sleep(60)  # Record for 60 seconds
        picam2.stop_recording()
        print(f"Saved: {filename}")

except KeyboardInterrupt:
    print("\nRecording stopped by user.")
    picam2.stop()
'''
