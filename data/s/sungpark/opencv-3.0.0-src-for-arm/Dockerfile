FROM armv7/armhf-ubuntu_core:15.04  
ENV QEMU_EXECVE 1  
COPY cross-build-tools/ /usr/bin  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
cmake \  
git \  
libgtk2.0-dev \  
pkg-config \  
python-dev \  
python-numpy \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
wget \  
unzip  
  
RUN cd /root \  
&& git clone https://github.com/opencv/opencv.git \  
&& cd /root/opencv \  
&& wget --tries 100 -O opencv.zip
https://github.com/Itseez/opencv/archive/3.0.0.zip \  
&& unzip *.zip \  
&& rm *.zip  
  
RUN [ "cross-build-end" ]  

