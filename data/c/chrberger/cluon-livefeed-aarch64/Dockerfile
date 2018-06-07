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
# Part to build cluon-livefeed.  
FROM docker.io/project31/aarch64-alpine-qemu:3.5-7 as builder  
MAINTAINER Christian Berger "christian.berger@gu.se"  
RUN [ "cross-build-start" ]  
  
RUN cat /etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/v3.7/main > /etc/apk/repositories && \  
echo http://dl-4.alpinelinux.org/alpine/v3.7/community >>
/etc/apk/repositories  
  
RUN apk update && \  
apk --no-cache add \  
g++  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN ln -sf cluon-complete-v0.0.90.hpp cluon-complete.cpp && \  
g++ -std=c++14 -Wall -D HAVE_CLUON_LIVEFEED -pthread -s -static -static-libgcc
-static-libstdc++ -o /tmp/cluon-livefeed cluon-complete.cpp  
  
RUN [ "cross-build-end" ]  
  
# Part to deploy cluon-livefeed.  
FROM docker.io/project31/aarch64-alpine-qemu:3.5-7  
MAINTAINER Christian Berger "christian.berger@gu.se"  
WORKDIR /usr/bin  
COPY \--from=builder /tmp/cluon-livefeed .  
ENTRYPOINT ["cluon-livefeed"]  
  

