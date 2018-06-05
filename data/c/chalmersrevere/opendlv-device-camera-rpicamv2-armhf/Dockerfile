# Copyright (C) 2018 Ola Benderius  
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
  
FROM resin/raspberry-pi-debian:buster as builder  
RUN [ "cross-build-start" ]  
RUN apt-get -y update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install cmake g++ git make upx  
  
RUN git clone https://github.com/raspberrypi/userland  
  
RUN mkdir userland/build && cd userland/build && cmake -D
CMAKE_BUILD_TYPE=Debug .. && make -j4 && make install  
  
RUN usermod -a -G video root  
  
RUN git clone https://github.com/cedricve/raspicam  
RUN mkdir raspicam/build && cd raspicam/build && cmake -D
CMAKE_BUILD_TYPE=Debug .. && make -j4 && make install  
  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=Debug -D CMAKE_INSTALL_PREFIX=/tmp/build-dest .. &&
\  
make && make install && upx -9 /tmp/build-dest/bin/opendlv-device-camera-
rpicamv2  
RUN [ "cross-build-end" ]  
  
FROM resin/raspberry-pi-debian:buster  
RUN [ "cross-build-start" ]  
WORKDIR /usr/bin  
COPY --from=builder /tmp/build-dest/ /usr/  
COPY --from=builder /usr/local/lib/libraspicam.* \  
/opt/vc/lib/libcontainers.so \  
/opt/vc/lib/libmmal.so \  
/opt/vc/lib/libmmal_components.so \  
/opt/vc/lib/libmmal_core.so \  
/opt/vc/lib/libmmal_util.so \  
/opt/vc/lib/libmmal_vc_client.so \  
/opt/vc/lib/libvchiq_arm.so \  
/opt/vc/lib/libvcos.so \  
/opt/vc/lib/libvcsm.so \  
/usr/lib/  
  
CMD ["/usr/bin/opendlv-device-camera-rpicamv2"]  
RUN [ "cross-build-end" ]

