# Zookeeper (Vanilla) for Orchestration on CentOS 7.  
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
# ZOOKEEPER  
################################################  
  
ENV ZOOKEEPER_VERSION 3.4.9  
ENV ZOOKEEPER_ARCHIVE zookeeper-$ZOOKEEPER_VERSION.tar.gz  
ENV ZOOKEEPER_ARCHIVE_URL
https://dist.apache.org/repos/dist/release/zookeeper/zookeeper-$ZOOKEEPER_VERSION/$ZOOKEEPER_ARCHIVE  
ENV ZOOKEEPER_ASC_URL $ZOOKEEPER_ARCHIVE_URL.asc  
ENV ZOOKEEPER_KEYS https://dist.apache.org/repos/dist/release/zookeeper/KEYS  
  
# Install Zookeeper  
RUN \  
yum -y update && yum clean all \  
&& wget $ZOOKEEPER_ARCHIVE_URL \  
&& wget $ZOOKEEPER_ASC_URL \  
&& wget $ZOOKEEPER_KEYS \  
&& gpg --import KEYS \  
&& gpg --verify $ZOOKEEPER_ARCHIVE.asc \  
&& mkdir /opt/zookeeper \  
&& tar xvf $ZOOKEEPER_ARCHIVE -C /opt/zookeeper \  
&& rm -f $ZOOKEEPER_ARCHIVE \  
&& rm -f $ZOOKEEPER_ARCHIVE.asc \  
&& rm -f KEYS \  
&& ln -s /opt/zookeeper/*zookeeper* /opt/zookeeper/default  
  
# Configuration volume  
VOLUME ["/opt/zookeeper/default/conf"]  
  
# Data volume  
VOLUME ["/data"]  
  
# Environment variables  
ENV PATH=$PATH:/opt/zookeeper/default/bin  
  
# The container stays idle  
CMD bash --login -i  

