FROM redis:2.8  
COPY redis.conf /usr/local/etc/redis/redis.conf  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD [ "/run.sh" ]

