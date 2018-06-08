FROM imega/base-builder:1.1.0  
EXPOSE 6379  
COPY . /  
  
RUN apk add --update redis && \  
rm -rf /var/cache/apk/*  
  
CMD ["redis-server","/redis.conf"]  

