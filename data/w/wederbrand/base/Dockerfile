# VERSION 1.1  
FROM ubuntu:16.04  
MAINTAINER Andreas Wederbrand andreas@wederbrand.se  
  
# install emacs and apt-get-utilities  
RUN apt-get update  
RUN apt-get install -y emacs-nox software-properties-common python-software-
properties curl wget git dnsutils  
  
ENV term xterm  
  
# Remove useless files  
RUN rm -rf /var/lib/apt/lists/*  
  
USER root  
CMD bash

