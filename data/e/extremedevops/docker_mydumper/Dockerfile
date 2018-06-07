FROM ubuntu:16.04  
MAINTAINER Leandro David Cacciagioni <leandro.21.2008@gmail.com>  
  
RUN apt-get update && apt-get -qqy install mydumper mysql-client && \  
apt-get autoremove -qqy && \  
apt-get clean && apt-get autoclean && \  
rm -rf /usr/share/man/?? && rm -rf /usr/share/man/??_* && rm -rf
/var/lib/apt/lists/*  

