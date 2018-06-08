# Redis v3.0  
#  
# docker run --rm pottava/redis:3.0 -v  
# docker run -d --name redis -p 6379:6379 pottava/redis:3.0  
# redis-cli -h <docker-host-ip-address>  
FROM alpine:3.3  
RUN apk --no-cache add redis  
  
VOLUME ["/var/lib/redis/"]  
EXPOSE 6379  
ENTRYPOINT ["redis-server"]  

