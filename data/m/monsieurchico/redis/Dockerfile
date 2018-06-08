#  
# Redis Dockerfile  
# git@github.com:monsieurchico/docker-redis.git  
#  
FROM ubuntu:14.04  
MAINTAINER Romain Derocle "rderocle@gmail.com"  
# prevent debian errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# updates  
RUN \  
apt-get update && \  
apt-get install -y --force-yes redis-server redis-tools && \  
rm -rf /var/lib/apt/lists/*  
  
# expose ports  
EXPOSE 6379  
# volumes  
VOLUME ["/etc/redis", "/var/lib/redis"]  
  
# add launch script  
COPY ./resources/startup.sh /startup.sh  
  
# define entrypoint  
ENTRYPOINT ["/bin/bash", "/startup.sh"]  
  
# define workdir  
WORKDIR /  

