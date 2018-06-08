# Dockerfile for Ubuntu 12.04 and Oracle Java 7  
FROM ubuntu:14.04  
MAINTAINER John Dorrance <jdorrance@mavendc.com>  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install software-
properties-common && add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
(echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections) && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin:$PATH  

