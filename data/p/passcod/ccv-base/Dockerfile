FROM ubuntu:15.10  
MAINTAINER Félix Saparelli <me@passcod.name>  
  
RUN apt update && DEBIAN_FRONTEND=noninteractive apt upgrade -y &&\  
DEBIAN_FRONTEND=noninteractive apt install -y \  
build-essential git wget libdispatch-dev libev-dev \  
libjpeg-dev libpng-dev libfftw3-dev libavcodec-dev \  
libavformat-dev libswscale-dev liblinear-dev &&\  
apt-get clean && rm -rf /var/lib/apt  
  

