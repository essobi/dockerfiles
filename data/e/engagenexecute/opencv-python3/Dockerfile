# Pull base image with batteries  
FROM buildpack-deps:jessie  
  
MAINTAINER EngageNExecute code@engagenexecute.com  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
git-core  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
cmake \  
git \  
wget \  
unzip \  
pkg-config \  
libswscale-dev \  
python3-dev \  
python3-numpy \  
python3-pip \  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libavformat-dev \  
&& apt-get -y clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  
  
RUN wget https://github.com/Itseez/opencv/archive/3.1.0.zip \  
&& unzip 3.1.0.zip \  
&& mkdir /opencv-3.1.0/cmake_binary \  
&& cd /opencv-3.1.0/cmake_binary \  
&& cmake .. \  
&& make install \  
&& rm /3.1.0.zip \  
&& rm -r /opencv-3.1.0  
  
# Set UTF-8 as locales  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
# ENV UTF-8  
ENV LC_ALL C.UTF-8  
  
# Disable warning driver1394 (camera)  
RUN ln /dev/null /dev/raw1394  

