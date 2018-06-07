FROM redis:3.2-alpine  
  
RUN apk add --update py-pip  
RUN pip install j2cli  
  
COPY redis.conf.j2 /  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

