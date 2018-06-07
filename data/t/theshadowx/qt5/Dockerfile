FROM ubuntu:17.04  
MAINTAINER Ali Diouri <alidiouri@gmail.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
  
RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list  
RUN apt update && \  
apt upgrade -y && \  
apt dist-upgrade -y && \  
apt install -y \  
git \  
wget \  
xvfb \  
flex \  
dh-make \  
debhelper \  
checkinstall \  
fuse \  
snapcraft \  
bison \  
libxcursor-dev \  
libxcomposite-dev \  
software-properties-common \  
build-essential \  
libssl-dev \  
libxcb1-dev \  
libx11-dev \  
libgl1-mesa-dev \  
libudev-dev \  
qt5-default \  
qtbase5-private-dev &&\  
apt clean  
  
WORKDIR /home/root/  
  
CMD ["/bin/bash"]

