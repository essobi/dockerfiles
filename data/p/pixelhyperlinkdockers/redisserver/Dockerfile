# PixelHyperlink Redis Server Docker  
#  
# VERSION 1.4.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with redis service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.4.0"  
LABEL com.pixelhyperlink.docker.redisserver.version="1.4.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.redisserver.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.redisserver.version.is-production="true"  
  
# Install redis.  
RUN apt-get update && \  
apt-get -y install redis-server  
  
# Expose redis.  
EXPOSE 6379  
VOLUME ["/var/lib/redis", "/var/log/redis"]  
  
# Copy redis config  
COPY ./redis.conf /etc/redis/redis.conf  
  
# Copy server start up scripts  
COPY ./redis_entrypoint.sh /opt/redis_entrypoint.sh  
  
# Change permission on startup scripts  
RUN chmod 755 /opt/redis_entrypoint.sh  
  
ENTRYPOINT ["/opt/redis_entrypoint.sh"]  

