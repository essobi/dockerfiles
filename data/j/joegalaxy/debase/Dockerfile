FROM debian:8.1  
MAINTAINER Joe Galaxy <github@simonebaglioni.com>  
  
ENV VERSION 0.3b  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update System  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# Basic Requirements (we install nginx, php5-fpm, supervisor)  
RUN apt-get -y install nginx php5-fpm php5-mysql curl supervisor  
  
# Install Extra PHP Modules  
RUN apt-get -y install php5-curl php5-gd php5-intl php5-mcrypt  
  
# Install debug and edit tools  
RUN apt-get -y install emacs-nox less htop  

