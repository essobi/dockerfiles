#  
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
#  
# Dockerfile for guacamole-server  
#  
# Start from CentOS base image  
FROM guacamole/guacamole:latest  
MAINTAINER Patrick Sodre <psodre@gmail.com>  
  
# Environment variables  
ENV \  
CONSUL_VERSION=0.7.2 \  
CONSUL_SHA256=aa97f4e5a552d986b2a36d48fdc3a4a909463e7de5f726f3c5a89b8a1be74a58
\  
CONSUL_TEMPLATE_VERSION=0.16.0 \  
CONSUL_TEMPLATE_SHA256=064b0b492bb7ca3663811d297436a4bbf3226de706d2b76adade7021cd22e156
\  
CONTAINERPILOT_VERSION=2.6.0 \  
CONTAINERPILOT_SHA1=c1bcd137fadd26ca2998eec192d04c08f62beb1f \  
CONTAINERPILOT=file:///etc/containerpilot.json  
  
# Install Consul  
# Releases at https://releases.hashicorp.com/consul  
RUN curl --retry 7 --fail -vo /tmp/consul.zip \  
"https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip"
\  
&& echo "${CONSUL_SHA256} /tmp/consul.zip" | sha256sum -c \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& rm /tmp/consul.zip \  
&& mkdir /config  
  
# Create empty directories for Consul config and data  
RUN mkdir -p /etc/consul \  
&& mkdir -p /var/lib/consul  
  
  
# Install Consul template  
# Releases at https://releases.hashicorp.com/consul-template/  
RUN curl --retry 7 --fail -Lso /tmp/consul-template.zip \  
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \  
&& echo "${CONSUL_TEMPLATE_SHA256} /tmp/consul-template.zip" | sha256sum -c \  
&& unzip /tmp/consul-template.zip -d /usr/local/bin \  
&& rm /tmp/consul-template.zip  
  
  
# Add ContainerPilot and its configuration  
RUN curl --retry 7 --fail -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz"
\  
&& echo "${CONTAINERPILOT_SHA1} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \  
&& rm /tmp/containerpilot.tar.gz  
  
# Add envsubst  
RUN apt-get update \  
&& apt-get install -y gettext-base \  
&& apt-cache policy docker-engine \  
&& apt-get clean  
  
# Copy configuration files  
COPY etc /etc  
COPY usr /usr  
  
ENV GUACAMOLE_HOME=${CATALINA_HOME}/.guacamole  
  
# Start Tomcat8  
EXPOSE 8080  
CMD [ "containerpilot", \  
"/usr/local/tomcat/bin/catalina.sh", "run" ]  
  

