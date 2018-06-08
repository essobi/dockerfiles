# Dockerfile to create an image for building and running OpenDaVINCI-based
apps.  
# Copyright (C) 2017 Christian Berger  
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
# Date: 2017-03-22  
  
FROM seresearch/ubuntu-16.04:latest  
MAINTAINER Christian Berger "christian.berger@gu.se"  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y --no-install-recommends \  
rpm \  
build-essential \  
python2.7 \  
ant \  
ccache \  
cmake \  
default-jdk \  
default-jre \  
ffmpeg \  
freeglut3-dev \  
git \  
libfuse-dev \  
libboost-dev \  
libncurses-dev \  
libopencv-dev \  
libopencv-core-dev \  
libopencv-highgui-dev \  
libopencv-imgproc-dev \  
libqt4-dev \  
libqt4-opengl-dev \  
libqwt5-qt4-dev \  
qt4-dev-tools && \  
apt-get clean && \  
apt-get autoremove  
  

