FROM alpine:3.6  
RUN apk add --no-cache redis sed bash  
  
COPY redis-master.conf /redis-master/redis.conf  
COPY redis-slave.conf /redis-slave/redis.conf  
COPY run.sh /run.sh  
  
ENV MASTER="true" \  
REDIS_MAXMEMORY="64mb" \  
REDIS_MAXMEMORY_POLICY="allkeys-lru"  
CMD [ "/run.sh" ]  
  
ENTRYPOINT [ "bash", "-c" ]  

