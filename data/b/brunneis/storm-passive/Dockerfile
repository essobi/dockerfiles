# Storm (Vanilla) for Orchestration on CentOS 7.  
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
# STORM  
################################################  
  
ENV STORM_VERSION 1.0.2  
ENV STORM_ARCHIVE apache-storm-$STORM_VERSION.tar.gz  
ENV STORM_ARCHIVE_URL https://dist.apache.org/repos/dist/release/storm/apache-
storm-$STORM_VERSION/$STORM_ARCHIVE  
ENV STORM_ASC_URL $STORM_ARCHIVE_URL.asc  
ENV STORM_KEYS https://dist.apache.org/repos/dist/release/storm/KEYS  
  
# Install Storm  
RUN \  
yum -y update && yum clean all \  
&& wget $STORM_ARCHIVE_URL \  
&& wget $STORM_ASC_URL \  
&& wget $STORM_KEYS \  
&& gpg --import KEYS \  
&& gpg --verify $STORM_ARCHIVE.asc \  
&& mkdir /opt/storm \  
&& tar xvf $STORM_ARCHIVE -C /opt/storm \  
&& rm -f $STORM_ARCHIVE \  
&& rm -f $STORM_ARCHIVE.asc \  
&& rm -f KEYS \  
&& ln -s /opt/storm/*storm* /opt/storm/default  
  
# Configuration volume  
VOLUME ["/opt/storm/default/conf"]  
  
# Data volume  
VOLUME ["/data"]  
  
# Environment variables  
ENV PATH=$PATH:/opt/storm/default/bin  
  
# The container stays idle  
CMD bash --login -i  

