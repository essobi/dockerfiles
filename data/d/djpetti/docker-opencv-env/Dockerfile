FROM nvidia/cuda:9.0-devel-ubuntu16.04  
MAINTAINER Daniel Petti  
  
# Prepares the environment for OpenCV install.  
# Install dependencies.  
RUN apt-get update  
RUN apt-get install -y libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \  
libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \  
libatlas-base-dev gfortran libhdf5-serial-dev python2.7-dev python-pip \  
wget cmake git  
  
RUN pip install numpy scipy  
  
# Download and extract OpenCV.  
RUN wget -O opencv.tar.gz
https://github.com/opencv/opencv/archive/3.4.0.tar.gz  
RUN mkdir opencv && tar -xvf opencv.tar.gz -C opencv --strip-components=1  
RUN wget -O opencv_contrib.tar.gz \  
https://github.com/opencv/opencv_contrib/archive/3.4.0.tar.gz  
RUN mkdir opencv_contrib && tar -xvf opencv_contrib.tar.gz -C opencv_contrib \  
\--strip-components=1  

