# Copyright (C) 2017 Christian Berger  
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
FROM ubuntu:16.04  
MAINTAINER Christian Berger "christian.berger@gu.se"  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD ./01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
ADD ./02_nolocales /etc/dpkg/dpkg.cfg.d/02_nolocales  
  
# The following list of libraries was determined from the binaries up to the  
# top most layer.  
RUN mkdir -p /usr/share/man/man1 && \  
apt-get update -y && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y --no-install-recommends \  
build-essential \  
git \  
cmake && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean  
  
RUN cd /tmp && \  
git config --global http.sslVerify false && \  
git clone https://github.com/pionate/libcluon.git && \  
mkdir build && cd build && \  
cmake -D CMAKE_INSTALL_PREFIX=/usr ../libcluon/libcluon && make &&
CTEST_OUTPUT_ON_FAILURE=1 make test && make install && \  
cd .. && rm -fr /tmp/libcluon /tmp/build  
  
# Test installation.  
RUN cd /tmp && \  
echo "#include <cluon/UDPSender.hpp>\r\n int main() {\r\n cluon::UDPSender
s(\"127.0.0.1\", 1234); s.send(\"Hello World\"); }" > /tmp/test.cpp && \  
g++ -std=c++14 -o test test.cpp -lcluon -pthread && \  
./test && rm -f test.cpp test  
  
RUN apt-get remove -y git && \  
apt-get -y autoremove  
  

