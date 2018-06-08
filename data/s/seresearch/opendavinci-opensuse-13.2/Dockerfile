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
  
FROM opensuse:13.2  
MAINTAINER Christian Berger "christian.berger@gu.se"  
  
RUN zypper --non-interactive --no-gpg-checks refresh && \  
zypper --non-interactive --no-gpg-checks update  
  
RUN zypper --non-interactive --no-gpg-checks install \  
ant \  
ant-junit \  
boost-devel \  
cmake \  
git \  
freeglut-devel \  
gcc \  
gcc-c++ \  
iproute2 \  
make \  
python \  
opencv-devel \  
psmisc \  
libqt4-devel \  
qwt-devel \  
wget  
  
RUN zypper --non-interactive --no-gpg-checks install gdb  
  
RUN zypper --non-interactive --no-gpg-checks install ncurses-devel  

