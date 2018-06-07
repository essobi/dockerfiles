FROM ubuntu:14.04.4  
  
MAINTAINER Chakkrit Termritthikun <chakkritte57@nu.ac.th>  
  
RUN \  
apt-get -q -y update && \  
apt-get -q -y install libopencv-dev build-essential checkinstall cmake pkg-
config && \  
apt-get -q -y install yasm libtiff4-dev libjpeg-dev libjasper-dev libavcodec-
dev libavformat-dev libswscale-dev && \  
apt-get -q -y install libdc1394-22-dev libxine-dev libgstreamer0.10-dev
libgstreamer-plugins-base0.10-dev libv4l-dev python-dev && \  
apt-get -q -y install python-numpy libtbb-dev libqt4-dev libgtk2.0-dev
libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev && \  
apt-get -q -y install libtheora-dev libvorbis-dev libxvidcore-dev x264
v4l-utils && \  
apt-get upgrade -q -y && \  
rm -rf /var/lib/apt/lists/*  
  
  
#RUN \  
# cd ~ && \  
# wget https://github.com/Itseez/opencv/archive/2.4.12.3.zip && \  
# unzip 2.4.12.3.zip && \  
# cd 2.4.12.3 && \  
# mkdir build && \  
# cd build && \  
# cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D
INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D
WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON .. && \  
# make && \  
# sudo make install  
  
CMD ["/bin/bash"]  

