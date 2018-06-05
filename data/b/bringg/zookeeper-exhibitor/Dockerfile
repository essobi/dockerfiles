# build gcsfuse  
FROM golang:1.10-alpine as gcsfuse  
RUN apk add --no-cache git musl-dev \  
&& go get -v -u github.com/googlecloudplatform/gcsfuse  
  
# build exhibitor  
FROM maven:3.5-alpine as exhibitor  
  
ARG EXHIBITOR_VERSION="1.7.0"  
ENV
EXHIBITOR_RELEASE="https://github.com/soabase/exhibitor/archive/exhibitor-$EXHIBITOR_VERSION.tar.gz"  
RUN wget -qO- $EXHIBITOR_RELEASE | tar -xvz -C / \  
&& ln -s /exhibitor* /exhibitor \  
&& cd /exhibitor \  
&& mvn -DskipTests=true install \  
&& sed -i "s/<version>1\\..\\.0/<version>$EXHIBITOR_VERSION/" exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml \  
&& mvn -f exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml package  
  
FROM openjdk:8-jdk-alpine  
LABEL maintainer "Bringg DevOps <devops@bringg.com>"  
  
ARG EXHIBITOR_VERSION="1.7.0"  
ARG ZK_VERSION="3.4.10"  
ENV
ZK_RELEASE="http://www.apache.org/dist/zookeeper/zookeeper-$ZK_VERSION/zookeeper-$ZK_VERSION.tar.gz"  
RUN \  
# Install required packages  
apk add \--no-cache bash fuse \  
\  
# Alpine doesn't have /opt dir  
&& mkdir -p /opt \  
\  
# Install ZK  
&& wget -qO- $ZK_RELEASE | tar -xvz -C /opt \  
&& ln -s /opt/zookeeper-* /opt/zookeeper  
  
# Add the optional web.xml for authentication and the wrapper script to setup
configs  
COPY include/ /opt/exhibitor/  
  
# Copy files from build containers  
COPY \--from=gcsfuse /go/bin/gcsfuse /usr/local/bin/  
COPY \--from=exhibitor /exhibitor/exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/target/exhibitor-$EXHIBITOR_VERSION.jar
/opt/exhibitor/exhibitor.jar  
  
WORKDIR /opt/exhibitor  
EXPOSE 2181 2888 3888 8181  
ENTRYPOINT ["bash", "-ex", "/opt/exhibitor/wrapper.sh"]  

