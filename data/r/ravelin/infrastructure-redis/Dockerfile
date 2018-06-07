############################################################  
# Redis - https://github.com/docker-
library/redis/tree/109323988b7663bceaf4a01c3353f8934dfc002e/2.8  
# Based on Phusion Image - https://github.com/phusion/baseimage-docker  
# ENV SUITABILITY: DEVELOPMENT  
############################################################  
  
FROM phusion/baseimage:0.9.15  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install redis  
RUN apt-get install -y redis-server  
  
# Enable redis & Configure redis  
RUN mkdir /etc/service/redis  
RUN sed -i 's/daemonize yes/daemonize no/g' /etc/redis/redis.conf  
RUN sed -i 's/bind 127.0.0.1/# bind 127.0.0.1/g' /etc/redis/redis.conf  
  
# Set Permissions  
RUN chown redis:redis /var/lib/redis  
RUN chown redis:redis /etc/redis/redis.conf  
  
# User redis user  
USER redis  
  
# Setup a volume that will contain the db  
VOLUME /var/lib/redis  
  
# Expose the port and run it  
EXPOSE 6379  
  
# Set the entrypoints  
ENTRYPOINT redis-server

