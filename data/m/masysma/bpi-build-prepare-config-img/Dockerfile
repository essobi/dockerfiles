FROM debian:8  
LABEL maintainer "Linux-Fan <Ma_Sys.ma@web.de"  
  
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
ARG MA_DEBIAN_MIRROR=http://ftp.de.debian.org/debian  
ENV MA_BPI_WORKDIR=/fs/ccnt_b0pr  
  
RUN \  
echo deb $MA_DEBIAN_MIRROR jessie main > /etc/apt/sources.list && \  
echo deb $MA_DEBIAN_MIRROR jessie-updates main \  
>> /etc/apt/sources.list && \  
echo deb http://security.debian.org/ jessie/updates main \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y xz-utils  
  
CMD [ "/bin/sh", "-ec", "if [ ! -d \"$MA_BPI_WORKDIR\" ]; then echo Error:
MA_BPI_WORKDIR not found. 1>&2; exit 1; fi; mkdir -p
\"$MA_BPI_WORKDIR/tmp/hostconfig\"; for i in \"$MA_BPI_WORKDIR/in\"/*; do tar
-C \"$i\" -c . | tar -C \"$MA_BPI_WORKDIR/tmp/hostconfig\" -xp; done; tar -C
\"$MA_BPI_WORKDIR/tmp\" -c hostconfig | xz -9 >
\"$MA_BPI_WORKDIR/out/hostconfig.tar.xz\"; fi" ]  

