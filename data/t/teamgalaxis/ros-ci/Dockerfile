FROM ros:kinetic-ros-base  
  
MAINTAINER Markus Kohout <kohout@embedded.rwth-aachen.de>  
  
ADD /python_packages.txt /python_packages.txt  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install build-essential cmake pkg-config \  
libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \  
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \  
libgtk2.0-dev wget zip unzip python-pip \  
libatlas-base-dev gfortran ocl-icd-opencl-dev \  
python2.7-dev openssh-client \  
ros-kinetic-perception \  
&& pip install -r /python_packages.txt \  
&& rosdep update  
  

