FROM redis  
  
COPY redis.conf /usr/local/etc/redis/redis.conf  
  
RUN chown -R redis:redis /usr/local/etc/redis  
  
# masterauth and requirepass should be same for sentinel fail-over  
ENV REDIS_DEFAULT_PASSWORD redis1234  
ENV MASTER_DEFAULT_PASSWORD "$REDIS_DEFAULT_PASSWORD"  
# base tunning for redis  
RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf;  
#sysctl vm.overcommit_memory=1  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]  

