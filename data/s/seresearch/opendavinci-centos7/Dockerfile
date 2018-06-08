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
  
FROM centos:centos7  
MAINTAINER Christian Berger "christian.berger@gu.se"  
  
RUN yum -y update && \  
yum -y upgrade  
  
RUN yum -y install \  
ant \  
ant-junit \  
automake \  
boost-devel \  
cmake \  
freeglut-devel \  
gcc \  
gcc-c++ \  
git \  
python27 \  
iproute \  
make \  
opencv-devel \  
psmisc \  
qt4-devel \  
qwt5-qt4-devel \  
kernel-devel \  
wget  
  
RUN yum -y install gdb-gdbserver  
  
RUN yum -y install ncurses-devel  

