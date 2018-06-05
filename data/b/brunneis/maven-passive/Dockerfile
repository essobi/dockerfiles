# Maven for Orchestration on CentOS 7.  
# Copyright (C) 2016 Rodrigo Martínez <dev@brunneis.com>  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
FROM brunneis/centos-jdk  
MAINTAINER "Rodrigo Martínez" <dev@brunneis.com>  
  
################################################  
# MAVEN  
################################################  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_ARCHIVE apache-maven-$MAVEN_VERSION-bin.tar.gz  
ENV MAVEN_ARCHIVE_URL
https://dist.apache.org/repos/dist/release/maven/maven-3/$MAVEN_VERSION/binaries/$MAVEN_ARCHIVE  
ENV MAVEN_ASC_URL $MAVEN_ARCHIVE_URL.asc  
ENV MAVEN_KEYS https://dist.apache.org/repos/dist/release/maven/KEYS  
  
# Install Maven  
RUN \  
yum -y update && yum clean all \  
&& wget $MAVEN_ARCHIVE_URL \  
&& wget $MAVEN_ASC_URL \  
&& wget $MAVEN_KEYS \  
&& gpg --import KEYS \  
&& gpg --verify $MAVEN_ARCHIVE.asc \  
&& mkdir /opt/maven \  
&& tar xvf $MAVEN_ARCHIVE -C /opt/maven \  
&& rm -f $MAVEN_ARCHIVE \  
&& rm -f $MAVEN_ARCHIVE.asc \  
&& rm -f KEYS \  
&& ln -s /opt/maven/*maven* /opt/maven/default  
  
# Data volume  
VOLUME ["/data"]  
  
# Environment variables  
ENV M2_HOME=/opt/maven/default \  
PATH=$M2_HOME/bin:$PATH  
  
# The container stays idle  
CMD bash --login -i  

