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
# Date: 2017-02-21  
FROM base/archlinux:latest  
MAINTAINER Christian Berger "christian.berger@gu.se"  
# prepare system  
RUN pacman-key --init  
RUN yes | pacman --noconfirm -Sc  
RUN yes | pacman --noconfirm -Sy pacman  
RUN pacman-db-upgrade  
RUN yes | pacman --noconfirm -S archlinux-keyring  
RUN pacman-key --init  
RUN yes | pacman --noconfirm -Syu --force  
  
# Installing OpenDaVINCI dependencies.  
RUN pacman --noconfirm --force -S \  
apache-ant \  
jdk8-openjdk \  
boost \  
cmake \  
ffmpeg2.8 \  
freeglut \  
gcc \  
git \  
junit \  
make \  
opencv \  
python2 \  
qt4 \  
qwt5 \  
ttf-dejavu \  
gdb \  
ncurses  

