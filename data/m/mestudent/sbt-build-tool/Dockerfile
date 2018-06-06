FROM cloudbees/java-build-tools:2.1.0  
MAINTAINER Piotr Plenik <piotr.plenik@gmail.com>  
  
#  
# Licensed to the Apache Software Foundation (ASF) under one or more  
# contributor license agreements. See the NOTICE file distributed with  
# this work for additional information regarding copyright ownership.  
# The ASF licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
  
#################################################  
# Inspired by  
# https://github.com/cloudbees/java-build-tools-
dockerfile/blob/master/Dockerfile  
# https://github.com/SeleniumHQ/docker-selenium/blob/master/Base/Dockerfile  
#################################################  
  
USER root  
  
#==============================  
# Set locale  
#==============================  
RUN set -ex; \  
apt-get update -qqy; \  
apt install -y locales; \  
dpkg-reconfigure locales; \  
locale-gen en_US.UTF-8 && locale -a  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
#==============================  
# Install docker client  
#==============================  
ENV DOCKER_VERSION 17.11.0-ce-rc2  
RUN set -ex; \  
wget -qO- "https://get.docker.io" | sh; \  
dockerd -v; \  
docker -v  
  
#==============================  
# SBT  
#==============================  
ENV SBT_VERSION 0.13.16  
RUN set -ex; \  
wget -qO- "https://cocl.us/sbt-${SBT_VERSION}.tgz" | tar xvz -C /usr/local; \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin  
  
#==============================  
# Install dependences  
#==============================  
USER jenkins  
RUN \  
cd ~/ && \  
mkdir project && \  
echo "sbt.version=$SBT_VERSION" > project/build.properties && \  
sbt -mem 1024 sbtVersion  
  

