FROM ubuntu:latest  
MAINTAINER Elliot Marx "elliot.marx@affirm.com"  
RUN apt-get update  
RUN apt-get install -y python python-pip wget vim mysql-client git  
  
RUN mkdir /platform  
RUN mkdir /platform/salt  
RUN mkdir /platform/all-the-things  
  
WORKDIR /platform  
VOLUME /platform/salt  
VOLUME /platform/all-the-things  

