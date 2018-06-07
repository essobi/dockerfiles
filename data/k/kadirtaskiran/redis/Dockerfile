FROM redis  
  
RUN mkdir /redislogs && chown redis:redis /redislogs  
VOLUME /redislogs  
  
COPY redis.conf /usr/local/etc/redis/redis.conf  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

