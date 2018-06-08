# Docker base image with Oracle JDK 8  
FROM debian:jessie  
MAINTAINER redspark <infra@redspark.io>  
  
USER root  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz -O
/tmp/jdk-8u60-linux-x64.tar.gz  
RUN tar -zxvf /tmp/jdk-8u60-linux-x64.tar.gz -C /tmp  
RUN mv /tmp/jdk1.8.0_60 /opt  
RUN update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_60/bin/java
0  
  
ENV JAVA_HOME /opt/jdk1.8.0_60  
ENV PATH $PATH:$JAVA_HOME/bin

