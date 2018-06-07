FROM alpine:latest  
  
RUN apk add --update openssh && rm -rf /var/cache/apk/*  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

