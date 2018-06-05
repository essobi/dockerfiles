# alexindigo/ubuntu_precise  
FROM ubuntu:12.04  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
# Make DEBIAN_FRONTEND less chatty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update stuff  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && apt-get update && apt-get upgrade -y  
  
# Dev essential dependencies  
RUN apt-get install -y build-essential curl  

