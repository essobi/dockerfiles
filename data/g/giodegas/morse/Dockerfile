FROM tutum/debian:wheezy  
  
MAINTAINER Giovanni De Gasperis @giodegas  
  
# System update and basic tools  
RUN apt-get update && apt-get -y upgrade && apt-get -y install curl build-
essential vim nano  
ENV TERM vt100  
  
# 3D Mesa libraries and xterm to run X apps, VNC server  
RUN apt-get -y install libglu1-mesa-dev freeglut3-dev mesa-common-dev xterm
vnc4server  
  
# Python 3.4.2 setup - taken from http://github.com/docker-
library/python/blob/master/3.4/Dockerfile  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
ENV PYTHON_VERSION 3.4.2  
RUN set -x \  
&& mkdir -p /usr/src/python \  
&& curl -SL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
\  
| tar -xJC /usr/src/python --strip-components=1 \  
&& cd /usr/src/python \  
&& ./configure --enable-shared \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s easy_install-3.4 easy_install \  
&& ln -s idle3 idle \  
&& ln -s pip3 pip \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python-config3 python-config  
  
RUN apt-get -y install apt-utils wget git libfreetype6 libxi-dev  
RUN apt-get -y install pkg-config cmake  
  
# get Blender executable  
RUN mkdir /opt/blender  
RUN wget -q
http://mirror.cs.umn.edu/blender.org/release/Blender2.73/blender-2.73-linux-
glibc211-x86_64.tar.bz2 -O /opt/blender/blender-2.73.tar.bz2  
WORKDIR /opt/blender  
RUN tar jxf blender-2.73.tar.bz2  
  
# Install Morse Robotic simulator, stable release  
WORKDIR /usr/src  
RUN git clone https://github.com/morse-simulator/morse -b master  
  
WORKDIR /usr/src/morse  
  
RUN mkdir build  
WORKDIR /usr/src/morse/build  
ENV MORSE_BLENDER /opt/blender/blender-2.73-linux-glibc211-x86_64/blender  
  
RUN cmake ..  
RUN make install  
RUN morse --noaudio check  
  

