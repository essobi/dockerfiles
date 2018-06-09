FROM ubuntu:trusty  
MAINTAINER Ove Ranheim <oranheim@gmail.com>  
  
# Java Version  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 162  
ENV JAVA_VERSION_BUILD 12  
ENV JAVA_SPECIFIER aa0333dd3019491ca4f6ddbe78cdb6d0  
ENV JAVA_PACKAGE jdk  
ENV LANG C.UTF-8  
# GOSU  
ENV GOSU_VERSION 1.10  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
ca-certificates git-core curl sudo \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Origin: https://hub.docker.com/r/oberthur/docker-ubuntu-java/~/dockerfile/  
RUN curl -kLOH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_SPECIFIER}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
tar -zxf
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-C /opt && \  
rm
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk  
  
RUN { \  
echo '#!/bin/bash'; \  
echo 'set -e'; \  
echo 'if [[ "$PATH" == ?(*:)"$JAVA_HOME/bin"?(:*) ]]; then'; \  
echo ' export JAVA_HOME=/opt/jdk'; \  
echo ' export PATH=$PATH:$JAVA_HOME/bin:'; \  
echo 'fi'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  

