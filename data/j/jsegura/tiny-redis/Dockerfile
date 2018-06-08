FROM alpine:3.2  
RUN apk add --update redis  
  
RUN mkdir /data && chown redis:redis /data  
VOLUME /data  
WORKDIR /data  
  
CMD ["redis-server"]  

