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
FROM alpine:3.7 as builder  
MAINTAINER Ola Benderius "ola.benderius@chalmers.se"  
RUN apk update && \  
apk --no-cache add \  
autoconf \  
automake \  
cmake \  
git \  
libtool \  
g++ \  
make \  
upx  
  
RUN git clone https://github.com/zeromq/libzmq.git && cd libzmq &&
./autogen.sh && mkdir build && cd build && cmake -DWITH_PERF_TOOL=OFF
-DZMQ_BUILD_TESTS=OFF -DENABLE_CPACK=OFF -DCMAKE_BUILD_TYPE=Release .. && make
&& make install  
  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/tmp/dest .. && \  
make && make install && upx -9 /tmp/dest/bin/opendlv-gw-seaman  
  
FROM alpine:3.7  
MAINTAINER Ola Benderius "ola.benderius@chalmers.se"  
RUN apk update && \  
apk --no-cache add \  
libstdc++  
  
WORKDIR /usr/bin  
COPY \--from=builder /tmp/dest /usr  
COPY \--from=builder /usr/local/lib64 /usr/lib  
CMD ["/usr/bin/opendlv-gw-seaman"]  

