FROM redis  
COPY docker-entrypoint.sh /  
COPY redis.conf /usr/local/etc/redis/redis.conf  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

