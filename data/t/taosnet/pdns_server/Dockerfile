FROM alpine  
MAINTAINER Chris Batis <clbatis@taosnet.com>  
  
RUN apk --no-cache add pdns-recursor  
COPY docker-pdns.sh /docker-pdns.sh  
  
ENTRYPOINT ["/docker-pdns.sh"]  
  
EXPOSE 53/udp 53/tcp 8081  

