FROM alpine:3.6  
MAINTAINER Erlend Finvåg <erlend.finvag@gmail.com>  
  
RUN apk add -U unbound && rm -rf /var/cache/apk/*  
COPY docker-entrypoint.sh /  
  
VOLUME /etc/unbound  
  
EXPOSE 53  
EXPOSE 53/udp  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

