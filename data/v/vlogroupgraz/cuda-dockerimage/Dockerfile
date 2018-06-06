FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
MAINTAINER Patrick Knöbelreiter <knoebelreiter@icg.tugraz.at>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" >
/etc/apt/sources.list.d/ros-latest.list && \  
apt-get update && apt-get install -y --allow-unauthenticated --allow-
downgrades --allow-remove-essential --allow-change-held-packages --no-install-
recommends \  
initramfs-tools \  
cuda-drivers \  
cuda-toolkit-8.0 \  
git \  
wget \  
libopencv-dev \  
cmake \  
build-essential \  
doxygen \  
openssh-client \  
cmake \  
libpng++-dev \  
gcc-4.9 \  
g++-4.9 \  
libboost-all-dev \  
libinsighttoolkit4-dev \  
libinsighttoolkit4.9 \  
libeigen3-dev \  
texlive-full \  
latexdiff \  
ros-kinetic-catkin \  
python-catkin-tools \  
python-catkin-pkg \  
libfftw3-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

