FROM redis  
  
ADD redis.conf /etc/redis.conf  
  
RUN mkdir -p /var/log/redis  
RUN chown -R redis: /var/log/redis  
  
EXPOSE 6379  
CMD [ "redis-server", "/etc/redis.conf" ]  

