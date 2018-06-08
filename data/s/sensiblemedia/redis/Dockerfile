FROM redis  
COPY files/redis.conf /usr/local/etc/redis/redis.conf  
COPY files/motd /etc/motd  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

