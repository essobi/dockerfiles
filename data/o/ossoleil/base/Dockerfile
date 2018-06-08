FROM ubuntu:15.10  
MAINTAINER Alessio Deiana <adeiana@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -qq upgrade && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  

