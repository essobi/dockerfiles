#!/bin/bash  
FROM mychiara/base:latest  
MAINTAINER Andy Ruck mychiara+docker __at__ gmail.com  
  
RUN apt-get update && \  
apt-get install -yq redis-server && \  
apt-get autoclean && apt-get autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Enable redis  
RUN mkdir /etc/service/redis  
ADD config/redis /etc/service/redis/run  
RUN chmod +x /etc/service/redis/run  
  
# Configure redis  
RUN sed -i 's/daemonize yes/daemonize no/g' /etc/redis/redis.conf && \  
sed -i 's/bind 127.0.0.1/# bind 127.0.0.1/g' /etc/redis/redis.conf  
  
# Setup a volume that will contain the db  
VOLUME "/var/lib/redis"  
  
# Expose the port and run it  
EXPOSE 6379  

