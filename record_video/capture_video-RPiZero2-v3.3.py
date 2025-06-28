# Not tested
# Resolved: Misses 1 min when starting new video (not tested.)
# Added Black background to time text.
# Added graceful shut down. Ctrl+C (not tested)
# Added min_segment_seconds, do not record if video clip wil be 60 seconds long.

from picamera2 import MappedArray, Picamera2
from picamera2.encoders import H264Encoder, Quality
from libcamera import controls
from libcamera import Transform
import time
import os
from datetime import datetime, timedelta
import cv2
from math import ceil

import subprocess


SAVE_DIR = "recorded_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

# Optional. To safely stop systemd services (mediamtx.service, stream.service)
# Run python code as sudo.
def stop_services(services):
    for service in services:
        try:
            # Check status
            result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
            if result.stdout.strip() == "active":
                print(f"[INFO] Stopping service: {service}")
                subprocess.run(["sudo", "systemctl", "stop", service], check=True)
            else:
                print(f"[INFO] Service already stopped: {service}")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to manage {service}: {e}")


def record_video(segment_minutes=15, quality=Quality.MEDIUM, resolution=(1280, 720), fps=24, transform=Transform(vflip=0), min_segment_seconds=60):
    assert 1 <= segment_minutes <= 60, "segment_minutes must be between 1 and 60"

    picam2 = Picamera2()
    video_config = picam2.create_video_configuration(
        main={"size": resolution, "format": "YUV420"},
        controls={"FrameRate": fps} #,
        #transform=transform
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
            # Text size and background box
            (text_width, text_height), baseline = cv2.getTextSize(timestamp, font, scale, thickness)
            x, y = origin
            cv2.rectangle(
                m.array,
                (x - 2, y - text_height - 4),  # top-left corner of background box
                (x + text_width + 2, y + baseline + 2),  # bottom-right corner
                (0, 0, 0),  # black color
                thickness=-1  # filled rectangle
            )

            # Now draw the text over it
            cv2.putText(m.array, timestamp, (x, y), font, scale, colour, thickness, cv2.LINE_AA)

    picam2.pre_callback = apply_timestamp
    picam2.start()

    print(f"[INFO] Recording in segments of {segment_minutes} minutes")

    # Try-finally for graceful shutdown. # not tested
    try:
        while True:
            now = datetime.now()

            # Find the start of the current segment (e.g., 12:00 if now is 12:17)
            segment_start_minute = (now.minute // segment_minutes) * segment_minutes
            segment_start_time = now.replace(minute=segment_start_minute, second=0, microsecond=0)

            # Next segment starts exactly `segment_minutes` after current segment
            next_segment_time = segment_start_time + timedelta(minutes=segment_minutes)

            # Duration until next segment starts
            duration_seconds = (next_segment_time - now).total_seconds()

            ## If we're at/near the boundary, wait slightly longer than needed
            '''
            if duration_seconds < 1:
                wait_time = max(0.05, 1.1 - duration_seconds)
                time.sleep(wait_time)
                continue
            '''
            # If waiting gap more than 1 sec
            # If the remaining duration is less than 15 seconds, I want to wait until the next segment start.
            if duration_seconds < min_segment_seconds: #15 sec:
                wait_time = max(0, duration_seconds) + 0.5  # Ensures wait_time ≥ 0.5s
                print(f"[INFO] Waiting {wait_time:.2f}s to cross segment boundary...")
                time.sleep(wait_time)
                continue


            timestamp = now.strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4")
            print(f"[RECORDING] {filename} from {now.strftime('%H:%M:%S')} to {next_segment_time.strftime('%H:%M:%S')}")

            picam2.start_and_record_video(
                filename,
                quality=quality,
                config=video_config,
                duration=round(duration_seconds),  # ceil() avoids truncating a partial second. ceil() might over-record by ~1 second.
                show_preview=False,
                audio=False
            )
            print(f"[SAVED] {filename}")
    except KeyboardInterrupt:
        print("\n[INFO][KeyboardInterrupt] Stopping recording...")
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(60) ## Wait a min before retrying
    finally:
        picam2.stop()
        picam2.close()


if __name__ == "__main__":
    # Run script with sudo
    #stop_services(["mediamtx.service", "stream.service"])

    record_video(segment_minutes=30, fps=24)
