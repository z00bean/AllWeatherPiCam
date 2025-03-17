sudo nano /etc/systemd/system/start_recording.service

sudo systemctl enable start_recording.service
sudo systemctl start start_recording.service




Stop the Service (Immediate):
sudo systemctl stop start_recording.service


Disable the Service (Prevent Running on Boot):
sudo systemctl disable start_recording.service


Remove the Service Permanently:
sudo systemctl disable start_recording.service
sudo rm /etc/systemd/system/start_recording.service
sudo systemctl daemon-reload
