# Raspberry Pi Zero 2W Camera Setup – Arducam IMX462

This guide provides step-by-step instructions for setting up the Arducam IMX462 camera on a Raspberry Pi Zero 2W, using libcamera and V4L2 tools.

## Prerequisites
- Raspberry Pi Zero 2W (or other compatible Raspberry Pi models)
- Arducam IMX462 camera module
- Raspberry Pi OS (Bullseye 6.1.21+ or Bookworm)
- Internet connection for installation

## Installation Steps

### 1. Install Required Packages

#### Step 1: Download the Arducam Installation Script
```
wget -O install_pivariety_pkgs.sh https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/releases/download/install_script/install_pivariety_pkgs.sh
```
```
chmod +x install_pivariety_pkgs.sh  
```

#### Step 2: Install libcamera
```
./install_pivariety_pkgs.sh -p libcamera_dev
```

#### Step 3: Install libcamera-apps
```
./install_pivariety_pkgs.sh -p libcamera_apps
```

## 2. Modify Configuration Files

### For Raspberry Pi 5 (Bookworm OS)
Edit the configuration file:  
sudo nano /boot/firmware/config.txt  

Add the following line under [all]:  
```
dtoverlay=arducam-pivariety
```

Save and reboot:  
```
sudo reboot
```

To enable the camera on cam0 port (Pi 5 only), modify the config:  
dtoverlay=arducam-pivariety,cam0  

### For Raspberry Pi 4 (Bookworm OS)
sudo nano /boot/firmware/config.txt  
dtoverlay=arducam-pivariety  
Save and reboot.  

### For Raspberry Pi 4 (Bullseye OS 6.1.21 and Later)
sudo nano /boot/config.txt  
dtoverlay=arducam-pivariety  
Save and reboot.  

## Using libcamera to Capture Images

### Preview Camera Output (10 Seconds)
```
libcamera-still -t 10000
```

### Capture an Image Without Display
```
libcamera-still -t 10000 -n -o test.jpg
```
test.jpg will be saved in the current directory.  

## Using V4L2 Tools for Manual Control

### 1. Modify Config File
sudo nano /boot/config.txt  

Add this line at the end of the file:  
dtoverlay=arducam-pivariety,media-controller=0  

Save and reboot:  
sudo reboot  

### 2. Check Camera Node
ls /dev/video*  

### 3. List Available Formats and Controls
v4l2-ctl --list-formats-ext  
v4l2-ctl -l  

### 4. Capture Data

#### Test Frame Rate
v4l2-ctl --set-fmt-video=width=1920,height=1080,pixelformat='GREY' --stream-mmap  

#### Save a Single Frame
v4l2-ctl --device /dev/video0 --set-fmt-video=width=1920,height=1080,pixelformat='Y10P' --stream-mmap --stream-to=frame.raw --stream-count=1  

#### Adjust Exposure and Gain
v4l2-ctl --device /dev/video0 -c exposure=1000 -c analogue_gain=200 --set-fmt-video=width=1920,height=1080,pixelformat='Y10P' --stream-mmap --stream-to=frame.raw --stream-count=1  

## Summary
This guide walks you through setting up the Arducam IMX462 on a Raspberry Pi Zero 2W, configuring the necessary drivers, and capturing images using libcamera and V4L2.  

For more details, refer to the official Arducam Documentation:  
https://docs.arducam.com/Raspberry-Pi-Camera/Pivariety-Camera/Quick-Start-Guide/  
