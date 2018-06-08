# Pull base image.  
FROM ubuntu:14.04.1  
  
MAINTAINER Francois Langelier  
  
ENV JAVA_VERSION 7u75-2.5.4-1~trusty1  
ENV JAVA_HOME /usr/lib/jvm/jdk  
# Install Java.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jdk=$JAVA_VERSION
&& \  
ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/lib/jvm/jdk && \  
rm -rf /var/lib/apt/lists/*  

