_MediaMTX_ is a ready-to-use and zero-dependency real-time media server and media proxy that allows to publish, read, proxy, record and playback video and audio streams. It has been conceived as a "media router" that routes media streams from one end to the other.

Live streams can be published to the server with:

|protocol|variants|video codecs|audio codecs|
|--------|--------|------------|------------|
|[SRT clients](#srt-clients)||H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3|
|[SRT cameras and servers](#srt-cameras-and-servers)||H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3|
|[WebRTC clients](#webrtc-clients)|WHIP|AV1, VP9, VP8, [H265](#supported-browsers), H264|Opus, G722, G711 (PCMA, PCMU)|
|[WebRTC servers](#webrtc-servers)|WHEP|AV1, VP9, VP8, [H265](#supported-browsers), H264|Opus, G722, G711 (PCMA, PCMU)|
|[RTSP clients](#rtsp-clients)|UDP, TCP, RTSPS|AV1, VP9, VP8, H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video, M-JPEG and any RTP-compatible codec|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G726, G722, G711 (PCMA, PCMU), LPCM and any RTP-compatible codec|
|[RTSP cameras and servers](#rtsp-cameras-and-servers)|UDP, UDP-Multicast, TCP, RTSPS|AV1, VP9, VP8, H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video, M-JPEG and any RTP-compatible codec|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G726, G722, G711 (PCMA, PCMU), LPCM and any RTP-compatible codec|
|[RTMP clients](#rtmp-clients)|RTMP, RTMPS, Enhanced RTMP|AV1, VP9, H265, H264|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G711 (PCMA, PCMU), LPCM|
|[RTMP cameras and servers](#rtmp-cameras-and-servers)|RTMP, RTMPS, Enhanced RTMP|AV1, VP9, H265, H264|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G711 (PCMA, PCMU), LPCM|
|[HLS cameras and servers](#hls-cameras-and-servers)|Low-Latency HLS, MP4-based HLS, legacy HLS|AV1, VP9, [H265](#supported-browsers-1), H264|Opus, MPEG-4 Audio (AAC)|
|[UDP/MPEG-TS](#udpmpeg-ts)|Unicast, broadcast, multicast|H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3|
|[Raspberry Pi Cameras](#raspberry-pi-cameras)||H264||

Live streams can be read from the server with:

|protocol|variants|video codecs|audio codecs|
|--------|--------|------------|------------|
|[SRT](#srt)||H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3|
|[WebRTC](#webrtc)|WHEP|AV1, VP9, VP8, [H265](#supported-browsers), H264|Opus, G722, G711 (PCMA, PCMU)|
|[RTSP](#rtsp)|UDP, UDP-Multicast, TCP, RTSPS|AV1, VP9, VP8, H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video, M-JPEG and any RTP-compatible codec|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G726, G722, G711 (PCMA, PCMU), LPCM and any RTP-compatible codec|
|[RTMP](#rtmp)|RTMP, RTMPS, Enhanced RTMP|H264|MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3)|
|[HLS](#hls)|Low-Latency HLS, MP4-based HLS, legacy HLS|AV1, VP9, [H265](#supported-browsers-1), H264|Opus, MPEG-4 Audio (AAC)|

Live streams be recorded and played back with:

|format|video codecs|audio codecs|
|------|------------|------------|
|[fMP4](#record-streams-to-disk)|AV1, VP9, H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video, M-JPEG|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3, G711 (PCMA, PCMU), LPCM|
|[MPEG-TS](#record-streams-to-disk)|H265, H264, MPEG-4 Video (H263, Xvid), MPEG-1/2 Video|Opus, MPEG-4 Audio (AAC), MPEG-1/2 Audio (MP3), AC-3|

**Features**

* Publish live streams to the server
* Read live streams from the server
* Streams are automatically converted from a protocol to another
* Serve multiple streams at once in separate paths
* Record streams to disk
* Playback recorded streams
* Authenticate users
* Redirect readers to other RTSP servers (load balancing)
* Control the server through the Control API
* Reload the configuration without disconnecting existing clients (hot reloading)
* Read Prometheus-compatible metrics
* Run hooks (external commands) when clients connect, disconnect, read or publish streams
* Compatible with Linux, Windows and macOS, does not require any dependency or interpreter, it's a single executable

**Note about rtsp-simple-server**

_rtsp-simple-server_ has been rebranded as _MediaMTX_. The reason is pretty obvious: this project started as a RTSP server but has evolved into a much more versatile product that is not tied to the RTSP protocol anymore. Nothing will change regarding license, features and backward compatibility.

## Table of contents

* [Installation](#installation)
  * [Standalone binary](#standalone-binary)
  * [Docker image](#docker-image)
  * [Arch Linux package](#arch-linux-package)
  * [OpenWrt binary](#openwrt-binary)
* [Basic usage](#basic-usage)
* [Publish to the server](#publish-to-the-server)
  * [By software](#by-software)
    * [FFmpeg](#ffmpeg)
    * [GStreamer](#gstreamer)
    * [OBS Studio](#obs-studio)
    * [OpenCV](#opencv)
    * [Unity](#unity)
    * [Web browsers](#web-browsers)
  * [By device](#by-device)
    * [Generic webcam](#generic-webcam)
    * [Raspberry Pi Cameras](#raspberry-pi-cameras)
  * [By protocol](#by-protocol)
    * [SRT clients](#srt-clients)
    * [SRT cameras and servers](#srt-cameras-and-servers)
    * [WebRTC clients](#webrtc-clients)
    * [WebRTC servers](#webrtc-servers)
    * [RTSP clients](#rtsp-clients)
    * [RTSP cameras and servers](#rtsp-cameras-and-servers)
    * [RTMP clients](#rtmp-clients)
    * [RTMP cameras and servers](#rtmp-cameras-and-servers)
    * [HLS cameras and servers](#hls-cameras-and-servers)
    * [UDP/MPEG-TS](#udpmpeg-ts)
* [Read from the server](#read-from-the-server)
  * [By software](#by-software-1)
    * [FFmpeg](#ffmpeg-1)
    * [GStreamer](#gstreamer-1)
    * [VLC](#vlc)
    * [Unity](#unity-1)
    * [Web browsers](#web-browsers-1)
  * [By protocol](#by-protocol-1)
    * [SRT](#srt)
    * [WebRTC](#webrtc)
    * [RTSP](#rtsp)
    * [RTMP](#rtmp)
    * [HLS](#hls)
* [Other features](#other-features)
  * [Configuration](#configuration)
  * [Authentication](#authentication)
    * [Internal](#internal)
    * [HTTP-based](#http-based)
    * [JWT-based](#jwt-based)
  * [Encrypt the configuration](#encrypt-the-configuration)
  * [Remuxing, re-encoding, compression](#remuxing-re-encoding-compression)
  * [Record streams to disk](#record-streams-to-disk)
  * [Playback recorded streams](#playback-recorded-streams)
  * [Forward streams to other servers](#forward-streams-to-other-servers)
  * [Proxy requests to other servers](#proxy-requests-to-other-servers)
  * [On-demand publishing](#on-demand-publishing)
  * [Expose the server in a subfolder](#expose-the-server-in-a-subfolder)
  * [Start on boot](#start-on-boot)
    * [Linux](#linux)
    * [OpenWrt](#openwrt)
    * [Windows](#windows)
  * [Hooks](#hooks)
  * [Control API](#control-api)
  * [Metrics](#metrics)
  * [pprof](#pprof)
  * [SRT-specific features](#srt-specific-features)
    * [Standard stream ID syntax](#standard-stream-id-syntax)
  * [WebRTC-specific features](#webrtc-specific-features)
    * [Authenticating with WHIP/WHEP](#authenticating-with-whipwhep)
    * [Solving WebRTC connectivity issues](#solving-webrtc-connectivity-issues)
    * [Supported browsers](#supported-browsers)
  * [HLS-specific features](#hls-specific-features)
    * [Supported browsers](#supported-browsers-1)
  * [RTSP-specific features](#rtsp-specific-features)
    * [Transport protocols](#transport-protocols)
    * [Encryption](#encryption)
    * [Corrupted frames](#corrupted-frames)
  * [RTMP-specific features](#rtmp-specific-features)
    * [Encryption](#encryption-1)
* [Compile from source](#compile-from-source)
  * [Standard](#standard)
  * [OpenWrt](#openwrt-1)
  * [Custom libcamera](#custom-libcamera)
  * [Cross compile](#cross-compile)
  * [Compile for all supported platforms](#compile-for-all-supported-platforms)
* [License](#license)
* [Specifications](#specifications)
* [Related projects](#related-projects)

## Installation

There are several installation methods available: standalone binary, Docker image, Arch Linux package and OpenWrt binary.

### Standalone binary

1. Download and extract a standalone binary from the [release page](https://github.com/bluenviron/mediamtx/releases) that corresponds to your operating system and architecture.

2. Start the server:

   ```sh
   ./mediamtx
   ```

### Docker image

Download and launch the image:

```
docker run --rm -it --network=host bluenviron/mediamtx:latest
```

Available images:

|name|FFmpeg included|RPI Camera support|
|----|---------------|------------------|
|bluenviron/mediamtx:latest|:x:|:x:|
|bluenviron/mediamtx:latest-ffmpeg|:heavy_check_mark:|:x:|
|bluenviron/mediamtx:latest-rpi|:x:|:heavy_check_mark:|
|bluenviron/mediamtx:latest-ffmpeg-rpi|:heavy_check_mark:|:heavy_check_mark:|

The `--network=host` flag is mandatory for RTSP to work, since Docker can change the source port of UDP packets for routing reasons, and this doesn't allow the server to identify the senders of the packets.

If the `--network=host` cannot be used (for instance, it is not compatible with Windows or Kubernetes), you can disable the RTSP UDP transport protocol, add the server IP to `MTX_WEBRTCADDITIONALHOSTS` and expose ports manually:

```
docker run --rm -it \
-e MTX_RTSPTRANSPORTS=tcp \
-e MTX_WEBRTCADDITIONALHOSTS=192.168.x.x \
-p 8554:8554 \
-p 1935:1935 \
-p 8888:8888 \
-p 8889:8889 \
-p 8890:8890/udp \
-p 8189:8189/udp \
bluenviron/mediamtx
```

### Arch Linux package

If you are running the Arch Linux distribution, run:

```sh
git clone https://aur.archlinux.org/mediamtx.git
cd mediamtx
makepkg -si
```

### OpenWrt binary

If the architecture of the OpenWrt device is amd64, armv6, armv7 or arm64, use the [standalone binary method](#standalone-binary) and download a Linux binary that corresponds to your architecture.

Otherwise, [compile the server from source](#openwrt-1).

## Basic usage

1. Publish a stream. For instance, you can publish a video/audio file with _FFmpeg_:

   ```sh
   ffmpeg -re -stream_loop -1 -i file.ts -c copy -f rtsp rtsp://localhost:8554/mystream
   ```

   or _GStreamer_:

   ```sh
   gst-launch-1.0 rtspclientsink name=s location=rtsp://localhost:8554/mystream filesrc location=file.mp4 \
   ! qtdemux name=d d.video_0 ! queue ! s.sink_0 d.audio_0 ! queue ! s.sink_1
   ```

2. Open the stream. For instance, you can open the stream with _VLC_:

   ```sh
   vlc --network-caching=50 rtsp://localhost:8554/mystream
   ```

   or _GStreamer_:

   ```sh
   gst-play-1.0 rtsp://localhost:8554/mystream
   ```

   or _FFmpeg_:

   ```sh
   ffmpeg -i rtsp://localhost:8554/mystream -c copy output.mp4
   ```

## Publish to the server

### By software

#### FFmpeg

FFmpeg can publish a stream to the server in multiple ways (SRT client, SRT server, RTSP client, RTMP client, UDP/MPEG-TS, WebRTC with WHIP). The recommended one consists in publishing as a [RTSP client](#rtsp-clients):

```
ffmpeg -re -stream_loop -1 -i file.ts -c copy -f rtsp rtsp://localhost:8554/mystream
```

The RTSP protocol supports multiple underlying transport protocols, each with its own characteristics (see [RTSP-specific features](#rtsp-specific-features)). You can set the transport protocol by using the `rtsp_transport` flag, for instance, in order to use TCP:

```sh
ffmpeg -re -stream_loop -1 -i file.ts -c copy -f rtsp -rtsp_transport tcp rtsp://localhost:8554/mystream
```

The resulting stream will be available in path `/mystream`.

#### GStreamer

GStreamer can publish a stream to the server in multiple ways (SRT client, SRT server, RTSP client, RTMP client, UDP/MPEG-TS, WebRTC with WHIP). The recommended one consists in publishing as a [RTSP client](#rtsp-clients):

```sh
gst-launch-1.0 rtspclientsink name=s location=rtsp://localhost:8554/mystream \
filesrc location=file.mp4 ! qtdemux name=d \
d.video_0 ! queue ! s.sink_0 \
d.audio_0 ! queue ! s.sink_1
```

If the stream is video only:

```sh
gst-launch-1.0 filesrc location=file.mp4 ! qtdemux name=d \
d.video_0 ! rtspclientsink location=rtsp://localhost:8554/mystream
```

The RTSP protocol supports multiple underlying transport protocols, each with its own characteristics (see [RTSP-specific features](#rtsp-specific-features)). You can set the transport protocol by using the `protocols` flag:

```sh
gst-launch-1.0 filesrc location=file.mp4 ! qtdemux name=d \
d.video_0 ! rtspclientsink protocols=tcp name=s location=rtsp://localhost:8554/mystream
```

The resulting stream will be available in path `/mystream`.

GStreamer can also publish a stream by using the [WebRTC / WHIP protocol](#webrtc). Make sure that GStreamer version is at least 1.22, and that if the codec is H264, the profile is baseline. Use the `whipclientsink` element:

```
gst-launch-1.0 videotestsrc \
! video/x-raw,width=1920,height=1080,format=I420 \
! x264enc speed-preset=ultrafast bitrate=2000 \
! video/x-h264,profile=baseline \
! whipclientsink signaller::whip-endpoint=http://localhost:8889/mystream/whip
```

#### OBS Studio

OBS Studio can publish to the server in multiple ways (SRT client, RTMP client, WebRTC client). The recommended one consists in publishing as a [RTMP client](#rtmp-clients). In `Settings -> Stream` (or in the Auto-configuration Wizard), use the following parameters:

* Service: `Custom...`
* Server: `rtmp://localhost`
* Stream key: `mystream`

If credentials are in use, use the following parameters:

* Service: `Custom...`
* Server: `rtmp://localhost`
* Stream key: `mystream?user=myuser&pass=mypass`

Save the configuration and click `Start streaming`.

If you want to generate a stream that can be read with WebRTC, open `Settings -> Output -> Recording` and use the following parameters:

* FFmpeg output type: `Output to URL`
* File path or URL: `rtsp://localhost:8554/mystream`
* Container format: `rtsp`
* Check `show all codecs (even if potentically incompatible)`
* Video encoder: `h264_nvenc (libx264)`
* Video encoder settings (if any): `bf=0`
* Audio track: `1`
* Audio encoder: `libopus`

Then use the button `Start Recording` (instead of `Start Streaming`) to start streaming.

Latest versions of OBS Studio can publish to the server with the [WebRTC / WHIP protocol](#webrtc). Use the following parameters:

* Service: `WHIP`
* Server: `http://localhost:8889/mystream/whip`
* Bearer Token: `myuser:mypass` (if internal authentication is enabled) or JWT (if JWT-based authentication is enabled)

Save the configuration and click `Start streaming`.

The resulting stream will be available in path `/mystream`.

#### OpenCV

Software which uses the OpenCV library can publish to the server through its GStreamer plugin, as a [RTSP client](#rtsp-clients). It must be compiled with GStreamer support, by following this procedure:

```sh
sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-ugly gstreamer1.0-rtsp python3-dev python3-numpy
git clone --depth=1 -b 4.5.4 https://github.com/opencv/opencv
cd opencv
mkdir build && cd build
cmake -D CMAKE_INSTALL_PREFIX=/usr -D WITH_GSTREAMER=ON ..
make -j$(nproc)
sudo make install
```

You can check that OpenCV has been installed correctly by running:

```sh
python3 -c 'import cv2; print(cv2.getBuildInformation())'
```

Check that the output contains `GStreamer: YES`.

Videos can be published with `cv2.VideoWriter`:

```python
from datetime import datetime
from time import sleep, time

import cv2
import numpy as np

fps = 15
width = 800
height = 600
colors = [
    (0, 0, 255),
    (255, 0, 0),
    (0, 255, 0),
]

out = cv2.VideoWriter('appsrc ! videoconvert' + \
    ' ! video/x-raw,format=I420' + \
    ' ! x264enc speed-preset=ultrafast bitrate=600 key-int-max=' + str(fps * 2) + \
    ' ! video/x-h264,profile=baseline' + \
    ' ! rtspclientsink location=rtsp://localhost:8554/mystream',
    cv2.CAP_GSTREAMER, 0, fps, (width, height), True)
if not out.isOpened():
    raise Exception("can't open video writer")

curcolor = 0
start = time()

while True:
    frame = np.zeros((height, width, 3), np.uint8)

    # create a rectangle
    color = colors[curcolor]
    curcolor += 1
    curcolor %= len(colors)
    for y in range(0, int(frame.shape[0] / 2)):
        for x in range(0, int(frame.shape[1] / 2)):
            frame[y][x] = color

    out.write(frame)
    print("%s frame written to the server" % datetime.now())

    now = time()
    diff = (1 / fps) - now - start
    if diff > 0:
        sleep(diff)
    start = now
```

The resulting stream will be available in path `/mystream`.
