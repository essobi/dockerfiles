  
# Debian stable.  
# version 0.0.1  
FROM debian:stable  
  
MAINTAINER stansage <me@stansage.com>  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt  
RUN apt-get update  
# Install server software  
RUN apt-get -y install openssh-server  

