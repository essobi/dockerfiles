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
# Kibana-5.4.0 *  
# X-PACK-5.4.0 *  
#******************************************************************************/  
FROM schneidermatic/centos:latest  
MAINTAINER schneidermatic  
  
## Set workdir  
WORKDIR /tmp  
  
ENV ES_VERSION=5.4.0  
ENV ES_INSTANCE=es1  
ENV KB_VERSION=5.4.0-linux-x86_64  
ENV KB_INSTANCE=kb1  
ENV INSTALL_XPACK=N  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
## Install net-tools  
RUN yum -y install net-tools  
RUN yum clean all  
  
## Fetch kibana file  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/kibana/kibana-${KB_VERSION}.tar.gz" -O
/tmp/kibana-${KB_VERSION}-linux-x86_64.tar.gz  
  
## Fetch x-pack file  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-${ES_VERSION}.zip"
-O /tmp/x-pack-${ES_VERSION}.zip  
  
## Set workdir  
WORKDIR /opt  
  
## Extract tar file  
RUN tar -xzvf /tmp/kibana-${KB_VERSION}-linux-x86_64.tar.gz  
  
## Create /prj (project) folder and sub folders  
RUN mkdir -p /prj/kibana/$KB_INSTANCE/{config,log}  
  
## Copy Scripts  
COPY src/scripts/setup.sh /opt/docker/scripts/setup.sh  
COPY src/scripts/setCrd.sh /opt/docker/scripts/setCrd.sh  
COPY src/scripts/kibanaw.sh /opt/docker/scripts/kibanaw.sh  
COPY src/scripts/bootstrap.sh /opt/docker/scripts/bootstrap.sh  
RUN chmod -R 775 /opt/docker/scripts/*  
  
## Set workdir  
WORKDIR /opt/docker/scripts  
  
## Set Credentials  
RUN ./setup.sh setCrd  
  
## Copy Elasticsearch config  
RUN cp /opt/kibana-${KB_VERSION}/config/* /prj/kibana/${KB_INSTANCE}/config/  
  
## Update supervisord.conf  
COPY src/config/supervisord.conf /etc/supervisord.conf  
  
## Set permissions  
RUN chown -R elastic:elastic /opt/kibana-${KB_VERSION}  
  
## Copy Kibana.yml  
COPY src/config/kibana.yml /prj/kibana/kb1/config/  
RUN chown -R elastic:elastic /prj/kibana  
RUN chmod -R 775 /prj/kibana  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- KIBANA Port(5601)  
EXPOSE 5601  

