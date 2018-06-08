FROM ubuntu:trusty  
  
MAINTAINER Jean Bordat <bordat.jean@gmail.com>  
  
ENV APT_GET_UPDATE 2015-03-08  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre-headless
wget && apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  

