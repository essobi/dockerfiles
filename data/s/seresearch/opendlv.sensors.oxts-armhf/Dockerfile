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
# Part to build oxts.  
FROM pipill/armhf-alpine:edge as builder  
MAINTAINER Christian Berger "christian.berger@gu.se"  
RUN [ "cross-build-start" ]  
  
RUN cat /etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/v3.7/main > /etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/v3.7/community >>
/etc/apk/repositories  
  
RUN apk update && \  
apk --no-cache add \  
ca-certificates \  
cmake \  
g++ \  
git \  
make  
WORKDIR /tmp  
RUN git clone https://github.com/se-research/opendlv.sensors.oxts.git && \  
cd opendlv.sensors.oxts && \  
mkdir build && \  
cd build && \  
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/tmp/oxts-dest .. &&
\  
make && make test && make install  
  
RUN [ "cross-build-end" ]  
  
# Part to deploy oxts.  
FROM pipill/armhf-alpine:edge  
MAINTAINER Christian Berger "christian.berger@gu.se"  
WORKDIR /usr/bin  
COPY \--from=builder /tmp/oxts-dest/bin/oxts .  
CMD ["/usr/bin/oxts"]  
  

