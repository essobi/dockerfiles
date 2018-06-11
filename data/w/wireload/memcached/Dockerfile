# WireLoad's Dockerized Memcached  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Viktor Petersson <vpetersson@wireload.net>  
  
# Refresh apt and install dependencies  
RUN apt-get update  
RUN apt-get install -y memcached  
  
# Cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 11211  
# Start a 128M memcached as user 'memcache'  
USER memcache  
CMD memcached -m 128 -p 11211 -l 0.0.0.0  

