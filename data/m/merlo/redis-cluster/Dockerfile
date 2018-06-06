FROM redis:alpine  
  
COPY conf /conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ "redis-server" ]  

