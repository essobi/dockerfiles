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
FROM alpine:3.7 as builder  
MAINTAINER Christian Berger "christian.berger@gu.se"  
RUN apk update && \  
apk --no-cache add \  
g++  
ADD . /opt/sources  
WORKDIR /opt/sources  
RUN ln -sf cluon-complete-v0.0.90.hpp cluon-complete.cpp && \  
g++ -std=c++14 -Wall -D HAVE_CLUON_LIVEFEED -pthread -s -static -static-libgcc
-static-libstdc++ -o /tmp/cluon-livefeed cluon-complete.cpp  
  
# Part to deploy cluon-livefeed.  
FROM scratch  
MAINTAINER Christian Berger "christian.berger@gu.se"  
COPY \--from=builder /tmp/cluon-livefeed /  
ENTRYPOINT ["/cluon-livefeed"]  
  

