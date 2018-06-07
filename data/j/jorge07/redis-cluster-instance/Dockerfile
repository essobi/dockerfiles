FROM redis:3.2.8-alpine  
  
ARG PORT=6379  
ADD rootfs /  
  
RUN sed -i -e "s/6379/$PORT/g" /usr/local/redis/redis.conf  
  
WORKDIR /data  
  
VOLUME /data  
  
CMD [ "redis-server", "/usr/local/redis/redis.conf" ]  

