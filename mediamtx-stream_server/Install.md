# Install MediaMTX on Raspberry Pi Zero 2 W (32-bit Bullseye)

## Download and Extract
```
bash
wget https://github.com/bluenviron/mediamtx/releases/download/v1.11.3/mediamtx_v1.11.3_linux_armv6.tar.gz
tar -xvzf mediamtx_v1.11.3_linux_armv6.tar.gz
cd mediamtx_v1.11.3_linux_armv6
```


### Run MediaMTX
```
./mediamtx
```

### (Optional) Move Binary to /usr/local/bin for Global Access
```
sudo mv mediamtx /usr/local/bin/
mediamtx
```


### Edit the configuration file before running:
```
nano mediamtx.yml
```



## Arch Linux package
If you are running the Arch Linux distribution, run
```
git clone https://aur.archlinux.org/mediamtx.git
cd mediamtx
makepkg -si
```