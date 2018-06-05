# Aerospike Server (Community) for Orchestration on CentOS 7.  
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
  
FROM brunneis/centos  
MAINTAINER "Rodrigo Martínez" <dev@brunneis.com>  
  
################################################  
# AEROSPIKE SERVER  
################################################  
  
ENV AEROSPIKE_VERSION 3.9.1.1  
ENV AEROSPIKE_ARCHIVE aerospike-server-community-${AEROSPIKE_VERSION}-el7.tgz  
ENV AEROSPIKE_ARCHIVE_URL "https://www.aerospike.com/artifacts/aerospike-
server-community/${AEROSPIKE_VERSION}/$AEROSPIKE_ARCHIVE"  
  
# Install Aerospike  
RUN \  
yum update -y \  
&& yum install -y logrotate \  
&& wget $AEROSPIKE_ARCHIVE_URL \  
&& wget $AEROSPIKE_ARCHIVE_URL".sha256" -O sha256 \  
&& cat sha256 | sha256sum -c - \  
&& mkdir aerospike \  
&& tar xzf $AEROSPIKE_ARCHIVE --strip-components=1 -C aerospike \  
&& rpm -i aerospike/aerospike-server-*.rpm \  
&& mkdir -p /var/log/aerospike/ \  
&& mkdir -p /var/run/aerospike/ \  
&& rm -rf $AEROSPIKE_ARCHIVE sha256 aerospike /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
# Configuration volume  
VOLUME ["/etc/aerospike"]  
  
# Data volume  
VOLUME ["/opt/aerospike/data"]  
  
# The container stays idle  
CMD bash --login -i  

