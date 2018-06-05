FROM ubuntu:18.04  
MAINTAINER Alexandr Bordun <bordun.alexandr@gmail.com>  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install locales  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
ENV LANGUAGE en_US  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get -y install wget curl git nano openssh-server htop sudo rsyslog
logrotate  
  
EXPOSE 22  

