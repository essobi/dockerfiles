#******************************************************************************  
# Copyright 2017 the original author or authors. *  
# *  
# Licensed under the Apache License, Version 2.0 (the "License"); *  
# you may not use this file except in compliance with the License. *  
# You may obtain a copy of the License at *  
# *  
# http://www.apache.org/licenses/LICENSE-2.0 *  
# *  
# Unless required by applicable law or agreed to in writing, software *  
# distributed under the License is distributed on an "AS IS" BASIS, *  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. *  
# See the License for the specific language governing permissions and *  
# limitations under the License. *  
#_____________________________________________________________________________*  
# Author: Markus Schneider *  
# Arch: x86_64 *  
# Entities: CentOS-7.2 *  
# Elasticsearch-5.4.0 *  
# X-PACK-5.4.0 *  
#******************************************************************************/  
FROM schneidermatic/java:latest  
MAINTAINER schneidermatic  
  
## Set workdir  
WORKDIR /tmp  
  
ENV ES_VERSION=5.4.0  
ENV ES_CLUSTER=es1  
ENV ES_HEAP_SIZE=2g  
ENV MAX_OPEN_FILES=261244  
ENV MAX_LOCKED_MEMORY=unlimited  
ENV INSTALL_XPACK=N  
  
  
##------------------------------------------------------------------------------  
## Performance Tweaks  
##------------------------------------------------------------------------------  
RUN echo "* - nofile 66000" >> /etc/security/limits.conf && \  
echo "* - memlock unlimited" >> /etc/security/limits.conf && \  
echo vm.max_map_count=262144 > /etc/sysctl.d/max_map_count.conf && \  
echo vm.swappiness=0 > /etc/sysctl.d/swappiness.conf  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
## Install net-tools  
RUN yum -y install net-tools  
RUN yum clean all  
  
## Fetch elasticsearch file  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz"
-O /tmp/elasticsearch-${ES_VERSION}.tar.gz  
  
## Fetch x-pack  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-${ES_VERSION}.zip"
-O /tmp/x-pack-${ES_VERSION}.zip  
  
## Set workdir  
WORKDIR /opt  
  
## Extract tar file  
RUN tar -xzvf /tmp/elasticsearch-${ES_VERSION}.tar.gz  
  
## Create /prj (project) folder and sub folders  
RUN mkdir -p /prj/elasticsearch/$ES_CLUSTER/{config,data,logs,work,scripts}  
  
## Copy Scripts  
COPY src/scripts/setup.sh /opt/docker/scripts/setup.sh  
COPY src/scripts/setCrd.sh /opt/docker/scripts/setCrd.sh  
COPY src/scripts/elasticsearchw.sh /opt/docker/scripts/elasticsearchw.sh  
COPY src/scripts/bootstrap.sh /opt/docker/scripts/bootstrap.sh  
RUN chmod -R 775 /opt/docker/scripts/*  
  
## Set workdir  
WORKDIR /opt/docker/scripts  
  
## Set Credentials  
RUN ./setup.sh setCrd  
  
## Copy Elasticsearch config  
RUN cp /opt/elasticsearch-${ES_VERSION}/config/*
/prj/elasticsearch/${ES_CLUSTER}/config/  
  
## Update supervisord.conf  
COPY src/config/supervisord.conf /etc/supervisord.conf  
  
## Set permissions  
RUN chown -R elastic:elastic /opt/elasticsearch-${ES_VERSION}  
  
## Copy elasticsearch.yml  
COPY src/config/elasticsearch.yml /prj/elasticsearch/es1/config/  
RUN chown -R elastic:elastic /prj/elasticsearch  
RUN chmod -R 775 /prj/elasticsearch  
  
## Copy additional configs & scripts  
COPY src/config/*.json /prj/elasticsearch/es1/config/  
COPY src/scripts/configure.sh /prj/elasticsearch/es1/scripts/  
  
## Volumes for storing data outside of the container  
VOLUME
["/prj/elasticsearch/${ES_CLUSTER}/data","/prj/elasticsearch/${ES_CLUSTER}/logs","/prj/elasticsearch/${ES_CLUSTER}/work"]  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- Elasticsearch (REST) Port(9200)  
## -- Elasticsearch (TRANSPORT) Port(9300)  
EXPOSE 9200 9300  

