# Licensed to the Apache Software Foundation (ASF) under one  
# or more contributor license agreements. See the NOTICE file  
# distributed with this work for additional information  
# regarding copyright ownership. The ASF licenses this file  
# to you under the Apache License, Version 2.0 (the  
# "License"); you may not use this file except in compliance  
# with the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing,  
# software distributed under the License is distributed on an  
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  
# KIND, either express or implied. See the License for the  
# specific language governing permissions and limitations  
# under the License.  
#  
FROM openjdk:8-jre  
LABEL maintainer="Mohammed Alsahli <mohmmad1024@gmail.com>"  
LABEL site="https://nifi.apache.org"  
  
ARG UID=1000  
ARG GID=1000  
ARG NIFI_VERSION=1.6.0  
ARG MIRROR=https://archive.apache.org/dist  
  
ENV NIFI_BASE_DIR /opt/nifi  
# ENV NIFI_HOME=${NIFI_BASE_DIR}/nifi-${NIFI_VERSION} \  
ENV NIFI_HOME=${NIFI_BASE_DIR}  
ENV NIFI_BINARY_URL=/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
ADD sh/ /opt/nifi/scripts/  
  
# Setup NiFi user  
RUN mkdir -p ${NIFI_HOME}/conf/templates \  
&& apt-get update \  
&& apt-get install -y jq xmlstarlet \  
&& curl -fSL ${MIRROR}/${NIFI_BINARY_URL} -o
${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz \  
&& echo "$(curl https://archive.apache.org/dist/${NIFI_BINARY_URL}.sha256)
*${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz" | sha256sum -c - \  
&& tar -xvzf ${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz -C
${NIFI_BASE_DIR} \--strip-components=1 \  
&& rm ${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
# Web HTTP(s) & Socket Site-to-Site Ports  
EXPOSE 8080 8443 10000  
WORKDIR ${NIFI_HOME}  
VOLUME
["${NIFI_HOME}/conf/templates","${NIFI_HOME}/database_repository","${NIFI_HOME}/flowfile_repository","${NIFI_HOME}/content_repository","${NIFI_HOME}/provenance_repository","${NIFI_HOME}/logs"]  
  
# Apply configuration and start NiFi  
CMD ${NIFI_BASE_DIR}/scripts/start.sh  

