#  
# Dockerfile to build latest OpenCV with Python2, Python3 and Java binding
support.  
#  
FROM ubuntu:14.04.2  
MAINTAINER Jerry Tian <jerryrt@gmail.com>  
  
#  
# Utility "apt-fast" is installed by default just to accelerate installl
progress.  
# All other dependencies are more or less needed by building phase of OpenCV.  
# The last "apt-get clean" command is needed to reduce Docker image size.  
#  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install software-properties-common -y && add-apt-repository
ppa:saiarcot895/myppa && apt-get update && apt-get -y install apt-fast \  
&& apt-fast install -y \  
build-essential cmake git pkg-config \  
libgtk2.0-dev libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev \  
python-dev python2.7-dev python3.4-dev python-numpy python3-numpy \  
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev \  
libdc1394-22-dev libv4l-0 libv4l-dev libgl1-mesa-dev libgles1-mesa-dev
libgles2-mesa-dev \  
libopenvg1-mesa-dev libglu1-mesa-dev \  
libgtkglext1 libgtkglext1-dev \  
openjdk-7-jdk ant \  
vtk6 libvtk6-dev \  
&& apt-get clean  
  
#  
# Git clone the repo from OpenCV official repository on GitHub.  
#  
RUN mkdir /opt/opencv-build && cd /opt/opencv-build \  
&& git clone https://github.com/Itseez/opencv && cd opencv \  
&& git checkout master && mkdir build  
  
WORKDIR /opt/opencv-build/opencv/build  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
  
#  
# OpenCV repository is kept but all building intermediate files are removed.  
# Installable path is set to "/opt".  
#  
# "FFMPEG" is an optional "I/O" part of OpenCV, since it generates a lot of  
# error when building with it, it is disabled explicitly now.  
#  
# All other dependencies is using the default settings from CMake file of
OpenCV.  
#  
RUN cmake -D CMAKE_BUILD_TYPE=Release -D WITH_FFMPEG=OFF -D
CMAKE_INSTALL_PREFIX=/opt .. \  
&& make -j2 && make install && make clean && cd .. && rm -rf build  
  
#  
# Let python(both v2 and v3) can find the newly install OpenCV modules.  
#  
RUN echo '/opt/lib/python2.7/dist-packages/'>/usr/lib/python2.7/dist-
packages/cv2.pth && echo '/opt/lib/python3.4/dist-
packages/'>/usr/lib/python3/dist-packages/cv2.pth  

