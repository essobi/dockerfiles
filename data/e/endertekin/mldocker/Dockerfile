############################################################  
# Dockerfile to build Python 2.7 \+ OpenCV 3.2 \+ Tensorflow 1.0 image  
# Based on Debian  
############################################################  
  
FROM debian:stable-slim  
MAINTAINER Ender Tekin <etekin@wisc.edu>  
ENV DEBIAN_FRONTEND noninteractive  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.0-cp27-none-
linux_x86_64.whl  
ENV OPENCV_REPO_URL git://github.com/opencv/opencv.git  
ENV OPENCV_CONTRIB_REPO_URL git://github.com/opencv/opencv_contrib.git  
ENV OPENCV_VERSION 3.2.0  
#Install git, python and some other image libraries that opencv needs, install
tensorflow, install opencv, cleanup  
RUN apt-get update && \  
apt-get install -y -q apt-utils build-essential cmake git pkg-config && \  
apt-get install -y -q python2.7 python2.7-dev python-pip && \  
apt-get install -y -q libavformat-dev libavcodec-dev libavfilter-dev
libswscale-dev && \  
apt-get install -y -q libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libeigen3-dev && \  
apt-get install -y -q libtesseract-dev libgtk2.0-dev && \  
apt-get autoremove && \  
apt-get clean && \  
pip install --upgrade pip && \  
pip install numpy && \  
pip install ${TF_BINARY_URL} && \  
cd /tmp && \  
git clone --depth 1 \--branch $OPENCV_VERSION $OPENCV_REPO_URL && \  
git clone --depth 1 \--branch $OPENCV_VERSION $OPENCV_CONTRIB_REPO_URL && \  
cd opencv && \  
mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib/modules .. && \  
make -j$(nproc) && \  
make install && \  
cd /tmp && \  
rm -rf opencv && \  
rm -rf opencv_contrib  
  

