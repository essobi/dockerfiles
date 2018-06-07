FROM alpine:3.6  
RUN apk add --no-cache git openssl dcron  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ADD sync.sh /etc/periodic/15min/sync.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

