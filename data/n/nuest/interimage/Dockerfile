FROM ubuntu:trusty  
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>  
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
## (Based on https://github.com/rocker-
org/rocker/blob/master/r-base/Dockerfile)  
## Set a default user. Available via runtime flag `--user interimage`  
## User should also have & own a home directory (for linked volumes to work
properly).  
RUN useradd interimage \  
&& mkdir /home/interimage \  
&& chown interimage:interimage /home/interimage \  
&& addgroup interimage staff  
  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
curl \  
zlib1g-dev \  
lib32z1-dev \  
libjpeg-dev \  
build-essential \  
gdb \  
make \  
qt4-default  
# qt4-dev-tools  
WORKDIR /home/interimage  
  
## Following http://www.lvc.ele.puc-
rio.br/projects/interimage/download/files/install_interimage_ubuntu.txt  
## Get source code  
RUN curl -L -# "http://www.lvc.ele.puc-
rio.br/projects/interimage/download/files/InterIMAGE_1.27_Linux.tar.gz" -o
interimage-src.tar.gz \  
&& tar xvzf interimage-src.tar.gz  
  
WORKDIR /home/interimage/terralib_cvs/terralibmw  
RUN qmake -r \  
&& make clean; make \  
&& cp -P Debug/* /usr/lib \  
&& ldconfig  
  
WORKDIR /home/interimage/ta_operators/build/linux-g++  
RUN export TA_TERRALIB_PATH="/home/interimage/terralib_cvs/" \  
&& qmake -r \  
&& make clean; make \  
&& cp -P ta_operators_base/Debug/* /usr/lib \  
&& cp -P ta_operators_base/Debug/* /home/interimage/bin_1.27/bin  
  
WORKDIR /home/interimage/InterIMAGE_Source_1.27  
RUN qmake -r \  
&& make clean; make  
  
WORKDIR /home/interimage/bin_1.27/bin  
RUN cp -r help/ /home/interimage/InterIMAGE_Source_1.27/bin \  
&& cp -r share/ /home/interimage/InterIMAGE_Source_1.27/bin  
  
# in addition to official instructions, copy all libraries from ~/bin_1.27/bin
to /usr/lib  
RUN cp -P *.so* /usr/lib  
  
WORKDIR /home/interimage/InterIMAGE_Source_1.27/bin  
  
CMD ["/bin/bash"]  

