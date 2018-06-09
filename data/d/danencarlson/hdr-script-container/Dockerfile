FROM debian:jessie  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
ADD sources.list /etc/apt/sources.list  
WORKDIR /tmp  
  
RUN apt-get update  
RUN apt-get -y install wget ufraw enfuse jhead gimp build-essential cmake git
libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-
dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev
libjasper-dev libdc1394-22-dev unzip dcraw ufraw-batch hugin-tools  
  
#RUN apt-get -y install openjdk-7-jre  
#RUN apt-get -y build-dep libcv2.4  
#RUN apt-get -y build-dep pfstools  
RUN apt-get -y install libgsl0-dev  
RUN apt-get -y remove liboctave-dev  
RUN apt-get clean  
  
RUN wget https://github.com/Itseez/opencv/archive/2.4.11.zip -O
opencv-2.4.11.zip  
RUN unzip -x opencv-2.4.11.zip && \  
cd opencv-2.4.11 && \  
mkdir build && cd build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_FFMPEG=OFF -D WITH_OPENCL=OFF -D
WITH_CUDA=OFF -D CMAKE_INSTALL_PREFIX=/usr/local .. && \  
make -j4 && make install && \  
cd /tmp && rm -rf opencv-2.4.11  
  
RUN wget
"http://downloads.sourceforge.net/project/pfstools/pfstools/2.0.4/pfstools-2.0.4.tgz?r=&ts=1481902322&use_mirror=superb-
dca2" -O pfstools-2.0.4.tgz  
RUN tar xvf pfstools-2.0.4.tgz && \  
cd pfstools-2.0.4 && \  
mkdir build && cd build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. && \  
make -j4 && make install && \  
cd /tmp && rm -rf pfstools-2.0.4  
  
RUN groupadd user && \  
useradd --uid 1000 --create-home --home-dir /home/user -g user user  
  
ADD createHDR.sh /usr/bin/  
ADD processBrackets.sh /usr/bin/  
  
RUN chmod 755 /usr/bin/createHDR.sh /usr/bin/processBrackets.sh  
  
USER user  
WORKDIR /home/user  
  

