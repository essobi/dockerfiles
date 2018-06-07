FROM alpine  
RUN apk update && apk add git  
COPY entrypoint-sync.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

