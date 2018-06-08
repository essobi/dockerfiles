#  
# Memcached Dockerfile  
# git@github.com:monsieurchico/docker-memcached.git  
#  
FROM ubuntu:latest  
MAINTAINER Romain Derocle "rderocle@gmail.com"  
# prevent debian errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# update os and install nginx  
RUN \  
apt-get update && \  
apt-get install -y memcached && \  
rm -rf /var/lib/apt/lists/*  
  
# expose ports  
EXPOSE 11211  
# add launch script  
COPY ./resources/startup.sh /startup.sh  
  
# define entrypoint  
ENTRYPOINT ["/bin/bash", "/startup.sh"]  
  
# define workdir  
WORKDIR /

