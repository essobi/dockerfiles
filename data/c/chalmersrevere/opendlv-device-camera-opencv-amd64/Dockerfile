# Copyright (C) 2018 Christian Berger  
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
# Part to build opendlv-device-camera-opencv.  
FROM alpine:3.7 as builder  
MAINTAINER Christian Berger "christian.berger@gu.se"  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/main > /etc/apk/repositories
&& \  
echo http://dl-4.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk update && \  
apk --no-cache add \  
cmake \  
g++ \  
opencv \  
opencv-dev \  
make  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/tmp .. && \  
make && make install  
  
# Part to deploy opendlv-device-camera-opencv.  
FROM alpine:3.7  
MAINTAINER Christian Berger "christian.berger@gu.se"  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/main > /etc/apk/repositories
&& \  
echo http://dl-4.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk update && \  
apk --no-cache add \  
opencv-libs \  
libcanberra-gtk3  
  
WORKDIR /usr/bin  
COPY \--from=builder /tmp/bin/opendlv-device-camera-opencv .  
ENV NO_AT_BRIDGE=1  
ENTRYPOINT ["/usr/bin/opendlv-device-camera-opencv"]  
  

