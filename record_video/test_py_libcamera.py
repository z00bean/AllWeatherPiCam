# sudo apt install python3-picamera2 --no-install-recommends
# Picamera2 is the libcamera-based replacement for Picamera
# https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
'''
from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
#picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
'''
'''
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size":(1920,1080)})
picam2.start_and_record_video("test1.h264", quality=Quality.HIGH, config=video_config, duration=5, show_preview=True, audio=False)
'''

from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video("test-libcampy.mp4", duration=5)
