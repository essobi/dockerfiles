FROM ubuntu:trusty  
MAINTAINER josh < josh [at] gmail {dot} com>  
  
RUN apt-get update && apt-get -y install python-software-properties software-
properties-common && \  
add-apt-repository "deb http://gb.archive.ubuntu.com/ubuntu $(lsb_release -sc)
universe" && \  
apt-get update  
  
RUN add-apt-repository ppa:saiarcot895/myppa && \  
apt-get update && \  
apt-get -y install apt-fast  
  
RUN add-apt-repository ppa:inkscape.dev/stable && \  
apt-get update && \  
apt-get -y install inkscape  

