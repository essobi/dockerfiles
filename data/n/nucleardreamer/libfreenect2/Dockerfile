FROM ubuntu:xenial  
LABEL maintainer "Flynn Joffray <nucleardreamer@gmail.com>"  
  
ARG DEBIAN_FRONTENT=noninteractive  
ARG TAG=false  
  
RUN apt-get update && apt-get install -yq \  
beignet-dev \  
build-essential \  
cmake \  
git \  
libusb-1.0.0-dev \  
libturbojpeg \  
libjpeg-turbo8-dev \  
libglfw3-dev \  
libopenni2-dev \  
opencl-headers \  
openni2-utils \  
pkg-config \  
udev  
  
RUN git clone https://github.com/OpenKinect/libfreenect2.git \  
&& cd libfreenect2 \  
&& /bin/bash -c "if ! [ $TAG == false ]; then git checkout tags/$TAG; fi" \  
&& mkdir build && cd build \  
&& cmake .. -DBUILD_OPENNI2_DRIVER=ON -DCMAKE_INSTALL_PREFIX=/root/freenect2 \  
&& make \  
&& make install \  
&& cp /libfreenect2/platform/linux/udev/90-kinect2.rules /etc/udev/rules.d/ \  
&& ldconfig /root/freenect2 \  
&& ln -s /libfreenect2/build/bin/Protonect /usr/local/bin/kinect_test \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

