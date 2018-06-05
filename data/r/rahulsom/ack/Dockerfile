FROM alpine  
  
RUN apk update && apk add --no-cache ack  
  
VOLUME /data  
WORKDIR /data  
ENTRYPOINT ["ack"]  

