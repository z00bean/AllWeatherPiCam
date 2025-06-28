# Not tested

from picamera2 import MappedArray, Picamera2
from picamera2.encoders import H264Encoder, Quality
from libcamera import controls
from libcamera import Transform
import time
import os
from datetime import datetime, timedelta
import cv2
from math import ceil

SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

def record_video(segment_minutes=15, quality=Quality.MEDIUM, resolution=(1280, 720), fps=24, transform=Transform(vflip=0)):
    assert 1 <= segment_minutes <= 60, "segment_minutes must be between 1 and 60"

    picam2 = Picamera2()
    video_config = picam2.create_video_configuration(
        main={"size": resolution, "format": "YUV420"},
        controls={"FrameRate": fps}
    )
    picam2.configure(video_config)

    # Timestamp overlay settings
    colour = (255, 255, 255)
    origin = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    thickness = 1

    def apply_timestamp(request):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with MappedArray(request, "main") as m:
            cv2.putText(m.array, timestamp, origin, font, scale, colour, thickness, cv2.LINE_AA)

    picam2.pre_callback = apply_timestamp
    picam2.start()

    print(f"[INFO] Recording in segments of {segment_minutes} minutes")

    while True:
        now = datetime.now()
        minute = now.minute
        next_segment_minute = ceil(minute / segment_minutes) * segment_minutes

        if next_segment_minute >= 60:
            next_segment_time = (now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))
        else:
            next_segment_time = now.replace(minute=next_segment_minute, second=0, microsecond=0)

        duration_seconds = (next_segment_time - now).total_seconds()
        if duration_seconds < 1:
            # Very rare case (race condition near exact time rollover)
            time.sleep(1)
            continue

        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4")
        print(f"[RECORDING] {filename} for {duration_seconds:.2f} seconds")

        picam2.start_and_record_video(
            filename,
            quality=quality,
            config=video_config,
            duration=int(duration_seconds),
            show_preview=False,
            audio=False
        )

        print(f"[SAVED] {filename}")


if __name__ == "__main__":
    record_video(segment_minutes=30, fps=24)
