# Pull base image  
FROM redis:4.0.8  
# Maintener  
MAINTAINER Mustafa Bayrak <mustafa.bayrak@windowslive.com>  
  
RUN apt-get update  
RUN apt install apt-utils -y  
RUN apt install vim -y  
  
# Copy config redis  
RUN mkdir -p /usr/local/etc/redis/  
COPY redis.conf /usr/local/etc/redis/redis.conf  
  
# Run redis server  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

