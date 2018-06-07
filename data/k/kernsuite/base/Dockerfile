FROM ubuntu:18.04  
MAINTAINER gijsmolenaar@gmail.com  
  
ADD docker-apt-install /usr/local/bin  
ADD sources.list /etc/apt  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv B7D042E7  
RUN apt-get update  
  

