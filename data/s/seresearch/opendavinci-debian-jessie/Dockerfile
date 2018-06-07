# Dockerfile to create an image for building and running OpenDaVINCI.  
# Copyright (C) 2016 Christian Berger  
#  
# This program is free software; you can redistribute it and/or  
# modify it under the terms of the GNU General Public License  
# as published by the Free Software Foundation; either version 2  
# of the License, or (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program; if not, write to the Free Software  
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
USA.  
#  
# Date: 2016-03-05  
FROM debian:jessie  
MAINTAINER Christian Berger "christian.berger@gu.se"  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://http.debian.net/debian jessie main" >>
/etc/apt/sources.list && \  
echo "deb http://http.debian.net/debian jessie-updates main" >>
/etc/apt/sources.list && \  
echo "deb http://security.debian.org/ jessie/updates main" >>
/etc/apt/sources.list && \  
apt-get update -y && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y  
  
# Installing OpenDaVINCI dependencies.  
RUN apt-get install -y --no-install-recommends \  
ant \  
build-essential \  
cmake \  
default-jre \  
default-jdk \  
freeglut3 \  
freeglut3-dev \  
git \  
libboost-dev \  
libopencv-dev \  
libopencv-core-dev \  
libopencv-highgui-dev \  
libopencv-imgproc-dev \  
libqt4-dev \  
libqt4-opengl-dev \  
libqwt5-qt4-dev \  
libqwt5-qt4 \  
qt4-dev-tools \  
rpm \  
psmisc \  
wget  
  
RUN apt-get install -y --no-install-recommends libfuse-dev  
  
RUN apt-get install -y --no-install-recommends gdbserver  
  
# Clean-up downloaded packages.  
RUN apt-get clean && \  
apt-get autoremove  
  

