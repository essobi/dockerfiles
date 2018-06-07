#******************************************************************************  
# Copyright 2016 the original author or authors. *  
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
# OpenNMS-18.0.3 *  
#******************************************************************************/  
FROM schneidermatic/java  
MAINTAINER schneidermatic  
  
## Set work dir  
WORKDIR /tmp  
  
## OPENNMS ENV  
ENV OPENNMS_HOME /opt/opennms  
ENV OPENNMS_VERSION 18.0.3-1  
## POSTGRES ENV  
ENV DB_HOST="pgdb1"  
ENV DB_PORT="5432"  
ENV DB_PASSWORD=""  
## Upgrading system  
RUN yum -y upgrade  
RUN yum clean all  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
## Add OpenNMS PGP Key  
RUN rpm --import http://yum.opennms.org/OPENNMS-GPG-KEY  
  
## Add PKGs Begin  
RUN rpm -Uvh
http://yum.opennms.org/stable/rhel7/jicmp/jicmp-1.4.6-1.x86_64.rpm  
RUN rpm -Uvh
http://yum.opennms.org/stable/rhel7/jicmp6/jicmp6-1.2.4-1.x86_64.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-
core-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-webapp-
jetty-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
provisioning-snmp-asset-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-jmx-config-
generator-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
northbounder-jms-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
protocol-cifs-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
protocol-dhcp-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
protocol-xml-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
protocol-nsclient-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
provisioning-snmp-hardware-inventory-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
ticketer-jira-${OPENNMS_VERSION}.noarch.rpm  
RUN rpm -Uvh http://yum.opennms.org/stable/common/opennms/opennms-plugin-
ticketer-otrs-${OPENNMS_VERSION}.noarch.rpm  
  
## File for initial OpenNMS DB installation  
RUN touch /opt/opennms/etc/install_onmsdb  
  
## Add Config  
RUN mkdir -p /opt/docker/config  
COPY src/config /opt/docker/config  
  
## Update supervisord.conf  
COPY src/config/supervisord.conf /etc/supervisord.conf  
  
## Update 'bootstrap' file  
COPY src/scripts/bootstrap.sh /opt/docker/scripts/bootstrap.sh  
RUN chmod 775 /opt/docker/scripts/bootstrap.sh  
  
## Add OpenNMS wrapper script  
ADD src/scripts/opennmsw.sh /opt/docker/scripts/opennmsw.sh  
RUN chmod 775 /opt/docker/scripts/opennmsw.sh  
  
## Add OpenNMS Configs  
COPY src/config/opennms-datasources.xml /opt/opennms/etc/opennms-
datasources.xml  
COPY src/config/logstash.xml /opt/opennms/etc/imports/pending/logstash.xml  
COPY src/config/logstash.xml /opt/opennms/etc/imports/logstash.xml  
COPY src/config/eventd-configuration.xml /opt/opennms/etc/eventd-
configuration.xml  
COPY src/config/eventconf.xml /opt/opennms/etc/eventconf.xml  
COPY src/config/enterprise.logstash.generic.events.xml
/opt/opennms/etc/events/enterprise.logstash.generic.events.xml  
RUN chmod -R 775 /opt/opennms/etc  
  
## Volumes for storing data outside of the container  
VOLUME ["/var/log/opennms","/var/opennnms"]  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- OpenNMS HTTP Port(8980)  
## -- OpenNMS HTTPS Port(8443)  
## -- OpenNMS JMX Port(18980)  
## -- OpenNMS KARAF RMI Port(1099)  
## -- OpenNMS KARAF SSH Port(8101)  
## -- OpenNMS MQ Port(61616)  
## -- OpenNMS Eventd Port(5817)  
## -- PostgreSQL Port(5432)  
## -- SNMP (AGENT) Port(161)  
## -- SNMP (SERVER) Port(162)  
## -- SSH Port(22)  
EXPOSE 8980 8443 18980 1099 8101 61616 5817 5432 162/udp 161/udp  

