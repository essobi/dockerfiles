FROM redis:3.0-alpine  
  
ADD redis-sentinel.conf /etc/redis-sentinel.conf  
  
# redis likes to write to it's own config file  
RUN chown redis:redis /etc/redis-sentinel.conf  
  
CMD ["redis-server", "/etc/redis-sentinel.conf", "--sentinel"]  

