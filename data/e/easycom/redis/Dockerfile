FROM redis:alpine  
MAINTAINER Frédéric T <xmedias@easycom.digital>  
  
COPY redis.conf /usr/local/etc/redis/redis.conf  
  
RUN mkdir -p /var/run/redis /var/log/redis && chown redis:redis /var/run/redis
/var/log/redis  
  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

