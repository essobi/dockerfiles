FROM ubuntu:14.04  
MAINTAINER Jujhar Singh <jujhar@jujhar.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN echo "LANG=\"en_GB.UTF-8\"" > /etc/default/locale  
RUN locale-gen en_GB.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN apt-get update  
RUN apt-get install -y \  
wget \  
imagemagick  

