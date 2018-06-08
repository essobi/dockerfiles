# use the ubuntu base image provided by dotCloud  
FROM ubuntu:quantal  
  
MAINTAINER Haroon Rafique https://github.com/hrafique  
  
# add community-maintained universe repository to sources  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN sed -e 's#quantal#quantal-security#' /etc/apt/sources.list | \  
tee -a /etc/apt/sources.list  
  
# date packages were last updated  
ENV REFRESHED_AT 2014-01-20  
ENV DEBIAN_FRONTEND noninteractive  
# resynchronize package index files from their sources  
RUN apt-get update  
  
RUN apt-get install -y --no-install-recommends \  
openjdk-7-jre-headless  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre  

