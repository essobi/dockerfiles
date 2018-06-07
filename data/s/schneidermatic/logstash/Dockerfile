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
# Logstash-5.3.2 *  
# Logstash-output-opennms-0.1.3 *  
# X-PACK-5.3.2  
#******************************************************************************/  
FROM schneidermatic/java:latest  
MAINTAINER markus.schneider73@gmail.com  
  
## Set workdir  
WORKDIR /tmp  
  
ENV ES_VERSION=5.3.2  
ENV ES_INSTANCE=es1  
ENV LS_INSTANCE=ls1  
ENV LOGSTASH_HOME=/opt/logstash-${ES_VERSION}  
ENV LOGSTASH_BASE=/prj/logstash/$LS_INSTANCE  
ENV LOGSTASH_OUTPUT_OPENNMS_VERSION=0.1.3  
ENV INSTALL_XPACK=N  
  
##------------------------------------------------------------------------------  
## System Config Tweaks  
##------------------------------------------------------------------------------  
RUN echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
## Install net-tools  
RUN yum -y install net-tools  
RUN yum clean all  
  
## Fetch Logstash file  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/logstash/logstash-${ES_VERSION}.tar.gz"
-O /tmp/logstash-${ES_VERSION}.tar.gz  
  
## Fetch Logstash OpenNMS Plugin  
RUN wget --no-cookies --no-check-certificate
"https://rubygems.org/downloads/logstash-output-
opennms-${LOGSTASH_OUTPUT_OPENNMS_VERSION}.gem" -O /tmp/logstash-output-
opennms-${LOGSTASH_OUTPUT_OPENNMS_VERSION}.gem  
  
## Fetch X-Pack file  
RUN wget --no-cookies --no-check-certificate
"https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-${ES_VERSION}.zip"
-O /tmp/x-pack-${ES_VERSION}.zip  
  
## Install Logstash  
WORKDIR /opt  
RUN tar -xzvf /tmp/logstash-${ES_VERSION}.tar.gz  
  
## Install Logstash Plugins  
# WORKDIR /opt/logstash-${ES_VERSION}/bin  
# RUN ./logstash-plugin install /tmp/logstash-output-
opennms-${LOGSTASH_OUTPUT_OPENNMS_VERSION}.gem  
# RUN ./logstash-plugin list  
## Create /prj (project) folder and sub folders  
RUN mkdir -p /prj/logstash/$LS_INSTANCE/{config,data,logs,scripts,test}  
  
## Copy supersiord.conf  
COPY src/config/supervisord.conf /etc/supervisord.conf  
  
## Copy all logstash files  
COPY src/config/logstash.conf /prj/logstash/$LS_INSTANCE/config  
COPY src/config/jvm.options /prj/logstash/$LS_INSTANCE/config  
COPY src/config/log4j2.properties /prj/logstash/$LS_INSTANCE/config  
COPY src/config/log4j2.properties.debug /prj/logstash/$LS_INSTANCE/config  
COPY src/config/logstash.yml /prj/logstash/$LS_INSTANCE/config  
COPY src/config/startup.options /prj/logstash/$LS_INSTANCE/config  
  
COPY src/scripts/logstashw.sh /opt/docker/scripts/logstashw.sh  
COPY src/scripts/lsdebug.sh /prj/logstash/$LS_INSTANCE/scripts/lsdebug.sh  
COPY src/scripts/health.sh /prj/logstash/$LS_INSTANCE/scripts/health.sh  
COPY src/scripts/run_logstash.sh
/prj/logstash/$LS_INSTANCE/test/run_logstash.sh  
COPY src/scripts/logwriter.sh /prj/logstash/$LS_INSTANCE/test/logwriter.sh  
COPY src/scripts/run_logwriter.sh
/prj/logstash/$LS_INSTANCE/test/run_logwriter.sh  
RUN chmod -R 775 /prj/logstash  
RUN chown -R sysadm:sysadm /prj/logstash  
  
## Copy Setup Scripts  
COPY src/scripts/setup.sh /opt/docker/scripts/setup.sh  
COPY src/scripts/setCrd.sh /opt/docker/scripts/setCrd.sh  
COPY src/scripts/bootstrap.sh /opt/docker/scripts/bootstrap.sh  
RUN chmod -R 775 /opt/docker/scripts/*  
  
## Set Credentials  
WORKDIR /opt/docker/scripts  
RUN ./setup.sh setCrd  
  
## Copy bashrc file for custom environment  
COPY src/scripts/bashrc /home/sysadm/.bashrc  
RUN chmod 700 /home/sysadm/.bashrc  
RUN chown sysadm:sysadm /home/sysadm/.bashrc  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- Logstash (Beats) Port(5044)  
EXPOSE 5044  

