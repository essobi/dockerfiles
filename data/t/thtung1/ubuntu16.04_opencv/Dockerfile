FROM ubuntu:16.04  
MAINTAINER Tran Hoang Tung <tran-hoang.tung@usth.edu.vn>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-
essential \  
cmake qt5-default libvtk6-dev zlib1g-dev libjpeg-dev libwebp-dev libpng-dev
libtiff5-dev \  
libjasper-dev libopenexr-dev libgdal-dev libdc1394-22-dev libavcodec-dev
libavformat-dev \  
libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm \  
libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev libtbb-dev
\  
libeigen3-dev python-dev python-tk python-numpy python3-dev python3-tk
python3-numpy \  
ant default-jdk doxygen unzip wget  
  
WORKDIR /root  
  
RUN wget https://github.com/opencv/opencv/archive/3.4.0.zip && unzip 3.4.0.zip
&& \  
mv opencv-3.4.0 OpenCV && cd OpenCV && mkdir build  

