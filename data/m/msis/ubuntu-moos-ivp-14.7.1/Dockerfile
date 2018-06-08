# Starting off an ubuntu:14.04  
FROM ubuntu:14.04  
# Feel free to email me if you need support  
MAINTAINER Mohamed Saad IBN SEDDIK <ms.ibnseddik@gmail.com>  
  
# build essantial packages for moos-ivp-14.7.1 (from README-GNULINUX.txt file)  
RUN apt-get update \  
&& apt-get install -y \  
g++ \  
subversion \  
xterm \  
cmake \  
libfltk1.3-dev \  
freeglut3-dev \  
libpng12-dev \  
libjpeg-dev \  
libxft-dev \  
libxinerama-dev \  
libtiff4-dev  
  
# create a sudoer user "moosuser" w/ toor as a password  
RUN useradd moosuser -G sudo -m \  
&& echo "moosuser:toor" | chpasswd  
  
# Download moos-ivp-14.7.1  
WORKDIR /home/moosuser/  
RUN svn co --non-interactive --trust-server-cert \  
https://oceanai.mit.edu/svn/moos-ivp-aro/releases/moos-ivp-14.7.1 \  
moos-ivp-14.7.1  
  
# Building MOOS-IvP  
WORKDIR /home/moosuser/moos-ivp-14.7.1  
# Build & Install MOOS  
RUN bash build-moos.sh install  
# Build & Install IvP  
RUN bash build-ivp.sh install  
  
USER moosuser  
ENV HOME /home/moosuser  
WORKDIR /home/moosuser  
  

