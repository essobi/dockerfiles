FROM redislabs/redisearch:1.0.8  
COPY redis.conf /usr/local/etc/redis/redis.conf  
CMD ["redis-server", "/usr/local/etc/redis/redis.conf", "--loadmodule",
"/usr/lib/redis/modules/redisearch.so"]  

