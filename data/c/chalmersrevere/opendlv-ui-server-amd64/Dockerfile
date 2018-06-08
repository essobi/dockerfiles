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
# Part to build opendlv-ui-server.  
FROM alpine:3.7 as builder  
MAINTAINER Ola Benderius "ola.benderius@chalmers.se"  
RUN apk update && \  
apk --no-cache add \  
cmake \  
g++ \  
make \  
upx \  
openssl-dev  
  
# The Alpine libwebsockets does not work (it needs openssl 1.1 apparently).
Let's compile it.  
RUN cd /tmp && wget
https://github.com/warmcat/libwebsockets/archive/v2.4.1.tar.gz && tar -zxvf
v2.4.1.tar.gz && cd libwebsockets-2.4.1 && mkdir build && cd build && cmake ..
&& make && make install  
  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/tmp/opendlv-ui-
server-dest .. && \  
make && make test && make install && upx -9 /tmp/opendlv-ui-server-
dest/bin/opendlv-ui-server  
  
# Part to deploy opendlv-ui-server.  
FROM alpine:3.7  
MAINTAINER Ola Benderius "ola.benderius@chalmers.se"  
RUN apk update && \  
apk --no-cache add \  
openssl  
  
WORKDIR /usr/bin  
COPY \--from=builder /tmp/opendlv-ui-server-dest /usr  
CMD ["/usr/bin/opendlv-ui-server"]  
  

