#######################################################################  
# Dockerfile to build an Ubuntu Oracle Java SDK container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:15.04  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
# Add Android SDK  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" |
/usr/bin/debconf-set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" |
/usr/bin/debconf-set-selections  
  
RUN apt-get update  
RUN apt-get install wget tmux build-essential software-properties-common
python-software-properties -y  
  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get install oracle-java8-set-default -y  
ENV JAVA_HOME /usr/bin/java  

