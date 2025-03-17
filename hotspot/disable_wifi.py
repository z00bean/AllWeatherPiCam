# disable_wifi.py
import time
import os

# Wait for 5 minutes (300 seconds)
time.sleep(300)

os.system("sudo systemctl stop mediamtx.service")

# Run the command to disable wlan0
os.system("sudo ip link set wlan0 down")