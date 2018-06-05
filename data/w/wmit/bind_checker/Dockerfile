FROM ubuntu:16.04  
MAINTAINER Phil Fenstermacher  
  
RUN apt-get update && apt-get install -y bind9utils  
COPY checkzones.sh /usr/local/bin/checkzones  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

