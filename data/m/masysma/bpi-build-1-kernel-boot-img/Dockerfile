FROM debian:8  
LABEL maintainer "Linux-Fan <Ma_Sys.ma@web.de>"  
  
# Ma_Sys.ma Scripts to build Debian images for a Banana Pi M2+EDU,  
# Copyright (c) 2017 Ma_Sys.ma.  
# For further info send an e-mail to Ma_Sys.ma@web.de.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
# in out tmp  
# in/BPI-M2P-bsp.tar.xz  
ARG MA_DEBIAN_MIRROR=http://ftp.de.debian.org/debian  
ENV MA_BPI_WORKDIR=/fs/ccnt_b1kb  
  
# TODO z AVOID emdebian.org DEPENDENCY AS TO RELY ON LOCAL SOURCES ONLY...  
RUN \  
mkdir /var/tmp/build && \  
echo deb $MA_DEBIAN_MIRROR jessie main > /etc/apt/sources.list && \  
echo deb $MA_DEBIAN_MIRROR jessie-updates main \  
>> /etc/apt/sources.list && \  
echo deb http://security.debian.org/ jessie/updates main \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y wget && \  
echo deb http://emdebian.org/tools/debian/ jessie main \  
>> /etc/apt/sources.list && \  
( wget -qO- \  
http://emdebian.org/tools/debian/emdebian-toolchain-archive.key \  
| apt-key add - ) && \  
apt-get update && \  
apt-get dist-upgrade -y && \  
dpkg --add-architecture i386 && \  
dpkg --add-architecture armhf && \  
apt-get update && \  
apt-get install -y \  
apt-utils build-essential gcc-arm-linux-gnueabihf git \  
g++-arm-linux-gnueabihf unzip sudo bc u-boot-tools \  
crossbuild-essential-armhf libc6-dev:armhf libc6:armhf \  
libstdc++6:armhf libstdc++6:i386 zlib1g:i386 dpkg-cross \  
device-tree-compiler libc6:i386 pkg-config libusb-1.0-0-dev \  
python-software-properties software-properties-common \  
libncurses5-dev busybox xz-utils  
  
COPY run_build.mk /var/tmp/build/Makefile  
COPY new_kernel.diff /var/tmp/build/  
  
CMD [ "/usr/bin/make", "-C", "/var/tmp/build" ]  

