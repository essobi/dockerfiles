# =========================================================================  
# =========================================================================  
#  
# Dockerfile for  
# eclipse-javascript-oxygen-3a + git/html/xml/css/mylyn + ...  
# in a Debian docker container.  
#  
# =========================================================================  
#  
# @author Jay Wheeler.  
# @version 0.0.3  
# @copyright © 2018. EarthWalk Software.  
# @license Licensed under the GNU General Public License, GPL-3.0-or-later.  
# @package ewsdocker/debian-eclipse-javascript  
# @subpackage Dockerfile  
#  
# =========================================================================  
#  
# Copyright © 2018. EarthWalk Software  
# Licensed under the GNU General Public License, GPL-3.0-or-later.  
#  
# This file is part of ewsdocker/debian-eclipse-javascript.  
#  
# ewsdocker/debian-eclipse-javascript is free software: you can redistribute  
# it and/or modify it under the terms of the GNU General Public License  
# as published by the Free Software Foundation, either version 3 of the  
# License, or (at your option) any later version.  
#  
# ewsdocker/debian-eclipse-javascript is distributed in the hope that it will  
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty  
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with ewsdocker/debian-eclipse-javascript. If not, see  
# <http://www.gnu.org/licenses/>.  
#  
# =========================================================================  
# =========================================================================  
FROM ewsdocker/debian-nodejs:0.0.2  
MAINTAINER Jay Wheeler <EarthWalkSoftware@gmail.com>  
  
# =========================================================================  
#  
# The following must be modified before running a build,  
# as there is no way to specify them in the build  
# command.  
#  
# Eclipse repository address  
#  
# =========================================================================  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ECLIPSE_RELEASE=oxygen  
ENV ECLIPSE_VERS=3a  
ENV ECLIPSE_IDE=javascript  
ENV
ECLIPSE_PKG="eclipse-${ECLIPSE_IDE}-${ECLIPSE_RELEASE}-${ECLIPSE_VERS}-linux-
gtk-x86_64.tar.gz"  
ENV ECLIPSE_DIR=eclipse  
  
#ENV ECLIPSE_HOST=http://pkgnginx  
ENV
ECLIPSE_HOST="http://mirror.csclub.uwaterloo.ca/eclipse/technology/epp/downloads/release/${ECLIPSE_RELEASE}/${ECLIPSE_VERS}"  
ENV ECLIPSE_URL="${ECLIPSE_HOST}/${ECLIPSE_PKG}"  
# =========================================================================  
ENV LMSBUILD_VERSION="0.0.3"  
ENV LMSBUILD_NAME=debian-eclipse-${ECLIPSE_IDE}  
ENV LMSBUILD_DOCKER="ewsdocker/${LMSBUILD_NAME}:${LMSBUILD_VERSION}"  
ENV
LMSBUILD_PACKAGE="eclipse-${ECLIPSE_IDE}-${ECLIPSE_RELEASE}-${ECLIPSE_VERS}"  
# =========================================================================  
COPY scripts/. /  
  
# =========================================================================  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
java-common \  
libgtk2.0-bin \  
libgtk-3-0 \  
libgtk-3-bin \  
libgtk-3-common \  
libgtk2.0-0 \  
libgtk2.0-common \  
libwebkitgtk-3.0 \  
openjdk-8-jre \  
openjdk-8-jre-headless \  
&& apt-get clean all \  
&& cd /usr/local/share \  
&& wget -q ${ECLIPSE_URL} \  
&& tar -xvf ${ECLIPSE_PKG} \  
&& ln -s /usr/local/share/${ECLIPSE_DIR}/eclipse /usr/local/bin/eclipse \  
&& printf "${LMSBUILD_DOCKER} (${LMSBUILD_PACKAGE}), %s @ %s\n" `date
'+%Y-%m-%d'` `date '+%H:%M:%S'` >> /etc/ewsdocker-builds.txt  
  
# =========================================================================  
VOLUME /project  
VOLUME /source  
VOLUME /userbin  
VOLUME /workspace  
  
WORKDIR /workspace  
  
# =========================================================================  
ENTRYPOINT ["/my_init", "--quiet"]  
CMD ["/usr/local/bin/eclipse"]  

