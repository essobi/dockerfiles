FROM ubuntu:xenial  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
ENV JAVA_VERSION 8u131  
  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
openjdk-8-jdk=${JAVA_VERSION}* && \  
apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
CMD [ "bash" ]  

