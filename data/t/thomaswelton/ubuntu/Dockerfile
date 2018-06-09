FROM ubuntu:precise  
  
MAINTAINER thomaswelton  
  
USER root  
ENV HOME /root  
  
# Update and upgrade packages  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vim curl git build-
essential make gcc wget  

