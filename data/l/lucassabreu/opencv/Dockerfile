FROM ubuntu:14.04  
  
ENV OPENCV_VERSION 3.2.0  
  
RUN apt-get update && apt-get install -y build-essential zip cmake git
libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev && \  
curl "https://codeload.github.com/opencv/opencv/zip/$OPENCV_VERSION" -o
/tmp/opencv.zip && cd /tmp && unzip opencv && rm opencv.zip && \  
mkdir -p /opt/opencv/lib && cd /opt/opencv/lib && cmake -D
CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local
"/tmp/opencv-$OPENCV_VERSION"  
RUN rm -rf "/tmp/opencv-$OPENCV_VERSION" && apt-get remove -y build-essential
zip cmake git  
  

