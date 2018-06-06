FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Christian Reinbacher <reinbacher@icg.tugraz.at>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
add-apt-repository -y ppa:george-edison55/cmake-3.x && \  
echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" >
/etc/apt/sources.list.d/ros-latest.list && \  
apt-get update && apt-get install -y --force-yes \--no-install-recommends \  
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
libinsighttoolkit4.5 \  
libeigen3-dev \  
texlive-full \  
latexdiff \  
ros-jade-catkin \  
python-catkin-tools \  
python-catkin-pkg \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

