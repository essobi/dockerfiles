# Dockerfile to create an image for running and building OpenDaVINCI-based
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
  
FROM ubuntu:16.04  
MAINTAINER Christian Berger "christian.berger@gu.se"  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD ./01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
ADD ./02_nolocales /etc/dpkg/dpkg.cfg.d/02_nolocales  
# The following list of libraries was determined from the binaries up to the  
# top most layer.  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y --no-install-recommends \  
freeglut3 \  
libatk1.0-0 \  
libaudio2 \  
libavcodec-ffmpeg-extra56 \  
libavformat-ffmpeg56 \  
libavutil-ffmpeg54 \  
libbluray1 \  
libcairo2 \  
libcrystalhd3 \  
libdatrie1 \  
libdc1394-22 \  
libdrm2 \  
libexpat1 \  
libffi6 \  
libfontconfig1 \  
libfreetype6 \  
libgdk-pixbuf2.0-0 \  
libgl1-mesa-glx \  
libglapi-mesa \  
libglib2.0-0 \  
libglu1-mesa \  
libgme0 \  
libgmp10 \  
libgnutls30 \  
libgomp1 \  
libgraphite2-3 \  
libgsm1 \  
libgssapi-krb5-2 \  
libgtk2.0-0 \  
libgtkglext1 \  
libharfbuzz0b \  
libhogweed4 \  
libice6 \  
libicu55 \  
libidn11 \  
libilmbase12 \  
libjasper1 \  
libjbig0 \  
libjpeg-turbo8 \  
libk5crypto3 \  
libkeyutils1 \  
libkrb5-3 \  
libkrb5support0 \  
libmodplug1 \  
libmp3lame0 \  
libncurses5 \  
libnettle6 \  
libnuma1 \  
libogg0 \  
libopencv-core2.4v5 \  
libopencv-highgui2.4v5 \  
libopencv-imgproc2.4v5 \  
libopencv-video2.4v5 \  
libopenexr22 \  
libopenjpeg5 \  
libopus0 \  
liborc-0.4-0 \  
libp11-kit0 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libpangoft2-1.0-0 \  
libpangox-1.0-0 \  
libpcap0.8 \  
libpixman-1-0 \  
libpng12-0 \  
libqt4-network \  
libqt4-opengl \  
libqt4-svg \  
libqtcore4 \  
libqtgui4 \  
libqwt5-qt4 \  
libraw1394-11 \  
librtmp1 \  
libschroedinger-1.0-0 \  
libshine3 \  
libsm6 \  
libsnappy1v5 \  
libsoxr0 \  
libspeex1 \  
libssh-gcrypt-4 \  
libswresample-ffmpeg1 \  
libswscale-ffmpeg3 \  
libtasn1-6 \  
libtbb2 \  
libthai0 \  
libtheora0 \  
libtiff5 \  
libtwolame0 \  
libusb-1.0-0 \  
libv4l-0 \  
libv4lconvert0 \  
libva1 \  
libvorbis0a \  
libvorbisenc2 \  
libvpx3 \  
libwavpack1 \  
libwebp5 \  
libx11-6 \  
libx11-xcb1 \  
libx264-148 \  
libx265-79 \  
libxau6 \  
libxcb1 \  
libxcb-dri2-0 \  
libxcb-dri3-0 \  
libxcb-glx0 \  
libxcb-present0 \  
libxcb-render0 \  
libxcb-shm0 \  
libxcb-sync1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxdmcp6 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxinerama1 \  
libxml2 \  
libxmu6 \  
libxrandr2 \  
libxrender1 \  
libxshmfence1 \  
libxt6 \  
libxvidcore4 \  
libxxf86vm1 \  
libzvbi0 \  
libfuse2 \  
gdbserver && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean  
  

