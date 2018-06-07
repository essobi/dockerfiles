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
# jdk1.8.0_131 *  
#******************************************************************************/  
  
FROM schneidermatic/centos:centos-7.2  
MAINTAINER schneidermatic  
  
## Set work dir  
WORKDIR /tmp  
  
## JAVA ENV  
ENV JAVA_VERSION 8u131  
ENV BUILD_VERSION b11  
ENV JAVA_HOME=/usr/java/jdk1.8.0_131  
ENV JAVA_DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm  
  
## OPENNMS ENV  
ENV OPENNMS_HOME /opt/opennms  
  
## Upgrading system  
# RUN yum -y upgrade  
# RUN yum clean all  
  
##------------------------------------------------------------------------------  
## BASE INSTALL  
##------------------------------------------------------------------------------  
  
## Install JDK  
## origin - https://github.com/Mashape/docker-java8  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "$JAVA_DOWNLOAD_URL" -O
/tmp/jdk-8-linux-x64.rpm  
RUN yum -y install ./jdk-8-linux-x64.rpm  
RUN yum clean all  

