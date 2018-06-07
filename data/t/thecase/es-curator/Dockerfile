FROM alpine:latest  
  
RUN apk add --update curl coreutils && rm -rf /var/cache/apk/*  
  
COPY crontab /etc/crontabs/root  
  
CMD ["/usr/sbin/crond", "-f"]  

