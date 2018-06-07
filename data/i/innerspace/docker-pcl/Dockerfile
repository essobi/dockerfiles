# Pull base image  
# based on \- https://larrylisky.com/2016/11/03/point-cloud-library-on-
ubuntu-16-04-lts/  
FROM ubuntu:16.04  
MAINTAINER Matt MacGillivray  
  
#RUN apt-get install -y software-properties-common  
RUN apt-get update && apt-get install -y \  
git build-essential linux-libc-dev \  
cmake cmake-gui \  
libusb-1.0-0-dev libusb-dev libudev-dev \  
mpi-default-dev openmpi-bin openmpi-common \  
libflann1.8 libflann-dev \  
libeigen3-dev \  
libboost-all-dev \  
libvtk5.10-qt4 libvtk5.10 libvtk5-dev \  
libqhull* libgtest-dev \  
freeglut3-dev pkg-config \  
libxmu-dev libxi-dev \  
qt-sdk openjdk-8-jdk openjdk-8-jre \  
openssh-client  
  
  
# PCL - build from source and install  
RUN cd /opt \  
&& git clone https://github.com/PointCloudLibrary/pcl.git pcl-trunk \  
&& ln -s /opt/pcl-trunk /opt/pcl \  
&& cd /opt/pcl && git checkout pcl-1.8.0 \  
&& mkdir -p /opt/pcl-trunk/release \  
&& cd /opt/pcl/release && cmake -DCMAKE_BUILD_TYPE=None -DBUILD_GPU=ON
-DBUILD_apps=ON -DBUILD_examples=ON .. \  
&& cd /opt/pcl/release && make -j3 \  
&& cd /opt/pcl/release && make install \  
&& cd /opt/pcl/release && make clean  

