FROM ubuntu:trusty  
MAINTAINER Jamie Furness <jamie@jamierf.co.uk>  
  
# Enable updates, universe, multiverse repositories  
RUN apt-get install -qy software-properties-common  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse"  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-
updates universe multiverse"  
RUN apt-get update -q  
  
# Install base dependencies  
RUN apt-get install -qy curl wget python git unrar unzip  

