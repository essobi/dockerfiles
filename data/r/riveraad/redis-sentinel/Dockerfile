FROM redis:3  
COPY start-sentinel.sh /start-sentinel.sh  
COPY start-redis.sh /start-redis.sh  
RUN chmod +x /start-sentinel.sh  
RUN chmod +x /start-redis.sh  
  
EXPOSE 5000 6379  
VOLUME ["/data"]  
  
CMD ["/start-redis.sh"]  

