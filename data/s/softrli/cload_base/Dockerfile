# cload_base  
#  
# Dockerfile to setup an updated and fixed base Ubuntu image.  
#  
# - Perform package update  
# - Perform package upgrade  
# - Setup locales  
#  
# VERSION 0.0.1  
FROM ubuntu  
MAINTAINER Romain Champourlier, romain@softr.li  
  
# Ensure everything is up-to-date  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y language-pack-en  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales

